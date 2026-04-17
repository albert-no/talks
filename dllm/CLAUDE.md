# Slide style spec

All slide work in this directory follows the conventions in `template.md`.

## Visual identity

- **Theme:** White background, Yonsei University Blue (`#003876`) as the primary accent color.
- **Logo:** Yonsei University emblem (`reference/kor-eng2.png`) appears on the title slide (top-right corner).
- **Font:** Noto Sans (300/400/500/600 weights).

## When adding or editing slides in dllm.html

- CSS variables and component classes are defined in the `<style>` block at the top of `dllm.html`. Reuse existing classes; do not invent new ones.
- Component vocabulary: `.slide`, `.card`, `.highlight`, `.pill`, `.divider`, `.cols`, `.grid-2`, `.grid-3`, `.math-block`, `.diagram-flow`, `.token-*`
- Math: KaTeX via `$...$` (inline) and `$$...$$` (display). Wrap display math in `<div class="math-block">`.
- Each slide is a `<div class="slide">` inside `#deck`. Default background is white. Active slide has class `active`.
- The title slide includes a `.title-logo` element for the Yonsei emblem.

## When generating a new talk

Use `template.md` as the Marp source. The style is white background with Yonsei Blue accent. Copy it, replace the content, run `marp <file>.md --pdf`.

## Style priorities

1. One idea per slide.
2. Prose emphasis: `**strong**` = Yonsei Blue accent, `*em*` = muted gray.
3. Key insight → `blockquote` (highlight box).
4. Math heavy slide → use `.math-block` in html, or `$$...$$` in md.
