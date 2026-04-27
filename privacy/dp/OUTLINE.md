# privacy/dp/ — Differential privacy + federated learning

Single talk (NeurIPS 2023): exact-optimal LDP mean estimation under shared randomness, with extensions to DP in modern ML.

## Files

| File | Purpose |
|---|---|
| `DP-FL.html` | Main slide deck |
| `dp-fl.pdf` | PDF export |
| `dp-fl.txt` | Compressed text outline / handout (does not duplicate the deck) |
| `figs/` | Slide figures (`sphereical_cap.jpg`, `rrsc.png`) |

---

## DP-FL.html

**Topic:** From DP foundations through PrivUnit to RRSC exact-optimality (NeurIPS 2023), then DP in modern ML (DP-SGD, DP-Diffusion, DP-RDM).

### Sections

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-250` |
| **01 — FL & mean estimation** | | `:255-359` |
| | Federated learning (4-step diagram) | `:266` |
| | Three challenges in FL (compress, privacy, utility) | `:325` |
| | **Core primitive: $\hat\mu = \frac{1}{n}\sum x_i$ with bits + LDP + low MSE** | `:348` |
| **02 — LDP vs Central DP** | | `:364-569` |
| | **Definition: $(\varepsilon,\delta)$-DP (Dwork et al. 2006)** | `:375, :378` |
| | Local vs central DP comparison | `:393` |
| | Central trust bar | `:399` |
| | LDP trust bar (untrusted server) | `:427` |
| | **Definition: LDP (density-ratio form)** | `:460, :465` |
| | **LDP mean estimation: minimax rate $\Theta(d/(n\min(\varepsilon, \varepsilon^2)))$ (DJW 2013)** | `:483, :488` |
| | Gaussian mechanism is suboptimal | `:501` |
| | **PrivUnit (Bhowmick et al. 2018): spherical-cap, optimal constant** | `:523, :528` |
| | Missing axis: communication / finite bits | `:543` |
| **03 — Exact optimality (NeurIPS 2023)** | | `:571-822` |
| | Problem setup (jointly optimize rate, utility, privacy) | `:581` |
| | LDP with shared randomness (seed U public) | `:612` |
| | **Result I — canonical protocols** (single encoder/decoder, unbiased) | `:653, :656` |
| | **Result II — codebook schemes are optimal** | `:673, :676` |
| | **Result III — RRSC: rotationally symmetric simplex codebook** | `:689, :694` |
| | **Result IV — k-closest encoding is optimal** (two-level density) | `:738, :743` |
| | RRSC → PrivUnit as M→∞ | `:756` |
| | Unified framework (SQKR, FT21, MMRC vs RRSC) | `:773` |
| | Experiments | `:799` |
| | Open question: optimal among all protocols? | `:811` |
| **04 — DP in modern ML** | | `:827-1004` |
| | DP-SGD pipeline (clip + noise + accounting) | `:837` |
| | **DP-Diffusion (Ghalebikesabi et al. 2023)** — public pretrain, private FT | `:852` |
| | **DP-RDM (Lebensold et al. 2024)** — privatize retrieval | `:878` |
| | DP-RDM pipeline diagram | `:905` |
| | DP-RDM intuition (privacy boundary, λ knob) | `:961` |
| | DP at realistic scale | `:982` |
| | Q&A | `:1009` |

### Key theorems / formulas

| Item | Line |
|---|---|
| (ε,δ)-DP definition | `:378-380` |
| LDP definition (density ratio ≤ e^ε) | `:465-466` |
| LDP minimax rate `Θ(d/(n min(ε,ε²)))` | `:488-490` |
| PrivUnit spherical-cap mechanism | `:528-529` |
| Result I: canonical protocols | `:656-663` |
| Result II: codebook optimality | `:676-678` |
| Result III: RRSC (Haar-rotated simplex) | `:694-697` |
| Result IV: k-closest two-level density | `:743-744` |
| Sampled Gaussian Mechanism | `:951-954` |

## dp-fl.txt

35-slide compressed outline (FL → challenges → mean est. → LDP vs DP → PrivUnit → RRSC → experiments → DP-Diffusion). Companion to the deck, not a duplicate. Quick reference handout.

## No companion `-note.html`

Unlike `mia/`, there is no separate notes file. Proof detail is in-deck (mostly Part 03). For deeper DP background outside this deck, look up the cited papers (DJW 2013, Bhowmick 2018, Ghalebikesabi 2023, Lebensold 2024).
