---
marp: true
math: katex
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600&display=swap');

  :root {
    --yonsei-blue: #003876;
    --blue:        #003876;
    --blue-light:  #1a5296;
    --text:        #1a1a1a;
    --muted:       #666666;
    --subtle:      #f4f6f9;
    --line:        #d9e1ea;
  }

  /* ── Base ── */
  section {
    font-family: 'Noto Sans', Arial, sans-serif;
    font-weight: 400;
    letter-spacing: -0.01em;
    background: #ffffff;
    color: var(--text);
    padding: 56px 72px 48px;
    font-size: 1.05rem;
    line-height: 1.6;
  }

  /* ── Typography ── */
  h1 {
    font-size: 2.4rem; font-weight: 600;
    letter-spacing: -0.04em; line-height: 1.15;
    margin-bottom: 0;
  }
  h2 {
    font-size: 1.75rem; font-weight: 500;
    letter-spacing: -0.03em; line-height: 1.2;
    margin-bottom: 6px;
  }
  h3 {
    font-size: 1.2rem; font-weight: 500;
    letter-spacing: -0.02em;
  }

  /* Blue rule beneath h2 (mimics .divider) */
  h2::after {
    content: '';
    display: block;
    width: 48px; height: 3px;
    background: var(--blue);
    border-radius: 2px;
    margin-top: 10px;
  }

  /* ── Accent: strong → blue, em → muted ── */
  strong { color: var(--blue); font-weight: 600; }
  em     { color: var(--muted); font-style: normal; }

  /* ── Blockquote → highlight box ── */
  blockquote {
    border-left: 3px solid var(--blue);
    padding: 12px 18px;
    margin: 14px 0;
    background: rgba(0, 0, 201, 0.04);
    border-radius: 0 6px 6px 0;
    font-style: normal;
    color: var(--text);
  }
  blockquote p { margin: 0; }

  /* ── Math display wrapper ── */
  .katex-display {
    background: var(--subtle);
    border-radius: 8px;
    padding: 14px 20px;
    margin: 14px 0;
    overflow-x: auto;
  }

  /* ── Tables ── */
  table { border-collapse: collapse; width: 100%; font-size: 0.95rem; }
  th {
    color: var(--blue); font-size: 0.8rem;
    text-transform: uppercase; letter-spacing: 0.06em;
    font-weight: 500;
    border-bottom: 2px solid var(--line);
    padding: 6px 14px;
  }
  td { padding: 8px 14px; border-bottom: 1px solid var(--line); }

  /* ── Code ── */
  code {
    font-size: 0.88em;
    background: var(--subtle);
    border-radius: 4px;
    padding: 1px 6px;
  }
  pre code { padding: 0; background: none; }
  pre {
    background: var(--subtle);
    border-radius: 8px;
    padding: 16px 20px;
    font-size: 0.85rem;
    line-height: 1.5;
  }

  /* ── Slide number ── */
  section::after {
    color: #bbb;
    font-size: 0.72rem;
    font-weight: 400;
  }

  /* ── Title slide ── */
  section.title {
    justify-content: flex-end;
    padding-bottom: 72px;
    border-top: 5px solid var(--blue);
  }
  section.title h1 { font-size: 2.8rem; margin-bottom: 16px; }
  section.title p  { color: var(--muted); font-size: 1.05rem; }

  /* ── Yonsei logo on title slide ── */
  section.title::after {
    content: '';
    position: absolute;
    top: 36px; right: 48px;
    width: 80px; height: 80px;
    background: url('../reference/kor-eng2.png') no-repeat center / contain;
  }

  /* ── Section divider slide ── */
  section.divider {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: var(--subtle);
  }
  section.divider h1 { font-size: 2.4rem; }
---

<!--
  HOW TO USE THIS TEMPLATE
  ========================
  Run:   marp template.md --pdf   (or --html, --pptx)
  Watch: marp --watch template.md

  Math:
    Inline  →  $x_t = \sqrt{\bar\alpha_t}\, x_0 + \sqrt{1-\bar\alpha_t}\,\epsilon$
    Display →  $$\mathcal{L} = \mathbb{E}\bigl[-\log p_\theta(x_0)\bigr]$$

  Accent colors in prose:
    **blue text** and *muted/gray text* are handled by CSS.

  Highlight box:
    > Key insight: blockquotes become left-bordered highlight boxes.

  Two-column layout (HTML in Marp):
    <div class="columns">
    <div>Left column</div>
    <div>Right column</div>
    </div>
    (add .columns { display:flex; gap:32px; } to the style block)
-->

---
<!-- _class: title -->

# Why Diffusion LLMs Behave Differently — and How to Control Them

Albert No · Yonsei University

*March 2026 · Invited Talk*

---

## Why Now?

Three forces arriving at once:

- **Autoregressive LLMs** dominate — but left-to-right decoding is a hard constraint
- **Discrete diffusion** models crossed from toy-scale to **competitive 7B+ systems** in < 2 years
- New generation paradigm → *new behaviors, new failure modes, new opportunities*

> **2024–2025**: dLLMs crossed the threshold from "interesting research direction" to "practical alternative" for the first time.

---

## The Forward Process

Tokens are *masked* progressively. At time $t$:

$$
q(x_t \mid x_0) = \prod_{i=1}^{L} \mathrm{Cat}\!\left(x_t^{(i)};\; (1-\beta_t)\, x_0^{(i)} + \beta_t\, m\right)
$$

where $m$ is the `[MASK]` token and $\beta_t \in [0,1]$ is the masking schedule.

**Key insight:** unlike continuous diffusion, there is no noise — only erasure.

---

## Reverse Process

The model learns to predict the original token at every masked position simultaneously:

$$
p_\theta(x_0 \mid x_t) = \prod_{i:\, x_t^{(i)}=m} p_\theta\!\left(x_0^{(i)} \mid x_t\right)
$$

This is the source of **parallel decoding** — all positions are resolved in $T$ passes, not $L$ steps.

---

## Math Tips: Inline vs. Display

**Inline** — use single `$…$` for variables inside prose.

> The masking ratio at step $t$ is $\bar\alpha_t = 1 - \beta_t$.

**Display** — use `$$…$$` on its own paragraph for standalone equations.
The rendered block sits on a light gray background automatically.

**Align environments** work too:

$$
\begin{aligned}
\mathcal{L}_{\mathrm{ELBO}} &= \mathbb{E}_q\!\left[\log p_\theta(x_0\mid x_T)\right]\\
                             &- \sum_{t=1}^{T} D_{\mathrm{KL}}\!\left(q(x_{t-1}\mid x_t, x_0)\;\|\;p_\theta(x_{t-1}\mid x_t)\right)
\end{aligned}
$$

---

## Comparison Table

| Property           | Autoregressive LLM | Discrete Diffusion LLM |
|--------------------|--------------------|------------------------|
| Decoding order     | Left → right       | **Any order**          |
| Passes per sample  | $L$ serial steps   | $T \ll L$ parallel     |
| Infilling          | Awkward            | **Native**             |
| Token dependencies | Causal only        | Bidirectional          |

---

<!-- _class: divider -->

# Part II
## Controllability

---

## Key Takeaways

- Diffusion LLMs introduce **bidirectional context** and **parallel decoding** — a fundamentally different inductive bias
- Current gap vs. AR: *fluency on open-ended generation*; dLLMs win on *constrained tasks*
- Controllability surfaces: masking schedules, token confidence, guided remasking

> **Next:** formal guarantees for constrained decoding without fine-tuning.

---
