# Talks repo conventions

This directory holds slide decks. Two authoring formats are used:

- **Marp Markdown** (`*.md` with Marp frontmatter, e.g. `template.md`) — native PDF export via `marp <file>.md --pdf`. No extra print setup needed.
- **Custom HTML decks** (`*.html` using the `.deck` / `.slide` engine, e.g. `dllm/dllm.html`, `mia/MIA.html`, `privacy/DP-FL.html`) — single-page apps that show one `.active` slide at a time and scale to viewport via JS.

## Visual identity (all decks)

- **Theme:** White background, Yonsei University Blue (`#003876`) as the primary accent.
- **Logo:** Yonsei emblem (`reference/kor-eng2.png`) on the title slide (top-right corner).
- **Font:** Yonsei official typeface (Light/Bold/Body/Logo TTFs in `reference/fonts/`), with Noto Sans as a web-safe fallback.

## Repo layout

```
reference/                  # canonical design system — single source of truth
  colors_and_type.css       # @font-face (Yonsei) + CSS token variables + base styles
  deck.css                  # slide engine + components
  deck.js                   # scale / nav / progress / brand-footer auto-inject
  deck-skeleton.html        # 5-slide starter (copy via scripts/new-talk.sh)
  kor-eng2.{png,pdf}        # Yonsei emblem (bilingual KOR/ENG lockup)
  fonts/                    # YonseiLight, YonseiBold, YonseiBody, YonseiLogo (TTF)
scripts/
  new-talk.sh               # scaffold <name>/<name>.html from the skeleton
  bundle.py                 # build <name>.standalone.html for distribution
  lint-deck.py              # validate deck against the canonical CSS
<talk>/<talk>.html          # authoring source — <link>s to ../reference/*
```

Only the authoring source (`<talk>.html`) is committed. The `.standalone.html`
bundle is a build artifact — gitignored, produced on demand for distribution.

## When adding or editing slides in a custom HTML deck

- Component vocabulary lives in `reference/deck.css` + `reference/colors_and_type.css`. Reuse existing classes; don't invent new ones unless genuinely new.
- Core classes: `.slide`, `.card`, `.highlight`, `.pill`, `.divider`, `.cols`, `.grid-2`, `.grid-3`, `.math-block`, `.diagram-flow`, `.token-*`, `.toc-*`, `.section-slide.left`, `.end-slide`.
- Math: KaTeX via `$...$` (inline) and `$$...$$` (display). Wrap display math in `<div class="math-block">`.
- Each slide is a `<div class="slide">` inside `#deck`. Default background is white. Active slide has class `active`.
- The title slide includes a `.title-logo` element for the Yonsei emblem (`<img class="title-logo" src="../reference/kor-eng2.png">`).

## Style priorities

1. One idea per slide.
2. Prose emphasis: `**strong**` = Yonsei Blue accent, `*em*` = muted gray.
3. Key insight → `<div class="highlight">` (HTML) or `blockquote` (Marp).
4. Math-heavy slide → `<div class="math-block">…$$…$$…</div>` (HTML) or `$$...$$` (Marp).

## Creating a new talk

```bash
scripts/new-talk.sh <talk-name>
```

Creates `<talk-name>/<talk-name>.html` — the authoring source, which links to `../reference/` for CSS/JS/fonts/logo.

For Marp decks, copy `template.md` and run `marp <file>.md --pdf`.

## Editing workflow

1. Edit `<talk>/<talk>.html`.
2. Open the same file in Chrome to preview — `reference/` must be alongside (it normally is, since both live in this repo).
3. `scripts/lint-deck.py --all` catches unknown classes and hardcoded colors.
4. When shipping / handing off: `scripts/bundle.py <talk>/<talk>.html` produces `<talk>.standalone.html` — the single file you send via email, upload to a conference portal, or stick on a USB stick. It is gitignored; don't commit it.

## Print-to-PDF

`reference/deck.css` includes the `@media print { @page { size: 1280px 720px; margin: 0 } … }` block so `Cmd+P → Save as PDF` produces a one-slide-per-page 1280×720 PDF.

1. Open the deck in Chrome (works on either `<talk>.html` or `<talk>.standalone.html`).
2. `Cmd+P`.
3. Destination: **Save as PDF**.
4. Margins: **None**. Headers/footers: **off**. Background graphics: **on**.
5. Save.

## Truly-offline handoff (standalone bundle)

`scripts/bundle.py <deck.html>` → `<deck>.standalone.html` — a single self-contained HTML with no network dependencies:

- `reference/colors_and_type.css` + `reference/deck.css` inlined as `<style>`.
- Yonsei TTFs base64-inlined into `@font-face`.
- KaTeX CSS + JS + KaTeX fonts fetched from jsdelivr (cached in `scripts/.cache/`) and base64-inlined.
- Logo (`reference/kor-eng2.png`) base64-inlined everywhere it's referenced (including via `data-brand-logo` which `deck.js` reads for the brand-footer).
- Google Fonts (Noto Sans fallback) is stripped from the bundle; the font stack still resolves to Yonsei → Arial.

Run once after each edit to the authoring source. The bundle is ~4 MB (Yonsei fonts + KaTeX); that's expected.
