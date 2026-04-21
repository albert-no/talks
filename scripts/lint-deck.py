#!/usr/bin/env python3
"""
lint-deck.py — validate a self-contained deck HTML against the talks design system.

Checks performed:
  1. Markers present: DECK STYLE BEGIN/END and DECK ENGINE BEGIN/END.
  2. In-sync: the marked style/script blocks match reference/deck.css and
     reference/deck.js (byte-level comparison with collapsed trailing whitespace).
  3. Classes used in the <body> markup are all defined in the canonical CSS
     (minus a tiny allow-list of third-party KaTeX classes).
  4. No hardcoded colors in `style="…"` attributes outside an allow-list.
     Prefer CSS variables (var(--…)) or tokens.

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
CSS_SRC = ROOT / "reference" / "deck.css"
JS_SRC  = ROOT / "reference" / "deck.js"

STYLE_BLOCK = re.compile(
    r"<!--\s*===\s*DECK STYLE BEGIN[^>]*-->\s*<style>(.*?)</style>\s*"
    r"<!--\s*===\s*DECK STYLE END\s*===\s*-->",
    re.S,
)
ENGINE_BLOCK = re.compile(
    r"<!--\s*===\s*DECK ENGINE BEGIN[^>]*-->\s*<script>(.*?)</script>\s*"
    r"<!--\s*===\s*DECK ENGINE END\s*===\s*-->",
    re.S,
)

# Third-party / framework classes we don't define ourselves, plus
# JS-semantic markers consumed by reference/deck.js (e.g. no-footer).
ALLOW_CLASSES = {
    "katex", "katex-display", "katex-html", "katex-mathml",
    "active", "deck", "filled",  # state modifiers are OK as class tokens
    "no-footer",                 # opt-out marker for brand-footer auto-inject
}

# Colors allowed to appear literally in inline style=.
ALLOW_INLINE_COLORS = {
    "transparent", "inherit", "currentcolor", "none",
}


def extract_classes(css: str) -> set[str]:
    # Match selectors like .foo, .foo-bar, .foo.bar — return any token after a dot.
    return set(re.findall(r"\.([A-Za-z_][A-Za-z0-9_-]*)", css))


def classes_used(body_html: str) -> set[str]:
    tokens: set[str] = set()
    for attr in re.findall(r'class="([^"]+)"', body_html):
        tokens.update(attr.split())
    return tokens


def style_attr_colors(body_html: str) -> list[tuple[int, str]]:
    """Return (approx_lineno, offending_fragment) for color hardcodes."""
    hits: list[tuple[int, str]] = []
    color_pat = re.compile(
        r"(#[0-9A-Fa-f]{3,8}\b|rgb[a]?\([^\)]+\)|hsl[a]?\([^\)]+\))"
    )
    for m in re.finditer(r'style="([^"]+)"', body_html):
        chunk = m.group(1)
        offset = m.start(1)
        for c in color_pat.finditer(chunk):
            value = c.group(0)
            if value.lower() in ALLOW_INLINE_COLORS:
                continue
            # rough line number
            lineno = body_html.count("\n", 0, offset + c.start()) + 1
            hits.append((lineno, value))
    return hits


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def lint_one(path: Path, canonical_css: str, canonical_js: str) -> int:
    html = path.read_text()
    rel = path.relative_to(ROOT) if ROOT in path.parents else path
    errors: list[str] = []
    warnings: list[str] = []

    style_m = STYLE_BLOCK.search(html)
    engine_m = ENGINE_BLOCK.search(html)

    if not style_m:
        errors.append("missing DECK STYLE BEGIN/END markers")
    if not engine_m:
        errors.append("missing DECK ENGINE BEGIN/END markers")

    if style_m:
        embedded = normalize(style_m.group(1))
        if embedded != normalize(canonical_css):
            warnings.append("style block drifted from reference/deck.css — run sync-style.py")
    if engine_m:
        embedded_js = normalize(engine_m.group(1))
        if embedded_js != normalize(canonical_js):
            warnings.append("engine block drifted from reference/deck.js — run sync-style.py")

    body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
    body = body_match.group(1) if body_match else ""
    defined = extract_classes(canonical_css)
    used = classes_used(body)
    unknown = {c for c in used if c not in defined and c not in ALLOW_CLASSES}
    if unknown:
        warnings.append(f"unknown classes used (define in reference/deck.css or remove): {sorted(unknown)}")

    color_hits = style_attr_colors(body)
    if color_hits:
        examples = "; ".join(f"line~{ln}: {frag}" for ln, frag in color_hits[:5])
        warnings.append(
            f"hardcoded colors in inline style= ({len(color_hits)} occurrence(s)); prefer var(--…). e.g. {examples}"
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
        if sub.name in {"reference", "scripts"}:
            continue
        for html in sorted(sub.glob("*.html")):
            paths.append(html)
    return [p for p in paths if p.exists()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if not CSS_SRC.exists() or not JS_SRC.exists():
        sys.exit("error: canonical reference/deck.css or deck.js missing")

    canonical_css = CSS_SRC.read_text()
    canonical_js = JS_SRC.read_text()

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
        worst = max(worst, lint_one(t, canonical_css, canonical_js))
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
