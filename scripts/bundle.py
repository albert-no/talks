#!/usr/bin/env python3
"""
bundle.py — build a truly-offline <deck>.standalone.html from a deck HTML file.

Inlines into a single self-contained file:
  - Local stylesheets + scripts (reference/colors_and_type.css, reference/deck.css,
    reference/deck.js, etc.) as inline <style>/<script>.
  - Remote stylesheets + scripts (KaTeX CDN) fetched and inlined, with nested
    url(...) font references recursively inlined as base64 data URIs.
  - Yonsei TTF @font-face references: TTFs base64-inlined.
  - <img src="..."> local images: base64-inlined as data: URIs.
  - data-brand-logo="..." on <body>: inlined so reference/deck.js's footer
    injection still works without the original PNG on disk.

Google Fonts (Noto Sans fallback) is stripped from the bundle; the stack
still falls through to Yonsei → Arial.

Remote fetches are cached in scripts/.cache/ keyed by URL.

Usage:
  scripts/bundle.py <deck.html>               # -> <deck>.standalone.html
  scripts/bundle.py --all                     # every deck in the repo
"""

from __future__ import annotations
import argparse
import base64
import hashlib
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(__file__).resolve().parent / ".cache"
UA_HEADERS = {
    # KaTeX jsdelivr returns .woff2 regardless, but set a real UA just in case.
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    ),
}

MIME = {
    ".woff2": "font/woff2",
    ".woff":  "font/woff",
    ".ttf":   "font/ttf",
    ".otf":   "font/otf",
    ".png":   "image/png",
    ".jpg":   "image/jpeg",
    ".jpeg":  "image/jpeg",
    ".gif":   "image/gif",
    ".svg":   "image/svg+xml",
    ".webp":  "image/webp",
}


def guess_mime(ref: str) -> str:
    ext = "." + ref.split("?")[0].rsplit(".", 1)[-1].lower()
    return MIME.get(ext, "application/octet-stream")


def fetch_bytes(ref: str, base_dir: Path, base_url: str | None = None) -> tuple[bytes, str]:
    """Return (bytes, resolved_source) for a URL or local relative path."""
    # Normalize protocol-relative URL.
    if ref.startswith("//"):
        ref = "https:" + ref
    if ref.startswith(("http://", "https://")):
        return _fetch_remote(ref)
    # Relative to a remote CSS?
    if base_url and base_url.startswith(("http://", "https://")):
        full = urllib.parse.urljoin(base_url, ref)
        return _fetch_remote(full)
    # Local path.
    p = (base_dir / ref).resolve()
    return p.read_bytes(), str(p)


def _fetch_remote(url: str) -> tuple[bytes, str]:
    CACHE.mkdir(exist_ok=True)
    h = hashlib.sha256(url.encode()).hexdigest()[:16]
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", url)[-80:]
    cache_file = CACHE / f"{h}_{safe}"
    if not cache_file.exists():
        req = urllib.request.Request(url, headers=UA_HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            cache_file.write_bytes(r.read())
    return cache_file.read_bytes(), url


def to_data_uri(data: bytes, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"


def inline_css(css: str, base_dir: Path, base_url: str | None = None) -> str:
    """Inline @import and url(...) references into the given CSS text."""

    # Drop Google Fonts @imports — truly-offline uses Yonsei → Arial fallback.
    css = re.sub(
        r"@import\s+url\(\s*['\"]?https?://fonts\.googleapis\.com[^)]+\)\s*;?",
        "/* google-fonts @import stripped by bundle.py */",
        css,
    )
    css = re.sub(
        r"@import\s+['\"]https?://fonts\.googleapis\.com[^'\"]+['\"]\s*;?",
        "/* google-fonts @import stripped by bundle.py */",
        css,
    )

    # Recurse into other @imports.
    def _import_repl(m: re.Match) -> str:
        ref = m.group(1).strip()
        try:
            data, src = fetch_bytes(ref, base_dir, base_url)
            inner = data.decode("utf-8", errors="replace")
            new_base_dir = base_dir if src.startswith(("http://", "https://")) else Path(src).parent
            new_base_url = src if src.startswith(("http://", "https://")) else None
            return f"/* inlined @import {ref} */\n{inline_css(inner, new_base_dir, new_base_url)}\n"
        except Exception as e:
            return f"/* @import skipped ({e}): {ref} */"

    css = re.sub(r"@import\s+url\(\s*['\"]?([^'\")]+)['\"]?\s*\)\s*;?", _import_repl, css)
    css = re.sub(r"@import\s+['\"]([^'\"]+)['\"]\s*;?", _import_repl, css)

    # Inline url(...) references (fonts, images).
    def _url_repl(m: re.Match) -> str:
        ref = m.group(1).strip()
        if ref.startswith("data:") or ref.startswith("#"):
            return m.group(0)
        try:
            data, src = fetch_bytes(ref, base_dir, base_url)
            return f"url({to_data_uri(data, guess_mime(src))})"
        except Exception as e:
            print(f"    warn: url({ref}) kept as-is ({e})", file=sys.stderr)
            return m.group(0)

    css = re.sub(r"url\(\s*['\"]?([^'\")]+?)['\"]?\s*\)", _url_repl, css)
    return css


RE_LINK_CSS = re.compile(
    r'<link\b(?=[^>]*\brel=["\']stylesheet["\'])[^>]*>', re.IGNORECASE
)
RE_LINK_HREF = re.compile(r'\bhref=["\']([^"\']+)["\']', re.IGNORECASE)
RE_SCRIPT_SRC = re.compile(
    r'<script\b(?=[^>]*\bsrc=["\'][^"\']+["\'])[^>]*>\s*</script>',
    re.IGNORECASE | re.DOTALL,
)
RE_SCRIPT_ATTR_SRC = re.compile(r'\bsrc=["\']([^"\']+)["\']', re.IGNORECASE)
RE_SCRIPT_ONLOAD = re.compile(r'\bonload=(?:"([^"]*)"|\'([^\']*)\')', re.IGNORECASE)
RE_IMG = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
RE_IMG_SRC = re.compile(r'\bsrc=["\']([^"\']+)["\']', re.IGNORECASE)
RE_BRAND = re.compile(r'(\bdata-brand-logo=)["\']([^"\']+)["\']', re.IGNORECASE)


def bundle(html_path: Path, out_path: Path) -> None:
    html = html_path.read_text()
    base_dir = html_path.parent

    # 1. Stylesheets — <link rel="stylesheet" href="...">
    def _link_repl(m: re.Match) -> str:
        tag = m.group(0)
        href_m = RE_LINK_HREF.search(tag)
        if not href_m:
            return tag
        href = href_m.group(1)
        # Skip google fonts — we drop Noto Sans fallback for offline builds.
        if "fonts.googleapis.com" in href:
            return "<!-- bundle: dropped google-fonts link -->"
        try:
            data, src = fetch_bytes(href, base_dir)
            css_text = data.decode("utf-8", errors="replace")
            base_url = src if src.startswith(("http://", "https://")) else None
            css_base_dir = base_dir if base_url else Path(src).parent
            inlined = inline_css(css_text, css_base_dir, base_url)
            return f"<style>\n/* bundled from {href} */\n{inlined}\n</style>"
        except Exception as e:
            return f"<!-- bundle: failed to inline {href}: {e} -->{tag}"

    html = RE_LINK_CSS.sub(_link_repl, html)

    # 2. Scripts — <script src="..."></script>
    def _script_repl(m: re.Match) -> str:
        tag = m.group(0)
        src_m = RE_SCRIPT_ATTR_SRC.search(tag)
        if not src_m:
            return tag
        src = src_m.group(1)
        try:
            data, _ = fetch_bytes(src, base_dir)
            js = data.decode("utf-8", errors="replace")
        except Exception as e:
            return f"<!-- bundle: failed to inline {src}: {e} -->{tag}"
        out = f"<script>\n/* bundled from {src} */\n{js}\n</script>"
        # Preserve onload handlers: run them after the inlined script loads,
        # guarded by DOMContentLoaded so document.body exists.
        onload_m = RE_SCRIPT_ONLOAD.search(tag)
        if onload_m:
            handler = (onload_m.group(1) or onload_m.group(2) or "").replace("</script>", "<\\/script>")
            out += (
                "\n<script>"
                "if (document.readyState === 'loading') "
                "document.addEventListener('DOMContentLoaded', function(){"
                f"{handler}"
                "}); else { "
                f"{handler}"
                " }</script>"
            )
        return out

    html = RE_SCRIPT_SRC.sub(_script_repl, html)

    # 3. <img src="LOCAL"> → data URI
    def _img_repl(m: re.Match) -> str:
        tag = m.group(0)
        s = RE_IMG_SRC.search(tag)
        if not s:
            return tag
        v = s.group(1)
        if v.startswith(("http://", "https://", "data:")):
            return tag
        try:
            data, src = fetch_bytes(v, base_dir)
            return tag[:s.start(1)] + to_data_uri(data, guess_mime(src)) + tag[s.end(1):]
        except Exception as e:
            print(f"    warn: <img src={v}> kept as-is ({e})", file=sys.stderr)
            return tag

    html = RE_IMG.sub(_img_repl, html)

    # 4. data-brand-logo="LOCAL" → data URI (deck.js reads this attribute)
    def _brand_repl(m: re.Match) -> str:
        prefix, val = m.group(1), m.group(2)
        if val.startswith(("http://", "https://", "data:")):
            return m.group(0)
        try:
            data, src = fetch_bytes(val, base_dir)
            return f'{prefix}"{to_data_uri(data, guess_mime(src))}"'
        except Exception:
            return m.group(0)

    html = RE_BRAND.sub(_brand_repl, html)

    out_path.write_text(html)
    size_kb = out_path.stat().st_size / 1024
    print(f"bundled  {html_path.relative_to(ROOT) if ROOT in html_path.parents else html_path.name}"
          f"  →  {out_path.name}  ({size_kb:.0f} KB)")


def discover_decks() -> list[Path]:
    decks: list[Path] = []
    for sub in sorted(ROOT.iterdir()):
        if not sub.is_dir() or sub.name.startswith((".", "_")):
            continue
        if sub.name in {"reference", "scripts", "design"}:
            continue
        for html in sorted(sub.glob("*.html")):
            if html.name.endswith(".standalone.html"):
                continue
            decks.append(html)
    return decks


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", help="deck HTML files")
    ap.add_argument("--all", action="store_true", help="bundle every deck in the repo")
    args = ap.parse_args()

    if args.all:
        targets = discover_decks()
    else:
        if not args.files:
            ap.error("pass a deck HTML or --all")
        targets = [Path(f).resolve() for f in args.files]

    for t in targets:
        if not t.exists():
            print(f"!!  {t}: does not exist", file=sys.stderr)
            continue
        if t.name.endswith(".standalone.html"):
            print(f"skip {t.name}: already a standalone bundle")
            continue
        out = t.parent / f"{t.stem}.standalone.html"
        bundle(t, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
