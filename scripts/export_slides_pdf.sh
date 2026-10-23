#!/usr/bin/env bash
# Export Reveal.js decks to PDF (GitHub-viewable).
# AI-assisted / AI-generated with Cursor (Grok, Anthropic, and OpenAI models).
# Direction: Alan J. Coppola.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT="${SLIDES_PORT:-18765}"
SIZE="${SLIDES_SIZE:-1920x1080}"

if [[ ! -x "$CHROME" ]]; then
  echo "Google Chrome not found at $CHROME" >&2
  exit 1
fi

python3 -m http.server "$PORT" --bind 127.0.0.1 \
  --directory "$ROOT/presentations" >/tmp/slides-http.log 2>&1 &
SERVER_PID=$!
cleanup() { kill "$SERVER_PID" 2>/dev/null || true; }
trap cleanup EXIT
for _ in 1 2 3 4 5 6 7 8 9 10; do
  if curl -sf -o /dev/null "http://127.0.0.1:${PORT}/invariants-quinn-witt-dabrowski/index.html"; then
    break
  fi
  sleep 0.3
done
if ! curl -sf -o /dev/null "http://127.0.0.1:${PORT}/invariants-quinn-witt-dabrowski/index.html"; then
  echo "HTTP server failed to serve slides; log:" >&2
  cat /tmp/slides-http.log >&2
  exit 1
fi

export_one() {
  local rel="$1"
  local out="$2"
  local url="http://127.0.0.1:${PORT}/${rel}"
  echo "Exporting $url -> $out"
  npx --yes decktape@3.14.0 \
    --chrome-path "$CHROME" \
    -s "$SIZE" \
    --load-pause 2500 \
    reveal "$url" "$out"
}

export_one \
  "invariants-quinn-witt-dabrowski/index.html" \
  "$ROOT/presentations/invariants-quinn-witt-dabrowski/invariants-quinn-witt-dabrowski.pdf"

export_one \
  "padic-homology-2026/index.html" \
  "$ROOT/presentations/padic-homology-2026/padic-homology-2026.pdf"

echo "Done."
