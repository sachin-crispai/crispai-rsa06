#!/usr/bin/env python3
"""
CrispAI RSA 2026 — Gradio Chat UI
Browser-based chat interface backed by local Ollama, with RSA redbook context.

Usage:
    uv run python scripts/chat-ui.py
    uv run python scripts/chat-ui.py --port 7860
    uv run python scripts/chat-ui.py --model qwen2.5:32b
    DEFAULT_MODEL=qwen2.5:32b uv run python scripts/chat-ui.py

Models:
    qwen2.5:7b   — default, fast (~5 GB VRAM/RAM)
    qwen2.5:32b  — higher quality, slower (~20 GB RAM)
"""

import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

import gradio as gr

# ── Config ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"

MODELS = {
    "qwen2.5:7b":  "Qwen 2.5 7B  — fast, ~5 GB RAM",
    "qwen2.5:32b": "Qwen 2.5 32B — quality, ~20 GB RAM",
}

DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "qwen2.5:7b")

SYSTEM_PROMPT = """You are CrispAI's RSA Conference 2026 field assistant. You have deep knowledge of:
- RSA Conference 2026 (March 23-26, Moscone Center, San Francisco)
- All 24 vendor technology clusters and their key players
- Booth locations (North Hall N- prefix, South Hall S- prefix, ESE- for Early Stage)
- Security technology categories: IAM, Zero Trust, SIEM, EDR/XDR, CNAPP, SOAR, threat intel, etc.
- Key questions to ask vendors at each booth

You are running offline on a local LLM. Be concise, practical, and actionable.
Focus on helping the user navigate the conference floor, compare vendors, and capture useful notes.
When listing vendors, always include booth numbers if known."""


# ── Context loading ───────────────────────────────────────────────────────────
def load_redbook_context() -> str:
    parts = []
    redbook = DOCS_DIR / "redbook" / "rsa_redbook.md"
    if redbook.exists():
        parts.append(f"=== RSA REDBOOK ===\n{redbook.read_text()[:6000]}")
    clusters_dir = DOCS_DIR / "clusters"
    if clusters_dir.exists():
        summaries = []
        for f in sorted(clusters_dir.glob("*.md")):
            summaries.append(f"--- {f.stem} ---\n{f.read_text()[:800]}")
        if summaries:
            parts.append("=== VENDOR CLUSTERS ===\n" + "\n\n".join(summaries))
    return "\n\n".join(parts)


CONTEXT = load_redbook_context()
CONTEXT_LOADED = bool(CONTEXT)


# ── Ollama helpers ────────────────────────────────────────────────────────────
def available_models() -> list[str]:
    """Return list of model names currently pulled in Ollama."""
    try:
        with urllib.request.urlopen(OLLAMA_TAGS_URL, timeout=3) as resp:
            data = json.loads(resp.read().decode())
            names = [m["name"] for m in data.get("models", [])]
            # Filter to known qwen models first, then include others
            known = [n for n in names if n in MODELS]
            others = [n for n in names if n not in MODELS]
            return known + others if (known + others) else list(MODELS.keys())
    except Exception:
        return list(MODELS.keys())


def ollama_chat(message: str, history: list, model: str) -> str:
    """Stream a response from Ollama, yielding partial text."""
    prompt = f"{SYSTEM_PROMPT}\n\nKNOWLEDGE BASE:\n{CONTEXT}\n\n"
    for turn in history[-6:]:
        if turn["role"] == "user":
            prompt += f"User: {turn['content']}\n"
        else:
            prompt += f"Assistant: {turn['content']}\n"
    prompt += f"User: {message}\nAssistant:"

    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": 0.3,
            "num_predict": 1024,
            "num_ctx": 32768,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    tokens = []
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            for line in resp:
                line = line.strip()
                if not line:
                    continue
                chunk = json.loads(line.decode("utf-8"))
                token = chunk.get("response", "")
                tokens.append(token)
                yield "".join(tokens)
                if chunk.get("done"):
                    break
    except urllib.error.URLError:
        yield "Cannot reach Ollama. Start it with: `brew services start ollama` or `ollama serve`"
    except Exception as e:
        yield f"Error: {e}"


# ── Gradio UI ─────────────────────────────────────────────────────────────────
def build_ui() -> gr.Blocks:
    pulled = available_models()
    default = DEFAULT_MODEL if DEFAULT_MODEL in pulled else (pulled[0] if pulled else DEFAULT_MODEL)

    context_status = (
        "RSA redbook loaded" if CONTEXT_LOADED else "No redbook docs found — general chat mode"
    )

    with gr.Blocks(
        title="CrispAI RSA Assistant",
        theme=gr.themes.Soft(primary_hue="red"),
        css="""
        #header { text-align: center; padding: 12px 0 4px; }
        #header h1 { font-size: 1.4rem; margin: 0; }
        #header p  { color: #666; font-size: 0.85rem; margin: 2px 0 0; }
        #status-bar { font-size: 0.78rem; color: #888; text-align: center; padding: 2px 0 8px; }
        """,
    ) as demo:
        gr.HTML("""
        <div id="header">
          <h1>CrispAI RSA 2026 Assistant</h1>
          <p>Offline · Powered by local Ollama · Moscone Center, SF</p>
        </div>
        """)
        gr.HTML(f'<div id="status-bar">Context: {context_status}</div>')

        with gr.Row():
            model_dd = gr.Dropdown(
                choices=pulled,
                value=default,
                label="Model",
                scale=2,
            )
            model_info = gr.Markdown(
                MODELS.get(default, ""),
                label="",
                elem_id="model-info",
            )

        model_dd.change(
            fn=lambda m: MODELS.get(m, ""),
            inputs=model_dd,
            outputs=model_info,
        )

        chatbot = gr.Chatbot(
            label="Chat",
            height=480,
            type="messages",
            show_label=False,
            placeholder="Ask about booths, vendors, clusters, or anything RSA 2026...",
        )

        with gr.Row():
            msg_box = gr.Textbox(
                placeholder='e.g. "Which IAM vendors are in the North Hall?"',
                show_label=False,
                scale=8,
                submit_btn=True,
            )
            clear_btn = gr.Button("Clear", scale=1, variant="secondary")

        # Example prompts
        gr.Examples(
            examples=[
                "What booths are in the North Hall?",
                "Compare CrowdStrike and SentinelOne",
                "What should I ask at the Wiz booth?",
                "Which vendors are in the Zero Trust cluster?",
                "Give me a 10-minute speed-run plan for Day 1",
            ],
            inputs=msg_box,
            label="Quick prompts",
        )

        def respond(message: str, history: list, model: str):
            if not message.strip():
                yield history, ""
                return
            history = history + [{"role": "user", "content": message}]
            history.append({"role": "assistant", "content": ""})
            for partial in ollama_chat(message, history[:-1], model):
                history[-1]["content"] = partial
                yield history, ""

        msg_box.submit(
            fn=respond,
            inputs=[msg_box, chatbot, model_dd],
            outputs=[chatbot, msg_box],
        )
        clear_btn.click(fn=lambda: ([], ""), outputs=[chatbot, msg_box])

    return demo


# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="CrispAI RSA Gradio Chat UI")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help="Override default model (env DEFAULT_MODEL also works)")
    args = parser.parse_args()

    global DEFAULT_MODEL
    DEFAULT_MODEL = args.model

    print(f"CrispAI RSA 2026 — Gradio Chat UI")
    print(f"Model  : {DEFAULT_MODEL}")
    print(f"Context: {'loaded' if CONTEXT_LOADED else 'not found'}")
    print(f"URL    : http://{args.host}:{args.port}")
    print()

    demo = build_ui()
    demo.launch(
        server_name=args.host,
        server_port=args.port,
        inbrowser=True,
        share=False,
    )


if __name__ == "__main__":
    main()
