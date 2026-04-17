# Talks repo conventions

This directory holds slide decks. Two authoring formats are used:

- **Marp Markdown** (`*.md` with Marp frontmatter, e.g. `template.md`) — native PDF export via `marp <file>.md --pdf`. No extra print setup needed.
- **Custom HTML decks** (`*.html` using the `.deck` / `.slide` engine, e.g. `dllm/dllm.html`, `mia/MIA.html`) — single-page apps that show one `.active` slide at a time and scale to viewport via JS.

## Visual identity (all decks)

- **Theme:** White background, Yonsei University Blue (`#003876`) as the primary accent.
- **Logo:** Yonsei emblem (`reference/kor-eng2.png`) on the title slide (top-right corner).
- **Font:** Noto Sans (300/400/500/600 weights).

## When adding or editing slides in a custom HTML deck

- CSS variables and component classes are defined in the `<style>` block at the top of the deck file. Reuse existing classes; do not invent new ones.
- Component vocabulary: `.slide`, `.card`, `.highlight`, `.pill`, `.divider`, `.cols`, `.grid-2`, `.grid-3`, `.math-block`, `.diagram-flow`, `.token-*`
- Math: KaTeX via `$...$` (inline) and `$$...$$` (display). Wrap display math in `<div class="math-block">`.
- Each slide is a `<div class="slide">` inside `#deck`. Default background is white. Active slide has class `active`.
- The title slide includes a `.title-logo` element for the Yonsei emblem.

## Style priorities

1. One idea per slide.
2. Prose emphasis: `**strong**` = Yonsei Blue accent, `*em*` = muted gray.
3. Key insight → `blockquote` (highlight box).
4. Math-heavy slide → use `.math-block` in HTML, or `$$...$$` in Marp markdown.

## When generating a new talk

- For Marp: copy `template.md`, replace the content, run `marp <file>.md --pdf`.
- For a custom HTML deck: follow the vocabulary above, and **always include the print-to-PDF CSS block below**.

## Print-to-PDF support (required in every custom HTML deck)

The on-screen engine hides all but the `.active` slide and applies a JS `transform` on `.deck`. Without a print stylesheet, `Cmd+P` only prints the current slide. Paste this block verbatim just before `</style>` in every HTML deck so **Chrome → File → Print → Save as PDF** produces a clean one-slide-per-page PDF at 1280×720:

```css
/* ── Print: one slide per page (Cmd+P → Save as PDF) ── */
@media print {
  @page { size: 1280px 720px; margin: 0; }
  html, body { width: 1280px; height: auto; overflow: visible; background: #fff; }
  .deck {
    position: static !important;
    top: auto !important; left: auto !important;
    transform: none !important;
    width: 1280px; height: auto;
  }
  .slide {
    position: relative !important;
    inset: auto !important;
    display: flex !important;
    width: 1280px; height: 720px;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
  }
  .slide:last-of-type { page-break-after: auto; break-after: auto; }
  .slide > * { animation: none !important; }
  .progress-bar, .slide-num { display: none !important; }
}
```

### How to export

1. Open the HTML file in Chrome.
2. `Cmd+P`.
3. Destination: **Save as PDF**.
4. Margins: **None**. Headers/footers: **off**. Background graphics: **on**.
5. Save.

The `@page { size: 1280px 720px }` rule sets the page size automatically; no custom paper-size config needed.
