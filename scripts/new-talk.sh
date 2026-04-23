#!/usr/bin/env bash
# new-talk.sh — scaffold a new deck from reference/deck-skeleton.html.
#
# Usage:
#   scripts/new-talk.sh <talk-name>
#
# Creates <talk-name>/<talk-name>.html, with <link>/<script> refs pointing
# at ../reference/. Run scripts/bundle.py later to produce the
# <talk-name>.standalone.html distribution bundle.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $(basename "$0") <talk-name>" >&2
  exit 1
fi

NAME="$1"
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

# Copy skeleton; rewrite relative paths from reference/-local to ../reference/,
# and set the title.
python3 - "$SKELETON" "$TARGET_HTML" "$NAME" <<'PY'
import sys, pathlib, re
src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
html = pathlib.Path(src).read_text()
html = html.replace('href="colors_and_type.css"', 'href="../reference/colors_and_type.css"')
html = html.replace('href="deck.css"',            'href="../reference/deck.css"')
html = html.replace('src="deck.js"',              'src="../reference/deck.js"')
html = html.replace('src="kor-eng2.png"',         'src="../reference/kor-eng2.png"')
html = re.sub(r'data-brand-logo="kor-eng2\.png"',
              'data-brand-logo="../reference/kor-eng2.png"', html)
html = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', html)
pathlib.Path(dst).write_text(html)
PY

echo
echo "Created $TARGET_HTML"
echo "Preview in Chrome:   open \"$TARGET_HTML\""
echo "Ship as standalone:  python3 $ROOT/scripts/bundle.py \"$TARGET_HTML\""
