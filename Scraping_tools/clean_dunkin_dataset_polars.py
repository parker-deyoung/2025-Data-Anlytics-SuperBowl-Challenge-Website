#!/usr/bin/env python3
"""
Twitter/X Dunkin' Dataset Cleaning Script — Polars Native
==========================================================
Cleans ~123k rows of Twitter data through a 12-step pipeline.
100% Polars — zero pandas usage.

Input:  /Users/nicholaspardon/Desktop/final_dataset_2025_for_release_CSV.csv
Output: /Users/nicholaspardon/Desktop/final_dataset_2025_for_release_cleaned_polars.csv

Dependencies: pip install polars emoji
"""

import ast
import re
import time

import emoji
import polars as pl

INPUT_PATH = "/Users/nicholaspardon/Desktop/final_dataset_2025_for_release_CSV.csv"
OUTPUT_PATH = "/Users/nicholaspardon/Desktop/final_dataset_2025_for_release_cleaned_polars.csv"

start_time = time.time()


# =============================================================================
# STEP 1: Load and Initial Type Safety
# =============================================================================
print("=" * 60)
print("STEP 1: Loading dataset...")
print("=" * 60)

ID_OVERRIDES = {
    "id": pl.Utf8,
    "author_id": pl.Utf8,
    "conversation_id": pl.Utf8,
    "in_reply_to_user_id": pl.Utf8,
    "edit_history_tweet_ids": pl.Utf8,
    "attachments.media_source_tweet_id": pl.Utf8,
}

try:
    df = pl.read_csv(
        INPUT_PATH,
        skip_rows=1,
        separator=",",
        schema_overrides=ID_OVERRIDES,
        encoding="utf8",
        infer_schema_length=10000,
    )
except Exception:
    df = pl.read_csv(
        INPUT_PATH,
        skip_rows=1,
        separator=",",
        schema_overrides=ID_OVERRIDES,
        encoding="utf8-lossy",
        infer_schema_length=10000,
    )

# Parse created_at to datetime
df = df.with_columns(
    pl.col("created_at").str.to_datetime("%Y-%m-%dT%H:%M:%S%.fZ", strict=False)
)

original_row_count = df.height
original_col_count = len(df.columns)
print(f"  Rows: {original_row_count:,}")
print(f"  Columns: {original_col_count}")
print(f"  Columns: {df.columns}")


# =============================================================================
# STEP 2: Exact Deduplication
# =============================================================================
print("\n" + "=" * 60)
print("STEP 2: Exact deduplication on tweet ID...")
print("=" * 60)

before = df.height
df = df.unique(subset=["id"], keep="first")
dupes_removed = before - df.height
print(f"  Rows removed: {dupes_removed:,}")
print(f"  Rows remaining: {df.height:,}")


# =============================================================================
# STEP 3: Near-Duplicate Text Detection
# =============================================================================
print("\n" + "=" * 60)
print("STEP 3: Flagging near-duplicate text (copypasta)...")
print("=" * 60)

text_counts = df.group_by("text").agg(pl.col("id").count().alias("text_freq"))
df = df.join(text_counts, on="text", how="left")
df = df.with_columns(
    ((pl.col("text_freq") > 1) & pl.col("text").is_not_null()).alias("is_possible_copypasta")
).drop("text_freq")

copypasta_count = df.select(pl.col("is_possible_copypasta").sum()).item()
print(f"  Tweets flagged as possible copypasta: {copypasta_count:,}")


# =============================================================================
# STEP 4: Retweet Flagging
# =============================================================================
print("\n" + "=" * 60)
print("STEP 4: Flagging retweets...")
print("=" * 60)

df = df.with_columns(
    (
        pl.col("text").fill_null("").str.starts_with("RT @")
        | pl.col("referenced_tweets").fill_null("").str.contains("'type': 'retweeted'")
    ).alias("is_retweet")
)

retweet_count = df.select(pl.col("is_retweet").sum()).item()
print(f"  Retweets flagged: {retweet_count:,}")


# =============================================================================
# STEP 5: Spam and Bot Filtering
# =============================================================================
print("\n" + "=" * 60)
print("STEP 5: Flagging spam/bot tweets...")
print("=" * 60)

# Hashtag ratio helper — needs map_elements because Polars doesn't have
# "sum of all match lengths" natively
def _hashtag_char_ratio(text: str) -> float:
    if text is None or text == "":
        return 0.0
    hashtags = re.findall(r"#\S+", text)
    hashtag_chars = sum(len(h) for h in hashtags)
    return hashtag_chars / len(text) if len(text) > 0 else 0.0

df = df.with_columns(
    (
        # 10+ hashtags
        (pl.col("text").fill_null("").str.count_matches("#") >= 10)
        # >50% hashtag characters
        | (
            pl.col("text")
            .fill_null("")
            .map_elements(_hashtag_char_ratio, return_dtype=pl.Float64)
            > 0.5
        )
        # Spam keywords in name/username
        | pl.col("name").fill_null("").str.to_lowercase().str.contains("onlyfans|leaked|nudes|promo")
        | pl.col("username").fill_null("").str.to_lowercase().str.contains("onlyfans|leaked|nudes|promo")
    ).alias("is_spam")
)

spam_count = df.select(pl.col("is_spam").sum()).item()
print(f"  Spam/bot tweets flagged: {spam_count:,}")


# =============================================================================
# STEP 6: Text Cleaning
# =============================================================================
print("\n" + "=" * 60)
print("STEP 6: Cleaning tweet text...")
print("=" * 60)

# --- Native chain for text_clean ---
df = df.with_columns(
    pl.col("text")
    .fill_null("")
    # Strip outer quotes
    .str.strip_chars('"')
    # Decode HTML entities (most common ones)
    .str.replace_all("&amp;", "&", literal=True)
    .str.replace_all("&lt;", "<", literal=True)
    .str.replace_all("&gt;", ">", literal=True)
    .str.replace_all("&quot;", '"', literal=True)
    .str.replace_all("&#39;", "'", literal=True)
    .str.replace_all("&apos;", "'", literal=True)
    # Remove t.co URLs
    .str.replace_all(r"https?://t\.co/\w+", "")
    # Normalize whitespace
    .str.replace_all(r"\s+", " ")
    .str.strip_chars(" ")
    .alias("text_clean")
)

# --- Emoji extraction (map_elements — unavoidable) ---
print("  Extracting emojis...")

def _extract_emojis(text: str) -> list:
    if text is None or text == "":
        return []
    return [item["emoji"] for item in emoji.emoji_list(text)]

def _strip_emojis(text: str) -> str:
    if text is None or text == "":
        return text
    return emoji.replace_emoji(text, replace="")

df = df.with_columns(
    pl.col("text_clean")
    .map_elements(_extract_emojis, return_dtype=pl.List(pl.Utf8))
    .alias("emoji_list")
)

df = df.with_columns(
    pl.col("emoji_list").list.len().alias("emoji_count"),
    pl.col("text_clean")
    .map_elements(_strip_emojis, return_dtype=pl.Utf8)
    .alias("text_no_emoji"),
)

emoji_tweets = df.select((pl.col("emoji_count") > 0).sum()).item()
total_emojis = df.select(pl.col("emoji_count").sum()).item()
print(f"  Tweets with emojis: {emoji_tweets:,}")
print(f"  Total emojis found: {total_emojis:,}")


# =============================================================================
# STEP 6b: Emoji Cleanup in User Metadata
# =============================================================================
print("\n" + "=" * 60)
print("STEP 6b: Cleaning emojis from user metadata...")
print("=" * 60)

def _clean_name(name: str) -> str:
    if name is None or name == "":
        return name
    return emoji.replace_emoji(str(name), replace="")

df = df.with_columns(
    pl.col("name")
    .map_elements(_clean_name, return_dtype=pl.Utf8)
    .str.replace_all(r"\s+", " ")
    .str.strip_chars(" ")
    .alias("name_clean"),
    pl.col("username")
    .map_elements(_clean_name, return_dtype=pl.Utf8)
    .str.replace_all(r"\s+", " ")
    .str.strip_chars(" ")
    .alias("username_clean"),
)
print("  Created name_clean and username_clean columns.")


# =============================================================================
# STEP 7: Location Data Cleanup
# =============================================================================
print("\n" + "=" * 60)
print("STEP 7: Cleaning location data...")
print("=" * 60)

JOKE_REGEX = (
    r"(?i)\b(everywhere|earth|universe|hell|heaven|behind you|your mom|"
    r"your house|your heart|nowhere|the moon|the sun|hogwarts|"
    r"wakanda|narnia|mordor|gotham|bikini bottom|the void|"
    r"in your dreams|under your bed|in your head|idk|"
    r"a galaxy far|nunya|wouldn.t you like to know)\b"
)

def _clean_location(loc: str) -> str:
    """Returns cleaned location or None for garbage entries."""
    if loc is None or loc == "":
        return None
    loc = re.sub(r"\s+", " ", loc).strip()
    if len(loc) < 2:
        return None
    # Entirely emojis
    stripped = emoji.replace_emoji(loc, replace="").strip()
    if not stripped:
        return None
    return loc

# First pass: whitespace + short + emoji-only via map_elements
df = df.with_columns(
    pl.col("location")
    .map_elements(_clean_location, return_dtype=pl.Utf8)
    .alias("location_clean")
)

# Second pass: null out joke locations (native Polars expression)
locs_before = df.select(pl.col("location_clean").is_not_null().sum()).item()
df = df.with_columns(
    pl.when(
        pl.col("location_clean").is_not_null()
        & pl.col("location_clean").str.to_lowercase().str.contains(JOKE_REGEX)
    )
    .then(pl.lit(None, dtype=pl.Utf8))
    .otherwise(pl.col("location_clean"))
    .alias("location_clean")
)
locs_after = df.select(pl.col("location_clean").is_not_null().sum()).item()

locs_had = df.select(pl.col("location").is_not_null().sum()).item()
nulled_locs = locs_had - locs_after
print(f"  Locations nulled out (non-places): {nulled_locs:,}")


# =============================================================================
# STEP 8: Nested Column Parsing
# =============================================================================
print("\n" + "=" * 60)
print("STEP 8: Parsing nested columns...")
print("=" * 60)

def _safe_parse(val):
    if val is None or (isinstance(val, str) and val.strip() == ""):
        return None
    try:
        return ast.literal_eval(str(val))
    except (ValueError, SyntaxError):
        return None

# --- entities.mentions → mention_count ---
print("  Parsing entities.mentions...")

def _mention_count(val) -> int:
    if val is None:
        return 0
    parsed = _safe_parse(val)
    return len(parsed) if isinstance(parsed, list) else 0

df = df.with_columns(
    pl.col("entities.mentions")
    .fill_null("")
    .map_elements(_mention_count, return_dtype=pl.Int64)
    .alias("mention_count")
)

# --- entities.hashtags → hashtag_count + hashtags_list ---
print("  Parsing entities.hashtags...")

def _extract_hashtags(val) -> list:
    if val is None:
        return []
    parsed = _safe_parse(val)
    if isinstance(parsed, list):
        return [item.get("tag", "") for item in parsed if isinstance(item, dict)]
    return []

df = df.with_columns(
    pl.col("entities.hashtags")
    .fill_null("")
    .map_elements(_extract_hashtags, return_dtype=pl.List(pl.Utf8))
    .alias("hashtags_list")
)
df = df.with_columns(
    pl.col("hashtags_list").list.len().alias("hashtag_count")
)

# --- entities.urls → url_count ---
print("  Parsing entities.urls...")

def _url_count(val) -> int:
    if val is None:
        return 0
    parsed = _safe_parse(val)
    return len(parsed) if isinstance(parsed, list) else 0

df = df.with_columns(
    pl.col("entities.urls")
    .fill_null("")
    .map_elements(_url_count, return_dtype=pl.Int64)
    .alias("url_count")
)

# --- entities.annotations → annotation_count ---
print("  Parsing entities.annotations...")

def _annotation_count(val) -> int:
    if val is None:
        return 0
    parsed = _safe_parse(val)
    return len(parsed) if isinstance(parsed, list) else 0

df = df.with_columns(
    pl.col("entities.annotations")
    .fill_null("")
    .map_elements(_annotation_count, return_dtype=pl.Int64)
    .alias("annotation_count")
)

# --- referenced_tweets → tweet_type ---
print("  Parsing referenced_tweets → tweet_type...")

def _tweet_type(val) -> str:
    if val is None:
        return "original"
    parsed = _safe_parse(val)
    if not isinstance(parsed, list) or len(parsed) == 0:
        return "original"
    types = {item.get("type", "") for item in parsed if isinstance(item, dict)}
    if "retweeted" in types:
        return "retweet"
    if "quoted" in types:
        return "quote"
    if "replied_to" in types:
        return "reply"
    return "original"

df = df.with_columns(
    pl.col("referenced_tweets")
    .fill_null("")
    .map_elements(_tweet_type, return_dtype=pl.Utf8)
    .alias("tweet_type")
)

type_dist = df.group_by("tweet_type").agg(pl.len().alias("count")).sort("count", descending=True)
print(f"  Tweet type distribution:")
for row in type_dist.iter_rows():
    print(f"    {row[0]}: {row[1]:,}")

# --- attachments.media_keys → media_count + has_media ---
print("  Parsing attachments.media_keys...")

def _media_count(val) -> int:
    if val is None:
        return 0
    parsed = _safe_parse(val)
    return len(parsed) if isinstance(parsed, list) else 0

df = df.with_columns(
    pl.col("attachments.media_keys")
    .fill_null("")
    .map_elements(_media_count, return_dtype=pl.Int64)
    .alias("media_count")
)
df = df.with_columns(
    (pl.col("media_count") > 0).alias("has_media")
)

media_tweets = df.select(pl.col("has_media").sum()).item()
print(f"  Tweets with media: {media_tweets:,}")


# =============================================================================
# STEP 9: Boolean and Numeric Type Cleanup
# =============================================================================
print("\n" + "=" * 60)
print("STEP 9: Fixing boolean and numeric types...")
print("=" * 60)

# possibly_sensitive → boolean
df = df.with_columns(
    pl.col("possibly_sensitive").cast(pl.Utf8).str.to_lowercase().eq("true").alias("possibly_sensitive")
)
print("  possibly_sensitive → bool")

# public_metrics.* → Int64
metric_cols = [c for c in df.columns if c.startswith("public_metrics.")]
for col in metric_cols:
    df = df.with_columns(
        pl.col(col).cast(pl.Utf8).cast(pl.Int64, strict=False).fill_null(0).alias(col)
    )
    print(f"  {col} → Int64")

# edit_controls.is_edit_eligible → boolean
if "edit_controls.is_edit_eligible" in df.columns:
    df = df.with_columns(
        pl.col("edit_controls.is_edit_eligible")
        .cast(pl.Utf8)
        .str.to_lowercase()
        .eq("true")
        .alias("edit_controls.is_edit_eligible")
    )
    print("  edit_controls.is_edit_eligible → bool")

# edit_controls.edits_remaining → Int64
if "edit_controls.edits_remaining" in df.columns:
    df = df.with_columns(
        pl.col("edit_controls.edits_remaining")
        .cast(pl.Utf8)
        .cast(pl.Int64, strict=False)
        .fill_null(0)
        .alias("edit_controls.edits_remaining")
    )
    print("  edit_controls.edits_remaining → Int64")


# =============================================================================
# STEP 10: Drop Low-Value Columns
# =============================================================================
print("\n" + "=" * 60)
print("STEP 10: Dropping low-value columns...")
print("=" * 60)

total_rows = df.height
null_counts = df.null_count().row(0, named=True)  # dict of {col: null_count}

# For string columns, also count empty strings
fill_rates = {}
for col_name in df.columns:
    nc = null_counts[col_name]
    if df.schema[col_name] == pl.Utf8:
        empty_count = df.select((pl.col(col_name) == "").sum()).item()
        fill_rates[col_name] = (total_rows - nc - (empty_count or 0)) / total_rows
    else:
        fill_rates[col_name] = (total_rows - nc) / total_rows

cols_to_drop = [col for col, rate in fill_rates.items() if rate < 0.03]

# Always drop these
always_drop = ["edit_controls.editable_until", "edit_history_tweet_ids"]
for col in always_drop:
    if col in df.columns and col not in cols_to_drop:
        cols_to_drop.append(col)

print("  Columns dropped (>97% empty or specified):")
for col in cols_to_drop:
    pct = fill_rates.get(col, 0) * 100
    print(f"    {col}: {pct:.1f}% filled")

df = df.drop([c for c in cols_to_drop if c in df.columns])
print(f"  Columns remaining: {len(df.columns)}")


# =============================================================================
# STEP 11: Reply Context Column
# =============================================================================
print("\n" + "=" * 60)
print("STEP 11: Adding reply context column...")
print("=" * 60)

df = df.with_columns(
    pl.col("in_reply_to_user_id").is_not_null().alias("is_reply")
)

reply_count = df.select(pl.col("is_reply").sum()).item()
print(f"  Replies flagged: {reply_count:,}")


# =============================================================================
# STEP 12: Final Validation and Output
# =============================================================================
print("\n" + "=" * 60)
print("STEP 12: Validation and output...")
print("=" * 60)

print("\n--- CLEANING SUMMARY ---")
print(f"  Original rows:        {original_row_count:,}")
print(f"  Final rows:           {df.height:,}")
print(f"  Rows deduplicated:    {dupes_removed:,}")
print(f"  Original columns:     {original_col_count}")
print(f"  Columns dropped:      {len(cols_to_drop)}")
print(f"  Final columns:        {len(df.columns)}")
print(f"  Spam flagged:         {spam_count:,}")
print(f"  Retweets flagged:     {retweet_count:,}")
print(f"  Copypasta flagged:    {copypasta_count:,}")
print(f"  Replies:              {reply_count:,}")

print("\n--- COLUMN DTYPES ---")
for col_name, dtype in df.schema.items():
    print(f"  {col_name}: {dtype}")

print("\n--- NULL PERCENTAGES ---")
null_counts_final = df.null_count().row(0, named=True)
for col_name in df.columns:
    null_pct = null_counts_final[col_name] / df.height * 100
    print(f"  {col_name}: {null_pct:.1f}%")

# Serialize List columns to strings for CSV compatibility
# (Polars CSV writer does not support nested List types)
list_cols = [col for col, dtype in df.schema.items() if dtype == pl.List(pl.Utf8)]
if list_cols:
    print(f"\n  Serializing list columns for CSV: {list_cols}")
    df = df.with_columns(
        [pl.col(c).list.join(", ").alias(c) for c in list_cols]
    )

# Write output
print(f"\nWriting cleaned dataset to: {OUTPUT_PATH}")
df.write_csv(OUTPUT_PATH)
print("  Output file written successfully.")

elapsed = time.time() - start_time
print(f"\nTotal execution time: {elapsed:.1f} seconds")
print("Done.")
