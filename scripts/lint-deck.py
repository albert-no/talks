#!/usr/bin/env python3
"""
lint-deck.py — validate a deck HTML against the talks design system.

Checks:
  1. Expected <link>/<script> references to reference/colors_and_type.css,
     reference/deck.css, reference/deck.js are present.
  2. Classes used in the body are all defined in reference/deck.css or
     reference/colors_and_type.css (minus a small allow-list).
  3. No hardcoded colors in inline style="..." attributes — prefer var(--…).

Exit codes: 0 clean, 1 warnings, 2 errors.

Usage:
  scripts/lint-deck.py <file.html> [<file.html> ...]
  scripts/lint-deck.py --all
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_DECK = ROOT / "reference" / "deck.css"
CSS_TYPE = ROOT / "reference" / "colors_and_type.css"
JS_SRC   = ROOT / "reference" / "deck.js"

ALLOW_CLASSES = {
    "katex", "katex-display", "katex-html", "katex-mathml",
    "active", "deck", "filled", "no-footer",
}

ALLOW_INLINE_COLORS = {
    "transparent", "inherit", "currentcolor", "none",
}


def extract_classes(*css_sources: str) -> set[str]:
    out: set[str] = set()
    for css in css_sources:
        out.update(re.findall(r"\.([A-Za-z_][A-Za-z0-9_-]*)", css))
    return out


def classes_used(body: str) -> set[str]:
    tokens: set[str] = set()
    for attr in re.findall(r'class="([^"]+)"', body):
        tokens.update(attr.split())
    return tokens


def style_attr_colors(body: str) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    pat = re.compile(r"(#[0-9A-Fa-f]{3,8}\b|rgb[a]?\([^\)]+\)|hsl[a]?\([^\)]+\))")
    for m in re.finditer(r'style="([^"]+)"', body):
        offset = m.start(1)
        for c in pat.finditer(m.group(1)):
            val = c.group(0)
            if val.lower() in ALLOW_INLINE_COLORS:
                continue
            ln = body.count("\n", 0, offset + c.start()) + 1
            hits.append((ln, val))
    return hits


def lint_one(path: Path, defined_classes: set[str]) -> int:
    html = path.read_text()
    rel = path.relative_to(ROOT) if ROOT in path.parents else path
    errors: list[str] = []
    warnings: list[str] = []

    is_standalone = path.name.endswith(".standalone.html")

    if not is_standalone:
        # Expect canonical <link>/<script> refs.
        required = [
            (r'href="[^"]*colors_and_type\.css"',  "colors_and_type.css link"),
            (r'href="[^"]*deck\.css"',             "deck.css link"),
            (r'src="[^"]*deck\.js"',               "deck.js script"),
        ]
        for pat, name in required:
            if not re.search(pat, html):
                errors.append(f"missing expected {name}")

    body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
    body = body_match.group(1) if body_match else ""

    # Include classes defined inside the deck's own <style> blocks.
    local_styles = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    all_defined = defined_classes | extract_classes(local_styles)

    used = classes_used(body)
    unknown = {c for c in used if c not in all_defined and c not in ALLOW_CLASSES}
    if unknown:
        warnings.append(f"unknown classes (define in reference/deck.css or remove): {sorted(unknown)}")

    hits = style_attr_colors(body)
    if hits:
        ex = "; ".join(f"line~{ln}: {v}" for ln, v in hits[:5])
        warnings.append(
            f"hardcoded colors in inline style= ({len(hits)} occurrence(s)); prefer var(--…). e.g. {ex}"
        )

    if not errors and not warnings:
        print(f"ok    {rel}")
        return 0

    status = "ERROR " if errors else "warn  "
    print(f"{status}{rel}")
    for e in errors:
        print(f"  [error] {e}")
    for w in warnings:
        print(f"  [warn ] {w}")
    return 2 if errors else 1


def discover() -> list[Path]:
    paths: list[Path] = [ROOT / "reference" / "deck-skeleton.html"]
    for sub in sorted(ROOT.iterdir()):
        if not sub.is_dir() or sub.name.startswith((".", "_")):
            continue
        if sub.name in {"reference", "scripts", "design"}:
            continue
        for html in sorted(sub.glob("*.html")):
            if html.name.endswith(".standalone.html"):
                continue
            paths.append(html)
    return [p for p in paths if p.exists()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if not CSS_DECK.exists() or not JS_SRC.exists() or not CSS_TYPE.exists():
        sys.exit("error: canonical reference files missing")

    defined = extract_classes(CSS_DECK.read_text(), CSS_TYPE.read_text())

    if args.all:
        targets = discover()
    else:
        if not args.files:
            ap.error("pass one or more HTML files, or --all")
        targets = [Path(f).resolve() for f in args.files]

    worst = 0
    for t in targets:
        if not t.exists():
            print(f"ERROR {t}: does not exist")
            worst = max(worst, 2)
            continue
        worst = max(worst, lint_one(t, defined))
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
