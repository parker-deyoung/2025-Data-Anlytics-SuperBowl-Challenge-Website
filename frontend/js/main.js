// ── DOM refs ──────────────────────────────────────────────────────────────────
const chatToggle   = document.getElementById("chatToggle");
const chatPanel    = document.getElementById("chatPanel");
const chatClose    = document.getElementById("chatClose");
const chatForm     = document.getElementById("chatForm");
const chatInput    = document.getElementById("chatInput");
const chatMessages = document.getElementById("chatMessages");
const sendBtn      = chatForm.querySelector(".chat-panel__send");

// ── Panel open / close ────────────────────────────────────────────────────────
function openPanel() {
  chatPanel.classList.add("is-open");
  chatPanel.setAttribute("aria-hidden", "false");
  chatInput.focus();
}

function closePanel() {
  chatPanel.classList.remove("is-open");
  chatPanel.setAttribute("aria-hidden", "true");
}

chatToggle.addEventListener("click", () => {
  chatPanel.classList.contains("is-open") ? closePanel() : openPanel();
});
chatClose.addEventListener("click", closePanel);

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && chatPanel.classList.contains("is-open")) closePanel();
});

// ── Message helpers ───────────────────────────────────────────────────────────
function appendMessage(text, role) {
  const wrap = document.createElement("div");
  wrap.classList.add("chat-msg", `chat-msg--${role}`);
  const p = document.createElement("p");
  p.textContent = text; // textContent avoids XSS from API response
  wrap.appendChild(p);
  chatMessages.appendChild(wrap);
  scrollBottom();
  return wrap;
}

function appendLoading() {
  const wrap = document.createElement("div");
  wrap.classList.add("chat-msg", "chat-msg--loading");
  wrap.innerHTML = `
    <div class="chat-loading-dots" aria-label="Thinking">
      <span></span><span></span><span></span>
    </div>`;
  chatMessages.appendChild(wrap);
  scrollBottom();
  return wrap;
}

function scrollBottom() {
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// ── Send a message ────────────────────────────────────────────────────────────
chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const message = chatInput.value.trim();
  if (!message) return;

  appendMessage(message, "user");
  chatInput.value = "";
  chatInput.disabled = true;
  sendBtn.disabled = true;

  const loadingEl = appendLoading();

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!res.ok) {
      let detail = `Server error (${res.status})`;
      try {
        const err = await res.json();
        if (err.detail) detail = err.detail;
      } catch (_) {}
      throw new Error(detail);
    }

    const data = await res.json();
    loadingEl.remove();
    appendMessage(data.answer, "bot");
  } catch (err) {
    loadingEl.remove();
    appendMessage("Sorry, I couldn't get an answer right now. Please try again.", "bot");
    console.error("[chatbot]", err);
  } finally {
    chatInput.disabled = false;
    sendBtn.disabled = false;
    chatInput.focus();
  }
});

// Enter submits; Shift+Enter reserved for future multi-line support
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    chatForm.requestSubmit();
  }
});
