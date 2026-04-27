# privacy/ — Privacy series

Three sub-tracks: diffusion (foundations course, no notes), DP (single NeurIPS 2023 talk), and MIA (5-lecture series with paired notes + legacy file).

## Subfolders

- **`diffusion/`** — Diffusion generative models from scratch (5 lectures). No companion `-note.html` files; proofs are in-deck. `note/2_difffusion.tex` is LaTeX source covering Lectures 1–2. See `diffusion/OUTLINE.md`.
- **`dp/`** — Differential privacy + federated learning (NeurIPS 2023 talk). Single deck `DP-FL.html` plus `dp-fl.txt` (compressed handout) and `figs/`. See `dp/OUTLINE.md`.
- **`mia/`** — Membership inference attacks (5 lectures, paired notes). Plus legacy `old/MIA.html`. See `mia/OUTLINE.md`.

## Quick lookup

| Topic | Where | Lines |
|---|---|---|
| Bayes-route reverse derivation | `diffusion/diffusion1-foundations.html` | `:194-345` |
| Tweedie's formula | `diffusion/diffusion1-foundations.html` | `:374` |
| DDPM VP forward + VLB + ε-loss | `diffusion/diffusion2-ddpm.html` | `:90-333` |
| Fokker–Planck + Anderson reverse SDE | `diffusion/diffusion3-sde-score.html` | `:135-315` |
| Score-matching theorem | `diffusion/diffusion3-sde-score.html` | `:339` |
| DDIM (deterministic, ODE, inversion) | `diffusion/diffusion4-ddim.html` | `:134-281` |
| Classifier-free guidance | `diffusion/diffusion5-guidance-discrete.html` | `:202-282` |
| Discrete diffusion + score-entropy loss | `diffusion/diffusion5-guidance-discrete.html` | `:287-425` |
| (ε,δ)-DP definition | `dp/DP-FL.html` | `:375-395` |
| Local DP minimax rate | `dp/DP-FL.html` | `:483` |
| PrivUnit mechanism | `dp/DP-FL.html` | `:523` |
| **RRSC + k-closest exact-optimality (NeurIPS 2023)** | `dp/DP-FL.html` | `:571-822` |
| DP-Diffusion / DP-RDM | `dp/DP-FL.html` | `:852-1004` |
| Yeom overfitting bound | `mia/mia3-theory.html` | `:143` |
| Sablayrolles BB≈WB | `mia/mia3-theory.html` | `:436` |
| LiRA | `mia/mia4-modern.html` | `:264-503` |
| RMIA | `mia/mia4-modern.html` | `:647-720` |
| InfoRMIA (LLM token-level) | `mia/mia5-llm.html` | `:427-590` |

## Theme connections

- **diffusion ↔ MIA**: diffusion-model MIA is a research frontier — `mia/mia4-modern.html:731-789` covers it. The diffusion-models theory in `privacy/diffusion/` provides the substrate.
- **DP ↔ MIA**: `mia/mia1-foundations.html:601-617` shows DP as MIA bound (`Adv ≤ e^ε−1+δ`); `dp/DP-FL.html` builds the DP machinery. DP-SGD is referenced from `mia/mia4-modern.html:117`.
- **Theoretical diffusion (`infotheory/diffusion/`) vs from-scratch (`privacy/diffusion/`)**: same math, different presentation. The infotheory series uses information-theoretic / hierarchical-VAE framing (cleaner for theory students); the privacy series uses the Bayes-+-Taylor route and goes further (5 lectures including SDE, DDIM, CFG, discrete).
