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

## Font sizes — don't fight the canonical scale

`reference/deck.css` owns the type scale: `h1` 3.6rem · `h2` 2.7rem · `h3` 1.85rem · `p`, `li` 1.55rem · `.small` 1.15rem · `.tiny` 0.95rem · `.math-block` 1.7rem. These are tuned for readability from the back of a lecture hall and must not be shadowed by a per-deck `<style>` block.

- **Don't** redefine `p`, `li`, `h1`, `h2`, `h3`, `.small`, `.tiny`, `.subtitle`, or `.math-block` `font-size` in a deck's inline `<style>`. If you find such overrides in an existing deck, delete them — they're the usual cause of "the fonts look small."
- **Do** size component-internal text (card body, `.paper-card .desc`, `.sr-box p`, SVG label text, etc.) in roughly the `1.05rem–1.35rem` range. Express sizes as fractions of the canonical body, not absolute pixels.
- When a slide feels cramped, cut content or split the slide — never shrink the type.

**Readability reference.** Kangwook Lee's BLISS seminar deck (<https://kangwooklee.com/talks/2026_03_BLISS/bliss_seminar.html>) is the minimum-acceptable visual weight. Zoomed-in captures: `reference/kangwook1.png`–`kangwook4.png`. If your deck renders noticeably smaller than those, check for canonical-token overrides first. See `DESIGN_SYSTEM.md §1.2` and §5.2 for the full rule.

## Authoring gotchas (learned the hard way)

These are the pitfalls that have eaten the most time. Do not re-learn them.

- **Don't override `.slide` positioning.** Canonical `.slide` is `position: absolute; inset: 0`. Child elements with `position: absolute` already anchor to the slide — you never need to add `style="position:relative"` to the slide itself. Doing so defeats `inset:0`, so the slide stops filling the deck and the auto-injected `.brand-footer` lands somewhere unpredictable.
- **Bottom-left is reserved for the brand footer.** `deck.js` injects `.brand-footer` at `bottom:18px; left:28px` on every content slide. When you absolute-position decorative content (images, floats, overlays) inside a slide, anchor to `right` and/or `top` — not `bottom-left` — and leave ~40 px of clear space at the bottom-left corner.
- **SVG `<text>` does not render KaTeX.** Auto-render walks the HTML DOM; SVG text is opaque to it, so `$g_1$` in an SVG `<text>` shows as the literal string `$g_1$`. When a diagram needs math-rendered labels, build it as HTML (flex/grid layout, div "boxes", CSS-styled circles) and use a thin SVG overlay for the arrows. See `privacy/DP-FL.html` slides 4, 9, 30 for the pattern (`.fl4-*`, `.ldp-*`, `.rdm-*`).
- **Use `$$…$$` (display math) for multi-row `\begin{cases}` / `\begin{align}`.** Inline `$…$` with `\displaystyle` can wrap or size unpredictably inside a narrow column. `$$…$$` inside a `.math-block` is the reliable form and guarantees the declaration stays on one line with the rows stacked inside.
- **Don't hack around overflow with `white-space:nowrap; overflow-x:auto`** on a math-block. The equation gets clipped at the right edge. Fix the content: shorten cases labels to math (`m \in \text{top-}k`, `\text{else}`), use `\dfrac` → `\tfrac` when you want less vertical weight, or split the slide.
- **Prefer static step-labeled diagrams over continuous animation.** For talks, auto-cycling animations (SMIL `animateMotion`, CSS keyframes) keep the audience waiting for the next frame. Show every step at once with ①②③④ badges on the relevant elements; the speaker controls the pacing. Keep animation for self-paced web versions only.
- **Descriptions shouldn't duplicate diagram equations.** If the diagram labels show `$g_i = \nabla\ell(\theta; D_i)$`, the description on the other side of the slide should just say "local gradient" in plain English. One artifact owns the math; the other owns the narrative.
- **Cut content, don't shrink type.** "Page X has text overflow" is a signal to trim the slide, not to reduce `font-size`. Drop bullets, split into two slides, or remove the section entirely. The canonical scale exists so speakers at the back of a lecture hall can read everything — preserve it.
- **Keep `data-screen-label` values in sync with actual slide position** when inserting or removing slides; they drive the on-screen slide label UI. Stale labels aren't fatal but they're confusing during review.
- **`bundle.py` onload gotcha (fixed 2026-04):** the KaTeX `renderMathInElement` invocation lives inside an `onload="..."` attribute that contains `'` characters. The bundler's regex must treat double- and single-quoted attributes as alternatives (`onload=(?:"([^"]*)"|'([^']*)')`) — not `[^"']+` — or the handler gets truncated at the first inner quote and no math renders in the standalone.

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
