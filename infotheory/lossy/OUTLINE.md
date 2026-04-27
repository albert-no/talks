# infotheory/lossy/ — Lossy compression (4 lectures)

Rate–distortion theory from Shannon's theorem to modern applied LLM compression. Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `lossy1-foundations.html` | `lossy1-foundations-note.html` | Rate–distortion foundations |
| `lossy2-gaussian-laplacian.html` | `lossy2-gaussian-laplacian-note.html` | Gaussian/Laplacian + Shannon LB + pruning + CROM |
| `lossy3-lattice-quip.html` | `lossy3-lattice-quip-note.html` | Lattice codes and QUIP# |
| `lossy4-turboquant.html` | `lossy4-turboquant-note.html` | TURBOQUANT — online VQ via random rotations |

---

## lossy1-foundations.html — R(D) foundations

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:28, :39` |
| **01 — Problem setup** | Distortion, block codes, achievable region | `:72-141` |
| | Lossless not enough | `:80` |
| | Three distortion functions | `:90` |
| | Block code, per-letter distortion | `:111` |
| | Achievable region & R(D) | `:119, :122` |
| **02 — Scalar quantization** | R∈{0,1,2}, Lloyd–Max | `:143-198` |
| | R=0: c*=μ, D(0)=σ² | `:158` |
| | R=1: one threshold | `:166` |
| | R=2: **Lloyd–Max coupling lemma** | `:175, :177` |
| | Lloyd–Max convergence | `:191` |
| **03 — Why blocks win** | VQ beats SQ even on i.i.d. | `:200-256` |
| | Round cells beat rectangles | `:216` |
| | Typical-shell concentration | `:250` |
| **04 — Shannon's theorem** | R(D)=inf I(X;X̂) s.t. E[d]≤D | `:258-311` |
| | **Theorem statement** | `:270` |
| | Why mutual information appears | `:277` |
| | Achievability — random codebook | `:284` |
| | Achievability — joint AEP | `:291` |
| | Converse (DPI + chain rule) | `:301` |
| **05 — Binary toy n=24, D=1/4** | Hamming balls, threshold rate | `:313-362` |
| | Bernoulli/Hamming setup | `:321` |
| | Threshold rate from ball volume | `:353` |

**Key:** Achievable region `:122`; Shannon theorem `:270`; achievability `:284`; converse `:301`; binary R(D)=1−H_b(D) `:326`.

### Note (`lossy1-foundations-note.html`)
- Lossless vs lossy continuous sources `:41`
- Distortion modeling `:47`
- Block-code definition `:53`
- Achievable region convexity `:59`
- Distortion-ball cover of typical set `:65`
- R=1 Gaussian computation `:77`
- Lloyd–Max convergence detail `:94`
- VQ vs SQ details `:105`
- Random-coding rare-event bound `:125`
- Search creates dependence `:137`
- Volume-counting threshold `:154`

---

## lossy2-gaussian-laplacian.html — Gaussian, Laplacian, Shannon LB, pruning, CROM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Gaussian R(D)** | (1/2)log(σ²/D), achievability + converse | `:63-129` |
| | Statement | `:71, :73` |
| | Achievability — backward Gaussian channel | `:78, :80` |
| | Forward form — linear shrinkage | `:87, :89` |
| | Converse — Gaussian maximizes entropy | `:94` |
| **02 — Shannon lower bound** | Gaussian = worst case | `:131-163` |
| | Statement (squared error) | `:139, :141` |
| | Proof — maximize entropy of error | `:148` |
| **03 — Laplacian R(D)** | Atom at zero in optimal reproduction | `:164-196` |
| | Setup + statement | `:172, :174` |
| | Converse — auxiliary density trick | `:179, :180` |
| | Achievability — sparse mixture | `:187, :189` |
| **04 — Pruning from R(D)** | Optimal NN compression is sparse | `:197-233` |
| | **Theorem — weight-distortion bounds output-distortion** | `:215` |
| | Pruning is optimal | `:222` |
| **05 — EVT and CROM** | Rateless lossy via extremes | `:234-270` |
| | CROM (send index, reconstruct spike) | `:249` |
| | Iterate with random rotations | `:257` |

**Key:** Gaussian R(D) `:73`; backward channel `:80`; Shannon LB `:141`; auxiliary density trick `:180`; layer-wise telescoping `:215`.

### Note (`lossy2-gaussian-laplacian-note.html`)
- Backward vs forward channel `:29`
- Auxiliary-density trick derivation `:45`
- Laplacian mixture verification (characteristic functions) `:59`
- Atom-at-zero is not artifact `:76`
- Why L1 not L2 for pruning `:82`
- Why CROM rotations Gaussianize `:88`

---

## lossy3-lattice-quip.html — Lattice codes + QUIP#

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Why structure** | Shannon says go to high d; cost says you can't | `:58-99` |
| | Standard VQ recap | `:66` |
| | Complexity wall | `:73` |
| **02 — Lattice codes** | Regular grid, uniform Voronoi, algebraic rounding | `:101-136` |
| | Definition | `:109, :110` |
| | **Packing gain** | `:117, :119` |
| | Fast O(d) rounding | `:129` |
| **03 — Finite codebook** | Base lattice Λ, scaling Δ, spherical shaping | `:138-163` |
| | Three components | `:147, :152` |
| | Why a sphere (typical set match) | `:156` |
| **04 — QUIP#** | Tseng et al. 2024 | `:165-216` |
| | Source–channel mismatch | `:173` |
| | Step 1: Hadamard rotation | `:180, :185` |
| | Step 2: Lattice quantize + code | `:189` |
| | Two-faced effective codebook | `:197` |

**Key:** Lattice definition `:110`; packing gain G(Λ) `:119`; QUIP# components `:147`; Hadamard Gaussianization `:185`.

### Note (`lossy3-lattice-quip-note.html`)
- Storage/search number derivation `:29`
- E8 buys-in-practice `:35`
- Fast rounding for E8 `:42`
- Why Hadamard specifically `:53`
- CLT precise argument `:59`
- Practical caveats (calibration, per-channel scales) `:71`

---

## lossy4-turboquant.html — TURBOQUANT (online VQ)

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — Setup, rotation idea** | Random rotation → known coordinate distribution | `:69-117` |
| | Random rotation creates known law | `:84` |
| | **Lemma 1 — coordinate of sphere point** | `:91, :93` |
| | Two distortions | `:102` |
| **02 — MSE TURBOQUANT** | Lloyd–Max on f_d, 4^{−b} exponent | `:120-163` |
| | Algorithm | `:128` |
| | One-bit anchor 1−2/π | `:144` |
| | **Theorem TURBOQUANT_mse** | `:152, :154` |
| | Panter–Dite formula | `:159` |
| **03 — Lower bound** | Sphere SLB + Yao | `:166-189` |
| **04 — Inner-product bias** | Good MSE ≠ good projections | `:192-213` |
| | One-bit MSE shrinks projections | `:200` |
| **05 — QJL & inner-product TURBOQUANT** | Two-stage decomposition | `:216-265` |
| | QJL definition | `:224` |
| | **Lemma — QJL unbiased, 1/d variance** | `:231, :233` |
| | Two-stage decomposition | `:241` |
| | **Theorem TURBOQUANT_prod** | `:249, :259` |
| **06 — KV cache** | Online, data-oblivious, attention-preserving | `:269-289` |

**Key:** Lemma 1 `:93`; TURBOQUANT_mse theorem `:154`; sphere SLB `:177`; Panter–Dite `:159`; QJL lemma `:233`; TURBOQUANT_prod theorem `:259`.

### Note (`lossy4-turboquant-note.html`)
- Slice argument for f_d `:29`
- Gaussian limit derivation `:36`
- Panter–Dite formula detail `:42`
- Computing ∫ f_d^{1/3} `:54`
- Key Gaussian identity in QJL `:66`
- Why two-stage is necessary asymptotically `:78`
