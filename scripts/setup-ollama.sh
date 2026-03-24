#!/usr/bin/env bash
# CrispAI RSA 2026 — Local LLM Setup
# Installs Ollama + pulls models for offline on-site use
# Run this BEFORE the conference while on WiFi
# Optimized for Apple Silicon M4

set -e

BOLD="\033[1m"
GREEN="\033[32m"
YELLOW="\033[33m"
RESET="\033[0m"

echo -e "${BOLD}CrispAI RSA 2026 — Local LLM Setup${RESET}"
echo "======================================"
echo "Target: Apple Silicon M4"
echo "Models: qwen2.5:7b (text) + llama3.2-vision:11b (photos)"
echo ""

# ── 1. Install Ollama ──────────────────────────────────────────────────────────
if command -v ollama &>/dev/null; then
    echo -e "${GREEN}✓ Ollama already installed: $(ollama --version)${RESET}"
else
    echo -e "${YELLOW}→ Installing Ollama via Homebrew...${RESET}"
    brew install ollama
    echo -e "${GREEN}✓ Ollama installed${RESET}"
fi

# ── 2. Install dcraw for Nikon NEF conversion ─────────────────────────────────
if command -v dcraw &>/dev/null; then
    echo -e "${GREEN}✓ dcraw already installed${RESET}"
else
    echo -e "${YELLOW}→ Installing dcraw (Nikon RAW converter)...${RESET}"
    brew install dcraw
    echo -e "${GREEN}✓ dcraw installed${RESET}"
fi

# ── 3. Start Ollama service ────────────────────────────────────────────────────
echo -e "${YELLOW}→ Starting Ollama service...${RESET}"
brew services start ollama 2>/dev/null || ollama serve &>/dev/null &
sleep 3
echo -e "${GREEN}✓ Ollama service running${RESET}"

# ── 4. Pull text reasoning model ──────────────────────────────────────────────
echo ""
echo -e "${YELLOW}→ Pulling qwen2.5:7b (text model, ~4.7GB)...${RESET}"
echo "  This is your offline research assistant and redbook chatbot."
ollama pull qwen2.5:7b
echo -e "${GREEN}✓ qwen2.5:7b ready${RESET}"

# ── 5. Pull vision model ───────────────────────────────────────────────────────
echo ""
echo -e "${YELLOW}→ Pulling llama3.2-vision:11b (vision model, ~7.9GB)...${RESET}"
echo "  This analyzes your booth photos from iPhone and Nikon camera."
ollama pull llama3.2-vision:11b
echo -e "${GREEN}✓ llama3.2-vision:11b ready${RESET}"

# ── 6. Verify ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}Models installed:${RESET}"
ollama list

echo ""
echo -e "${BOLD}${GREEN}Setup complete!${RESET}"
echo ""
echo "Usage:"
echo "  # Chat with redbook offline:"
echo "  ./scripts/crisp-rsa 'Which booths are in the North Hall?'"
echo ""
echo "  # Convert photos (iPhone HEIC + Nikon NEF → JPEG):"
echo "  bash scripts/convert-photos.sh ~/Desktop/RSA-Day1/"
echo ""
echo "  # Analyze a booth photo:"
echo "  python scripts/photo-ingest.py booth_photo.jpg"
echo ""
echo -e "${YELLOW}Disk space used:${RESET}"
du -sh ~/.ollama/models/ 2>/dev/null || echo "  (models dir not found yet)"
