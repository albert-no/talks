#!/usr/bin/env python3
"""
sync-style.py — re-inline canonical CSS/JS into self-contained deck HTML files.

Source of truth:
  talks/reference/deck.css   -> replaces the block between DECK STYLE BEGIN / END
  talks/reference/deck.js    -> replaces the block between DECK ENGINE BEGIN / END

Outputs stay fully self-contained: other teams can still open the HTML
directly in Chrome with no external dependencies.

Usage:
  scripts/sync-style.py <file.html> [<file.html> ...]
  scripts/sync-style.py --all                # sync every deck in the repo
  scripts/sync-style.py --check <file.html>  # report drift without writing
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_SRC = ROOT / "reference" / "deck.css"
JS_SRC  = ROOT / "reference" / "deck.js"

STYLE_MARK = (
    r"(<!--\s*===\s*DECK STYLE BEGIN[^>]*-->\s*)"
    r"<style>.*?</style>"
    r"(\s*<!--\s*===\s*DECK STYLE END\s*===\s*-->)"
)
ENGINE_MARK = (
    r"(<!--\s*===\s*DECK ENGINE BEGIN[^>]*-->\s*)"
    r"<script>.*?</script>"
    r"(\s*<!--\s*===\s*DECK ENGINE END\s*===\s*-->)"
)


def load_sources() -> tuple[str, str]:
    if not CSS_SRC.exists():
        sys.exit(f"error: missing canonical CSS at {CSS_SRC}")
    if not JS_SRC.exists():
        sys.exit(f"error: missing canonical JS at {JS_SRC}")
    return CSS_SRC.read_text(), JS_SRC.read_text()


def substitute(html: str, css: str, js: str) -> tuple[str, dict]:
    """Return (new_html, summary) where summary tracks what got replaced."""
    summary = {"style": False, "engine": False, "missing_markers": []}

    def _style_repl(m: re.Match) -> str:
        summary["style"] = True
        return f"{m.group(1)}<style>\n{css.rstrip()}\n</style>{m.group(2)}"

    def _engine_repl(m: re.Match) -> str:
        summary["engine"] = True
        return f"{m.group(1)}<script>\n{js.rstrip()}\n</script>{m.group(2)}"

    new_html, n_style = re.subn(STYLE_MARK, _style_repl, html, count=1, flags=re.S)
    new_html, n_engine = re.subn(ENGINE_MARK, _engine_repl, new_html, count=1, flags=re.S)

    if n_style == 0:
        summary["missing_markers"].append("DECK STYLE BEGIN/END")
    if n_engine == 0:
        summary["missing_markers"].append("DECK ENGINE BEGIN/END")

    return new_html, summary


def discover_decks() -> list[Path]:
    decks: list[Path] = []
    decks.append(ROOT / "reference" / "deck-skeleton.html")
    for sub in sorted(ROOT.iterdir()):
        if not sub.is_dir() or sub.name.startswith((".", "_")):
            continue
        if sub.name in {"reference", "scripts"}:
            continue
        for html in sorted(sub.glob("*.html")):
            decks.append(html)
    return [d for d in decks if d.exists()]


def sync_one(path: Path, css: str, js: str, *, check: bool) -> int:
    original = path.read_text()
    updated, summary = substitute(original, css, js)

    if summary["missing_markers"]:
        print(f"!!  {path.relative_to(ROOT)}: missing markers — {', '.join(summary['missing_markers'])}")
        return 2

    if updated == original:
        print(f"ok  {path.relative_to(ROOT)}: already in sync")
        return 0

    if check:
        print(f"DRIFT  {path.relative_to(ROOT)}: would update (style={summary['style']}, engine={summary['engine']})")
        return 1

    path.write_text(updated)
    what = []
    if summary["style"]: what.append("style")
    if summary["engine"]: what.append("engine")
    print(f"synced  {path.relative_to(ROOT)}: {' + '.join(what)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", help="HTML files to sync")
    ap.add_argument("--all", action="store_true", help="sync every deck in the repo")
    ap.add_argument("--check", action="store_true", help="report drift without writing")
    args = ap.parse_args()

    css, js = load_sources()

    if args.all:
        targets = discover_decks()
    else:
        if not args.files:
            ap.error("pass one or more HTML files, or --all")
        targets = [Path(f).resolve() for f in args.files]

    worst = 0
    for t in targets:
        if not t.exists():
            print(f"!!  {t}: does not exist")
            worst = max(worst, 2)
            continue
        worst = max(worst, sync_one(t, css, js, check=args.check))
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
