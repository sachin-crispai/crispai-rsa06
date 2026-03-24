#!/usr/bin/env bash
# CrispAI RSA 2026 — Ollama Chat UI Launcher
# Starts Ollama, ensures models are available, then launches a chat UI.
#
# Usage:
#   bash scripts/launch-chat.sh               # default: Open WebUI
#   bash scripts/launch-chat.sh --ui gradio   # RSA-aware Gradio UI
#   bash scripts/launch-chat.sh --ui openwebui
#   bash scripts/launch-chat.sh --model qwen2.5:32b
#   bash scripts/launch-chat.sh --pull-only   # just ensure models are local
#
# Models managed:
#   qwen2.5:7b   — fast, low RAM (~5GB), good for most queries
#   qwen2.5:32b  — high quality, needs ~20GB RAM, slower first token
#
# Best practices baked in:
#   - Ollama is started if not already running
#   - Models are verified locally before launch (no surprise downloads on-site)
#   - Open WebUI uses uvx (no Docker, no npm required)
#   - Gradio UI includes RSA redbook context from docs/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# ── Defaults ──────────────────────────────────────────────────────────────────
UI="${UI:-openwebui}"
DEFAULT_MODEL="qwen2.5:7b"
OLLAMA_PORT=11434
OPENWEBUI_PORT=8080
GRADIO_PORT=7860

# ── Arg parsing ───────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --ui)       UI="$2"; shift 2 ;;
    --model)    DEFAULT_MODEL="$2"; shift 2 ;;
    --pull-only) PULL_ONLY=1; shift ;;
    -h|--help)
      sed -n '/^# Usage:/,/^$/p' "$0" | head -20
      exit 0 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# ── Helpers ───────────────────────────────────────────────────────────────────
log()  { echo "  $*"; }
ok()   { echo "  ✓ $*"; }
err()  { echo "  ✗ $*" >&2; }
step() { echo; echo "▶ $*"; }

ollama_running() {
  curl -sf "http://localhost:${OLLAMA_PORT}/" >/dev/null 2>&1
}

model_available() {
  ollama list 2>/dev/null | grep -q "^$1"
}

# ── Step 1: Start Ollama ──────────────────────────────────────────────────────
step "Ollama daemon"

if ollama_running; then
  ok "Ollama is already running on port ${OLLAMA_PORT}"
else
  log "Starting Ollama..."
  if command -v brew &>/dev/null && brew services list | grep -q ollama; then
    brew services start ollama
  else
    # Start in background and wait for it
    ollama serve &>/tmp/ollama.log &
    OLLAMA_PID=$!
    log "Waiting for Ollama to be ready (pid ${OLLAMA_PID})..."
    for i in $(seq 1 15); do
      sleep 1
      if ollama_running; then break; fi
      if [[ $i -eq 15 ]]; then
        err "Ollama did not start. Check /tmp/ollama.log"
        exit 1
      fi
    done
  fi
  ok "Ollama started"
fi

# ── Step 2: Verify / pull models ─────────────────────────────────────────────
step "Model availability"

MODELS=("qwen2.5:7b" "qwen2.5:32b")

for model in "${MODELS[@]}"; do
  if model_available "$model"; then
    ok "${model} — available locally"
  else
    echo
    echo "  ⚠  ${model} is NOT pulled locally."
    echo "     Pull it now? This requires internet access."
    read -r -p "     Pull ${model}? [y/N] " yn
    if [[ "${yn,,}" == "y" ]]; then
      ollama pull "$model"
      ok "${model} pulled"
    else
      log "Skipping ${model} — you can pull later with: ollama pull ${model}"
    fi
  fi
done

# Verify the default model we'll use is actually available
if ! model_available "$DEFAULT_MODEL"; then
  err "Default model '${DEFAULT_MODEL}' is not available. Run with a different --model or pull it first."
  exit 1
fi

[[ "${PULL_ONLY:-0}" == "1" ]] && { ok "Pull-only mode done."; exit 0; }

# ── Step 3: Launch UI ─────────────────────────────────────────────────────────
case "${UI}" in

  openwebui|open-webui)
    step "Launching Open WebUI (port ${OPENWEBUI_PORT})"
    if ! command -v uvx &>/dev/null; then
      err "uvx not found. Install uv first: curl -LsSf https://astral.sh/uv/install.sh | sh"
      exit 1
    fi
    log "Starting Open WebUI via uvx..."
    log "This may take a moment on first run (downloads Open WebUI package)."
    echo
    echo "  Open WebUI → http://localhost:${OPENWEBUI_PORT}"
    echo "  Press Ctrl+C to stop."
    echo
    # Point Open WebUI at local Ollama; disable auth for local offline use
    OLLAMA_BASE_URL="http://localhost:${OLLAMA_PORT}" \
    WEBUI_AUTH=false \
      uvx open-webui serve --port "${OPENWEBUI_PORT}"
    ;;

  gradio)
    step "Launching RSA-aware Gradio UI (port ${GRADIO_PORT})"
    if ! command -v uv &>/dev/null; then
      err "uv not found. Install: curl -LsSf https://astral.sh/uv/install.sh | sh"
      exit 1
    fi
    echo
    echo "  Gradio UI → http://localhost:${GRADIO_PORT}"
    echo "  Press Ctrl+C to stop."
    echo
    DEFAULT_MODEL="$DEFAULT_MODEL" uv run python "${SCRIPT_DIR}/chat-ui.py" --port "${GRADIO_PORT}"
    ;;

  *)
    err "Unknown UI: '${UI}'. Use --ui openwebui or --ui gradio"
    exit 1
    ;;

esac
