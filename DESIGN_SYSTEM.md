# Talks design system

Canonical rules for slide decks. **Audience**: academic conference talks and master-level lectures. **Mode**: math-heavy with rigorous theorem/proof, plus high-level intuition. **Visual**: minimal — short abstract phrases, not full sentences. Applies to custom HTML decks and the Marp template; when they disagree, `reference/deck.css` wins.

**Source files.** `reference/colors_and_type.css` (font-face + CSS tokens), `reference/deck.css` (engine + components). Decks `<link>` to these — never duplicate.

**Reference target.** Kangwook Lee's BLISS deck (<https://kangwooklee.com/talks/2026_03_BLISS/bliss_seminar.html>; captures in `reference/kangwook*.png`) is the minimum acceptable visual weight. If a deck renders smaller, suspect a per-deck `<style>` shadowing the canonical tokens — see GOTCHAS.

---

## Quick reference

| What I want to do | Where to look |
|---|---|
| Add a content slide | Recipes → Content slide |
| State a theorem rigorously | Math-heavy → Theorem |
| Show a proof rigorously | Math-heavy → Proof |
| Show proof intuition (color, build-up) | Math-heavy → Intuition + Build-up |
| Bracket a multi-step proof | Math-heavy → Multi-step proof pattern |
| Stack two related equations | Math-heavy → Stacked equations |
| Substitute variables back into a result | Math-heavy → Substitution |
| Label terms in a long equation | Math-heavy → Underbrace labels |
| Inline / display math | Recipes → Math slide |
| Add an exercise next to its content | Recipes → Inline exercise |
| Show an algorithm cleanly | Recipes → Algorithm slide |
| Visualize a chain / dependency | Recipes → Chain diagram |
| Cite a paper | Components → `.cite` + Recipes → Paper-overview |
| Section divider | Recipes → Section divider |
| Title slide / Closer | Recipes → Title / Closer |
| Diagram with math labels | Recipes → Diagram (HTML + SVG arrows) |
| Make a diagram dominate the slide | Recipes → Diagram dominates |
| Build-up of nearly identical slides | Recipes → Build-up no-fade |
| Recall a definition the audience may have forgotten | Recipes → Recall card |
| Cite a paper (venue order, not arXiv) | Conventions → Citations |
| What "page N" means | Conventions → Page numbering |
| Trace a debugging issue | `GOTCHAS.md` |

---

## Priorities (ranked, non-negotiable)

When rules conflict, lower number wins.

### 0. Font sizes — strongest rule

Important content (audience must read it during the talk) → body size. Non-important content → companion `<deck>-note.html` file, *not* shrunk to fit.

- The canonical scale is `reference/deck.css`. Don't redefine `p`, `li`, `h1`, `h2`, `h3`, `.subtitle`, `.cite`, `.small`, `.tiny`, or `.math-block` `font-size` in a deck's inline `<style>`. Don't put inline `style="font-size:…"` on prose.
- `.tiny` is banned everywhere. `.small` on prose (paragraphs, list items, captions, anything inside `.highlight` / `.card` / `.cols` / `.grid-*` / `.math-block` / under a `<table>`) is banned.
- Two on-slide slots permit sub-body text: `<div class="cite">` citations, and `.small` inside a diagram (only when the label is a non-crucial sub-label *and* compression breaks the layout).
- Component-internal text (pill labels, token chips, code blocks) stays at its native compact size — these are design tokens, not author overrides.
- When a slide feels cramped, **cut content or split the slide**. There is no slide budget.

### 1. Density — 7×7 rule + abstract phrases

**Hard ceiling: 7×7.** ≤ 7 visual lines per slide, ≤ 7 words per line. Soft target: ≤ 40 words of body text per content slide.

**Phrases, not sentences.** Telegraphic noun phrases. Drop narrative connectors ("this means…", "in other words…", "essentially", "actually"). Drop soft qualifiers ("very", "quite", "fairly"). Speaker narrates; the slide is a visual anchor. This applies to `h2` titles too — short and abstract (3–6 words), not action-title sentences.

**Math is not prose.** A theorem statement, definition, or equation in a `.math-block` doesn't count toward the 40-word ceiling. The ceiling exists to keep prose lean — math earns its space.

**One claim per line.** When a paragraph, `<li>`, `.highlight`, or `.card` carries multiple distinct claims joined by periods, split each into its own `<p>` (or convert the run to a `<ul>` if there are 3+ short claims). Two assertions that look like one sentence read as one idea — the audience won't track both. This applies inside `.highlight` / `.card` too: separate `<p>` siblings, not concatenated sentences.

**Math-comma-math — anti-pattern.** Most of the time, starting a clause with math is fine. The specific failure is when the *previous* clause also *ended* in math: "For large $N$, $N\sigma^2$ dominates" — the two glyphs sit on either side of the comma and the eye reads them as one continuous expression ($N, N\sigma^2$). Insert a noun in the second clause ("the second term $N\sigma^2$ dominates") or restructure so the boundary isn't math-comma-math.

**Em-dash mid-sentence — anti-pattern.** "X is a sparsifier — pruning emerges" wraps awkwardly at slide font sizes; the dash often orphans alone on a line. Replace with a colon plus `<br>` (one-shot internal break is allowed by Priority 1 step 2) or split into two `<p>` tags. Em-dashes are only safe when they're part of a technical glyph (`7–8B`, `fill-in-the-middle`).

**Numerical anchors next to closed-form formulas.** When a slide states a closed-form `R(D)`, `D(R)`, or any quantity-as-function, pin a concrete number for the running example next to it: `R(D) = 1 - H_b(D)$, &nbsp;$R(\tfrac14) \approx 0.189$ bits` reads in one glance. The audience reads the formula; the speaker says the number; both belong on the slide.

When prose visibly wraps:

1. **Compress.** Most overflow is wordiness, not a layout problem. Collapse to noun phrases.
2. **Split** at a natural sentence/colon/independent-clause boundary into two adjacent `<p>` tags. `<br>` only at a deliberate internal clause break (rare).
3. **Glue inseparable phrases with `&nbsp;`** reactively when the browser visibly breaks one — article+noun (`a&nbsp;dataset`), preposition+object (`in&nbsp;the&nbsp;model`), number+unit (`7B&nbsp;parameters`).
4. **Never break within a phrase.** `<br>` as orphan-shim is banned (see GOTCHAS).

### 2. Overflow — content stays in bounds

Content must fit inside 1280×720 and clear the auto-injected `.brand-footer` at bottom-left (~40 px reserved). Footer collision is overflow even if text is inside the slide rectangle.

When something overflows: compress (Priority 1) → split the slide → move secondary detail to `<deck>-note.html`. **Never** shrink type. **Never** compress vertical rhythm (`margin`, `padding`, `line-height`) on prose. Discipline is upstream — write short phrases from the first draft.

For multi-slide proofs, a "(continued)" `h2` and a brief one-line recap is the canonical recovery — see Math-heavy → Proof.

**Visual element budget.** A content slide gets `h2` + `divider` + at most **5 child elements**. A `.math-block` counts as 1 (taller than a prose line). A `<table>` counts by row count (header + N data rows). A `.highlight` counts as 1 regardless of internal `<p>` count. **If a slide carries `.math-block` + `<table>` + `.highlight` together, it's already over budget — split before previewing.** This rule predicts overflow without rendering; honor it at draft time.

### 3. Empty space — no middle voids

Empty space at the *bottom* of a slide is fine. Empty space *in the middle* is not.

- Don't pad with `<div class="spacer*">`. Trust natural element margins.
- Don't wrap 2–3-line content in `.cols + .card` — `.cols { flex: 1; align-items: stretch }` makes short cards stretch into tall hollow boxes. Use `.grid-2` (no flex stretch) with bare `<h3>` + `<p>` for short dichotomies.
- If a slide is too sparse to hold itself, merge or expand. Never pad.

### Style rules (informed by priorities)

1. **One idea per slide.** And **one exhibit** — one chart, table, diagram, theorem, proof chunk, or equation block per slide. If two seem needed, ask: one comparison (combine) or two points (two slides)?
2. **Speaker narrates; slide is a visual anchor.** Telegraphic phrases over sentences.
3. **Prose emphasis.** `**strong**` → Yonsei Blue. `*em*` → muted gray (never italic — see GOTCHAS).
4. **Key insight** → `<div class="highlight">` (HTML) or `>` blockquote (Marp). Max one per slide.
5. **Math.** Inline `$…$`, display `$$…$$` inside `<div class="math-block">`.
6. **Paper attribution** → `<div class="cite">` footnote at the bottom. Not a side card.
7. **Ghost deck test.** Read only the `h2` titles in sequence. They should outline the lecture arc clearly. If they don't, fix the outline before drafting bodies. Titles stay short and abstract — not full sentences.

---

## Tokens

### Color

| Token | Value | Generic use |
|---|---|---|
| `--yonsei-blue` | `#003876` | Primary accent: `strong`, dividers, list bullets, h2 underline. |
| `--blue-light` | `#1a5296` | Secondary accent: cards, pill outlines. |
| `--accent` | `#005baa` | Tertiary; use sparingly. |
| `--charcoal` | `#1a1a1a` | Body text. |
| `--gray-text` | `#666666` | Muted (`em`, `.cite`, subtitles). AA at ≥14px. |
| `--slate` | `#e8ecf0` | Borders, table rules. |
| `--light` / `--subtle` | `#f4f6f9` | Card / math-block / divider-slide background. |
| `--white` | `#FFFFFF` | Slide background. |
| `--success` | `#2e8b57` | `ul.check`, `.token-safe`. |
| `--warn` | `#d94040` | `.token-eos`. |

**Color in math contexts** (one role per color, applied consistently across the deck):

| Color | Math meaning |
|---|---|
| `--yonsei-blue` | What's being introduced / the active step / the term to focus on |
| `--charcoal` | Established / given / already proved |
| `--gray-text` | Future / not yet proven / parenthetical aside |
| `--success` | Equality that closes a chain / final claim |
| `--warn` | Counterexample / where standard argument breaks |

Never recolor for decoration. Pick once, apply consistently — color carries semantic load when it's stable.

### Typography

`'Yonsei', 'Noto Sans', Arial, sans-serif`. Yonsei TTFs declared via `@font-face` in `colors_and_type.css`. No italic face exists — see GOTCHAS.

| Role | Size | Weight | Line height |
|---|---|---|---|
| `h1` | 3.6rem (4rem on title, 4.2rem on left-section) | 700 | 1.08 |
| `h2` | 2.7rem | 700 | 1.12 |
| `h3` | 1.85rem | 700 | 1.22 |
| body `p`, `li` | 1.55rem | 300–400 | 1.5 |
| `.subtitle` | 1.75rem (1.9rem on title) | 300 | — |
| `.cite` | 0.85rem | — | — |
| `.small` | 1.15rem | — | (gated — see Priority 0) |
| `.tiny` | 0.95rem | — | (banned — see Priority 0) |
| `.code-block` | 1.25rem | 500 (kw 700, fn 600) | 1.6 |

`text-wrap: balance` on `h1`/`h2`/`h3`/`.subtitle`; `text-wrap: pretty` on `p`/`li`/`.small`/`.tiny`. Don't override.

### Spacing & misc

- Slide padding `56px 72px 48px` (title slide `72px 88px`). Don't change — anchors print layout.
- Border radius: `12px` (card), `10px` (diagram-box), `8px` (math-block, highlight, pre), `6px` (token), `3.667em` (pill).
- Spacers (`.spacer-sm`/`.spacer`/`.spacer-lg`) — almost never useful. See Priority 3.
- Viewport: fixed 1280×720, scaled via JS `transform`. Same for `@page` print size.
- Motion: `fadeIn` 0.4s on every direct child of `.slide.active`, staggered 0.06–0.30s. Disabled in print. Don't override. **No other animation language** — proof build-ups use multi-slide progressions, not CSS keyframes (see Math-heavy → Build-up).

---

## Components

Every class below is defined in `reference/deck.css`. Reuse — don't invent.

**Containers** — `.slide`, `.title-slide`, `.section-slide`, `.section-slide.left`, `.end-slide`.

**Backgrounds** — `.bg-light` (subtle gray), `.bg-accent` (Yonsei blue, white text, inverts component defaults; reserve for section dividers and statement slides).

**Building blocks** — `.card`, `.highlight` (max one per slide), `.pill` / `.pill-fill`, `.divider`, `.math-block`, `.code-block` (with `.kw` / `.fn` / `.cm` / `.str` for syntax tokens), `.diagram-flow` / `.diagram-box`, `.cite`, `.brand-footer` (auto-injected).

**Token chips** — `.token-mask` / `-gen` / `-fixed` / `-eos` / `-safe` / `-pad` / `-pad2` / `-pad3`.

**Layout** — `.cols`, `.col-2-3` / `.col-1-3`, `.grid-2`, `.grid-3`.

**Lists** — `ul` (default blue dot), `ul.check` (green ✓), `ul.arrow` (blue →), `ul.num` (numbered badge).

**TOC slide** — `.toc-list` / `.toc-item` / `.toc-num` / `.toc-rule` / `.toc-label` / `.toc-sub`.

**Engine UI** (auto-injected, hidden in print) — `.progress-bar`, `.slide-num`.

For exact CSS — padding, border, hover, `.bg-accent` inversion — read `reference/deck.css`. Don't paraphrase here.

---

## Math-heavy talks (theorem / proof / intuition)

The repo's primary mode. Three slide types and one pairing pattern.

### Theorem

Rigorous statement. Assumptions, claim, citation. Use a `.card` with an inline label (`<h3>Theorem N (Author, Year).</h3>`) and place the assertion in a `.math-block`.

```html
<div class="slide">
  <h2>Concentration of empirical mean</h2><div class="divider"></div>
  <div class="card">
    <h3>Theorem (Hoeffding, 1963).</h3>
    <p>Let $X_1, \dots, X_n$ be independent with $X_i \in [a_i, b_i]$. For $t > 0$:</p>
    <div class="math-block">$$\Pr\!\left[\bar X_n - \mathbb{E}\bar X_n \ge t\right] \le \exp\!\left(-\tfrac{2 n^2 t^2}{\sum_i (b_i - a_i)^2}\right).$$</div>
  </div>
  <div class="cite">Hoeffding, "Probability Inequalities for Sums of Bounded Random Variables", JASA 1963.</div>
</div>
```

### Proof

Rigorous derivation, one logical step per visual line. Multi-slide if it doesn't fit at body size — never shrink (Priority 0). Use `<h2>Proof (continued)</h2>` and one recap line on continuation slides.

```html
<div class="slide">
  <h2>Proof — MGF bound</h2><div class="divider"></div>
  <div class="math-block">$$\Pr[\bar X_n - \mathbb{E}\bar X_n \ge t]
    = \Pr\!\left[e^{s n (\bar X_n - \mathbb{E}\bar X_n)} \ge e^{snt}\right]
    \le e^{-snt}\, \mathbb{E}\!\left[e^{s n (\bar X_n - \mathbb{E}\bar X_n)}\right].$$</div>
  <p>Markov, then independence, then optimize $s > 0$. <em>(next: bound each factor)</em></p>
</div>
```

### Intuition

High-level picture. One visual metaphor; speaker narrates the geometry. This is where color and (controlled) build-up pay off.

```html
<div class="slide">
  <h2>Why concentration is exponential</h2><div class="divider"></div>
  <div class="cols">
    <div>
      <p><strong>Each $X_i$:</strong> small wiggle.</p>
      <p><strong>Average of $n$:</strong> wiggles cancel.</p>
      <p><strong>Rate:</strong> exponential, not polynomial.</p>
    </div>
    <div><!-- HTML+SVG sketch of tail decay --></div>
  </div>
</div>
```

### Pairing pattern

For results the audience must really understand:

1. **Intuition** (1 slide) — picture, geometry, why we should expect the result.
2. **Theorem** (1 slide) — rigorous statement.
3. **Proof** (1–N slides) — rigorous derivation.
4. **Discussion** (optional) — what's tight, what generalizes.

For results the audience just needs to know exists, theorem-only is fine; cite the proof.

### Build-up for proof intuition (controlled "animation")

Auto-cycling animation is banned for talks (speaker loses pacing — see GOTCHAS). For proof intuition, use **progressive slides** instead: duplicate the slide N times; on slide $k$, color the first $k$ steps with Yonsei Blue (active/established) and the remaining steps with `--gray-text` (upcoming). Speaker advances at their own pace; the audience sees the build-up animation would have given, without the loop.

```html
<!-- Step k of N for the same idea slide -->
<div class="slide">
  <h2>Why Hoeffding works (2 of 4)</h2><div class="divider"></div>
  <ol class="num">
    <li style="color:var(--charcoal)">Markov on the moment-generating function</li>
    <li style="color:var(--yonsei-blue)"><strong>Independence factors the MGF ← here</strong></li>
    <li style="color:var(--gray-text)">Bound each factor (Hoeffding's lemma)</li>
    <li style="color:var(--gray-text)">Optimize the free parameter $s$</li>
  </ol>
</div>
```

Use the math-context color table above. One color = one role across the whole deck.

### Stacked equations belong in one block

Two related equations stacked vertically → single `<div class="math-block">` with `\begin{aligned}`, **not** two adjacent `math-block` divs. Adjacent blocks introduce too much vertical gap; the eye reads them as separate ideas instead of two lines of one chain.

```html
<!-- yes: tight stacking -->
<div class="math-block">$$\begin{aligned}
  X^{(0)} &= X, \\
  X^{(n)} &= X^{(n-1)} + Z^{(n)}.
\end{aligned}$$</div>

<!-- no: too much gap, reads as two unrelated equations -->
<div class="math-block">$$X^{(0)} = X.$$</div>
<div class="math-block">$$X^{(n)} = X^{(n-1)} + Z^{(n)}.$$</div>
```

**Exception**: when the second equation is a *key conclusion* deserving its own moment (final result, closing claim), promote it to its own `math-block` so it lands separately from the working math above. The visual gap then becomes signal, not noise.

**Margin override when two blocks are unavoidable.** Each `.math-block` carries ~30 px of vertical padding/margin. Two stacked blocks add up to ~60 px of dead space, often pushing a closing highlight or footer off the slide. If you genuinely need two adjacent `math-block` divs (e.g. a derivation followed by a one-line conclusion), override the default with inline `style="margin: 8px 0;"` on each — never leave them at default and hope.

### Multi-step proof pattern

For derivations that span 4+ logical steps, bracket the sequence. Definitions precede roadmaps; recap is a chained equation, not a re-listed bullet summary.

1. **Setup** — define variables and the problem (one slide).
2. **Outline** — show the *target* (e.g., the Bayes formula we're about to simplify) in a `math-block`, followed by an `<ol>` of the step labels. This previews the path.
3. **Step 1 … Step k** — one logical step per slide, body math at body size.
4. **Recap** — a single `aligned` block showing the unified equation chain, with each step labeled above its relation symbol via `\stackrel{(k)}{=}` or `\stackrel{(k)}{\approx}`. Don't reuse the bulleted outline as a recap — outline previews step *labels*, recap shows the equation *chain*.

```html
<!-- Recap form -->
<div class="math-block">$$\begin{aligned}
  P_{X|Y}(x|y)
    &= \frac{P_{Y|X}(y|x)\,P_X(x)}{P_Y(y)} \\
    &\stackrel{(1)}{\approx}\; \tfrac{P_{Y|X}\,[P_X(y) + P'_X(y)(x-y)]}{P_Y(y)} \\
    &\stackrel{(2)}{\approx}\; P_{Y|X}\!\left[1 + \tfrac{P'_X(y)}{P_X(y)}(x-y)\right] \\
    &\stackrel{(3)}{\approx}\; \cdots \\
    &\stackrel{(4)}{=}\; \mathcal{N}(\mu_*, \sigma^2)(x).
\end{aligned}$$</div>
```

### Substitution

When applying an abstract result by relabeling variables, show the abstract form first, then the substitution arrow, then the concrete form. Don't jump straight to the substituted form — the reader loses sight of which result you're invoking.

```html
<p>Step 4 result, with $X = \tilde X^{(n-1)}$ and $Y = \tilde X^{(n)}$:</p>
<div class="math-block">$$X\,|\,Y \;\sim\; \mathcal{N}(Y + \sigma^2\partial_y \log P_X(Y),\; \sigma^2).$$</div>
<p>Substitute $X \to \tilde x^{(n-1)}$, $Y \to \tilde x^{(n)}$:</p>
<div class="math-block">$$\tilde x^{(n-1)} = \tilde x^{(n)} + \sigma^2\,\partial \log P_{X^{(n)}}(\tilde x^{(n)}) + \tilde z^{(n)}.$$</div>
```

### Underbrace labels

Use `\underbrace{...}_{\text{name}}` to label parts of a long equation in place. **Label the per-term operand, not the whole sum**: a `\sum_n` over labeled terms is more useful than a single label on the whole sum, because the label names the per-step object the reader will reason about later.

```latex
%% yes: sum is outside, each summand labeled
\sum_{n=2}^{N} \underbrace{\bigl(-\log\tfrac{p_\theta}{q}\bigr)}_{L_{n-1}}

%% no: wrong abstraction level — `\sum L_{n-1}` is not the natural object
\underbrace{-\sum_{n=2}^{N} \log\tfrac{p_\theta}{q}}_{\sum L_{n-1}}
```

### Recall before derive

When deriving B from A, state A first as a self-contained fact (own paragraph + `math-block`), *then* derive B. Don't refer to A in a trailing parenthetical or "where …, known in closed form since $A$" clause — that hides the prerequisite under the consequence and the reader has to re-parse.

```html
<!-- yes: A first, B derived from it -->
<p>Conditional forward marginal (closed form):</p>
<div class="math-block">$$q(X^{(n)}|X^{(0)}) = \mathcal{N}(\sqrt{\bar α_n}\,X^{(0)},\; 1-\bar α_n).$$</div>
<p>Hence the reverse posterior is also Gaussian:</p>
<div class="math-block">$$q(X^{(n-1)}|X^{(n)}, X^{(0)}) = \mathcal{N}(\mu_n, \beta_n).$$</div>

<!-- no: prerequisite tucked in a trailing clause -->
<p>The reverse posterior is Gaussian:</p>
<div class="math-block">$$q(\cdots) = \mathcal{N}(\mu_n, \beta_n),$$</div>
<p>where $\mu_n$ uses the conditional score, known in closed form since $q(X^{(n)}|X^{(0)}) = \mathcal{N}(\ldots)$.</p>
```

---

## Conventions

### Page numbering

The on-screen `slide-num` indicator (and any user reference to "page N") counts **every** `<div class="slide">` element in document order — title slide, TOC, section dividers, content slides, recap, end-slide all included. `deck.js` enumerates them with `querySelectorAll('.slide')` and shows `(current+1) / total`. When the user says "page 23", count from 1 starting at the title.

When you edit, prefer matching slides by content (`<h2>` text, distinctive class) rather than position — slide numbers shift the moment you insert or remove anything. Only treat the page number as a navigation hint, not a stable identifier.

### Citations

`<div class="cite">…</div>` format: `Authors (in venue order), "Title", Venue YYYY` — no arXiv ID unless explicitly requested. Use the **venue's** author order (PMLR / NeurIPS / JMLR / journal proceedings page), not arXiv's, since they sometimes differ. `et al.` is acceptable for 4+ authors after first reference; spell out all authors on the first slide that introduces a paper.

```html
<!-- yes -->
<div class="cite">Isik, Weissman, and No, "An Information-Theoretic Justification for Model Pruning", AISTATS 2022.</div>

<!-- no: arXiv-only attribution -->
<div class="cite">Isik et al., arXiv:2102.08329.</div>
```

---

## Recipes

**Title slide**
```html
<div class="slide title-slide active">
  <img class="title-logo" src="../reference/kor-eng2.png" alt="Yonsei University">
  <div class="pill pill-fill">Talk type</div>
  <h1>Title</h1>
  <div class="divider"></div>
  <p class="subtitle">Subtitle</p>
  <p>Speaker · Affiliation · Date</p>
</div>
```

**Content slide**
```html
<div class="slide">
  <h2>Heading</h2><div class="divider"></div>
  <p>Phrase with <strong>blue accent</strong> and <em>muted aside</em>.</p>
  <div class="highlight">Key insight (one max).</div>
</div>
```

**Three-pillar / comparison**
```html
<div class="grid-3">
  <div class="card" style="text-align:center;"><h3>①</h3><p>…</p></div>
  …×3
</div>
```
For short 2-column dichotomies use `.grid-2` with bare `<h3>` + `<p>` (no `.card` wrapper — Priority 3).

**Math slide**
```html
<p>Setup with inline $x_t$.</p>
<div class="math-block">$$\mathcal{L} = \mathbb{E}[-\log p_\theta(x_0)]$$</div>
```
Use `$$…$$` for `\begin{cases}` and `\begin{align}`. Inline `$…$\displaystyle$…$` with `nowrap` is fragile — see GOTCHAS.

**Code / pseudocode block**
```html
<div class="code-block"><span class="cm"># Membership inference, simplest form</span>
<span class="kw">def</span> <span class="fn">attack</span>(model, x, τ):
    return model.<span class="fn">loss</span>(x) <span class="kw">&lt;</span> τ      <span class="cm"># member if loss is small</span>
</div>
```
Tokens: `.kw` (keyword, blue, 700), `.fn` (function name, accent, 600), `.cm` (comment, gray), `.str` (string, green, 600). Render at 1.25rem / weight 500 — large and thick enough to read from the back row. Pseudocode is fine; full Python listings rarely fit (move to the note file).

**Paper-overview slide** (citation as footnote, not card)
```html
<div class="cite">Author(s), "Paper Title", Venue Year</div>
```
One citation per slide. Don't wrap title in `<em>` (gray-on-gray is mud).

**Section divider (left, numbered)**
```html
<div class="slide section-slide left">
  <div class="section-num">02</div>
  <h1>Controllability</h1>
  <div class="divider"></div>
  <p class="subtitle">Masking schedules, guided remasking, safety</p>
</div>
```
`.section-slide` (centered, `.bg-accent`) for dramatic interludes; `.left` for structural part breaks inside a long talk.

**TOC slide**
```html
<h2>Contents</h2><div class="divider"></div>
<div class="toc-list">
  <div class="toc-item">
    <div class="toc-num">01</div>
    <div class="toc-rule"></div>
    <div><div class="toc-label">Section name</div><div class="toc-sub">Subtitle</div></div>
  </div>
  …×4
</div>
```

**Closer**
```html
<div class="slide end-slide">
  <div class="big-word">Q&amp;A</div>
  <p class="big-word-sub">Thank you.</p>
</div>
```

**Diagram with math labels.** Build structure in HTML (flex/grid + divs), use SVG only for arrows. Reference: `.fl4-*` / `.ldp-*` / `.rdm-*` in `privacy/DP-FL.html`. Never put `$…$` inside SVG `<text>` — KaTeX skips it (see GOTCHAS).

**Algorithm slide.** A single styled box, centered. Don't pad with a right-column auxiliary diagram — the algorithm is the exhibit. Per-deck define `.<deck>-algo` once if reused (background `--light`, left border 3px `--yonsei-blue`, padding `16px 22px`, radius `0 10px 10px 0`).

Use a counter-based `::before` for step numbers — default `<ol>` markers render too small and lack the visual weight needed at slide font sizes. Pad the step body left so the number visibly precedes the text:

```css
.<deck>-algo ol { margin: 0; padding-left: 0; list-style: none; counter-reset: step; }
.<deck>-algo ol li {
  counter-increment: step;
  padding: 8px 0 8px 56px;
  position: relative;
  line-height: 1.45;
}
.<deck>-algo ol li::before {
  content: counter(step) ".";
  position: absolute; left: 12px; top: 8px;
  font-weight: 700; color: var(--yonsei-blue);
  width: 36px; text-align: right;
}
.<deck>-algo ol li + li { border-top: 1px solid var(--slate); }
```

```html
<div class="slide">
  <h2>Training Algorithm</h2><div class="divider"></div>
  <div class="d2-algo" style="max-width:880px; margin:36px auto 22px;">
    <ol>
      <li>Sample $X^{(0)} \sim p_{\text{data}}$.</li>
      <li>Sample $\epsilon \sim \mathcal{N}(0,1)$.</li>
      <li>Form $X^{(n)} = \sqrt{\bar α_n}\,X^{(0)} + \sqrt{1-\bar α_n}\,\epsilon$.</li>
      <li>Gradient step on $\|\epsilon - \epsilon_\theta(X^{(n)}, n)\|^2$.</li>
    </ol>
  </div>
  <p style="text-align:center;">Caption (e.g., weighting choice).</p>
</div>
```

`max-width` ≈ 880px for compact algorithms, ≈ 1040px when a step carries long math. Caption below, centered. Add a side diagram only if it conveys real new information beyond what's in the algorithm. Algorithms always live in a per-deck `.<deck>-algo` styled box — never `.code-block`.

**Build-up no-fade pattern.** When several consecutive slides differ only by a single value (Lloyd–Max iteration, Bayes-step coloring, table-cell update), the engine's per-element fadeIn (`animation: fadeIn 0.4s ease both` with 0.06–0.30s stagger) makes navigation feel like a flash on every click. Disable it on those slides only with a per-deck class:

```html
<style>
.<deck>-no-fade.active > * { animation: none !important; }
</style>

<div class="slide <deck>-no-fade">…</div>
<div class="slide <deck>-no-fade">…</div>
```

Result: consecutive build-up slides feel like a single animated frame change. Keep the fade-in on every other slide where it helps the eye land. Pattern complements (does not replace) the multi-slide proof build-up — see Math-heavy → Build-up.

**Recall card.** When a slide depends on a definition the audience saw 5+ slides ago (typical-set definition, AEP, KKT, a specific lemma), lead with a small recall card. Cheaper than asking the audience to remember:

```html
<div class="card" style="padding: 10px 16px; margin-bottom: 10px;">
  <p><strong>Recall (typical set).</strong> $T_\varepsilon^{(n)}(P) = \{z^n : |\hat P_{z^n}(a) - P(a)| < \varepsilon \;\forall a\}$. <strong>AEP:</strong> $|T_\varepsilon^{(n)}(P)| \doteq 2^{nH(P)}$.</p>
</div>
<p>Now we use this to count Hamming-ball volumes…</p>
```

Use only when the dependency is non-obvious. Don't pile up Recall cards — one per slide max.

**Diagram dominates.** When the user says "make the diagram much larger" or the slide is essentially "this picture, plus one short caption", check three things in order:

1. Does the SVG carry a `style="max-width: <small>"` constraint? Remove it. (`max-width` belongs on the wrapper `<div>`, not the SVG itself.)
2. Is the layout `.cols` (two equal-width children)? Switch to `.cols` with `.col-1-3` (text) + `.col-2-3` (diagram) so the diagram gets 2/3 of the slide.
3. Is the SVG viewBox unnecessarily small (e.g. `220×130`)? Bump to `~400×240` so labels render at readable absolute pixel sizes — labels at `1.0–1.4rem` need a viewBox where `font-size` math lands in a sensible scale relative to the SVG's content.

```html
<div class="slide">
  <h2>Setup and Statement</h2><div class="divider"></div>
  <div class="cols">
    <div class="col-1-3"><!-- text + math --></div>
    <div class="col-2-3"><!-- big SVG with HTML overlays --></div>
  </div>
</div>
```

For pure single-diagram slides, drop the cols entirely and center the SVG with `max-width: ~960px; margin: 24px auto`.

**KaTeX overlays on SVG.** KaTeX skips SVG `<text>` nodes — math labels go in absolute-positioned HTML spans on top of the SVG. Recommended sizes:

- Axis labels (`$X_1$`, `$X_2$`, `$\widehat X^n$`): `font-size: 1.3–1.4rem; font-weight: 700;`
- Threshold / index labels (`$\tau_i$`, `$\hat x_j$`): `font-size: 1.0–1.1rem; font-weight: 600;`
- Annotation labels (atom mass, density names): `font-size: 1.1–1.4rem; font-weight: 600;`

Position via `left: %; top: %;` computed against the viewBox: for viewBox `W × H` and SVG coord `(x, y)`, `left = x/W·100%`, `top = y/H·100%`. Use `transform: translate(-50%, -50%)` for centered labels, `transform: translate(-100%, -50%)` for right-aligned (typical for y-axis labels).

```html
<div style="position: relative;">
  <svg viewBox="0 0 400 240" style="display: block; width: 100%;">…</svg>
  <span style="position: absolute; left: 50%; top: 87%;
               transform: translate(-50%, -50%);
               font-size: 1.1rem;">$\hat x = 0$</span>
</div>
```

**Never** put `max-width` on the SVG — put it on the wrapper instead, otherwise labels and SVG can drift apart.

**Inline exercise.** Plain `<p><strong>Exercise.</strong> …</p>` placed next to the related content (definition, theorem, formula). Optional `<em>Hint:</em>` clause. **Don't** create a trailing "Check It Yourself" slide; **don't** introduce per-deck `.exercise-list` styling — the standalone exercise slide pattern was retired.

```html
<div class="math-block">$$f(x) = \tfrac{1}{\pi}\,\tfrac{\gamma}{x^2+\gamma^2}.$$</div>
<p><strong>Exercise.</strong> Verify $\int_{-\infty}^{\infty} f(x)\,dx = 1$.</p>
```

If a slide is already at element budget and the exercise would push past the footer, move it to the *sibling slide that introduces the fact the exercise verifies* — not the slide that uses the fact.

**Chain / dependency diagram.** Inline flex row of math glyphs joined by token-colored arrows. Active edge in `--yonsei-blue`, sleeping edges in `--gray-text`. Place adjacent to the claim it supports (e.g. a Markov-chain illustration above the Markov identity). For longer chains use ellipsis nodes (`$\cdots$`) in `--gray-text`.

```html
<div style="display:flex; justify-content:center; align-items:center; gap:14px; margin:18px 0; font-size:1.55rem;">
  <span>$X^{(0)}$</span>
  <span style="color:var(--gray-text);">$\to$</span>
  <span>$\cdots$</span>
  <span style="color:var(--gray-text);">$\to$</span>
  <span>$X^{(n-1)}$</span>
  <span style="color:var(--yonsei-blue); font-weight:700;">$\to$</span>
  <span>$X^{(n)}$</span>
  <span style="color:var(--gray-text);">$\to$</span>
  <span>$X^{(N)}$</span>
</div>
```

For boxed nodes (more visual weight), use `.diagram-flow` + `.diagram-box` instead. For a plain inline chain, the bare flex above is lighter and fits more nodes.

---

## Companion note files

When detail is worth recording but doesn't fit on the slide (full-sentence explanations, derivations the proof slide skipped, secondary examples, "FYI" context), put it in `<deck>/<deck>-note.html` — one section per slide, in slide order, headed by the slide's title. Plain HTML so KaTeX `$…$` / `$$…$$` works the same as in the deck. The note file does not use the `.deck` / `.slide` engine; a simple `<article>` per slide is enough.

For lectures, the note file is also the natural home for the **expanded proof** when the slide carries the abbreviated version.

Not a paper draft, not a transcript. The speaker's reading companion.

---

## OUTLINE.md (per-folder index)

Every folder carries an `OUTLINE.md`: root navigator, folder overview, leaf subfolder. Leaf files list every deck's section table with `file:line` pointers and every named theorem/lemma/key formula with its line number. They are the canonical map for finding "where does proof X live" without grepping.

### Read-side rule — consult before writing

**Before writing or substantively rewriting any slide content, read the relevant `OUTLINE.md` files.** The cost is a few seconds; the reward is avoiding redefinition, contradiction, or duplication. Two scenarios trigger this:

1. **In-track continuity (same lecture series).** When extending a multi-deck series — e.g., writing `privacy/mia/mia3-theory.html` — open `privacy/mia/OUTLINE.md` and `privacy/OUTLINE.md` first. Confirm what notation, definitions, attacks, theorems, and benchmarks earlier decks already established. Do not redefine $(\varepsilon, \delta)$-DP if `privacy/dp/DP-FL.html` covered it; refer back via a brief "Recall (Lecture X)" instead. Conversely, if a prerequisite has *not* been covered, decide whether to (a) add a one-slide recap, (b) point students to the prior deck, or (c) defer the topic. Skipping this check produces decks that talk past each other.

2. **Cross-folder reuse (same topic, different track).** When writing on a topic that may already live elsewhere — diffusion (`infotheory/diffusion/` vs `privacy/diffusion/` vs `dllm/dllm.html`), DP (`privacy/dp/` vs `privacy/mia/mia1-foundations.html`), MI bounds (`infotheory/mi/` vs anywhere CLIP/InfoNCE comes up) — open the **root `OUTLINE.md` quick-lookup table** and the relevant leaf files in the *other* folder. Decide explicitly: reuse the derivation as-is, adapt to the new framing, link via "see also", or deliberately contradict (with rationale). Do not rederive a theorem in track B that already has a clean statement and proof in track A's notes — link to `<file>:<line>` instead.

When the OUTLINE entries you find are too coarse to answer the question, descend into the cited `<file>:<line>` and confirm. The OUTLINE points; it does not replace reading the deck.

### Write-side rule — keep outlines accurate

**Maintenance rule (non-negotiable):** any slide edit that changes a section boundary, line range, or named theorem location requires the corresponding `OUTLINE.md` line numbers to be updated *in the same change*. Adding a slide → add the entry. Removing a slide → remove it. Renaming a section → rename it everywhere it is cited (leaf, folder, root quick-lookup). Bulk renumbering after a multi-slide insertion is part of the edit, not a follow-up.

If you cannot locate a topic from the OUTLINE files, the OUTLINE files are stale — fix them, don't work around them. Stale outlines are worse than no outlines because they mislead.

When creating a new deck, add a stub entry in the leaf `OUTLINE.md` before writing the deck (file path + topic line). Cross-references to other decks (in the root quick-lookup table) get added when the relevant content is actually present.

---

## Extension checklist

Before adding a new component:

1. Is it a styled variation of an existing component? Use inline `style=` (with `var(--…)`, never hardcoded colors).
2. One-off on a single slide? Keep it inline.
3. Reused in ≥2 decks? Add it to `reference/deck.css` first, then this doc, then use it.

New components must document: name, purpose, default + `.bg-accent` appearance, an example, token dependencies. Candidates worth adding when you've reused the pattern enough to feel friction: `.theorem`, `.proof-step`, `.intuition-callout`. Until then, the recipes above using existing `.card` / `.math-block` / `.highlight` are the canonical form.

---

For pitfalls and lessons learned (italic prose collapse, KaTeX delimiter escape, em-dash orphans, the standalone-bundle bug, etc.), see **`GOTCHAS.md`**.
