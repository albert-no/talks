# Pitfalls and lessons learned

Issues that have eaten time. Search here before re-debugging.

## Fonts look small → canonical tokens were shadowed

Symptom: body / headings render smaller than the Kangwook reference (`reference/kangwook*.png`) or smaller than a sibling deck.

Cause: a per-deck `<style>` redefined `p`, `li`, `h2`, `h3`, `.small`, `.tiny`, `.subtitle`, or `.math-block` `font-size`. Canonical values in `reference/deck.css` are tuned for back-of-room readability after the JS scale transform.

Fix: delete the override. Component-scoped sizes (e.g. `.sr-box p`, `.paper-card .desc`) at `1.05–1.35rem` are fine; canonical tokens are off-limits.

## Brand footer drifts → a slide opted out of `inset: 0`

Symptom: "Yonsei University" wordmark moves or disappears on specific slides.

Cause: that slide has inline `style="position:relative"`. Canonical `.slide` is `position: absolute; inset: 0` — overriding to `relative` breaks the fill, so the auto-injected `.brand-footer` lands somewhere unpredictable. Children with `position: absolute` already anchor to the slide; you don't need to force `relative`.

Fix: remove the `position:relative`. Anchor decorative content to `right`/`top` and leave bottom-left clear (~40 px) for the footer.

## Bottom-left is reserved for the brand footer

`deck.js` injects `.brand-footer` at `bottom:18px; left:28px` on every content slide. Decorative content absolute-positioned in the bottom-left corner collides with it.

Fix: anchor decorative content (images, floats, overlays) to `right` and/or `top`. Leave ~40 px clear in the bottom-left.

## `$g_1$` shows as literal text → label is in SVG `<text>`

Symptom: math inside a diagram renders as `$g_1$` instead of italic *g* with a subscript.

Cause: KaTeX auto-render walks the HTML DOM but doesn't descend into SVG text nodes.

Fix: build diagram structure in HTML (flex/grid layout, div boxes, CSS-styled circles) with a thin SVG overlay for arrows only. Pattern: `.fl4-*` (slide 4), `.ldp-*` (slide 9), `.rdm-*` (slide 30) in `privacy/DP-FL.html`.

## `\begin{cases}` clipped at right edge

Symptom: right column of cases (typically "otherwise") cut off.

Cause: math-block uses `$\displaystyle …$` with `white-space:nowrap; overflow-x:auto`. The forced layout overflows.

Fix: use `$$…$$` (display math) inside a plain `.math-block` — KaTeX sizes naturally. Shorten case labels: `m \in \text{top-}k` instead of long English; `\text{else}` instead of `\text{otherwise}`. If still doesn't fit → cut a bullet (Priority 2).

## Wide single-line math-block clips at right edge

Symptom: a `.math-block` extends past the slide right boundary or pushes the brand footer.

Cause: long single-line equations from `\quad`/`\qquad` separators stacking inseparable fragments, universal-quantifier preambles (`\forall S, \forall x`), or verbose annotations (`\text{(loss on } x\text{)}`).

Fix:
- **Drop universal quantifiers** when implicit from context (most theorem statements).
- **Use `,` not `\qquad`** to separate stacked definitions: `D_1 = D \cup \{x\}, \quad D_0 = D \setminus \{x\}` — not `\qquad`.
- **Drop side annotations** that the speaker can narrate (e.g., `(loss on $x$)` after `T(x) = \ell(f_\theta, x)`).
- **Cut the `- 0`** and similar always-true terms (`(\bar D - 0)/s` → `\bar D / s`).
- If still wide after compression, split into two `.math-block`s on consecutive lines, or split the slide.

## Tables with KaTeX in cells overflow horizontally

Symptom: a multi-column `<table>` with math (e.g., `$\max_c f_\theta(x)_c$`) extends past the slide right edge — sometimes past the slide rectangle entirely.

Cause: KaTeX widens cell content unpredictably; the browser can't compress columns past their math width. A 3rd column is often redundant.

Fix:
- **Cap at 2 columns** when KaTeX is in cells. If a 3rd column duplicates info from the first (e.g., "Signal" describing what "Test Statistic" already implies), merge or drop.
- **Cap at ~6 rows** total (header + 5 data). More → split or move the rest to the note file.
- A table is one exhibit. Adding `.math-block` + `.highlight` on the same slide breaks Priority 2 — see the visual element budget in `DESIGN_SYSTEM.md` → Priority 2.

## `.diagram-flow` inside `.cols` or `.grid-*` wraps ugly

Symptom: 3+ `.diagram-box` elements inside a 1/2 or 1/3-width column wrap onto multiple rows; combined with `<br>` in box labels (e.g., `Genomic<br>Databases`), boxes become 2-line cramped rectangles.

Cause: `.diagram-flow` is `display: flex; flex-wrap: wrap`. In a narrow container the boxes wrap; the `<br>` inside labels then stacks each box vertically. Result: a 2D mess.

Fix:
- **`.diagram-flow` always goes at full slide width** — never inside `.cols` or `.grid-*` or wrapped in a `.card` that lives in a column.
- Put bullets / prose above (full width), then `.diagram-flow` below (full width). Or vice versa.
- **Single-line labels in `.diagram-box`** — `Genomic DBs` not `Genomic<br>Databases`. If the label genuinely needs a second word, drop the `<br>` and let the box grow horizontally.
- For 4+ boxes that won't fit in one horizontal line at full slide width, switch to a vertical layout (one box per row) or split across slides.

## "Three ingredients:" → that prose belongs in the title

Symptom: a slide reads `<h2>The Attack Setup</h2>` then `<p>Three ingredients:</p>` then a `.grid-3` with 3 cards. The `<p>` is doing the work the title should do.

Cause: the title was written as a topic label (`"The Attack Setup"`) and the structural prose (`"Three ingredients:"`) was added to introduce the cards. They duplicate function.

Fix: make the structural prose the title — `<h2>Three Ingredients</h2>` — and delete the `<p>`. Saves a line and tightens the ghost-deck arc. Same pattern for `"Three steps:"` → `<h2>Three Steps</h2>`, `"Common test statistics:"` → `<h2>Common Test Statistics</h2>`, etc.

## Animation in live talks waits for the audience

Symptom: speaker is forced to pause for an animation loop.

Cause: SMIL `animateMotion` / CSS keyframe cycles dictate pacing the speaker doesn't control.

Fix: keep diagrams static with ①②③④ badges; speaker narrates the sequence. For **proof intuition build-ups**, use multi-slide progression instead of CSS animation — duplicate the slide N times, recolor one more step into Yonsei Blue per copy, leave upcoming steps in `--gray-text`. Speaker advances at their own pace; the audience gets the same build-up animation would have given, without the loop. Pattern documented in `DESIGN_SYSTEM.md` → Math-heavy → Build-up. Auto-cycling animation is fine only for self-paced web versions.

## Description duplicates diagram equations

Symptom: diagram labels show `$g_i = \nabla\ell(\theta; D_i)$` and the description on the other side of the slide repeats the same equation in plain English.

Fix: one artifact owns the math, the other owns the narrative. If the diagram has the equation, the description just says "local gradient".

## Parenthesized text renders as italic math → KaTeX delimiter escape bug

Symptom: `(learned or heuristic)` renders as italic `learnedorheuristic`; `[M]` in a token chip is slanted at the wrong height.

Cause: the KaTeX `onload` handler must double-escape LaTeX delimiters. The handler lives inside an HTML `onload="…"` attribute, so strings pass through HTML and JS string parsing. With single backslashes (`'\('`), the JS parser eats `\(` as an unrecognized escape, leaving KaTeX with bare `(`, `)`, `[`, `]` as delimiters — every parenthesized phrase becomes inline math.

```html
<!-- correct: double backslash -->
{left:'\\(',right:'\\)',display:false},
{left:'\\[',right:'\\]',display:true}

<!-- wrong: silently broken -->
{left:'\(',right:'\)',display:false},
```

`reference/deck-skeleton.html` has the canonical handler; match it exactly. Audit: `grep -c "'\\\\(" *.html` should be ≥ 1 per deck.

## Italic prose collapses spaces → Yonsei has no italic face

Symptom: a phrase rendered with `<i>` or inline `font-style: italic` reads as glued letters (e.g. "all positions" → "allpositions").

Cause: Yonsei TTFs are all `font-style: normal`; Noto Sans is loaded without italic. The browser synthesizes oblique by skewing normal glyphs ~12°, which inherits upright metrics and breaks kerning.

Fix:
- No `<i>`, no inline `font-style: italic`. `em` is globally `font-style: normal; color: var(--gray-text)` — that *is* the muted look. Use `<strong>` (Yonsei Blue) for emphasis.
- In KaTeX math, English phrases go in `\text{…}`. Bare `all positions` in math mode renders each letter as italic math with zero inter-letter space. Identifier letters stay italic — correct math typography.
- If non-math prose still renders italic, suspect the KaTeX delimiter bug above.

## Em-dashes break lines awkwardly → use colons / commas / parens

Symptom: `"X — Y"` wraps with the dash on its own line, or one clause orphans a single word.

Cause: em-dash (`—`), en-dash (`–`), and double-hyphen (`--`) are strong wrap points at slide font sizes.

Fix: rewrite the connector. Colon for definitions/expansions. Comma for soft pause. Period for full stop. Parens for asides. Keep dashes only as part of a technical glyph (`7–8B`, `fill-in-the-middle`, arrows `→`, `↔`). Audit: `grep -nE ' — | -- | – ' <deck>.html` should be ~empty.

## Dangling single words at end of line

Symptom: a bullet ending in "…in <2 years" wraps "years" or "2 years" alone; an h3 reading "Architectural inductive biases" lands "biases" on line 2.

Fix, in order:
1. **Trust CSS first.** `text-wrap: pretty` / `balance` rebalance most orphans automatically.
2. **Remove em-dashes** in the line — most common structural cause.
3. **Shorten or restructure.** Trim a redundant qualifier, split, or reword.
4. **Glue with `&nbsp;`** — e.g., `in &lt;2&nbsp;years` so the last two tokens wrap together. Sparingly, only for technical phrases that must stay together.
5. **Never use `<br>` as orphan-shim.** Fragile across widths and prints oddly. (Priority 1 step 2b *does* permit `<br>` at a deliberate internal clause boundary inside one sentence — that's a different use.)

## `<br>` after a hyphen orphans the hyphen

Symptom: `Neyman-<br>Pearson` renders as `Neyman-` / `Pearson`. Trailing hyphen reads as a broken syllable.

Fix: keep the compound on one line (let the box grow), or rename to a hyphen-free label (`ML-as-a-Service` → `Cloud ML APIs`).

## Standalone bundle renders raw `$...$` strings

Symptom: `<deck>.standalone.html` shows literal math; the authoring source renders fine.

Cause (fixed 2026-04): `scripts/bundle.py` regex `onload=["\']([^"\']+)["\']` treated either quote as terminator, so the KaTeX handler was truncated at the first inner `'`.

Fix in code: regex now uses alternation — `onload=(?:"([^"]*)"|'([^']*)')`. Verify after bundling: `chrome --headless --dump-dom <standalone>.html | grep -c 'class="katex"'` should be ≥ 1 for any math deck.

## Full-sentence prose → rewrite to noun phrases

Symptom: bullets and card bodies read like paragraphs from a paper. Speaker re-reads instead of adding context.

Fix:
- **Drop narrative connectors.** "This means that X" → "X". "In other words, Y" → "Y". Delete "as we will see", "subsequently", "it is important to note".
- **Cut soft qualifiers.** "essentially", "actually", "basically", "indeed", "very", "quite", "fairly".
- **Compress to noun phrases.** "The attack achieves high precision, meaning most positive predictions are correct" → "High precision: most positives correct".
- **Keep technical specifics.** Variables, numbers, dates, author names, math.
- **Target ~40–60% word reduction** when rewriting an existing wordy deck. If you have to shrink the font to keep a bullet on one line, you haven't rewritten it yet.

After compression, strip any residual `class="small"` / `class="tiny"` / inline `font-size` overrides (Priority 0).

## Paper-title cards steal half the slide → use `.cite`

Symptom: every paper-overview slide has a 2-column layout with the right column holding paper title + venue, ~50% of the slide for attribution alone.

Fix: delete the card. Replace with `<div class="cite">Author(s), "Title", Venue Year</div>` at the bottom. Don't wrap the title in `<em>` — `em` is gray, and gray-on-gray reads as mud. Keep the author `.pill` at the top as a recurring section label, but add `.cite` only on the paper-overview slide (not every follow-up).

## Stale `data-screen-label`

Symptom: the on-screen slide label says "Slide 7 — Forward process" but the deck has rearranged and slide 7 is now something else.

Fix: keep `data-screen-label` values in sync with actual slide position when inserting or removing slides. Not fatal, just confusing during review.
