#!/usr/bin/env python3
"""
CrispAI RSA 2026 — Booth Photo Analyzer
Analyzes booth photos using local Ollama vision LLM (qwen2.5vl:7b)
and appends structured notes to docs/field-notes/photo-log.md

Usage:
    python scripts/photo-ingest.py <photo.jpg>          # single photo
    python scripts/photo-ingest.py <directory/>         # batch all JPEGs
    python scripts/photo-ingest.py booth.jpg --day 2    # tag with day number
"""

import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import urllib.request
import urllib.error

REPO_ROOT = Path(__file__).parent.parent
PHOTO_LOG = REPO_ROOT / "docs" / "field-notes" / "photo-log.md"
OLLAMA_URL = "http://localhost:11434/api/chat"
VISION_MODEL = "qwen2.5vl:7b"

PROMPT = """You are analyzing a photo taken at RSA Conference 2026 at Moscone Center, San Francisco.

Look at this booth photo and extract:
1. Company/vendor name (look for banners, signage, badges, booth numbers)
2. Booth number if visible (format: N-XXXX, S-XXXX, ESE-XX, or numeric)
3. Primary product or service being showcased (1 sentence)
4. Key technology stack or category (e.g., EDR, IAM, SIEM, Cloud Security, etc.)
5. Any notable messaging, taglines, or demos visible
6. Anything interesting or unique about the booth/demo

Respond in this exact JSON format:
{
  "vendor": "Company Name or Unknown",
  "booth": "booth number or Unknown",
  "product": "one-sentence description",
  "category": "security category",
  "messaging": "key tagline or message visible",
  "notes": "anything interesting or unique"
}

If you cannot determine something, use "Unknown" for that field.
Only respond with the JSON object, no other text."""


def encode_image(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_photo(image_path: Path) -> dict:
    """Send image to local Ollama vision model and return structured result."""
    image_b64 = encode_image(image_path)

    payload = json.dumps({
        "model": VISION_MODEL,
        "messages": [{"role": "user", "content": PROMPT, "images": [image_b64]}],
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 512,
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            raw_text = result.get("message", {}).get("content",
                        result.get("response", "")).strip()

            # Extract JSON from response (handle markdown code blocks)
            json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            else:
                return {
                    "vendor": "Parse Error",
                    "booth": "Unknown",
                    "product": raw_text[:200],
                    "category": "Unknown",
                    "messaging": "",
                    "notes": "Could not parse structured response"
                }
    except urllib.error.URLError:
        print("  ✗ Cannot reach Ollama. Start it with:")
        print("    OLLAMA_FLASH_ATTENTION=1 /opt/homebrew/opt/ollama/bin/ollama serve")
        sys.exit(1)
    except json.JSONDecodeError as e:
        return {
            "vendor": "JSON Error",
            "booth": "Unknown",
            "product": f"JSON decode error: {e}",
            "category": "Unknown",
            "messaging": "",
            "notes": ""
        }


def append_to_log(image_path: Path, analysis: dict, day: int):
    """Append analysis result to photo-log.md."""
    filename = image_path.name

    row = (
        f"| {filename} "
        f"| {analysis.get('vendor', 'Unknown')} "
        f"| {analysis.get('booth', 'Unknown')} "
        f"| {analysis.get('category', 'Unknown')} "
        f"| {analysis.get('product', '')[:80]} "
        f"| {analysis.get('notes', '')[:60]} |\n"
    )

    log_content = PHOTO_LOG.read_text() if PHOTO_LOG.exists() else ""
    day_header = f"## Day {day} —"

    if day_header in log_content:
        lines = log_content.split("\n")
        insert_idx = None
        in_section = False
        for i, line in enumerate(lines):
            if day_header in line:
                in_section = True
            elif in_section and line.startswith("## ") and day_header not in line:
                insert_idx = i
                break
        if insert_idx:
            lines.insert(insert_idx, row.rstrip())
        else:
            lines.append(row.rstrip())
        PHOTO_LOG.write_text("\n".join(lines))
    else:
        with open(PHOTO_LOG, "a") as f:
            f.write(f"\n## Day {day} — {datetime.now().strftime('%A, %B %d')}\n\n")
            f.write("| File | Vendor | Booth | Category | Product | Notes |\n")
            f.write("|------|--------|-------|----------|---------|-------|\n")
            f.write(row)


def process_photo(image_path: Path, day: int, verbose: bool = True):
    if not image_path.exists():
        print(f"  ✗ File not found: {image_path}")
        return None

    if verbose:
        print(f"\n📸 Analyzing: {image_path.name}")
        print("   Sending to qwen2.5vl:7b (Metal GPU)...")

    analysis = analyze_photo(image_path)
    append_to_log(image_path, analysis, day)

    if verbose:
        print(f"   Vendor   : {analysis.get('vendor', 'Unknown')}")
        print(f"   Booth    : {analysis.get('booth', 'Unknown')}")
        print(f"   Category : {analysis.get('category', 'Unknown')}")
        print(f"   Product  : {analysis.get('product', '')[:80]}")
        if analysis.get("notes"):
            print(f"   Notes    : {analysis.get('notes', '')[:80]}")
        print(f"   ✓ Logged to photo-log.md")

    return analysis


def main():
    parser = argparse.ArgumentParser(
        description="Analyze RSA booth photos with local LLM vision"
    )
    parser.add_argument("target", help="Photo file or directory of photos")
    parser.add_argument("--day", type=int, default=1,
                        help="Conference day number (1-4, default: 1)")
    parser.add_argument("--model", default=VISION_MODEL,
                        help=f"Ollama vision model (default: {VISION_MODEL})")
    args = parser.parse_args()

    target = Path(args.target)
    day = args.day

    print(f"CrispAI RSA 2026 — Photo Analyzer")
    print(f"Model : {args.model}")
    print(f"Day   : {day}")
    print("─" * 40)

    if target.is_dir():
        photos = sorted([
            p for p in target.iterdir()
            if p.suffix.lower() in {".jpg", ".jpeg"}
        ])
        if not photos:
            print(f"No JPEG files found in {target}")
            print("Run convert-photos.sh first to convert HEIC/NEF files.")
            sys.exit(1)

        print(f"Found {len(photos)} photos to analyze\n")
        results = []
        for photo in photos:
            result = process_photo(photo, day)
            if result:
                results.append(result)

        print(f"\n{'─' * 40}")
        print(f"✓ Analyzed {len(results)}/{len(photos)} photos")
        print(f"✓ Results logged to: {PHOTO_LOG}")

    elif target.is_file():
        process_photo(target, day)
    else:
        print(f"✗ Target not found: {target}")
        sys.exit(1)


if __name__ == "__main__":
    main()
