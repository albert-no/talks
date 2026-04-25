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

**Priority 1 (after Priority 0): the Line-breaks rule in §"Line breaks — Priority 1" below.** Goal is minimal slides. Leave content alone if it already fits on one line — two short sentences on one line are fine. Act only when prose visibly wraps: compress first; if still multi-line, split at a natural boundary (two adjacent `<p>` tags); glue inseparable phrases with `&nbsp;` reactively.

**Priority 2 (after Priorities 0 and 1, which always come first): the Overflow rule in §"Overflow — Priority 2" below.** Content must stay inside the slide bounds and clear of the bottom-left brand footer ("YONSEI UNIVERSITY"). When something overflows, compress and split — never shrink (Priority 0 forbids that) and never wedge with line-break tricks (Priority 1 forbids that). Detail that doesn't fit on the slide goes in a companion `-note.html` file (see §"Companion note files" below).

**Priority 3 (after 0, 1, and 2 — they always come first): the Empty-space rule in §"Empty space — Priority 3" below.** Empty space at the bottom of a slide is fine; empty space *in the middle* is not. Don't pad with `<div class="spacer*">`. Don't wrap 2–3-line content in `.cols` + `.card` (`.cols` stretches; cards become tall hollow boxes). If a slide is too sparse to hold itself up, merge or expand — never pad.

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

## Line breaks — Priority 1

**After Priority 0 (font-sizes), this is the next rule.** Goal: minimal slides. Fewer visual lines, less for the audience to re-read, more room for the speaker to elaborate.

**Leave content alone if it already fits.** Two short sentences on one line are fine. Split only when the browser would wrap anyway, and at a worse place than you can choose. Don't split for the sake of splitting.

When prose visibly wraps in preview, act in this order:

1. **Compress first** (§`DESIGN_SYSTEM.md §7.12`). Drop narrative connectors, cut soft qualifiers, compress to noun phrases, move detail to narration or the per-slide appendix. Most "doesn't fit" problems are really "too many words" problems — solve with rewriting, not structural changes.
2. **If still multi-line after compression,** split at a natural boundary:
   - a clear sentence end, a colon, or an independent-clause break → split into two adjacent `<p>` tags (identical visual under `margin: 0`, cleaner semantic);
   - a single sentence with an internal comma-level clause-break → `<br>` at that boundary (rare).
3. **Glue inseparable phrases with `&nbsp;` reactively** — only when the browser visibly breaks one in preview:
   - article/adjective + noun (`a&nbsp;dataset`, `large&nbsp;model`)
   - preposition + short object (`in&nbsp;the&nbsp;model`)
   - number + unit (`7B&nbsp;parameters`, `≈80%&nbsp;accuracy`)
   - Hyphenated compounds are covered by the existing `<br>`-after-`-` rule in Authoring gotchas.
4. **Never break within a phrase.** The browser may do so automatically under `text-wrap: pretty`; if it happens in preview, apply step 3 or rewrite.

**`<br>` policy.** Allowed at a deliberate internal clause boundary (step 2b). Banned as an orphan-shim — for that, see Authoring gotchas (use `&nbsp;` or compression).

**Interaction with Priority 0.** Priority 0 forces body size (1.55rem). Some content that fit on one line at `.small` will now wrap. Don't shrink to avoid the wrap — compress, or accept a clean split per step 2.

## Overflow — Priority 2

**After Priority 0 (font-sizes) and Priority 1 (line-breaks) — both of which always come first — this is the next rule.** Overflow is any content that escapes the slide's intended drawing area:

- **Off-slide.** Text or elements positioned past the 1280×720 slide bounds; partially or fully invisible at presentation scale.
- **Footer collision.** Content that overlaps the auto-injected `.brand-footer` (the "YONSEI UNIVERSITY" lockup `deck.js` injects on every content slide; reserve ~40 px of clear space at the bottom-left corner — see Authoring gotchas).

**The fix is upstream, not downstream.** Visually auditing every slide in a browser at presentation scale is impractical, so the discipline starts at draft time: write short, abstract phrases from the first pass — telegraphic noun phrases, not full sentences (Style priority #2). If you're tempted to write a wordy slide, you've already failed Priority 2; rewrite before you preview.

When overflow shows up anyway, act in this order:

1. **Compress** (per Priority 1, step 1). Drop connectors, qualifiers, full sentences; collapse to noun phrases. Most overflow is wordiness, not a layout problem.
2. **Split the slide.** If the content is still too tall or too wide after compression, divide one idea-heavy slide into two slides at a natural boundary. There is no slide budget — use as many slides as you need.
3. **Move secondary detail to the per-slide note file** (see §"Companion note files" below). Useful but non-essential content lives there, not on the slide.
4. **Reposition decorative elements** that anchor to `bottom-left` so they respect the footer's reserved space (anchor to `right` and/or `top` instead).

**Banned shortcuts.**

- **Don't shrink to fit.** Priority 0 forbids `.small` / `.tiny` / inline `font-size` on prose. Overflow is never a reason to override Priority 0.
- **Don't compress vertical rhythm.** No squeezing `margin` / `padding` / `line-height` on prose to recover space — that's a layout hack that breaks the canonical look.
- **Don't push content past the footer.** Footer collision is overflow even if the text is technically still inside the slide rectangle.

**Interaction with Priorities 0 and 1.** Priority 0 forces body size; Priority 1 forbids using line-break tricks to wedge in extra content. Priority 2 closes the loop: if after honoring 0 and 1 the slide still doesn't fit, the answer is *less content* — split, or move detail to the note file. Never cram.

## Empty space — Priority 3

**After Priorities 0, 1, and 2 — which always come first — this is the next rule.** *Empty space at the bottom of a slide is fine. Empty space in the middle is not.* The "few blocks at the top, one line at the bottom, hollow gap between" pattern is the symptom this rule kills.

Two authoring patterns cause it. Both are forbidden:

- **Don't use `<div class="spacer">` / `-sm` / `-lg` between content blocks.** Natural element margins already space things correctly; spacers stack on top, and on a slide whose content already spaces itself, the extra gap shows up as a void in the middle. Remove them. The legitimate use is the rare case where two adjacent blocks genuinely collide — almost never on a content slide.
- **Don't wrap 2–3-line content in `.cols` + `.card`.** `deck.css` defines `.cols { flex: 1; align-items: stretch }`, so `.cols` grabs all remaining vertical space on the slide and stretches each card to match — short cards become tall hollow boxes with content at the top and empty bottom. Use `.cols + .card` only when each column carries substantive content (≈5+ lines, or math/diagrams that fill the space). For short side-by-side dichotomies, use `.grid-2` (no flex stretching) with bare `<h3>` + `<p>`, no card wrapper.
- **If a slide has so little content that the natural empty bottom dominates** (e.g., 3 bullets and nothing else), it isn't a slide — merge it into the adjacent slide or drop it. Don't pad.

**Interaction with Priorities 0/1/2.** Priority 0 forces body size; Priority 1 forbids line-break tricks; Priority 2 forbids cramming when crowded. Priority 3 closes the other side of the loop: when the slide is *under-full*, the answer is also content-driven — combine, expand, or accept the empty bottom. Never inject filler.

## Companion note files

**The slide is the visual anchor; the note file is the long form.** When you have detail worth recording but too long for a slide — full-sentence explanations, derivations, secondary examples, "FYI" context, extra citations — write it into a companion note file rather than the slide.

- **Naming.** `<deck>/<deck>.html` is the slides; `<deck>/<deck>-note.html` is the notes. Example: `mia/mia1-foundations.html` ↔ `mia/mia1-foundations-note.html`. The note file lives next to its deck.
- **Structure.** One section per slide, in slide order, each headed with the slide's `data-screen-label` or `<h2>` title. Plain prose is fine — full sentences, longer explanations, examples. HTML (not Markdown) so KaTeX math via `$…$` / `$$…$$` works the same as in the deck. The note file does not use the `.deck` / `.slide` engine; a simple `<article>` or `<section>` per slide is enough.
- **When to use it.** When Priority 1 or Priority 2 says "move detail to narration / per-slide appendix", that detail goes in the note file. The note file is where rule #2 ("speaker narrates; the slide is a visual anchor") gets its safety net — nothing is lost when the slide stays minimal.
- **What it isn't.** Not a paper draft, not a transcript, not a tutorial. It's the speaker's reading companion and the reader's after-the-fact reference. Keep it tight.

## Authoring gotchas (learned the hard way)

These are the pitfalls that have eaten the most time. Do not re-learn them.

- **Don't override `.slide` positioning.** Canonical `.slide` is `position: absolute; inset: 0`. Child elements with `position: absolute` already anchor to the slide — you never need to add `style="position:relative"` to the slide itself. Doing so defeats `inset:0`, so the slide stops filling the deck and the auto-injected `.brand-footer` lands somewhere unpredictable.
- **Bottom-left is reserved for the brand footer.** `deck.js` injects `.brand-footer` at `bottom:18px; left:28px` on every content slide. When you absolute-position decorative content (images, floats, overlays) inside a slide, anchor to `right` and/or `top` — not `bottom-left` — and leave ~40 px of clear space at the bottom-left corner.
- **SVG `<text>` does not render KaTeX.** Auto-render walks the HTML DOM; SVG text is opaque to it, so `$g_1$` in an SVG `<text>` shows as the literal string `$g_1$`. When a diagram needs math-rendered labels, build it as HTML (flex/grid layout, div "boxes", CSS-styled circles) and use a thin SVG overlay for the arrows. See `privacy/DP-FL.html` slides 4, 9, 30 for the pattern (`.fl4-*`, `.ldp-*`, `.rdm-*`).
- **Use `$$…$$` (display math) for multi-row `\begin{cases}` / `\begin{align}`.** Inline `$…$` with `\displaystyle` can wrap or size unpredictably inside a narrow column. `$$…$$` inside a `.math-block` is the reliable form and guarantees the declaration stays on one line with the rows stacked inside.
- **Don't hack around overflow with `white-space:nowrap; overflow-x:auto`** on a math-block. The equation gets clipped at the right edge. Fix the content: shorten cases labels to math (`m \in \text{top-}k`, `\text{else}`), use `\dfrac` → `\tfrac` when you want less vertical weight, or split the slide.
- **Prefer static step-labeled diagrams over continuous animation.** For talks, auto-cycling animations (SMIL `animateMotion`, CSS keyframes) keep the audience waiting for the next frame. Show every step at once with ①②③④ badges on the relevant elements; the speaker controls the pacing. Keep animation for self-paced web versions only.
- **Descriptions shouldn't duplicate diagram equations.** If the diagram labels show `$g_i = \nabla\ell(\theta; D_i)$`, the description on the other side of the slide should just say "local gradient" in plain English. One artifact owns the math; the other owns the narrative.
- **Paper attribution goes in a bottom footnote, not a side card.** When a slide is about a specific paper, put the citation in a `<div class="cite">Author(s), "Title", Venue Year</div>` at the bottom. Don't waste half the slide on a 2-column layout where the right column is a card holding the paper title in `<em>"…"</em>`. One citation per slide; informal is fine. Keep the author `.pill` at the top for section context, but put `.cite` only on the paper-overview slide (not every follow-up slide about the same paper). See `DESIGN_SYSTEM.md §2.19` and §7.13.
- **KaTeX delimiter escape in `onload` — use `\\(` not `\(`.** The `renderMathInElement(document.body,{delimiters:[…]})` call lives inside an HTML `onload="…"` attribute, so strings pass through two layers of parsing (HTML → JS). The LaTeX delimiters must be written `'\\('`, `'\\)'`, `'\\['`, `'\\]'`. A single backslash (`'\('`) gets silently eaten by the JS string parser as an unrecognized escape, leaving KaTeX with bare `(`, `)`, `[`, `]` as delimiters — every parenthesized or bracketed phrase in the deck then renders as italic math with no word spacing (`(learned or heuristic)` → italic `learnedorheuristic`, `[M]` in a token chip → slanted math `M` at a different height than neighboring word tokens). The canonical handler is in `reference/deck-skeleton.html`; match it exactly. Audit: `grep -c "'\\\\(" *.html` should return 0 across all decks.
- **Never use italic for prose.** Yonsei has no italic face (all four TTFs are `font-style: normal`), and Noto Sans Italic isn't loaded either. Browsers fake italic by oblique-skewing normal glyphs, which collapses kerning. `em` is globally pinned to `font-style: normal; color: var(--gray-text)` — don't use `<i>`, don't set `font-style: italic`. In LaTeX math, wrap English phrases in `\text{…}`; bare `all positions` in math mode renders each letter as an italic math variable with zero inter-letter spacing.
- **Avoid em-dashes in slide prose.** Don't use `—` (em-dash), `–` (en-dash), or `--` (double-hyphen) as a general connector in titles, subtitles, bullets, cards, or captions. The dash reads as a pause in print but at slide sizes it either (a) forces an awkward line break between the dash and the second clause or (b) leaves whichever side is shorter dangling as an orphan. Rewrite instead: a colon (`:`), a comma, a period, or parentheses almost always reads better. The only exceptions are tight technical glyphs where the dash is part of the name (`7–8B scale`, `fill-in-the-middle`) or an arrow (`→`, `↔`). When converting existing text, read the sentence aloud — if the dash is doing the work of a colon ("X: it does Y"), use a colon; if it's parenthetical ("X (the reason being Y)"), use parens; if it's a full stop in disguise, split into two sentences.
- **Avoid dangling single words at the end of a line.** `deck.css` now sets `text-wrap: pretty` on `p` / `li` / `.small` / `.tiny` and `text-wrap: balance` on `h1` / `h2` / `h3` / `.subtitle`, which prevents most orphans automatically. When a stubborn orphan remains (usually a bullet where the last 1–2 words wrap to their own line), fix the content first: shorten the bullet, split the sentence, or restructure. Last resort: glue the final two or three words with `&nbsp;` (non-breaking space) so the wrapper moves them together. **Don't use `<br>` as an orphan-shim** — it creates fragility at different column widths. (Priority 1 does permit `<br>` at a deliberate internal clause boundary; that's a different use.) Also watch for em-dash constructions which are the single most common cause of orphans: rewriting `"X — Y"` as `"X: Y"` almost always fixes the orphan on its own.
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
