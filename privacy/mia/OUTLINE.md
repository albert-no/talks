# privacy/mia/ — Membership inference attacks (5 lectures)

5-lecture series, paired `<deck>.html` + `<deck>-note.html`. Plus legacy `old/MIA.html` (single-file deck superseded by mia1+mia2). Notes contain extra proof detail and tables.

## Files

| Deck | Note | Topic |
|---|---|---|
| `mia1-foundations.html` | `mia1-foundations-note.html` | Foundations (2008–2019): Homer, MI game, DP bounds, evaluation |
| `mia2-shadow.html` | `mia2-shadow-note.html` | Shadow models: Shokri, LOGAN (GANs), Hisamoto (seq2seq) |
| `mia3-theory.html` | `mia3-theory-note.html` | Theory: Yeom (overfitting), Sablayrolles (BB≈WB), Salem (relaxed), Nasr (FL) |
| `mia4-modern.html` | `mia4-modern-note.html` | Modern: LiRA, Ye hierarchy, RMIA, label-only, defenses |
| `mia5-llm.html` | `mia5-llm-note.html` | LLMs: perplexity, neighbourhood, SPV, context-aware, InfoRMIA |
| `old/MIA.html` | — | Legacy consolidated deck (Lectures 1–2 era) |

---

## mia1-foundations.html

| Part | Topic | Line |
|---|---|---|
| **01** — Why MIA matters | central question, real-world stakes | `:78-140` |
| **02** — Homer et al. 2008 | distance statistic, t-test, NIH closure | `:141-276` |
| | Distance `D(Y_{i,j}) = \|Y_{i,j}-M_j\|-\|Y_{i,j}-Pop_j\|` | `:195` |
| | Aggregation t-test | `:224` |
| | NIH database closure | `:263` |
| **03** — Reconstruction → distinguishability | | `:277-442` |
| | IND-CPA cryptographic analogy | `:382` |
| | Privacy = indistinguishability → MIA | `:422` |
| **04** — The MI game | challenger, adversary, neighboring DBs | `:443-592` |
| | **Neighboring DBs** `D_1=D∪{x}, D_0=D\{x}` | `:471` |
| | **Advantage** `\|Pr[A=1\|b=1]-Pr[A=1\|b=0]\|` | `:489` |
| | **Neyman–Pearson lemma** `Λ(x) = p(T\|H1)/p(T\|H0)` | `:558` |
| | Error types | `:576` |
| **05** — DP, MI, taxonomy | | `:593-794` |
| | **DP bounds MI advantage** `Adv ≤ e^ε−1+δ` | `:606` |
| | Privacy attack taxonomy (membership/attribute/extraction/inversion) | `:682` |
| | Threat model spectrum | `:705` |
| | ROC, AUC, **TPR @ low FPR (Carlini critique)** | `:722-763` |
| | Standard benchmarks (CIFAR, Purchase, Texas, WikiMIA) | `:794` |

**Note (`mia1-foundations-note.html`):** DP→MI bound full proof `:57-72`; why log-log ROC matters `:45`; metric pitfalls `:49-53`.

---

## mia2-shadow.html

| Part | Topic | Line |
|---|---|---|
| **01** — Shokri et al. 2017 | shadow model paradigm | `:62-367` |
| | 3-stage architecture (shadows → labeled data → attack net) | `:99` |
| | Shadow data strategies | `:165` |
| | **Per-class attack models** `A_c: R^\|C\| → {0,1}` | `:212` |
| | Results: 93% precision, 91% recall (Purchase-100) | `:243` |
| | Pseudocode | `:316` |
| | Confidence-threshold baseline `1[max_c f(x)_c > τ]` | `:342` |
| **02** — LOGAN (Hayes et al.): MIA on GANs | | `:368-451` |
| | Discriminator + reconstruction-based attacks | `:398` |
| | Results: MNIST DCGAN ~74%, CIFAR ~69% | `:437` |
| **03** — Seq2seq (Hisamoto et al.): MT models | | `:452-575` |
| | **Perplexity** `PPL(x,y)=exp(-1/T Σ log p(y_t\|y_{<t},x))` | `:478, :505` |
| | seq2seq vs LLM MIA comparison | `:532` |

**Note (`mia2-shadow-note.html`):** Full Google results table including Texas-100 `:42-50`; calibration for LLMs vs seq2seq `:53-63`.

---

## mia3-theory.html

| Part | Topic | Line |
|---|---|---|
| **01** — Yeom et al. 2018 (overfitting) | | `:78-325` |
| | **Generalization gap** `Δ = R_pop − R_train` | `:104` |
| | **Threshold attack** `A(z) = 1[ℓ(f,z) ≤ τ]`, `τ = R_pop` | `:124` |
| | **Theorem: Adv_MI ≤ Δ** | `:143` |
| | Proof (3 parts: Markov on TPR, Markov on FPR, subtract) | `:156, :174, :192` |
| | Limitations (avg vs per-sample, threshold-only) | `:307` |
| **02** — Sablayrolles et al. 2019 (BB vs WB) | | `:326-520` |
| | **Bayes-optimal MI** `Λ(z) = p(Φ\|z∈D)/p(Φ\|z∉D)` | `:358` |
| | White-box features (loss, gradients, activations) | `:396` |
| | **Theorem: Λ_BB → Λ_WB** | `:436` |
| | Loss sufficiency intuition | `:451` |
| | Experimental validation (BB-WB gap < 1% AUC) | `:486` |
| **03** — Salem et al. (ML-Leaks) | three relaxations | `:521-657` |
| | No-shadow baseline `1[max_c > τ]` | `:606` |
| | Graceful degradation (~5% drop) | `:631` |
| **04** — Nasr et al. 2019 (white-box + FL) | | `:659-773` |
| | Per-layer gradients as features | `:685` |
| | Why gradients (members → small structured grads) | `:709` |
| | FL vulnerability: shared Δθ exposes WB info | `:728` |
| | Passive vs active attacks in FL | `:751` |
| **05** — Synthesis | timeline 2008–2019 | `:775-836` |

**Key theorems:** Yeom bound `:143`; Bayes-optimal `:358`; BB→WB convergence `:436`.

**Note (`mia3-theory-note.html`):** Full Yeom proof `:40-61`; per-sample vulnerability `:64-68`; bound tightness `:78-87`; ML-Leaks results table `:90-100`; Sablayrolles validation `:103-113`.

---

## mia4-modern.html

| Part | Topic | Line |
|---|---|---|
| **01** — Defenses recap | DP-SGD, comparison, broken adaptive defenses | `:86-181` |
| | **DP-SGD update** `g̃_t = (1/B)(Σ clip(g_i,C) + N(0,σ²C²I))` | `:122` |
| | Defenses broken by adaptive attacks (MemGuard, label smoothing, etc.) | `:168` |
| **02** — Why early evaluations misled | label-only MIA | `:182-256` |
| | Label-only (Choquette-Choo 2020) — boundary distance, ~100 queries | `:207-244` |
| **03** — LiRA: Carlini et al. 2022 | | `:257-524` |
| | **Likelihood ratio** `Λ(z) = p(ℓ\|z∈D)/p(ℓ\|z∉D)` | `:285` |
| | Estimating distributions (N/2 IN, N/2 OUT, fit Gaussians) | `:299` |
| | **LiRA formula** Gaussian PDFs | `:324` |
| | **Per-example calibration** `(μ_in,σ_in,μ_out,σ_out)` per z | `:339` |
| | Online vs offline | `:355` |
| | Computational cost (256 models for CIFAR-10) | `:376` |
| | TPR@0.01% FPR is 10–50× higher than prior | `:432` |
| | Evaluation revolution | `:449` |
| | Offline algorithm pseudocode | `:487` |
| **04** — Unified view (Ye et al. 2022) | | `:525-646` |
| | **Attack power hierarchy: LiRA ≥ Reference ≥ Population ≥ Threshold** | `:600` |
| | Privacy Meter (open-source tool) | `:629` |
| **05** — RMIA: Zarifzadeh et al. 2023 | | `:647-730` |
| | **Formula** `Λ(z) = p_θ(z) / (1/R Σ p_{θ_r}(z))` | `:674` |
| | Population ranking | `:689` |
| | RMIA TPR@0.1%: ~11% with 2–8 models (vs LiRA's 256) | `:704` |
| **06** — Beyond classification | diffusion model MIA | `:731-913` |
| | Reconstruction-loss timestep analysis | `:742, :764` |
| | LR paradigm universal | `:799` |

**Key formulas:** DP-SGD `:122`; LiRA LR `:285, :324`; RMIA LR `:674`; attack hierarchy `:600`.

**Note (`mia4-modern-note.html`):** Side-by-side pseudocode threshold/LiRA/RMIA `:43-74`; defense comparison table `:78-87`; cost-vs-power table `:92-103`.

---

## mia5-llm.html

| Part | Topic | Line |
|---|---|---|
| **01** — Why LLMs are different | | `:102-220` |
| | Three threat models (pre-train/FT/context) | `:139` |
| | **Perplexity baseline** `PPL(x) = exp(-1/T Σ log p_θ(x_t\|x_{<t}))` | `:166` |
| | Calibration challenge (5 strategies) | `:208` |
| **02** — Neighbourhood attack | | `:221-306` |
| | Mask-and-fill with T5 | `:245` |
| | **Score** `s(x) = log p_θ(x) − (1/K) Σ log p_θ(x̃^k)` | `:263` |
| **03** — SPV-MIA & context-aware | | `:307-426` |
| | SPV-MIA (target generates own calibration data) | `:316` |
| | Self-prompting strategies | `:330` |
| | LLaMA 0.85 AUC, GPT-2 0.80 (fine-tuning) | `:358` |
| | **Context-aware**: `s(x) = Var_c[log p_θ(x\|c)]` | `:395` |
| **04** — InfoRMIA | token-level | `:427-592` |
| | **Token surprise** `I_t = −log p_θ(x_t\|x_{<t})` | `:455` |
| | **Formulation** `s(x) = Σ w_t log(p_θ/p_ref)` | `:475` |
| | Identifying informative tokens (entities) | `:490` |
| | **Information-theoretic foundation** `I(z∈D; x_t \| x_{<t})` | `:545` |
| | SOTA: WikiMIA 0.74 AUC, 12% TPR@1% FPR | `:572` |
| **05** — Evaluation & scale | | `:593-683` |
| | Calibration zoo summary | `:618` |
| | Benchmarks: WikiMIA, MIMIR | `:656` |
| | **Larger models memorize more** | `:673` |
| **06** — MIA → extraction | | `:684-764` |
| | Chain: generate → rank by MIA → extract | `:696` |
| | Pseudocode: perplexity+neighbourhood `:733`, InfoRMIA `:751` |
| **07** — Defenses & governance | | `:765-894` |
| | DP fine-tuning | `:776` |
| | Deduplication (Carlini scaling laws) | `:795` |
| | Machine unlearning + MIA verification | `:812` |
| | GDPR / NYT v OpenAI | `:835` |
| **08** — Synthesis | timeline 2008–2025, four eras | `:895-1180` |
| | Open problems: pre-training detection, multi-modal, reference-free, agents/RAG | `:1000-1043` |
| | Key equations summary | `:1145-1175` |

**Key formulas:** Perplexity `:166`; Neighbourhood score `:263`; SPV `:348`; Context-aware variance `:395`; **InfoRMIA** `:475`; MI `:545`.

**Note (`mia5-llm-note.html`):** Side-by-side pseudocode perplexity/neighbourhood/InfoRMIA `:43-72`; full calibration zoo with InfoRMIA row `:74-79`.

---

## old/MIA.html

Legacy consolidated deck (~`:45` title) covering the foundational material now spread across mia1 + mia2 (Homer, indistinguishability, DP connection, evaluation, Shokri shadow models). Newer 5-lecture series supersedes it. Reference paths in this file are off by one level (broken before and after the recent reorg) — not actively used.
