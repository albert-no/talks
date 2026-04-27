# infotheory/mi/ — Mutual-information estimation (2 lectures)

Variational MI bounds → contrastive learning (InfoNCE/CLIP). Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `mi1-bounds.html` | `mi1-bounds-note.html` | Variational lower bounds on MI (BA, DV, NWJ, MINE) |
| `mi2-infonce-clip.html` | `mi2-infonce-clip-note.html` | InfoNCE and CLIP |

---

## mi1-bounds.html — Variational lower bounds on MI

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Setup** | Density ratios from samples | `:63-95` |
| | MI as KL | `:71` |
| | Samples-only setting | `:82` |
| | Density-ratio framing | `:89` |
| **02 — Barber–Agakov** | Variational LB via q(x\|y) | `:97-138` |
| | **Theorem (BA bound)** | `:105, :107` |
| | Proof — add and subtract log q | `:116` |
| | BA in practice → MLE | `:123` |
| **03 — Donsker–Varadhan** | Dual KL representation, MINE | `:140-183` |
| | **Theorem (DV representation)** | `:148, :150` |
| | DV bound on MI | `:159` |
| | Proof — tilt Q by e^T | `:166` |
| | MINE — neural DV estimator | `:172` |
| **04 — NWJ** | Linear-surrogate variant | `:185-220` |
| | Theorem (Nguyen, Wainwright, Jordan 2010) | `:198, :199` |
| | NWJ vs DV variance trade | `:205` |
| **05 — Tradeoffs** | High MI is fundamentally hard | `:222-262` |
| | High-MI barrier (McAllester–Stratos) | `:230, :232` |
| | Three bounds side-by-side | `:239` |
| | Choosing your bound | `:251` |

**Key theorems:** BA bound `:107`; DV representation `:151`; DV→MI bound `:159`; NWJ bound `:199`; McAllester–Stratos variance bound `:232`.

### Note (`mi1-bounds-note.html`)
- Density ratio as unifying view `:25`
- MINE estimator bias `:31`
- McAllester–Stratos lower bound `:37`
- Toy bivariate Gaussian detail `:43`
- f-divergences and f-GAN connection `:55`
- Why CLIP/InfoNCE is different from these `:67`

---

## mi2-infonce-clip.html — InfoNCE and CLIP

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:34, :45` |
| **01 — InfoNCE** | K-class softmax bounded by log K | `:73-119` |
| | Setup — 1 positive, K−1 negatives | `:81` |
| | **Theorem (InfoNCE bound)** | `:89, :91` |
| | Proof sketch | `:101` |
| | Optimal critic = log-density-ratio | `:110, :112` |
| **02 — CLIP architecture** | InfoNCE at web scale | `:122-179` |
| | Two encoders, one space | `:130` |
| | Separable critic + symmetric loss | `:150` |
| | N×N similarity matrix | `:159` |
| **03 — Zero-shot classification** | Reusing the contrastive head | `:181-221` |
| | CLIP as classifier | `:189` |
| | Why it works — InfoNCE ≈ MAP | `:201` |
| | Prompt engineering | `:209` |
| **04 — Practice** | Bias, variance, batch size | `:223-269` |
| | Four bounds side-by-side | `:231` |
| | Why batch size matters | `:245` |

**Key:** InfoNCE bound `:93`; optimal critic = log-ratio `:112`; log K saturation `:96`.

### Note (`mi2-infonce-clip-note.html`)
- Full InfoNCE proof detail `:25`
- Why exactly log K saturation `:42`
- Temperature τ in CLIP `:48`
- Why symmetric loss `:55`
- CLIP zero-shot recipe `:62`
- Robustness / other zero-shot capabilities `:73`
- What CLIP doesn't do well `:79`
