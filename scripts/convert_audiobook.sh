#!/usr/bin/env bash
# Convert lucid dreaming audiobook AIFF files to web-friendly MP3.
# Usage: ./scripts/convert_audiobook.sh

set -euo pipefail

SRC="${1:-/Users/ryanhamilton/pythonenv/lucid dream book/book_tts_audio}"
OUT="$(cd "$(dirname "$0")/.." && pwd)/assets/lucid-dreaming/audio"

mkdir -p "$OUT"

FILES=(
  "copyright.aiff"
  "dedication.aiff"
  "01-the-art-and-science-of-lucid-dreaming.aiff"
  "02-build-dream-recall-the-foundation-of-lucidity.aiff"
  "03-reality-checks-and-awareness-training.aiff"
  "04-wake-back-to-bed-w-b-t-b-working-with-your-sleep.aiff"
  "05-m-i-l-d-mnemonic-induction-of-lucid-dreams.aiff"
  "06-digital-dreamwork-using-technology-strategically.aiff"
  "07-integrating-lucid-dreaming-into-your-life.aiff"
  "08-targeted-dream-incubation.aiff"
  "09-w-i-l-d-and-the-hypnagogic-doorway.aiff"
  "10-staying-lucid-stabilization-and-depth.aiff"
  "11-lucid-encounters-with-fear.aiff"
  "12-the-range-of-lucid-dreaming.aiff"
  "13-sleep-quality-the-foundation-under-lucid-dreamin.aiff"
  "glossary.aiff"
  "references.aiff"
)

for f in "${FILES[@]}"; do
  base="${f%.aiff}"
  echo "Converting $f..."
  ffmpeg -y -i "$SRC/$f" -codec:a libmp3lame -b:a 64k -ac 1 -ar 22050 "$OUT/${base}.mp3" -loglevel error
done

echo "Done. $(ls -1 "$OUT"/*.mp3 | wc -l | tr -d ' ') MP3 files in $OUT"
du -sh "$OUT"
