# Talks Design System

Canonical spec for all decks in this repo. Applies to both **custom HTML decks** (e.g. `dllm/dllm.html`, `mia/MIA.html`, `privacy/DP-FL.html`) and the **Marp markdown** template (`template.md`). When the two disagree, `reference/deck.css` is the source of truth — Marp follows it.

Companion to `CLAUDE.md`. `CLAUDE.md` tells you *how* the repo is organized and built; this file tells you *what things look like* and *which class to use*.

**Source files:** the canonical tokens and components live in `reference/colors_and_type.css` (font loading + CSS variables) and `reference/deck.css` (slide engine + components). Decks link to these via `<link rel="stylesheet" href="../reference/…">`. Do not duplicate.

**Type scale note (2026-04).** The type scale below is the MID presentation scale — larger than the original compact scale to be readable from the back of a lecture hall. `h1` 3.6rem, `h2` 2.7rem, body 1.55rem. Bullet dots and diagram boxes are correspondingly larger.

**Reference target.** Kangwook Lee's BLISS seminar deck (<https://kangwooklee.com/talks/2026_03_BLISS/bliss_seminar.html>) is our readability benchmark. Zoomed-in captures of his rendering live in `reference/kangwook1.png`–`kangwook4.png`; the fonts in those shots are the *minimum acceptable* visual weight for our decks. If your slide renders noticeably smaller than those, something is wrong — most likely a per-deck `<style>` is shadowing the canonical tokens.

**Rule: don't shadow canonical tokens per-deck.** A deck's own `<style>` block must not redefine `p`, `li`, `h1`, `h2`, `h3`, `.small`, `.tiny`, `.subtitle`, or `.math-block` `font-size`. Those belong to `reference/deck.css`. Deck-local rules may only size **component classes** (`.card .desc`, `.paper-card .title`, `.sr-box p`, etc.), and those sizes should be expressed as fractions of the canonical body — roughly `1.05rem`–`1.3rem` for in-card copy. When content doesn't fit, reduce content — never shrink type.

---

## 1. Design Tokens

### 1.1 Color

| Token | Value | Use |
|---|---|---|
| `--yonsei-blue` | `#003876` | Primary accent. All `strong`, dividers, list bullets, h2 underline. |
| `--blue-light` | `#1a5296` | Secondary accent in cards, pill outlines, timeline numerals. |
| `--accent` | `#005baa` | Tertiary accent; token-pad fills. Use sparingly. |
| `--charcoal` | `#1a1a1a` | Body text. |
| `--dark` | `#2d2d2d` | Reserved alt text. Rarely needed. |
| `--gray-text` | `#666666` | Muted text (`em`, `.small`, `.tiny`, subtitles). Min 14px. |
| `--slate` | `#e8ecf0` | Card borders, table rules, token-fixed fill. |
| `--light` / `--subtle` | `#f4f6f9` | Card background, math block background, divider slide background. |
| `--line` | `#d9e1ea` | Marp table rule color. |
| `--white` | `#FFFFFF` | Slide background. |
| `--success` | `#2e8b57` | `ul.check` ticks, `.token-safe`. Affirmative only. |
| `--warn` | `#d94040` | `.token-eos`, urgent/negative. Never for regular body copy. |
| `--blue-glow` | `rgba(0,56,118,0.12)` | Corner accent gradient on every slide. |

**Contrast note.** `--charcoal` on white ≈ 15:1 (AAA). `--yonsei-blue` on white ≈ 10.6:1 (AAA). `--gray-text` on white ≈ 5.7:1 — **passes AA for body text ≥14px, fails for anything <14px**. `.tiny` at 0.8rem on gray is the edge case; prefer `--charcoal` there if readability matters.

### 1.2 Typography

Font family: Yonsei official typeface (`'Yonsei', 'Noto Sans', Arial, sans-serif`). Yonsei TTFs ship locally in `reference/fonts/` and are declared via `@font-face` in `colors_and_type.css` (Light 300, Bold 700, plus `YonseiBody` for Korean body copy and `YonseiLogo` for the wordmark). Noto Sans is a web-safe fallback from Google Fonts; the offline bundler strips it.

| Role | Size | Weight | Tracking | Line height |
|---|---|---|---|---|
| `h1` | 3.6rem (4rem on title, 4.2rem on left-section) | 700 | -0.04em | 1.08 |
| `h2` | 2.7rem | 700 | -0.03em | 1.12 |
| `h3` | 1.85rem | 700 | -0.02em | 1.22 |
| body `p`, `li` | 1.55rem | 300–400 | -0.01em | 1.5 |
| `.subtitle` | 1.75rem (1.9rem on title) | 300 | — | — |
| `.small` | 1.15rem | — | — | — |
| `.tiny` | 0.95rem | — | — | — |

Accent rules: `strong` → blue + weight 600. `em` → `--gray-text`, **not italic**. These are semantic — never hardcode colors inline when the right accent will do.

> **No italic, ever (prose).** Yonsei ships only four `font-style: normal` TTFs and we import Noto Sans without italic, so the browser synthesizes oblique by skewing normal glyphs — kerning breaks, adjacent words visually glue (e.g. "all positions" reads "allpositions"). Don't use `<i>`, inline `font-style: italic`, or rely on default `em` italic. In LaTeX math, wrap English phrases in `\text{…}`; bare words in math mode inherit the italic math face with zero spacing. See §7.6.

### 1.3 Spacing

Slide padding: `56px 72px 48px` (top / sides / bottom). Title slide uses `72px 88px`. Don't change these — they anchor the print-to-PDF layout.

| Spacer | Height |
|---|---|
| `.spacer-sm` | 12px |
| `.spacer` | 20px |
| `.spacer-lg` | 32px |
| `.flex-grow` | flex: 1 (fills remaining vertical space) |

Component internal padding lives on the component — see §2.

### 1.4 Border radius

| Value | Use |
|---|---|
| `12px` | `.card` |
| `10px` | `.diagram-box` |
| `8px` | `.math-block`, `.highlight` (right edge), `pre` |
| `6px` | `.token` |
| `3px` / `2px` | `.divider` end caps |
| `3.667em` | `.pill` (intentionally pill-shaped) |
| `50%` | `ul` bullet, numbered list counters |

### 1.5 Motion

```css
@keyframes fadeIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
```

Applied to every direct child of `.slide.active`, with staggered delays `0.06s → 0.30s` for children 2–6. Duration 0.4s, easing `ease`. Disabled in `@media print`.

### 1.6 Viewport

Fixed 1280 × 720px canvas, scaled to viewport via JS `transform`. Same dimensions govern the print stylesheet (`@page { size: 1280px 720px }`). Don't design for any other aspect ratio.

---

## 2. Components

### 2.1 `.slide` — slide container

Every slide is `<div class="slide">` inside `#deck`. Exactly one has `.active` at a time (the engine toggles this). `padding: 56px 72px 48px`, `display:flex; flex-direction:column`.

Background modifiers (all currently render **white** except `.bg-accent`):
- `.bg-navy`, `.bg-dark`, `.bg-deep` — intentional aliases for white; kept for future theming without touching markup.
- `.bg-light` — `--light` background. Good for side-by-side contrast slides.
- `.bg-accent` — Yonsei blue background, white text. Inverts all component defaults (cards get translucent white, bullets go white, highlight border goes white). Reserve for section dividers and big statement slides.

Every slide gets a subtle top-right radial-gradient corner accent via `.slide::before`. Don't override.

### 2.2 `.title-slide`

First slide. Adds `border-top: 5px solid var(--yonsei-blue)`, larger h1 (3rem, blue), and a `.title-logo` image element positioned top-right (80px, the Yonsei emblem at `reference/kor-eng2.png`). Required markup:

```html
<div class="slide title-slide active">
  <img class="title-logo" src="../reference/kor-eng2.png" alt="Yonsei University">
  <div class="pill pill-fill">…type of talk…</div>
  <h1>Talk title</h1>
  <div class="divider"></div>
  <p class="subtitle">One-line subtitle</p>
  <p>Speaker · Affiliation</p>
  <p class="small">Date</p>
</div>
```

### 2.3 `.section-slide`

Part dividers between acts of the talk. Centered, often paired with `.bg-accent`:

```html
<div class="slide section-slide bg-accent">
  <h1>Part II</h1>
  <div class="divider"></div>
  <p class="subtitle">Controllability</p>
</div>
```

### 2.4 `.divider`

Blue underline rule, 64 × 3px. Place immediately after `h2` on content slides, or under `h1` on title/section slides. Inverts to white inside `.bg-accent`.

### 2.5 `.pill`

Inline tag / chip. `1.5px` blue outline, `--blue-light` text, 6×20px padding.

Variants:
- default — outlined
- `.pill-fill` — solid blue, white text. Used for talk-type label on title slide.

### 2.6 `.card`

Neutral panel. `--light` background, `--slate` border, 12px radius, `24px 28px` padding. Inverts inside `.bg-accent` (translucent white fill + border).

Common pattern — 3-card grid:
```html
<div class="grid-3">
  <div class="card" style="text-align:center;">…</div>
  …
</div>
```

### 2.7 `.highlight`

Key-insight callout. Left border 3px blue, soft blue gradient background. Right-side border-radius only. Use **one per slide max** — it loses impact otherwise.

In Marp, `>` blockquotes render as this component automatically.

### 2.8 Layout helpers

| Class | Behavior |
|---|---|
| `.cols` | Horizontal flex; equal children unless overridden. |
| `.col-2-3`, `.col-1-3` | Flex-ratio overrides inside `.cols`. |
| `.grid-2` | 2-column grid, 24px gap. |
| `.grid-3` | 3-column grid, 24px gap. |

### 2.9 Lists

Default `ul` uses a blue dot bullet. Variants:
- `ul.check` — green ✓
- `ul.arrow` — blue →
- `ul.num` — blue circular numeric badge

All invert on `.bg-accent`. Items get `padding-left: 24px` and `margin-bottom: 8px`.

### 2.10 `.math-block`

Display-math wrapper. `--light` background, 8px radius, centered, 1.15rem. Put KaTeX `$$…$$` inside:

```html
<div class="math-block">$$\mathcal{L} = \mathbb{E}[-\log p_\theta(x_0)]$$</div>
```

Inline math: just `$x$` in the flow — auto-renders via the `<script>` in the head.

### 2.11 `.diagram-flow` / `.diagram-box`

Horizontal flowchart. `.diagram-box` is an outlined blue rounded box; `.filled` inverts it. Arrows between boxes go in a separate span (`.diagram-arrow`).

### 2.12 `.token-*`

Mini chips for showing token states in decoding diagrams.

| Class | Color | Meaning |
|---|---|---|
| `.token-mask` | dashed slate | `[MASK]` token |
| `.token-gen` | solid blue | just generated |
| `.token-fixed` | solid gray | already committed |
| `.token-eos` | solid red (`--warn`) | end-of-sequence |
| `.token-safe` | solid green | passed a safety check |
| `.token-pad` / `-pad2` / `-pad3` | blue / purple / amber | arbitrary categories when you need 3+ |

### 2.13 Tables

Thin, uppercase headers in blue, `--slate` rules. No outer borders. Inverts on `.bg-accent`.

### 2.14 `.progress-bar` + `.slide-num`

Engine adds these once per deck. `.progress-bar` is a 3px blue bar anchored to slide bottom; `.slide-num` sits bottom-right. Both hidden in print.

### 2.15 `.brand-footer`

Subtle Yonsei lockup at bottom-left of content slides. Gives every slide (not just the title) the same institutional anchor the official Yonsei template uses. Optional per deck — include when presenting externally; skip for internal/draft decks.

```css
.brand-footer {
  position: absolute; bottom: 18px; left: 28px;
  display: flex; align-items: center; gap: 8px;
  font-size: 0.72rem; color: var(--gray-text);
  letter-spacing: 0.12em; text-transform: uppercase;
  font-weight: 500;
  z-index: 100;
}
.brand-footer img { height: 18px; opacity: 0.9; }
.bg-accent .brand-footer { color: rgba(255,255,255,0.85); }
```

Markup:
```html
<div class="brand-footer">
  <img src="../reference/kor-eng2.png" alt="">
  <span>Yonsei University</span>
</div>
```

Hidden in print (add `.brand-footer { display:none !important; }` inside `@media print` if it clutters the PDF; keep visible otherwise).

### 2.16 `.toc` — agenda / contents slide

Numbered list with a blue vertical rule between each number and its label. One-row-per-section; four rows is the sweet spot (matches official template).

```css
.toc-list { display: flex; flex-direction: column; gap: 22px; margin-top: 16px; }
.toc-item {
  display: grid;
  grid-template-columns: auto 3px 1fr;
  gap: 24px;
  align-items: center;
}
.toc-num {
  font-size: 1.6rem; font-weight: 600;
  color: var(--yonsei-blue); letter-spacing: -0.02em;
}
.toc-rule {
  background: var(--yonsei-blue);
  align-self: stretch;
  min-height: 40px;
  border-radius: 2px;
}
.toc-label { font-size: 1.25rem; font-weight: 500; color: var(--charcoal); }
.toc-sub { font-size: 0.95rem; color: var(--gray-text); margin-top: 2px; }
```

Usage:
```html
<div class="slide">
  <h2>Contents</h2><div class="divider"></div>
  <div class="toc-list">
    <div class="toc-item">
      <div class="toc-num">01</div>
      <div class="toc-rule"></div>
      <div>
        <div class="toc-label">Where do dLLMs stand?</div>
        <div class="toc-sub">Field progress</div>
      </div>
    </div>
    <!-- repeat -->
  </div>
</div>
```

### 2.17 `.section-slide.left`

Left-aligned variant of `.section-slide`. Reads like a book-chapter opener — "01" in blue, title on the next line. Keep the centered version (default) for dramatic interludes; use `.left` for structural part breaks inside a long talk.

```css
.section-slide.left {
  align-items: flex-start;
  text-align: left;
  padding: 96px 96px;
}
.section-slide.left .section-num {
  font-size: 1.6rem; font-weight: 600;
  color: var(--yonsei-blue);
  letter-spacing: -0.02em;
  margin-bottom: 8px;
}
.section-slide.left h1 { font-size: 3rem; margin-bottom: 0; }
.section-slide.left .divider { margin: 14px 0 18px; }
.section-slide.left .subtitle { font-size: 1.2rem; color: var(--gray-text); }
```

Usage:
```html
<div class="slide section-slide left">
  <div class="section-num">02</div>
  <h1>Controllability</h1>
  <div class="divider"></div>
  <p class="subtitle">Masking schedules, guided remasking, safety</p>
</div>
```

Works on white or `.bg-accent` (background flips, accent becomes white).

### 2.18 `.end-slide`

Closing slide — Q&A, Thank You, or similar. Centered, big, on-brand (white background, blue word).

```css
.end-slide { justify-content: center; align-items: center; text-align: center; }
.end-slide .big-word {
  font-size: 5rem; font-weight: 600;
  color: var(--yonsei-blue);
  letter-spacing: -0.04em;
  line-height: 1;
}
.end-slide .big-word-sub {
  margin-top: 18px;
  color: var(--gray-text);
  font-size: 1.1rem;
}
```

Usage:
```html
<div class="slide end-slide">
  <div class="big-word">Q&amp;A</div>
  <p class="big-word-sub">Thank you.</p>
</div>
```

---

## 3. Slide engine (JS)

Lives in a single `<script>` at the end of the body. Three responsibilities:

1. **Scale.** Reads viewport, sets `transform: translate(-50%,-50%) scale(min(vw/1280, vh/720))` on `.deck`. Re-runs on resize.
2. **Navigate.** Keyboard (←/→/↑/↓/Space/PgUp/PgDn/Home/End), touch swipe (>50px threshold), click (right-half = next, left-half = prev; ignores clicks on `<a>` / `<button>`).
3. **Indicate.** Updates `#slideNum` text and `#progressBar` width.

Do not modify. Copy verbatim into new decks.

---

## 4. Print-to-PDF (required)

Every custom HTML deck must include the `@media print` block from `CLAUDE.md §Print-to-PDF support`. Without it, `Cmd+P` prints only the active slide. The block:

- Forces `@page { size: 1280px 720px; margin: 0 }`.
- Neutralizes the JS scale transform.
- Makes all slides flow, one per page.
- Disables animations and hides progress/slide-num UI.

Export recipe: Chrome → `Cmd+P` → Save as PDF → Margins **None** → Background graphics **on** → Save.

---

## 5. Usage guidelines

### 5.1 Style priorities (from `CLAUDE.md`)

1. **One idea per slide.** If you need two cards of prose, it's two slides.
2. **Prose emphasis.** `**strong**` = Yonsei Blue accent (important terms, new concepts). `*em*` = muted gray (parenthetical asides). Don't mix.
3. **Key insight → blockquote** (Marp) or `.highlight` (HTML). Max one per slide.
4. **Math-heavy slide.** Wrap display math in `.math-block` / `$$…$$`.

### 5.2 Do / Don't

| Do | Don't |
|---|---|
| Reuse existing classes. | Invent new component classes per deck. |
| Keep the `<style>` block byte-identical across decks. | Ad-hoc color tweaks in a single deck. |
| Use `.bg-accent` for section dividers and statement slides. | Use `.bg-accent` for dense content slides — it fights with cards and highlights. |
| Let the engine handle nav — don't add custom click targets. | Bind click handlers directly on slides. |
| Pair `h2` with `.divider` on every content slide. | Skip the divider; the slide feels unanchored. |
| Put title-logo and title-slide together. | Use `.title-logo` on non-title slides. |
| Scale component-internal text in the `1.05rem–1.35rem` range (relative to canonical body at 1.55rem). | Redefine `p` / `li` / `h2` / `h3` / `.small` / `.tiny` / `.math-block` in a per-deck `<style>`. Those are canonical; deck.css owns them. |
| When a slide feels cramped, cut content or split the slide. | Shrink the type scale to cram in more. The Kangwook reference shots (`reference/kangwook*.png`) show the minimum acceptable size. |
| Build math-labelled diagrams as HTML (flex/grid + divs) with a thin SVG overlay for arrows only. | Put `$x_i$` inside an SVG `<text>` — KaTeX auto-render skips SVG text and the literal `$x_i$` will show. |
| Use `$$…$$` (display math) inside a `.math-block` for `\begin{cases}` and other multi-row constructs. | Use `$…$\displaystyle$…$` with `white-space:nowrap` + `overflow-x:auto` to force layout — the cases overflow gets clipped at the right edge. |
| Prefer static step-labeled diagrams (①②③④ badges) so everything is visible at once. | Ship continuous SMIL / CSS animation for talks — the audience waits through each loop. Keep auto-animation for self-paced web versions only. |
| Anchor absolute-positioned decorative content to `right` / `top` and leave ≥ 40 px clear in the bottom-left. | Absolute-position floats to `bottom-left`, where the auto-injected `.brand-footer` (Yonsei wordmark) already lives. |
| Let `.slide` keep its canonical `position: absolute; inset: 0`. Child `position:absolute` elements anchor to it automatically. | Write `style="position:relative"` on a `.slide` to give children a positioning context. It overrides `inset:0`, so the slide no longer fills the deck and `.brand-footer` lands out of place. |

### 5.3 Slide recipes

**Content slide**
```
<h2> + <div class="divider"></div>
<div class="cols"> … prose on left, .card on right … </div>
(optional) <div class="highlight"> key insight </div>
```

**Three-pillar slide**
```
<h2> + <div class="divider"></div>
<div class="grid-3">
  <div class="card" style="text-align:center;">①  <h3>…</h3>  <p class="small">…</p></div>
  … ×3 …
</div>
```

**Comparison slide**
```
<h2> + <div class="divider"></div>
<table>
  <thead><tr><th>…</th><th>…</th></tr></thead>
  <tbody>…</tbody>
</table>
```

**Math-heavy slide**
```
<h2> + .divider
<p>Setup prose with inline $x_t$.</p>
<div class="math-block">$$…$$</div>
<p><strong>Key insight:</strong> …</p>
```

**Section divider (centered)**
```
<div class="slide section-slide bg-accent">
  <h1>Part N</h1> <div class="divider"></div> <p class="subtitle">…</p>
</div>
```

**Section divider (left, numbered — §2.17)**
```
<div class="slide section-slide left">
  <div class="section-num">02</div>
  <h1>Controllability</h1>
  <div class="divider"></div>
  <p class="subtitle">…</p>
</div>
```

**Contents / agenda slide (§2.16)**
```
<h2>Contents</h2> + .divider
<div class="toc-list">
  <div class="toc-item">
    <div class="toc-num">01</div>
    <div class="toc-rule"></div>
    <div><div class="toc-label">…</div><div class="toc-sub">…</div></div>
  </div>
  … ×4 …
</div>
```

**Closer slide (§2.18)**
```
<div class="slide end-slide">
  <div class="big-word">Q&amp;A</div>
  <p class="big-word-sub">Thank you.</p>
</div>
```

**Diagram with math-rendered labels (HTML + SVG-arrows pattern)**

When the diagram needs KaTeX-rendered labels (e.g. `$C_1$`, `$g_i$`, `$M(x_i)$`), build the structural layer in HTML and use SVG only for arrows. The `.fl4-*` classes in `privacy/DP-FL.html` (slide 4) and the `.ldp-*` classes (slide 9) are the reference.
```
<div class="diag-wrap">
  <div class="diag-server">Server · holds $\theta$</div>
  <svg class="diag-arrows" viewBox="0 0 600 110" preserveAspectRatio="none">
    <g stroke="#003876" stroke-width="2" fill="none" marker-end="url(#ar)">
      <path d="…"/> …
    </g>
  </svg>
  <div class="diag-clients">
    <div class="diag-client">
      <div class="dot">$C_1$</div>
      <div class="lbl">① compute $g_1$ from $D_1$</div>
    </div>
    …
  </div>
</div>
```
- The arrow SVG uses `preserveAspectRatio="none"` and a wide viewBox so the arcs stretch with the HTML boxes.
- Labels ("① compute $g_1$ from $D_1$") are plain HTML — KaTeX auto-render picks them up and turns the `$…$` into math.
- Component-level font sizes for the boxes should stay in the `1.1rem – 1.35rem` range; don't override canonical `p` / `li` inside the diagram.

---

## 6. Extension checklist

When you think you need a new component, check first:

1. Is it actually a styled variation of `.card`, `.pill`, `.highlight`, or `.diagram-box`? Use an inline `style=` rather than a new class.
2. Is it a one-off on a single slide? Keep it inline.
3. Is it something you'll reuse in ≥2 decks? Then add it here first, then to the skeleton, then use it.

New components must document: name, purpose, default + inverted (`.bg-accent`) appearance, an example snippet, and any token dependencies.

---

## 7. Common pitfalls (lessons learned)

These are the mistakes that keep reappearing in per-deck work. `CLAUDE.md` has the short form; this section explains why.

### 7.1 Fonts "look small" → somebody shadowed the canonical tokens

Symptom: body text / headings on a deck look noticeably smaller than the Kangwook reference (`reference/kangwook*.png`) or smaller than a sibling deck.

Cause: a per-deck `<style>` block redefined `p`, `li`, `h2`, `h3`, `.small`, `.tiny`, `.subtitle`, or `.math-block` `font-size`. Canonical values live in `reference/deck.css` and were tuned for back-of-room readability after the deck's `transform: scale()` is applied.

Fix: delete those overrides. Component-scoped sizes (e.g. `.sr-box p`, `.paper-card .desc`) are fine in the `1.05rem–1.35rem` range, but canonical tokens are off-limits.

### 7.2 Brand footer moves around → a slide opted out of `inset: 0`

Symptom: the "Yonsei University" wordmark drifts vertically or horizontally, or disappears, on specific slides.

Cause: that slide has an inline `style="position:relative"`. `.slide` is canonically `position: absolute; inset: 0`; overriding it to `relative` breaks the fill. Children with `position: absolute` already anchor to the slide (since `absolute` *is* a positioned value) — you don't need to force `relative`.

Fix: remove the `position:relative` override. Anchor any absolutely-positioned decorative content (images, overlays) to `right`/`top` and leave the bottom-left clear for the footer.

### 7.3 "$g_1$" shows as literal text → label is in SVG `<text>`

Symptom: inline math inside a diagram renders as `$g_1$` instead of italic *g* with a subscript.

Cause: the label sits inside an SVG `<text>` element. KaTeX auto-render walks the HTML DOM; it doesn't descend into SVG text nodes.

Fix: move the math-bearing labels to HTML. Use an HTML+CSS layout for the diagram structure (flex/grid, div "boxes", CSS-styled circles) and a thin SVG overlay for arrows only. Reference implementations: `.fl4-*` (slide 4), `.ldp-*` (slide 9), `.rdm-*` (slide 30) in `privacy/DP-FL.html`.

### 7.4 Cases block gets clipped → shorten content or switch to `$$…$$`

Symptom: the right column of `\begin{cases}` (typically "otherwise" / "if …") is cut off at the slide's right edge.

Cause: the math-block uses `$\displaystyle …$` with `white-space:nowrap; overflow-x:auto` to coerce layout, and the rendered width exceeds the container.

Fix: use `$$…$$` (display math) inside a plain `.math-block` — KaTeX will size itself naturally. Shorten the cases labels to math form: `m \in \text{top-}k` instead of `\text{if } \langle v, U_m\rangle \text{ is among the top } k$; `\text{else}` instead of `\text{otherwise}`. If it still overflows, the slide has too much content — cut a bullet.

### 7.5 Animation for live talks is a mistake

Symptom: during a talk, the audience is waiting for the animation to finish before the speaker can make the next point.

Cause: SMIL `animateMotion` / CSS keyframe cycles loop indefinitely and dictate pacing that the speaker doesn't control.

Fix: make the diagram static and label every step with ①②③④ badges placed directly on the relevant elements. The speaker controls pacing by talking through the steps in order. Keep auto-animation for self-paced web versions of the deck.

### 7.6 Parenthesized text renders as italic math → KaTeX delimiter escape bug

Symptom: plain prose with `(...)` or `[...]` renders in italic math font with no inter-letter space. Examples: `(learned or heuristic)` shows as `learnedorheuristic`, `[M]` inside a `.token-mask` shows a slanted italic `M` distinct in height from the upright `is`/`blue` word tokens next to it.

Cause: the KaTeX auto-render `onload` handler defines four delimiter pairs. The latter two are supposed to be LaTeX-style `\(...\)` and `\[...\]`. In the HTML attribute, they must be written **double-escaped** so the JS string parser leaves a literal backslash in place:

```html
<!-- CORRECT — double backslash -->
onload="renderMathInElement(document.body,{delimiters:[
  {left:'$$',right:'$$',display:true},
  {left:'$', right:'$', display:false},
  {left:'\\(',right:'\\)',display:false},
  {left:'\\[',right:'\\]',display:true}
],throwOnError:false});"

<!-- WRONG — single backslash -->
{left:'\(',right:'\)',display:false},
{left:'\[',right:'\]',display:true}
```

With the wrong form, the JS string parser treats `\(` as an unrecognized escape and silently drops the backslash. KaTeX then sees its left delimiter as a bare `(` (and `)`, `[`, `]`), so any parenthesized or bracketed prose gets rendered as inline math — italic math font, no word spacing, different line metrics from surrounding text.

Fix:
- Use the double-backslash form in every deck's `onload` attribute. `reference/deck-skeleton.html` has the correct version; `scripts/new-talk.sh` will propagate it for new talks.
- Audit existing decks: `for f in */*.html; do grep -H "renderMathInElement" "$f" | grep -c "\\\\\\\\(" ; done`. Each deck must show a `\\\\(` occurrence, not `'\\(` (single).
- After fixing, hard-reload with DevTools "Disable cache" — the handler runs on script onload, not on page DOM-ready, so stale behavior isn't obvious from a casual refresh.

### 7.7 Italic prose collapses spaces → Yonsei has no italic face

Symptom: a word or phrase rendered with `font-style: italic` (via `<i>` or inline `style="font-style:italic"`) reads as a single glued string.

Cause: `reference/colors_and_type.css` registers four Yonsei TTFs, all with `font-style: normal` — there is no italic face. The Noto Sans import only pulls weights 300–700, again without italic. When the browser is asked to render italic it falls back to *synthesized oblique*: it skews the normal glyphs by ~12°. Synthesized oblique inherits the upright metrics, so kerning pairs and side-bearings are wrong, and on tight lines (table rows, card copy) adjacent words visually merge.

Fix:
- **No italic in prose.** `em` is globally `font-style: normal; color: var(--gray-text)` — that is the intended "muted" look. Use `<strong>` (Yonsei Blue accent) for emphasis instead.
- **No `<i>`, no inline `font-style: italic`.** If you catch these in a deck, rip them out.
- **In KaTeX math, English phrases belong in `\text{…}`.** `\text{all positions}` gives real spaces; bare `all positions` in math mode renders each letter in the italic math face with zero inter-letter space. Identifier letters stay italic (correct math typography); the rule only applies to English phrases.
- **If prose that isn't in math mode still renders italic, suspect §7.6** before blaming the font stack.

### 7.8 Standalone bundle renders equations as raw `$...$` strings

Symptom: `<deck>.standalone.html` shows literal `$x_i$` text; the authoring source renders fine.

Cause (historical, fixed 2026-04): `scripts/bundle.py` re-emits the KaTeX `onload="renderMathInElement(document.body, {delimiters:[{left:'$$',…}]});"` handler into a small inline script. Its earlier regex `onload=["\']([^"\']+)["\']` treated both quote types as terminators, so the handler was truncated at the first inner `'` and never called.

Fix (in the code): the regex now uses alternation — `onload=(?:"([^"]*)"|'([^']*)')` — and takes whichever group matched. Verify after bundling with `chrome --headless --dump-dom <standalone>.html | grep -c 'class="katex"'` — should be ≥ 1 for any deck with math.

---

## 8. Source files

- **Canonical CSS:** `reference/colors_and_type.css` (font-face + tokens) and `reference/deck.css` (engine + components). Decks link to these; they are not duplicated per deck.
- **Canonical JS:** `reference/deck.js`.
- **Fonts:** `reference/fonts/Yonsei{Light,Bold,Body,Logo}.TTF`.
- **Marp equivalent:** `template.md` — stays in sync with the CSS tokens, but Marp can't do the full component set (no cards, no token chips, no diagram-flow).
- **Brand assets:** `reference/kor-eng2.png` (Yonsei emblem), `reference/kor-eng2.pdf` (vector).
- **Build:** `scripts/new-talk.sh <name>` creates a new deck, `scripts/bundle.py <deck.html>` produces the truly-offline `.standalone.html` sibling.
