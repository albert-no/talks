# Slide style spec

All slide work in this directory follows the conventions in `template.md`.

## When adding or editing slides in dllm.html

- CSS variables and component classes are defined in the `<style>` block at the top of `dllm.html`. Reuse existing classes; do not invent new ones.
- Component vocabulary: `.slide`, `.card`, `.highlight`, `.pill`, `.divider`, `.cols`, `.grid-2`, `.grid-3`, `.math-block`, `.diagram-flow`, `.token-*`
- Math: KaTeX via `$...$` (inline) and `$$...$$` (display). Wrap display math in `<div class="math-block">`.
- Each slide is a `<div class="slide [bg-*]">` inside `#deck`. Active slide has class `active`.
- Background classes: `bg-navy`, `bg-dark`, `bg-deep`, `bg-light`, `bg-accent`.

## When generating a new talk

Use `template.md` as the Marp source. The style is minimal (white background, single blue accent). Copy it, replace the content, run `marp <file>.md --pdf`.

## Style priorities

1. One idea per slide.
2. Prose emphasis: `**strong**` = blue accent, `*em*` = muted gray.
3. Key insight → `blockquote` (highlight box).
4. Math heavy slide → use `.math-block` in html, or `$$...$$` in md.
