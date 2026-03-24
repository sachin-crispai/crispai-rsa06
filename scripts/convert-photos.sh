#!/usr/bin/env bash
# CrispAI RSA 2026 — Photo Converter
# Converts iPhone HEIC and Nikon NEF (RAW) photos to JPEG for LLM analysis
# Usage: bash scripts/convert-photos.sh [source_dir] [output_dir]
#
# Dependencies:
#   - sips (built-in macOS) — for HEIC conversion
#   - dcraw (brew install dcraw) — for Nikon NEF conversion

set -e

SOURCE_DIR="${1:-.}"
OUTPUT_DIR="${2:-${SOURCE_DIR}/jpeg}"
RESIZE_WIDTH=1600  # Optimal for LLM vision — fast but high enough detail

BOLD="\033[1m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
RESET="\033[0m"

mkdir -p "$OUTPUT_DIR"

heic_count=0
nef_count=0
jpg_count=0
skip_count=0

echo -e "${BOLD}CrispAI Photo Converter${RESET}"
echo "Source: $SOURCE_DIR"
echo "Output: $OUTPUT_DIR"
echo "Resize width: ${RESIZE_WIDTH}px"
echo "────────────────────────────────"

# ── HEIC (iPhone) → JPEG ──────────────────────────────────────────────────────
while IFS= read -r -d '' file; do
    basename=$(basename "$file" .HEIC)
    basename_lower=$(basename "$file" .heic)
    # handle both .HEIC and .heic
    name="${basename%.*}"
    out="$OUTPUT_DIR/${name}.jpg"

    if [[ -f "$out" ]]; then
        echo -e "  ${YELLOW}skip${RESET}  $name.jpg (exists)"
        ((skip_count++))
        continue
    fi

    echo -e "  ${BLUE}HEIC${RESET}  $(basename "$file") → ${name}.jpg"
    sips -s format jpeg -s formatOptions 85 \
         --resampleWidth $RESIZE_WIDTH \
         "$file" --out "$out" &>/dev/null
    ((heic_count++))
done < <(find "$SOURCE_DIR" -maxdepth 2 \( -iname "*.heic" \) -print0)

# ── NEF (Nikon RAW) → JPEG ────────────────────────────────────────────────────
if command -v dcraw &>/dev/null; then
    while IFS= read -r -d '' file; do
        name=$(basename "$file" .NEF)
        name="${name%.nef}"
        out="$OUTPUT_DIR/${name}.jpg"

        if [[ -f "$out" ]]; then
            echo -e "  ${YELLOW}skip${RESET}  ${name}.jpg (exists)"
            ((skip_count++))
            continue
        fi

        echo -e "  ${BLUE}NEF ${RESET}  $(basename "$file") → ${name}.jpg"
        # dcraw: -c output to stdout, -w use camera white balance, -T TIFF
        # Then sips converts TIFF to JPEG and resizes
        dcraw -c -w -T "$file" 2>/dev/null | \
            sips -s format jpeg -s formatOptions 85 \
                 --resampleWidth $RESIZE_WIDTH \
                 --stdin --out "$out" &>/dev/null || {
            # fallback: direct dcraw JPEG extraction if embedded
            dcraw -e "$file" 2>/dev/null
            thumb="${file%.NEF}.thumb.jpg"
            thumb_lower="${file%.nef}.thumb.jpg"
            [[ -f "$thumb" ]] && mv "$thumb" "$out"
            [[ -f "$thumb_lower" ]] && mv "$thumb_lower" "$out"
        }
        ((nef_count++))
    done < <(find "$SOURCE_DIR" -maxdepth 2 \( -iname "*.nef" \) -print0)
else
    echo -e "${YELLOW}⚠  dcraw not found — skipping NEF files. Run: brew install dcraw${RESET}"
fi

# ── Already-JPEG: just resize if needed ──────────────────────────────────────
while IFS= read -r -d '' file; do
    name=$(basename "$file")
    out="$OUTPUT_DIR/$name"

    # Skip if file is already in output dir
    [[ "$(realpath "$file")" == "$(realpath "$out" 2>/dev/null)" ]] && continue
    [[ -f "$out" ]] && { ((skip_count++)); continue; }

    echo -e "  ${BLUE}JPG ${RESET}  $name → resized"
    sips -s formatOptions 85 \
         --resampleWidth $RESIZE_WIDTH \
         "$file" --out "$out" &>/dev/null
    ((jpg_count++))
done < <(find "$SOURCE_DIR" -maxdepth 1 \( -iname "*.jpg" -o -iname "*.jpeg" \) -print0)

# ── Summary ───────────────────────────────────────────────────────────────────
echo "────────────────────────────────"
echo -e "${GREEN}Done!${RESET}"
echo "  HEIC converted : $heic_count"
echo "  NEF converted  : $nef_count"
echo "  JPEG resized   : $jpg_count"
echo "  Skipped        : $skip_count"
echo ""
echo "Output directory: $OUTPUT_DIR"
echo "Total files: $(ls "$OUTPUT_DIR"/*.jpg 2>/dev/null | wc -l | tr -d ' ')"
echo ""
echo "Next: python scripts/photo-ingest.py $OUTPUT_DIR"
