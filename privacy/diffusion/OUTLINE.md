# privacy/diffusion/ — Diffusion generative models (5-lecture series)

Master-level course on diffusion: Bayes-route foundations → DDPM → SDE → DDIM → guidance + discrete diffusion. **No companion `-note.html` files** — proofs are in-deck. `note/2_difffusion.tex` is LaTeX source covering Lectures 1–2.

## Files

| Deck | Topic |
|---|---|
| `diffusion1-foundations.html` | Generative models, VE forward, Bayes-route reverse, Tweedie |
| `diffusion2-ddpm.html` | VP forward, DDPM, VLB three-term decomposition, ε-loss |
| `diffusion3-sde-score.html` | Continuous-time SDE, Fokker–Planck, Anderson reverse, score matching |
| `diffusion4-ddim.html` | Non-Markovian forward, deterministic sampling, probability-flow ODE |
| `diffusion5-guidance-discrete.html` | Classifier guidance, CFG, inpainting, discrete diffusion |
| `note/2_difffusion.tex` | LaTeX source for Lectures 1–2 (rigorous mathematical write-up) |

---

## diffusion1-foundations.html — Foundations

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-68` |
| **01 — Generative models** | | `:72-129` |
| | Realistic is not enough | `:81` |
| | Sampling is non-trivial (Cauchy) | `:96` |
| | Inverse transform sampling (1D) | `:107` |
| | High dimension breaks this | `:118` |
| **02 — VE forward process** | | `:134-178` |
| | Forward `X^(n) = X^(n-1) + Z^(n)` | `:143` |
| | n steps in one shot | `:155` |
| | Terminal distribution | `:166` |
| | Goal: reverse the chain | `:178` |
| **03 — Reverse via Bayes** | Taylor + complete-square route | `:194-345` |
| | Setup | `:203` |
| | Proof outline | `:212` |
| | Step 1: Taylor expand P_X | `:226` |
| | Step 2: approximate P_Y | `:235` |
| | Step 3: substitute back | `:249` |
| | **Step 4: complete the square — KEY reverse conditional** | `:262` |
| | Reverse conditional, compactly (score) | `:287, :290` |
| | Reverse sampling rule | `:298` |
| | Why not subtract noise? | `:308` |
| **04 — Score function & Tweedie** | | `:353-424` |
| | Score function `s(x;n) = ∂_x log P_{X^(n)}` | `:362` |
| | **Tweedie's formula (Robbins 1956)** | `:374, :378` |
| | Train a denoiser, not a score | `:388` |
| | Denoiser-to-score conversion | `:399, :405` |

**Key:** Reverse conditional `:287-290`; Tweedie `:378-380`; denoiser-to-score `:405`.

---

## diffusion2-ddpm.html — DDPM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-85` |
| **01 — VP forward** | | `:90-152` |
| | Why variance preserving | `:99` |
| | **VP forward** `X^(n) = √(1−β_n) X^(n-1) + √β_n Z^(n)` | `:114` |
| | n steps in one shot, `ᾱ_n = ∏(1−β_i)` | `:126, :129` |
| | **Convergence: MGF proof** → `N(0,1)` | `:139, :142` |
| **02 — DDPM reverse** | | `:157-184` |
| | Reverse conditional, VP version | `:166` |
| | What the network learns | `:176` |
| **03 — Variational lower bound** | | `:189-333` |
| | Generative model | `:198` |
| | Why maximize marginal | `:213` |
| | Likelihood → VLB (Jensen) | `:225` |
| | Markov rewrite | `:238` |
| | **Three-term decomposition `L_N + Σ L_n + L_0`** | `:262, :265` |
| | L_N: match the prior | `:271` |
| | **L_n: match each reverse step (training signal)** | `:286` |
| | Target posterior is Gaussian | `:299` |
| | KL for matched-variance Gaussians | `:312` |
| | **ε-prediction reparameterization, `s_θ = −ε_θ/√(1−ᾱ_n)`** | `:321, :324` |
| **04 — Algorithms** | | `:336-410` |
| | Training algorithm (5 steps) | `:345` |
| | Sampling algorithm | `:361, :371` |
| | Three approximation errors | `:380` |

**Key:** VP forward `:114`; one-shot `:129`; MGF proof `:142`; VLB three-term `:265`; ε-loss `:324`.

---

## diffusion3-sde-score.html — SDE + score matching

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-67` |
| **01 — Discrete to continuous** | | `:72-129` |
| | VE as SDE `dX_t = √β dZ_t` | `:81` |
| | VP as SDE (OU) | `:91` |
| | General forward SDE | `:104` |
| **02 — Fokker–Planck** | | `:135-220` |
| | **Theorem (1D FP):** `∂_t p_t = −∂_x(f p_t) + (g²/2)∂_x² p_t` | `:144, :148` |
| | Proof — test function route | `:156-210` |
| **03 — Anderson's reverse SDE** | | `:225-315` |
| | **Theorem (Anderson 1982):** reverse drift = `f − g² ∂_x log p_t` | `:234, :239` |
| | Proof outline (reverse-time FP, p_t solves both) | `:248-292` |
| | Why Anderson matters (DDPM = Euler–Maruyama) | `:306` |
| **04 — Score matching** | | `:320-475` |
| | Natural loss is intractable | `:329` |
| | **Theorem (Vincent 2011): score matching = denoising** | `:339, :344` |
| | Proof (Bayes posterior trick) | `:351-400` |
| | VP noise kernel | `:413` |
| | ε-reparameterization | `:423` |
| | Example: OU | `:435` |
| | Multi-dimensional extension | `:445` |
| | DDPM is discrete score matching | `:458` |

**Key theorems:** Fokker–Planck `:148`; Anderson reverse SDE `:239`; score matching `:344`; OU kernel `:439`.

---

## diffusion4-ddim.html — DDIM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-85` |
| **01 — What DDPM loss sees** | | `:90-127` |
| | DDPM ε-loss recap | `:99` |
| | **KEY: only marginals enter** | `:108` |
| | DDIM in one sentence | `:120` |
| **02 — Non-Markovian forward** | | `:134-207` |
| | Setup | `:142` |
| | Forward conditional (depends on x_n+1 and x_0) | `:154` |
| | **Marginals match DDPM (claim + proof by induction)** | `:164, :175` |
| | DDPM as special case | `:189` |
| | σ_n→0: deterministic forward | `:199` |
| **03 — Sampling** | | `:212-281` |
| | Training unchanged (same ε-net) | `:221` |
| | **Predicted clean signal** `x̂_0` | `:234` |
| | DDIM reverse update | `:243` |
| | Sampling algorithm | `:251` |
| | **Probability-flow ODE** (σ_n=0 limit) | `:272, :275` |
| **04 — Consequences** | | `:286-347` |
| | Three benefits (fewer steps, inversion, interpolation) | `:294` |
| | DDPM or DDIM? | `:318` |

**Key:** Marginal invariance `:164-167`; predicted-clean inversion `:234`; ODE `:275-276`.

---

## diffusion5-guidance-discrete.html — Guidance + discrete diffusion

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-85` |
| **01 — Classifier guidance** | | `:90-147` |
| | Conditional generation | `:99` |
| | **Bayes decomposition** `∇log P(X\|Y) = ∇log P(X) + ∇log P(Y\|X)` | `:113, :119` |
| | Time-dependent classifier on noisy inputs | `:126` |
| | Guided reverse SDE | `:137` |
| **02 — Inpainting** | | `:151-197` |
| | Setup (Ω mask) | `:160` |
| | Approximating the conditional score | `:171` |
| | Inpainting sampler | `:181` |
| **03 — Classifier-free guidance** | | `:202-282` |
| | Why drop the classifier | `:211` |
| | **CFG identity**: `ω log P(X\|Y) + (1−ω) log P(X)` | `:223, :227` |
| | Dual-role network (drop probability `p_drop`) | `:234` |
| | **CFG sampling rule** `ε̃ = ω ε_θ(X,y) − (ω−1) ε_θ(X,∅)` | `:249` |
| | CFG in practice | `:261` |
| **04 — Discrete diffusion** | | `:287-425` |
| | What breaks (no additive noise) | `:295` |
| | Forward: transition matrices | `:310` |
| | Uniform vs absorbing | `:320` |
| | Continuous-time limit | `:341` |
| | **Reverse rate matrix**: `Q̄_t(y,x) = (p_t(y)/p_t(x)) Q_t(x,y)` | `:350` |
| | **Discrete score = ratio vector** `s(x,t)_y = p_t(y)/p_t(x)` | `:362, :365` |
| | Squared loss fails | `:375` |
| | **Score-entropy loss (Lou et al. 2024)** | `:388, :391` |
| | Sequence space (Hamming-sparsity) | `:399` |

**Key:** Bayes decomposition `:119`; CFG identity `:227`; CFG sampling `:249`; discrete ratio score `:365`; score entropy `:391`.

---

## note/2_difffusion.tex

LaTeX source — rigorous write-up of foundational material:
- Sec 1: Generative models (distribution learning, sampling, Cauchy, inverse transform)
- Sec 2: 1D diffusion — VE forward + Bayes-route reverse

Underlying material for Lectures 1–2 (the deck versions are condensed presentations of this).
