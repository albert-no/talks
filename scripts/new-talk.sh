#!/usr/bin/env bash
# new-talk.sh — scaffold a new self-contained deck from reference/deck-skeleton.html.
#
# Usage:
#   scripts/new-talk.sh <talk-name>
#
# Creates talks/<talk-name>/<talk-name>.html, inlining the current canonical
# CSS/JS (via scripts/sync-style.py) and fixing the logo path to ../reference/.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $(basename "$0") <talk-name>" >&2
  exit 1
fi

NAME="$1"
# sanitize: lowercase, replace spaces with dashes, strip anything weird
SLUG=$(echo "$NAME" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9-_' '-' | sed -E 's/^-+|-+$//g')

if [[ -z "$SLUG" ]]; then
  echo "error: invalid name '$NAME'" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKELETON="$ROOT/reference/deck-skeleton.html"
TARGET_DIR="$ROOT/$SLUG"
TARGET_HTML="$TARGET_DIR/$SLUG.html"

if [[ ! -f "$SKELETON" ]]; then
  echo "error: skeleton missing at $SKELETON" >&2
  exit 1
fi

if [[ -e "$TARGET_DIR" ]]; then
  echo "error: '$SLUG' already exists at $TARGET_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

# Copy skeleton and rewrite the logo paths from "kor-eng2.png" (skeleton
# lives next to the image) to "../reference/kor-eng2.png" (decks are one
# folder below). Also update the <title>.
python3 - "$SKELETON" "$TARGET_HTML" "$NAME" <<'PY'
import sys, pathlib, re
src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
html = pathlib.Path(src).read_text()
html = html.replace('src="kor-eng2.png"', 'src="../reference/kor-eng2.png"')
html = re.sub(r'data-brand-logo="kor-eng2\.png"',
              'data-brand-logo="../reference/kor-eng2.png"', html)
html = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', html)
pathlib.Path(dst).write_text(html)
PY

# Pull in the latest canonical CSS/JS in case the skeleton is stale.
python3 "$ROOT/scripts/sync-style.py" "$TARGET_HTML"

echo
echo "Created $TARGET_HTML"
echo "Open it in Chrome to preview:"
echo "  open \"$TARGET_HTML\""
