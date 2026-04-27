# infotheory/lossy/ — Lossy compression (4 lectures)

Rate–distortion theory from Shannon's theorem to modern applied LLM compression. Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `lossy1-foundations.html` | `lossy1-foundations-note.html` | Rate–distortion foundations |
| `lossy2-gaussian-laplacian.html` | `lossy2-gaussian-laplacian-note.html` | Gaussian/Laplacian + Shannon LB + pruning + CROM |
| `lossy3-lattice-quip.html` | `lossy3-lattice-quip-note.html` | Lattice codes, QUIP, QUIP# |
| `lossy4-turboquant.html` | `lossy4-turboquant-note.html` | TURBOQUANT — online VQ via random rotations |

---

## lossy1-foundations.html — R(D) foundations

Section 05 collapsed: the binary toy now lives inside section 04 as the worked random-coding example, between Converse and the formal achievability slides.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:74, :85` |
| **01 — Problem setup** | Distortion, block codes, achievable region | `:113-183` |
| | Lossless not enough | `:121` |
| | Three distortion functions | `:131` |
| | Block code, per-letter distortion | `:152` |
| | Achievable region & R(D) | `:160` |
| **02 — Scalar quantization** | R∈{0,1,2}, Lloyd–Max alternating updates | `:185-372` |
| | Toy Gaussian setup (bullets + cases) | `:193` |
| | R=0: c*=μ, distortion=σ² | `:208` |
| | R=1: one threshold (scalar quantizer) | `:220` |
| | R=2: **Lloyd–Max coupling lemma** | `:229` |
| | Lloyd–Max — initial state | `:245` |
| | Lloyd–Max — Step ① (update x̂) | `:275` |
| | Lloyd–Max — Step ② (update τ) | `:305` |
| | Lloyd–Max — converged | `:335` |
| | Lloyd–Max convergence proof | `:365` |
| **03 — Why blocks win** | VQ beats SQ even on i.i.d. | `:374-506` |
| | Vector quantization | `:382` |
| | Round cells beat rectangles (5-4-5-4-5 hex tiling) | `:390` |
| | Sphere-like cells win | `:496` |
| **04 — Shannon's theorem (with binary worked example)** | Converse, binary toy, random coding | `:508-704` |
| | **Theorem statement** | `:516` |
| | Why mutual information appears (intuition) | `:527` |
| | Converse — outline | `:545` |
| | Converse step 1 — rate ≥ I (DPI) | `:557` |
| | Converse step 2 — single-letterize | `:568` |
| | Converse step 3 — convexity | `:579` |
| | Converse — summary | `:591` |
| | Binary toy — setup | `:603` |
| | Binary R(D) and the test channel | `:610` |
| | One source, many candidates | `:619` |
| | Codebook of 16 candidates (red-marked diffs) | `:627` |
| | Empirical joint matches the test channel (2×2 contingency) | `:660` |
| | Threshold rate from ball volume | `:677` |
| | Achievability — random codebook | `:686` |
| | Achievability — joint AEP | `:695` |
| Recap / End | | `:706` |

**Key:** Achievable region `:160`; Lloyd–Max examples `:245, :275, :305, :335`; Shannon theorem `:516`; converse `:545–:591`; binary worked example `:603–:677`; achievability `:686, :695`.

### Note (`lossy1-foundations-note.html`)
- Lossless vs lossy continuous sources
- Distortion modeling
- Block-code definition
- Achievable region convexity
- Distortion-ball cover of typical set
- R=1 Gaussian computation
- Lloyd–Max convergence detail
- VQ vs SQ details
- Random-coding rare-event bound
- Search creates dependence
- Volume-counting threshold

---

## lossy2-gaussian-laplacian.html — Gaussian, Laplacian, Shannon LB, pruning, CROM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Gaussian R(D)** | (1/2)log(σ²/D), achievability + converse | `:63-129` |
| | Statement | `:71` |
| | Achievability — backward Gaussian channel | `:78` |
| | Forward form — linear shrinkage | `:87` |
| | Converse — Gaussian maximizes entropy | `:94` |
| | Geometric picture | `:102` |
| **02 — Shannon lower bound** | Gaussian = worst case | `:131-162` |
| | Statement (squared error) | `:139` |
| | Proof — maximize entropy of error | `:148` |
| | Gaussian hits the bound — hardest source | `:156` |
| **03 — Laplacian R(D)** | Atom at zero in optimal reproduction | `:164-195` |
| | Setup + statement | `:172` |
| | Converse — auxiliary density trick | `:179` |
| | Achievability — sparse mixture | `:187` |
| **04 — Pruning from R(D)** | Optimal NN compression is sparse | `:197-232` |
| | Network and compressed weights | `:205` |
| | **Theorem — weight-distortion bounds output-distortion** | `:213` |
| | Pruning is optimal | `:222` |
| **05 — EVT and CROM** | Rateless lossy via extremes | `:234-269` |
| | Extremes are almost predictable | `:242` |
| | CROM (send index, reconstruct spike) | `:249` |
| | Iterate with random rotations | `:257` |
| Recap | | `:271` |

**Key:** Gaussian R(D) `:71`; backward channel `:78`; Shannon LB `:139`; auxiliary density trick `:179`; layer-wise telescoping `:213`.

**Bug fixed:** literal `<` inside math (e.g. `0<D\le σ²`) was being parsed as start of `<i>`/`<D>` tags by the HTML lexer, cascading garbage into all subsequent slides. Replaced with `&lt;` at lines 73, 79, 174.

### Note (`lossy2-gaussian-laplacian-note.html`)
- Backward vs forward channel
- Auxiliary-density trick derivation
- Laplacian mixture verification (characteristic functions)
- Atom-at-zero is not artifact
- Why L1 not L2 for pruning
- Why CROM rotations Gaussianize

---

## lossy3-lattice-quip.html — Lattice codes, QUIP, QUIP#

Restructured: dedicated section for original QUIP separate from QUIP#. Heavy material moved to note.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Why structure** | Cost says you can't search 2^{nR} | `:63-117` |
| | What a real quantizer must do (motivation) | `:71` |
| | Standard VQ recap | `:83` |
| | The complexity wall | `:90` |
| | Uniform quantization buys speed | `:107` |
| **02 — Lattice codes** | Core concept only | `:120-158` |
| | Definition | `:128` |
| | **Packing gain — regularity buys distortion** | `:136` |
| | Fast O(d) rounding via algebra | `:148` |
| **03 — Finite codebook** | Base lattice Λ, scaling Δ, spherical shaping | `:160-185` |
| | Three components | `:168` |
| | Why a sphere — match the typical set | `:178` |
| **04 — QUIP: incoherence processing** | Chee, Cai, Kuleshov, De Sa 2023 | `:187-237` |
| | The proxy loss | `:195` |
| | Incoherence — spectral outlier bound | `:204` |
| | Random rotations make weights incoherent | `:212` |
| | **LDLQ — adaptive per-coordinate rounding** | `:220` |
| | QUIP — end-to-end | `:228` |
| **05 — QUIP#: Hadamard + lattice** | Tseng, Chee, Sun, Kuleshov, De Sa 2024 | `:239-305` |
| | Two upgrades over QUIP | `:247` |
| | Step 1: Randomized Hadamard Transform | `:264` |
| | Step 2: E8 lattice codebook | `:273` |
| | BlockLDLQ — adaptive block rounding | `:281` |
| | The two-faced effective codebook | `:289` |
| Recap | | `:307` |

**Key:** Lattice definition `:128`; packing gain `:136`; QUIP proxy loss `:195`; LDLQ `:220`; RHT `:264`; E8 codebook `:273`; BlockLDLQ `:281`.

**Papers:**
- QUIP — arXiv:2307.13304 (Chee et al, 2023)
- QUIP# — arXiv:2402.04396 (Tseng et al, 2024)

### Note (`lossy3-lattice-quip-note.html`)
- Storage/search numerics for the complexity wall
- Linear-quantization MSE penalty (≤1.53 dB across all d)
- Lattice as additive subgroup, translation symmetry
- Packing-gain scale invariance, Zador lower bound
- E8 construction, 240 minimum vectors, Viazovska 8D optimality
- E8 fast-rounding algorithm (4 steps)
- Proxy loss derivation, orthogonal invariance
- Formal incoherence definition
- Why Kronecker rotation; why RHT requires sign-flip diagonal
- LDLQ exact theorem, tr(D) vs tr(H) comparison
- LDLQ ↔ OPTQ/GPTQ equivalence
- Berry–Esseen + union-bound argument for RHT incoherence
- BlockLDLQ Theorem 4.1 statement
- E8P codebook compression (16 → 8 bit lookup)
- Practical caveats (calibration, per-channel scales, RVQ, fine-tuning, activation quantization, non-power-of-2 dims, RFFT fallback)

---

## lossy4-turboquant.html — TURBOQUANT (online VQ for KV cache)

KV-cache motivation moved to the front of the deck.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:57, :67` |
| **KV cache intro** | What it is, why compress | `:105-130` |
| | What is the KV cache? | `:105` |
| | Why compress the KV cache? | `:119` |
| **01 — Setup, rotation idea** | Random rotation → known coordinate distribution | `:132-189` |
| | Why scalar quantization fails | `:140` |
| | Random rotation creates a known law | `:151` |
| | **Lemma 1 — coordinate of a sphere point** | `:160` |
| | Two distortions | `:171` |
| **02 — MSE TURBOQUANT** | Lloyd–Max on f_d, 4^{−b} exponent | `:191-236` |
| | Algorithm: TURBOQUANT_mse (algorithmic style) | `:199` |
| | One-bit anchor 1−2/π | `:214` |
| | **Theorem and proof outline** | `:222` |
| **03 — Lower bound** | Sphere SLB + Yao | `:238-262` |
| | Sphere SLB | `:246` |
| | Yao + constant gap | `:255` |
| **04 — Inner-product bias** | Good MSE ≠ good projections | `:264-288` |
| | One-bit MSE shrinks projections | `:272` |
| | Geometric reason — shrunken norm | `:280` |
| **05 — QJL & inner-product TURBOQUANT** | Two-stage decomposition | `:290-340` |
| | QJL definition | `:298` |
| | **Lemma — QJL unbiased, 1/d variance** | `:305` |
| | Two-stage decomposition | `:315` |
| | **Algorithm and theorem (TURBOQUANT_prod)** | `:324` |
| **06 — KV cache** | Why TURBOQUANT fits the KV cache | `:342-363` |
| | Online, data-oblivious, attention-preserving | `:350` |
| Recap | | `:365` |

**Key:** Lemma 1 `:160`; TURBOQUANT_mse theorem `:222`; sphere SLB `:246`; QJL lemma `:305`; TURBOQUANT_prod `:324`.

### Note (`lossy4-turboquant-note.html`)
- KV cache — what and why (cache size formula, online/data-oblivious/attention-preserving constraints)
- Why a random rotation Gaussianizes any fixed unit vector (Haar invariance → uniform spherical → Gaussian marginal)
- Where 4^{−b} comes from (Gaussian R(D) derivation); lossy-quantizer bias (1-bit shrinks magnitude to σ√(2/π))
- Lemma 1 — full proof (slice argument + co-area Jacobian + Beta normalization + Gaussian limit)
- Lloyd–Max on f_d — alternating updates, Bennett high-resolution limit, sample-free codebook, orthogonal invariance
- Panter–Dite formula and ∫ f_d^{1/3}
- QJL lemma — unbiasedness and variance proof
- Inner-product TURBOQUANT — two-stage decomposition derivation and bit-budget split
