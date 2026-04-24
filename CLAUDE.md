# Talks repo conventions

This directory holds slide decks. Two authoring formats are used:

- **Marp Markdown** (`*.md` with Marp frontmatter, e.g. `template.md`) — native PDF export via `marp <file>.md --pdf`. No extra print setup needed.
- **Custom HTML decks** (`*.html` using the `.deck` / `.slide` engine, e.g. `dllm/dllm.html`, `mia/mia1-foundations.html`, `privacy/DP-FL.html`) — single-page apps that show one `.active` slide at a time and scale to viewport via JS.

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

**Priority 0 (highest, overrides all others): the Font-sizes rule below.** Any time another rule or instinct would push you toward shrinking text — adding `.small` / `.tiny` to prose, inline `font-size` overrides, cramming to avoid a slide split — Priority 0 wins. When in doubt, cut content or split the slide.

1. One idea per slide.
2. **The speaker narrates; the slide is a visual anchor.** Slides carry abstract phrases and key terms, not full explanatory sentences. Drop narrative connectors ("This means…", "In other words…", "It is important to note…") and soft qualifiers ("essentially", "actually", "basically"). Target telegraphic noun phrases over complete sentences. See `DESIGN_SYSTEM.md §7.12` for the full rule.
3. Prose emphasis: `**strong**` = Yonsei Blue accent, `*em*` = muted gray.
4. Key insight → `<div class="highlight">` (HTML) or `blockquote` (Marp).
5. Math-heavy slide → `<div class="math-block">…$$…$$…</div>` (HTML) or `$$...$$` (Marp).
6. Paper attribution → `<div class="cite">` footnote at the bottom. See `DESIGN_SYSTEM.md §2.19`.

## Font sizes — the strongest rule in this file

**This is Priority 0.** When any other rule or instinct pushes you toward shrinking text, this one wins. Re-read before every deck edit.

`reference/deck.css` owns the type scale: `h1` 3.6rem · `h2` 2.7rem · `h3` 1.85rem · `p`, `li` 1.55rem · `.math-block` 1.7rem · `.cite` 0.85rem. The `.small` (1.15rem) and `.tiny` (0.95rem) classes exist in the CSS but are off-limits to authors outside the narrow slot below. Tuned for the back row of a lecture hall.

**Binary rule: important → body size; non-important → `.cite` or off-slide.** "Important" = the audience should read it during the talk. "Non-important" = the audience can follow without reading it (they'll catch it later from the printed slides). On-slide, only two slots permit sub-body text: `.cite` citations and `.small` diagram sub-labels.

- **`.tiny` is banned.** Everywhere. Even "check it later" text shouldn't require squinting at a printed handout.
- **`.small` on prose is banned.** Not on `<p>`, `<li>`, captions, summary remarks, side notes, or text inside `.highlight` / `.card` / `.cols` / `.grid-*` / `.math-block` / under a `<table>`. If a sentence is important enough to put on the slide, it's important enough to render at body size.
- **Citations → `<div class="cite">` only** (§2.19 of `DESIGN_SYSTEM.md`). Any citation-shaped `<p class="small">Author et al., "Title", Venue Year</p>` converts to `.cite`.
- **`.small` inside a diagram** (`.diagram-box`, `.diagram-flow`) is the one other allowed slot, and **only when both** (a) the content is a non-crucial sub-label the audience can follow without reading and (b) compressing the label to body size breaks the layout. Default: body size inside diagrams too. Before reaching for `.small`, try to compress the label or delete it (speaker narrates).
- **Non-important prose that isn't a citation or diagram sub-label doesn't belong on the slide.** Move it to the per-slide appendix / speaker-notes file.
- **Never** put inline `style="font-size:..."` overrides on prose. The canonical scale is the entire vocabulary.
- **Never** redefine `p`, `li`, `h1`, `h2`, `h3`, `.subtitle`, `.cite`, `.small`, `.tiny`, or `.math-block` `font-size` in a deck's inline `<style>` block.
- **Component-internal text** (pill labels, token chips, code blocks) stays at its native compact size — these are design elements, not prose.
- **When a slide feels cramped, cut content or split the slide. Use as many slides as you need.** The canonical scale is non-negotiable; there is no slide budget. One idea per slide and if two ideas are fighting, split them.

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
- **Cut content, don't shrink type.** "Page X has text overflow" is a signal to trim the slide, not to reduce `font-size`. Drop bullets, split into two slides, or remove the section entirely. **There is no slide budget — split as many times as you need.** The canonical scale exists so speakers at the back of a lecture hall can read everything — preserve it. For what sub-body text is permitted on a slide, see §"Font sizes — the strongest rule" above.
- **Write for verbal narration, not self-service reading.** The speaker explains context and transitions; the slide carries the key terms and the math. Rewrite full sentences to telegraphic noun phrases ("The attack achieves high precision, meaning most positive predictions are correct" → "High precision: most positives correct"). Drop narrative connectors ("This means…", "In other words…", "As we will see…") and soft qualifiers ("essentially", "actually", "basically"). Target ~40–60% word reduction when cleaning up a wordy deck. After rewriting, strip every `class="small"` / `class="tiny"` from prose and every inline `font-size:…` override that existed to cope with overflow — shorter content fits canonical sizes. See `DESIGN_SYSTEM.md §7.12`.
- **Paper attribution goes in a bottom footnote, not a side card.** When a slide is about a specific paper, put the citation in a `<div class="cite">Author(s), "Title", Venue Year</div>` at the bottom. Don't waste half the slide on a 2-column layout where the right column is a card holding the paper title in `<em>"…"</em>`. One citation per slide; informal is fine. Keep the author `.pill` at the top for section context, but put `.cite` only on the paper-overview slide (not every follow-up slide about the same paper). See `DESIGN_SYSTEM.md §2.19` and §7.13.
- **KaTeX delimiter escape in `onload` — use `\\(` not `\(`.** The `renderMathInElement(document.body,{delimiters:[…]})` call lives inside an HTML `onload="…"` attribute, so strings pass through two layers of parsing (HTML → JS). The LaTeX delimiters must be written `'\\('`, `'\\)'`, `'\\['`, `'\\]'`. A single backslash (`'\('`) gets silently eaten by the JS string parser as an unrecognized escape, leaving KaTeX with bare `(`, `)`, `[`, `]` as delimiters — every parenthesized or bracketed phrase in the deck then renders as italic math with no word spacing (`(learned or heuristic)` → italic `learnedorheuristic`, `[M]` in a token chip → slanted math `M` at a different height than neighboring word tokens). The canonical handler is in `reference/deck-skeleton.html`; match it exactly. Audit: `grep -c "'\\\\(" *.html` should return 0 across all decks.
- **Never use italic for prose.** Yonsei has no italic face (all four TTFs are `font-style: normal`), and Noto Sans Italic isn't loaded either. Browsers fake italic by oblique-skewing normal glyphs, which collapses kerning. `em` is globally pinned to `font-style: normal; color: var(--gray-text)` — don't use `<i>`, don't set `font-style: italic`. In LaTeX math, wrap English phrases in `\text{…}`; bare `all positions` in math mode renders each letter as an italic math variable with zero inter-letter spacing.
- **Avoid em-dashes in slide prose.** Don't use `—` (em-dash), `–` (en-dash), or `--` (double-hyphen) as a general connector in titles, subtitles, bullets, cards, or captions. The dash reads as a pause in print but at slide sizes it either (a) forces an awkward line break between the dash and the second clause or (b) leaves whichever side is shorter dangling as an orphan. Rewrite instead: a colon (`:`), a comma, a period, or parentheses almost always reads better. The only exceptions are tight technical glyphs where the dash is part of the name (`7–8B scale`, `fill-in-the-middle`) or an arrow (`→`, `↔`). When converting existing text, read the sentence aloud — if the dash is doing the work of a colon ("X: it does Y"), use a colon; if it's parenthetical ("X (the reason being Y)"), use parens; if it's a full stop in disguise, split into two sentences.
- **Avoid dangling single words at the end of a line.** `deck.css` now sets `text-wrap: pretty` on `p` / `li` / `.small` / `.tiny` and `text-wrap: balance` on `h1` / `h2` / `h3` / `.subtitle`, which prevents most orphans automatically. When a stubborn orphan remains (usually a bullet where the last 1–2 words wrap to their own line), fix the content first: shorten the bullet, split the sentence, or restructure. Last resort: glue the final two or three words with `&nbsp;` (non-breaking space) so the wrapper moves them together. Don't force-break with `<br>` as a workaround — that creates fragility at different column widths. Also watch for em-dash constructions which are the single most common cause of orphans: rewriting `"X — Y"` as `"X: Y"` almost always fixes the orphan on its own.
- **Never land `<br>` immediately after a `-`.** `Neyman-<br>Pearson` or `ML-as-a-<br>Service` leaves a dangling hyphen that reads as a broken syllable. Keep hyphenated compounds on one line, or rename to a hyphen-free label (`ML-as-a-Service` → `Cloud ML APIs`).
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
