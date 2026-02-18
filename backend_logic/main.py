import os
import re
import ast
import asyncio
from collections import Counter
from contextlib import asynccontextmanager
from pathlib import Path

import polars as pl
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import google.generativeai as genai

# ── Paths ─────────────────────────────────────────────────────────────────────
_REPO_ROOT = Path(__file__).parent.parent
_ENV_PATH = Path(__file__).parent / ".env"
_DATA_PATH = _REPO_ROOT / "backend_logic" / "data" / "final_dataset_cleaned_polars.csv"
_FRONTEND_DIR = _REPO_ROOT / "frontend"

load_dotenv(_ENV_PATH)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ── Globals populated at startup ──────────────────────────────────────────────
df: pl.DataFrame | None = None
BRANDS: list[str] = []
ROW_COUNT: int = 0
SCHEMA_INFO: dict = {}
CODE_MODEL = None
FORMAT_MODEL = None

# Max code-gen retries before falling back to a graceful error message
_MAX_RETRIES = 2


# ── System prompt builder ─────────────────────────────────────────────────────
def _build_code_system_prompt() -> str:
    schema_lines = "\n".join(f"  {col}: {dtype}" for col, dtype in SCHEMA_INFO.items())
    brands_lines = "\n".join(f"  - {b}" for b in BRANDS)
    return f"""You are a data analyst assistant with access to a Polars DataFrame called `df`.
The DataFrame contains {ROW_COUNT:,} tweets about Super Bowl LX (2026) advertisements.

## Column Schema ({len(SCHEMA_INFO)} columns)
{schema_lines}

## Unique Brands (column: `brand`) — always include the `_1` suffix in filter expressions
{brands_lines}

## Tweet Types (column `tweet_type`): original, quote, reply, retweet

## Boolean columns: is_retweet, is_spam, is_possible_copypasta, has_media, is_reply
(Polars Boolean dtype — filter with pl.col("x") == True or just .filter(pl.col("x")))

## Key numeric columns
public_metrics.retweet_count, public_metrics.like_count, public_metrics.reply_count,
public_metrics.quote_count, public_metrics.impression_count, public_metrics.bookmark_count,
emoji_count, mention_count, hashtag_count, url_count, media_count

## Text columns
- `text`       — raw tweet text (may contain HTML entities, URLs)
- `text_clean` — cleaned tweet text (use this for keyword searches)
- `text_no_emoji` — cleaned text with emojis stripped

## Emoji column
- `emoji_list` — string like "['🔥', '🏈']" listing emojis found in the tweet
- `emoji_count` — integer count of emojis in the tweet

## Pre-injected helpers (no import needed)
- `pl`      — polars module
- `df`      — the DataFrame
- `re`      — Python re module (for regex operations on strings)
- `Counter` — collections.Counter (for frequency counting)
Standard Python builtins: len, str, int, float, bool, list, dict, tuple, set, sorted,
round, min, max, sum, abs, any, all, range, enumerate, zip, map, filter, isinstance,
next, iter, type, hasattr, getattr, True, False, None

## Instructions
When given a user question, respond with ONLY raw Python code — no markdown fences, no explanation.
The code must:
1. Use the existing `df` variable (polars.DataFrame) — never re-read the CSV
2. Define a variable named `result` containing a string, number, list, or dict
3. Use only the injected names listed above — no import statements
4. Handle nulls and edge cases (use .fill_null(0), .drop_nulls(), guard against empty results)

## Examples

### Simple count
User: How many tweets did Pepsi get?
result = df.filter(pl.col("brand").str.starts_with("Pepsi")).shape[0]

### Top brands by metric (null-safe)
User: Which brand had the most likes?
result = (
    df
    .with_columns(pl.col("public_metrics.like_count").fill_null(0).alias("likes"))
    .group_by("brand")
    .agg(pl.col("likes").sum())
    .sort("likes", descending=True)
    .head(5)
    .to_dicts()
)

### Percentage
User: What percentage of tweets were retweets?
result = round(df.filter(pl.col("is_retweet") == True).shape[0] / df.shape[0] * 100, 2)

### Keyword search (use text_clean, not "content")
User: How many tweets mention the word "funny"?
result = df.filter(pl.col("text_clean").str.contains(r"(?i)\bfunny\b")).shape[0]

### Emoji frequency for a brand (using emoji_list column + Counter)
User: What are the top emojis used in Doritos tweets?
rows = (
    df
    .filter(pl.col("brand").str.starts_with("Doritos"))
    .filter(pl.col("emoji_count") > 0)
    .select("emoji_list")
    .to_series()
    .drop_nulls()
    .to_list()
)
counts = Counter()
for row in rows:
    if row:
        for part in row.strip("[]").split(","):
            e = part.strip().strip("'\" ")
            if e:
                counts[e] += 1
result = counts.most_common(5)

### Handling no-match gracefully
User: How many tweets are about BrandX?
filtered = df.filter(pl.col("brand") == "BrandX_1")
result = filtered.shape[0] if filtered.shape[0] > 0 else 0

### Complex cleaning with temporary columns
User: Which brand's tweets have the most media on average?
result = (
    df
    .with_columns(pl.col("media_count").fill_null(0).alias("media"))
    .group_by("brand")
    .agg(pl.col("media").mean().round(2).alias("avg_media"))
    .sort("avg_media", descending=True)
    .head(5)
    .to_dicts()
)
"""


# ── Lifespan ──────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    global df, BRANDS, ROW_COUNT, SCHEMA_INFO, CODE_MODEL, FORMAT_MODEL

    print(f"[startup] Loading dataset from {_DATA_PATH} ...")
    df = pl.read_csv(str(_DATA_PATH), infer_schema_length=5000, try_parse_dates=True)
    BRANDS = sorted(df["brand"].unique().to_list())
    ROW_COUNT = len(df)
    SCHEMA_INFO = {col: str(dtype) for col, dtype in df.schema.items()}

    system_prompt = _build_code_system_prompt()

    CODE_MODEL = genai.GenerativeModel(
        "gemini-2.0-flash",
        system_instruction=system_prompt,
    )
    FORMAT_MODEL = genai.GenerativeModel(
        "gemini-2.0-flash",
        system_instruction=(
            "You are a friendly data analyst assistant. Given a user question and a raw query result, "
            "write a clear, concise 1-3 sentence answer in natural language. "
            "Do not show code or raw data structures. Format large numbers with commas. "
            "When mentioning brand names, remove the '_1' suffix "
            "(e.g. 'Pepsi Zero Sugar_1' becomes 'Pepsi Zero Sugar')."
        ),
    )

    print(f"[startup] {ROW_COUNT:,} rows | {len(BRANDS)} brands | ready")
    yield
    df = None


# ── App ───────────────────────────────────────────────────────────────────────
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# ── Sandbox ───────────────────────────────────────────────────────────────────
_FORBIDDEN_RE = re.compile(
    r"\b(import|open|exec|eval|compile|__import__|os|sys|subprocess|shutil|pathlib|socket|builtins)\b"
    r"|__[a-z_]+__"
)

_SAFE_BUILTINS = {
    # Types
    "str": str, "int": int, "float": float, "bool": bool,
    "list": list, "dict": dict, "tuple": tuple, "set": set,
    # Numeric
    "len": len, "round": round, "min": min, "max": max, "sum": sum, "abs": abs,
    # Iteration
    "sorted": sorted, "enumerate": enumerate, "zip": zip, "range": range,
    "any": any, "all": all, "next": next, "iter": iter,
    "map": map, "filter": filter,
    # Introspection
    "isinstance": isinstance, "type": type, "hasattr": hasattr, "getattr": getattr,
    # Constants
    "True": True, "False": False, "None": None,
    # Debug
    "print": print,
}

_BLOCKED_AST_NODES = (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal, ast.Delete)


def execute_safe(code: str, dataframe: pl.DataFrame):
    """Run Gemini-generated Polars code in a restricted namespace.

    Returns the `result` variable value, or an Exception on failure.
    """
    if _FORBIDDEN_RE.search(code):
        return ValueError("Generated code contains forbidden patterns.")

    try:
        tree = ast.parse(code, mode="exec")
    except SyntaxError as e:
        return SyntaxError(f"Syntax error in generated code: {e}")

    for node in ast.walk(tree):
        if isinstance(node, _BLOCKED_AST_NODES):
            return ValueError(f"Disallowed statement type: {type(node).__name__}")

    namespace: dict = {
        "__builtins__": _SAFE_BUILTINS,
        "pl": pl,
        "df": dataframe,
        "re": re,           # injected — no import needed in generated code
        "Counter": Counter, # injected — no import needed in generated code
    }
    try:
        exec(compile(tree, "<gemini>", "exec"), namespace)  # noqa: S102
    except Exception as e:
        return RuntimeError(f"Execution error: {e}")

    if "result" not in namespace:
        return ValueError("Generated code did not define a `result` variable.")

    raw = namespace["result"]
    if isinstance(raw, pl.DataFrame):
        return raw.to_dicts()
    if isinstance(raw, pl.Series):
        return raw.to_list()
    return raw


def _strip_fences(text: str) -> str:
    """Remove markdown code fences that Gemini sometimes wraps around code."""
    text = re.sub(r"^```(?:python)?\s*\n?", "", text.strip(), flags=re.IGNORECASE)
    text = re.sub(r"\n?```\s*$", "", text.strip())
    return text.strip()


def _truncate_result(value, max_rows: int = 30):
    """Cap large results before sending to FORMAT_MODEL to avoid token overflow."""
    if isinstance(value, list) and len(value) > max_rows:
        return value[:max_rows] + [f"... ({len(value):,} total items)"]
    if isinstance(value, str) and len(value) > 4000:
        return value[:4000] + f"... (truncated, {len(value):,} total chars)"
    return value


# ── Request / Response models ─────────────────────────────────────────────────
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str
    debug_code: str | None = None


# ── Routes ────────────────────────────────────────────────────────────────────
@app.get("/api/health")
async def health():
    return {"status": "ok", "rows": ROW_COUNT, "brands": len(BRANDS)}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if df is None:
        raise HTTPException(503, "Dataset not loaded yet.")

    message = req.message.strip()
    if not message:
        raise HTTPException(400, "Message cannot be empty.")

    # ── Code generation with auto-retry on failure ────────────────────────────
    code: str | None = None
    result_value = None
    last_error: str | None = None

    for attempt in range(_MAX_RETRIES + 1):
        if attempt == 0:
            prompt = f"User question: {message}"
        else:
            print(f"[retry {attempt}] Feeding error back to CODE_MODEL: {last_error[:120]}")
            prompt = (
                f"Your previous code raised an error. Fix it.\n\n"
                f"Original question: {message}\n\n"
                f"Failed code:\n{code}\n\n"
                f"Error: {last_error}\n\n"
                "Write corrected code only. No explanation."
            )

        try:
            code_resp = await asyncio.to_thread(CODE_MODEL.generate_content, prompt)
            code = _strip_fences(code_resp.text)
        except Exception as e:
            raise HTTPException(502, f"Code generation failed: {e}")

        result_value = execute_safe(code, df)

        if not isinstance(result_value, Exception):
            break  # success — exit retry loop

        last_error = str(result_value)

    # ── All retries exhausted ─────────────────────────────────────────────────
    if isinstance(result_value, Exception):
        print(f"[error] All {_MAX_RETRIES + 1} attempts failed. Last error: {last_error}")
        try:
            fallback = await asyncio.to_thread(
                FORMAT_MODEL.generate_content,
                f"Question: {message}\n\n"
                "The data query could not be completed after multiple attempts. "
                "Briefly apologize and suggest the user try rephrasing.",
            )
            return ChatResponse(answer=fallback.text, debug_code=code)
        except Exception:
            return ChatResponse(
                answer="I wasn't able to answer that. Please try rephrasing your question.",
                debug_code=code,
            )

    # ── Format result as natural language ─────────────────────────────────────
    try:
        truncated = _truncate_result(result_value)
        fmt_resp = await asyncio.to_thread(
            FORMAT_MODEL.generate_content,
            f"User question: {message}\n\nRaw data result: {truncated!r}\n\nWrite a clear, friendly answer.",
        )
        return ChatResponse(answer=fmt_resp.text, debug_code=code)
    except Exception as e:
        raise HTTPException(502, f"Response formatting failed: {e}")


# ── Static files (MUST be declared last) ─────────────────────────────────────
app.mount("/", StaticFiles(directory=str(_FRONTEND_DIR), html=True), name="static")
