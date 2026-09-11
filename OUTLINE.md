# Talks repo — content outline

Slide decks for Yonsei talks (academic conferences + master-level lectures). Repo conventions in `CLAUDE.md`, design rules in `DESIGN_SYSTEM.md`, pitfalls in `GOTCHAS.md`.

Each topic folder has its own `OUTLINE.md`. Leaf subfolders have detailed per-deck outlines with slide and theorem line numbers. **For specific content, descend into the relevant folder's OUTLINE.md.**

## Folders

### `courses/` — semester-long lecture series

- **`courses/infotheory/`** — Information-theory course. Four artifact types: `lectures/` (slides), `notes/` (LaTeX notes), `exam/`, and `overleaf/` (frozen archive). See `courses/infotheory/OUTLINE.md`.
  - `lectures/` — slide series, 8 numbered topic folders (paired decks + `-note.html`):
    - `01-entropy/` — Foundations: entropy, KL, joint/conditional MI, DPI, Fano (2 lectures)
    - `02-lossless/` — Codes/Kraft/Huffman, AEP/arithmetic, Markov/LZ (3 lectures)
    - `03-diffentropy/` — Differential entropy, MaxEnt/Gaussian/EPI, AWGN/water-filling/I-MMSE (3 lectures)
    - `04-lossy/` — Rate–distortion + LLM compression (4 lectures)
    - `05-mi/` — Variational MI bounds, InfoNCE/CLIP (2 lectures); closes with $f$-divergence unification
    - `06-divergence/` — $f$-divergence + GAN ($\equiv$ JS), Fisher divergence + score matching ($\equiv$ diffusion) (2 lectures)
    - `07-diffusion/` — Diffusion as hierarchical VAE; closes with score-matching equivalence (3 lectures)
    - `08-ib/` — Information Bottleneck: IB Lagrangian, VIB, information plane (2 lectures)
  - `notes/` — canonical LaTeX notes (2026); `exam/` — finals 2024–26; `overleaf/` — frozen legacy source
- **`courses/privacy/`** — Privacy series. Three artifact types: `lectures/` (slides, 6 numbered topic folders), `exam/` (homework/midterm/final set), and `overleaf/` (frozen legacy source). See `courses/privacy/OUTLINE.md`.
  - `lectures/01-dp/` — Differential privacy: 8 decks, `dp1`–`dp7` foundations + `dp8-fl.html` capstone (NeurIPS 2023: RRSC result). LaTeX source in `tex/dp.tex`
  - `lectures/02-generative/` — Generative-model review: 5 diffusion lectures (Bayes-route, DDPM, SDE, DDIM, guidance + discrete) + 1 brief LLM deck. `note/2_difffusion.tex` is LaTeX source for Diffusion Lectures 1–2
  - `lectures/03-memorization/` — Memorization in generative models (2 decks split 2026-05: `memorization-diffusion.html` covers intro/lawsuits/Bartz, three formal definitions, diffusion detection, SAIL, CLIP-pad, with companion note `memorization-diffusion-note.html`; `memorization-llm.html` covers exposure theory → Feldman → extraction/Min-K → ACR → books → defenses, math-detail revision 2026-08 at 128 slides with companion note `memorization-llm-note.html`). Paper-figure assets in `figs/`
  - `lectures/04-mia/` — Membership inference attacks (5 lectures, paired notes; legacy `old/MIA.html`)
  - `lectures/05-unlearning/` — Machine unlearning (2 decks, both math-detail revised 2026-08 with per-slide companion notes: `unlearning1-foundations.html` 109 slides — definitions, certified deletion with proofs, SISA, classification, metrics-as-test; `unlearning2-llm.html` 100 slides — why the certificate does not transfer, the LLM objective family, benchmarks as main figure + measurement claim, closure under fine-tuning; sourced from `slide.pdf`). Paper-figure assets in `figs/`
  - `lectures/06-watermark/` — LLM watermarking (1 deck + speaker note, 123 slides: hypothesis-test frame, green-list, distortion-free, undetectable, limits, robust, radioactivity/SynthID/dgMARK)
  - `exam/` — homework (HW1–4), midterms 2025–26, finals 2024–25 + 2026/27 drafts (`.tex`/`.pdf`/`.html`, shared style files)
  - `overleaf/` — frozen Overleaf archive: lecture-note `.tex` (`1_dp`/`2_difffusion`/`3_watermark`/`4_MIA`), `hw_exam/` (all HW + exams), `images/`, `old/` drafts, `.bib`/style files
- **`courses/deepmath/`** — Deep Learning Math course (**junior undergrad AI majors**). Mathematical foundations: probability/information theory/estimation (9 decks, from `tex/probability25.tex` + 2 added topics) and linear algebra/optimization (4 decks, from `tex/optimization25.tex`). Full theorem–proof–implication arcs at slow pace; AI-application motivation per deck (CE loss, diffusion, Netflix completion, SGD). The rigorous-undergrad counterpart to the grad treatments in `infotheory/` and `privacy/`. Each deck carries an HTML speaker note plus a screen-reader Markdown edition of that note at `<deck>/<deck>-note.md` (plain ASCII, LaTeX math, verbal figure descriptions). See `courses/deepmath/OUTLINE.md`.
- **`courses/trustworthy-ai/`** — Trustworthy AI course (**junior/senior undergrad**, mixed majors, 15 weeks × 1.5 hr). Concept-first: each lecture is motivation → foundational works → 2025–26 frontier, ≤1 intuitive formula per concept, no proofs, plus an optional Colab demo. Decks live flat (`lecNN-*.html`). Five modules: Foundations (Wk 1) · Privacy & Data (2–5) · Reliability (6–7) · Security (8–11) · Provenance & Fairness (12–14) · Synthesis (15). **All 15 lectures + 4 backups + 15 technical supplements (`lecNNtech.html`) — screenshot-audited, real cited paper figures embedded, lint-clean** (no figure-TODO markers remain). Each lecture has a `-note.html` speaker script; each has an optional `lecNNtech.html` holding the formal math the main deck keeps as a picture. Backups: sycophancy, copyright, agentic autonomy, model stealing. The light undergrad pass over topics treated rigorously in `courses/privacy/`. See `courses/trustworthy-ai/OUTLINE.md`.

### `talks/` — standalone research presentations

- **`talks/icml2026/`** — ICML 2026 5-min SlidesLive recording for the position paper "The Term 'Machine Unlearning' Is Overused in LLMs" (Yoon, Jun, No). 10 slides. Poster ID 67198.
- **`talks/kics260521dllm/`** — Diffusion LLMs (KICS, 2026-05-21): general-audience invited talk on masked-discrete diffusion (Rainbow Padding, A2D, dgMARK, Reversal Curse, DAPD). 1 deck, no notes.
- **`talks/math260624dllm/`** — Diffusion LLMs (math conference, June 2026): mathematician-facing variant of the KICS talk — more Gaussian SDE theory, deeper SEDD/RADD, formal DAPD problem, lab work compressed; adds Mercury/DiffusionGemma "in practice" slide. 1 deck, no notes.
- **`talks/postech260821/`** — POSTECH Ok-lab seminar (2026-08-21, 50 min, graduate AI audience): "Small Interventions, Large Effects" — REFT first-token diversification, SafePath 8-token safety primer, few-shot Benign DPO attack (GPT fine-tuning-service framing + TenBenign prior art), 4-slide unlearning-position close (two slides adapted from the icml2026 deck); high-level connections to SEAG/LSC/FedVPA-GP; lab-author photos on section dividers; 3 lab-publication slides (papers in the talk + other records since 2025: unlearning/safety, discrete diffusion) before the closer. 45 slides (incl. 4 NeurIPS-2026 rebuttal slides for REFT and Benign DPO), figures captured from papers, no notes. Renamed from `talks/postech260819/` 2026-08-20.
- **`talks/researchintro2609/`** — "Finding a Research Project" seminar (Sep 2026, first-year graduate students with no research experience, currently taking LLM/agent/RL courses): four sections — what a project is (new / nontrivial / defensible, and the single-prompt test), where to start (topics from your own interests, then **reproduce first** and work the gap reproduction exposes; worked RAG-QA example), reading the field (ML timeline, recent-beats-retro and how to do a recent topic at small scale, how to survey), and justification (wall label, positioning sentence, smallest convincing experiment, one-page brief). "Project is a new artwork" is the framing, used on two slides only. 33 slides, 13 inline SVG exhibits, no captured figures, no notes.
- **`talks/sangnam2609/`** — Sangnam Institute of Management "AI Leader" week 3 (Sep 2026, 3–4 h, business executives at freshman technical level): introduction to machine learning, rewritten from Albert's Korean source deck in English. 4 decks: model-is-a-function · linear regression and overfitting (incl. scaling laws) · gradient descent and classification (logistic = linear + squash) · frontier advances and AI-safety incidents (~1 h). Optimization mathematics, cross-validation, regularization, and the SVM/kernel chain deliberately dropped.
- **`talks/seoul/`** — Seoul AI governance talk.

## Quick lookup — where does X live?

| Topic | Location |
|---|---|
| Entropy definition / Gibbs / log-sum | `courses/infotheory/lectures/01-entropy/entropy1-entropy-kl.html:131, :507, :582` |
| Chain rule / DPI / Fano | `courses/infotheory/lectures/01-entropy/entropy2-joint-mi-fano.html:111, :426, :518` |
| Mutual information (discrete) | `courses/infotheory/lectures/01-entropy/entropy2-joint-mi-fano.html:240` |
| Kraft / Kraft–McMillan / Shannon / Huffman | `courses/infotheory/lectures/02-lossless/lossless1-codes.html:213, :252, :293, :493` |
| AEP / source coding theorem / arithmetic coding | `courses/infotheory/lectures/02-lossless/lossless2-aep-arithmetic.html:98, :205, :413` |
| Markov entropy rate / LZ78 | `courses/infotheory/lectures/02-lossless/lossless3-markov-universal.html:156, :283` |
| Differential entropy + bin discretization | `courses/infotheory/lectures/03-diffentropy/diffentropy1-foundations.html:106, :117` |
| Gaussian MaxEnt / Hadamard / EPI | `courses/infotheory/lectures/03-diffentropy/diffentropy2-maxent-gaussian.html:143, :221, :332` |
| Shannon–Hartley / water-filling / I-MMSE | `courses/infotheory/lectures/03-diffentropy/diffentropy3-mi-awgn.html:161, :291, :389` |
| Score function / Tweedie's formula | `courses/privacy/lectures/02-generative/diffusion1-foundations.html:679, :695` (theorem + 3-slide proof); theorem at `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:121` |
| DDPM forward + VLB derivation | `courses/privacy/lectures/02-generative/diffusion2-ddpm.html:187-708`; `courses/infotheory/lectures/07-diffusion/diff2-diffusion.html:153-212` |
| SDE / Fokker–Planck / Anderson reverse | `courses/privacy/lectures/02-generative/diffusion3-sde-score.html` (FP `:379`, Anderson `:618`, score matching `:868`, VP kernel `:1021`) |
| DDIM (non-Markovian, deterministic, ODE) | `courses/privacy/lectures/02-generative/diffusion4-ddim.html` (loss invariance `:223`, σ-family `:463`, marginal invariance `:475`, predicted clean `:715`, exact Euler `:900`, PF-ODE `:975`) |
| Classifier guidance + inpainting + CFG | `courses/privacy/lectures/02-generative/diffusion5-guidance-discrete.html` (conditional score `:241`, tilted target `:445`, coordinatewise forward `:555`, exact paste `:633`, CFG identity `:811`) |
| Discrete diffusion / score-entropy loss | `courses/privacy/lectures/02-generative/diffusion5-guidance-discrete.html` (rate matrix `:1204`, reverse rate `:1217`, ratio score `:1308`, score entropy `:1373`, denoising score entropy `:1445`); `talks/kics260521dllm/kics260521dllm.html:192-205` (SEDD) |
| LLM overview (tokens, transformer, NLL, post-training, sampling) | `courses/privacy/lectures/02-generative/llm.html` (chain rule `:214`, attention `:329`, causal mask `:369`, generation cost `:499`) |
| Cross-entropy = entropy + KL; perplexity | `courses/privacy/lectures/02-generative/llm.html:547, :592, :604` |
| KL-regularized RLHF optimum → DPO (+ NPO preview) | `courses/privacy/lectures/02-generative/llm.html:810` (theorem), `:917` (DPO), `:939` (NPO) |
| Temperature / top-$k$ / nucleus sampling | `courses/privacy/lectures/02-generative/llm.html:975, :987, :1043` |
| LLM privacy-hook map (loss / verbatim / sampling / conditional) | `courses/privacy/lectures/02-generative/llm.html:1089` |
| Rate–distortion theorem (Shannon) | `courses/infotheory/lectures/04-lossy/lossy1-foundations.html:258-311` |
| Lloyd–Max / scalar quantization | `courses/infotheory/lectures/04-lossy/lossy1-foundations.html:143-199` |
| Gaussian R(D), Shannon lower bound, pruning | `courses/infotheory/lectures/04-lossy/lossy2-gaussian-laplacian.html:63-232` |
| Lattice / E8 / QUIP# | `courses/infotheory/lectures/04-lossy/lossy3-lattice-quip.html` |
| TURBOQUANT (online VQ for KV cache) | `courses/infotheory/lectures/04-lossy/lossy4-turboquant.html` |
| Variational MI lower bounds (BA, DV, NWJ, MINE) | `courses/infotheory/lectures/05-mi/mi1-bounds.html` |
| $f$-divergence unification of MI bounds | `courses/infotheory/lectures/05-mi/mi1-bounds.html:261-280` |
| InfoNCE / CLIP | `courses/infotheory/lectures/05-mi/mi2-infonce-clip.html` |
| $f$-divergence definition + properties (DPI, info inequality) | `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:121, :229` |
| GAN $\equiv$ Jensen–Shannon minimization (theorem + proof) | `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:330, :341-350` |
| Hockey-stick divergence (DP connection) | `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:166` |
| Fisher divergence + score function | `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:91, :141` |
| Denoising score matching theorem (Vincent 2011) | `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:193, :220-253` |
| Diffusion ELBO $\equiv$ DSM theorem | `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:198` (capstone); cites Vincent from `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:193` |
| MIA foundations (Homer power analysis, MI game, Neyman–Pearson, DP ROC cap, metrics) | `courses/privacy/lectures/04-mia/mia1-foundations.html` |
| Homer 2008 genome MIA, undergrad pass (no proofs; $D_j$ number line, one-SNP vs 500k, power table) | `courses/trustworthy-ai/lec03-mia.html:228` |
| Shadow models as Monte-Carlo estimation of $P_1,P_0$ (Shokri / per-class / LOGAN / seq2seq) | `courses/privacy/lectures/04-mia/mia2-shadow.html` |
| Shadow-model correctness + mis-specification (Prop 1, Thm 1, Cor 1 — with proofs) | `courses/privacy/lectures/04-mia/mia2-shadow.html:280, :321, :437` |
| Optimal GAN discriminator $D^\star = p_{\text{data}}/(p_{\text{data}}+p_g)$ + JSD identity (proofs) | `courses/privacy/lectures/04-mia/mia2-shadow.html:1152, :1186` — privacy framing (attack signal is a density ratio); information-theoretic framing at `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:330` |
| Uncalibrated perplexity threshold — degenerate LRT, pooling costs half the population | `courses/privacy/lectures/04-mia/mia2-shadow.html:1423, :1500` |
| MIA theory (Yeom / Sablayrolles / ML-Leaks / Nasr) | `courses/privacy/lectures/04-mia/mia3-theory.html` |
| LiRA, RMIA, label-only, attack hierarchy | `courses/privacy/lectures/04-mia/mia4-modern.html` |
| Closed form of the LiRA test (Thm 1) + per-example calibration dominates pooling (Prop 1) | `courses/privacy/lectures/04-mia/mia4-modern.html:385, :548` |
| Nested conditioning cannot hurt (Thm 2) — and why the ordering is only partial | `courses/privacy/lectures/04-mia/mia4-modern.html:951, :1021` |
| Post-processing cannot help an MIA defense (Prop 5 / Cor 3, proved from DPI) | `courses/privacy/lectures/04-mia/mia4-modern.html:1609, :1632` |
| Diffusion MIA — per-timestep reconstruction loss as the membership statistic | `courses/privacy/lectures/04-mia/mia4-modern.html:1747, :1811` |
| LLM MIA (perplexity, neighbourhood, SPV-MIA, context-aware, InfoRMIA) as five estimators of one null | `courses/privacy/lectures/04-mia/mia5-llm.html:545` |
| Blind baselines beat published LLM MIAs — a benchmark validity failure (Prop 7, proved) | `courses/privacy/lectures/04-mia/mia5-llm.html:1424, :1472` |
| Per-record instability: good AUC, coin-flip decisions (Prop 6, proved) | `courses/privacy/lectures/04-mia/mia5-llm.html:1306` |
| Extractable $\subsetneq$ inferable (Prop 8, proved, with counterexample to the converse) | `courses/privacy/lectures/04-mia/mia5-llm.html:1733, :1768` |
| Bartz v. Anthropic $1.5B settlement (Reuters cite) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:162` |
| Memorization defined three ways (extraction / SSCD / Webster taxonomy) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:269, :426, :518` |
| Diffusion memorization — Carlini/Somepalli/Webster/Wen/Ross | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:215-891` |
| Local intrinsic dimension (small-ball def + Levina–Bickel MLE) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:815, :855` |
| Smoothed thin support — $D-k$ eigenvalues at $-\sigma^{-2}$ (theorem + proof) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:941-1012` |
| SAIL — Lemmas 4.1–4.3 with proofs + eigenvalue figure + objective | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:892-1421` |
| CLIP padding-embedding memorization (Kim & No 2026) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:1423-1620` |
| Memorization — canary, exposure theory, $k$-extractable | `courses/privacy/lectures/03-memorization/memorization-llm.html:196-460`, `:735` |
| Counterfactual memorization + long-tail theorem (Feldman) | `courses/privacy/lectures/03-memorization/memorization-llm.html:511-660` |
| Repetition scaling formal law | `courses/privacy/lectures/03-memorization/memorization-llm.html:872` |
| Min-K%++ probe | `courses/privacy/lectures/03-memorization/memorization-llm.html:1162` |
| ACR (Schwarzschild 2024) + MiniPrompt + counting bound | `courses/privacy/lectures/03-memorization/memorization-llm.html:1268-1534` |
| Cooper book extraction (open-weight LLMs) | `courses/privacy/lectures/03-memorization/memorization-llm.html:1586-1666` |
| Certified $(\varepsilon,\delta)$-unlearning (Definition 3; Props 1–2; certified $\ne$ DP) | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:259-381` |
| Influence function (IU) — derived from the IFT, leads into the Newton block | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:463-571` |
| Theorems 1–3: Newton step (proved), Gaussian certification, Sekhari capacity | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:572-983` |
| MIA recall + Proposition 4 (certification caps every metric; HW4 woven in) | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:1522-1571` |
| SCRUB / SalUn / $\ell_1$-sparse / RURK classification unlearn | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:1241-1412` |
| IDI / COLA (lab unlearning eval, both with paper figures) | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:1641-1748` |
| Why certified unlearning fails for LLMs (P1–P4; Prop 1, Lemmas 2–3, Prop 4) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:107-460` |
| GA / NPO / SimNPO / entropy-max / ELM / RMU — one weighted-gradient family (Props 5/8/9/10, Thms 6/7) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:461-911` |
| TOFU / WMDP / RWKU / MUSE — main figure + what each actually measures (Thm 11, Cor 12, Props 13–14) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:912-1304` |
| Deletion vs suppression — closure under a fine-tuning budget (Def 15, Prop 16, Cor 17) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:1305-1613` |
| Benign + syntactic relearning (lab), DUSK, R-TOFU | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:1407-1520` |
| Position: "Unlearning" overused in LLMs (5-min ICML talk) | `talks/icml2026/icml2026.html` |
| How to find a research project topic (reproduce-then-find-the-gap) | `talks/researchintro2609/researchintro2609.html` |
| REFT (first-token diversification for RLVR) | `talks/postech260821/postech260821.html:167-464` (rebuttal: 403-449) |
| SafePath (8-token safety primer for LRMs) | `talks/postech260821/postech260821.html:466-589` |
| Benign DPO attack + fine-tuning-as-a-service | `talks/postech260821/postech260821.html:591-774` (rebuttal: 695-745) |
| Kirchenbauer green-list + z-test + entropy-bound proof | `courses/privacy/lectures/06-watermark/watermark.html:245-592` |
| Gumbel distribution + Gumbel-max trick + full proof | `courses/privacy/lectures/06-watermark/watermark.html:616-742` |
| Aaronson rule + distortion-free definition and proof | `courses/privacy/lectures/06-watermark/watermark.html:743-810` |
| Kuditipudi ITS + edit-distance robustness | `courses/privacy/lectures/06-watermark/watermark.html:824-957` |
| Christ–Gunn–Zamir undetectable + PRF construction | `courses/privacy/lectures/06-watermark/watermark.html:1014-1268` |
| Watermarking limits, impossibility, detection/distortion tradeoff | `courses/privacy/lectures/06-watermark/watermark.html:1270-1422` |
| Unigram-Watermark robustness + adaptive $\delta_t$ | `courses/privacy/lectures/06-watermark/watermark.html:1487-1620` |
| SynthID-Text production watermark | `courses/privacy/lectures/06-watermark/watermark.html:1705` |
| dgMARK diffusion-LM watermark (scheme + detection) | `courses/privacy/lectures/06-watermark/watermark.html:1745-1774` |
| **DP foundations series (dp1–dp7)** | `courses/privacy/lectures/01-dp/dp1`…`dp7-ml-paradigms.html` |
| DP definition / LDP vs central / PrivUnit | `courses/privacy/lectures/01-dp/dp8-fl.html:364-569` |
| RRSC + k-closest exact-optimality (NeurIPS 2023) | `courses/privacy/lectures/01-dp/dp8-fl.html:571-822` |
| DP-SGD / DP-Diffusion / DP-RDM | `courses/privacy/lectures/01-dp/dp8-fl.html:827-1004` |
| Continuous SDE diffusion at a glance (Song et al.) | `talks/kics260521dllm/kics260521dllm.html:99` |
| Masked diffusion at a glance | `talks/kics260521dllm/kics260521dllm.html:115` |
| Reverse process needs a ratio (concrete score) | `talks/kics260521dllm/kics260521dllm.html:179` |
| Rainbow Padding (EOS overflow, ICLR 2026) | `talks/kics260521dllm/kics260521dllm.html:319-461` |
| DAPD (attention dependency graph, ICML 2026) | `talks/kics260521dllm/kics260521dllm.html:463-669` |
| Diffusion-LLM safety (A2D) | `talks/kics260521dllm/kics260521dllm.html:694` |
| dgMARK (diffusion-LLM watermarking, ICML 2026) | `talks/kics260521dllm/kics260521dllm.html:707` |
| Reversal curse in MDMs | `talks/kics260521dllm/kics260521dllm.html:720` |
| Threat-model framing (knowledge × timing), trust dimensions | `courses/trustworthy-ai/lec01-introduction.html:333, :296` |
| $(\varepsilon,\delta)$-DP intuition (undergrad) / formal | `lec02-privacy-dp.html:536` · formal in `lec02tech.html` |
| Statistical indistinguishability (heights example, intuition) | `courses/trustworthy-ai/lec02-privacy-dp.html:681` |
| DP-SGD intuition (clip + noise) / formal algorithm | `lec02-privacy-dp.html:960` · formal in `lec02tech.html` |
| Formal math per lecture (definitions, derivations, algorithms) | `courses/trustworthy-ai/lecNNtech.html` (15 supplements) |
| AI governance & regulation (EU AI Act + Omnibus timeline, US EOs, Korea AI Basic Act, NIST RMF/GenAI Profile, frontier-lab safety frameworks, summits/AISIs) | `courses/trustworthy-ai/lec15-governance.html` (see leaf OUTLINE §03–04) |

## Cross-references

Same topic, different decks (use the more recent / more detailed):
- **VAE / ELBO**: rigorous derivation `courses/infotheory/lectures/07-diffusion/diff1-vae-elbo.html`
- **Hierarchical-VAE view of diffusion**: `courses/infotheory/lectures/07-diffusion/diff2-diffusion.html` (information-theoretic, Markov rewrite)
- **Diffusion from-scratch (Bayes route)**: `courses/privacy/lectures/02-generative/diffusion1-foundations.html` (Taylor + complete-square proof, less abstract)
- **Tweedie**: convolution-derivative proof `courses/privacy/lectures/02-generative/diffusion1-foundations.html:692-753`; alternate proof `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:135`
- **$f$-divergence variational dual**: brief in `courses/infotheory/lectures/05-mi/mi1-bounds.html:261` (KL instances); full development in `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:121-300`
- **Score matching $\equiv$ diffusion training**: Vincent DSM theorem + proof `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:193-253`; ELBO $\equiv$ DSM capstone `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:156-209`

## Companion notes pattern

`<deck>.html` is the deck. `<deck>-note.html` (where present) holds:
- Long-form proofs (theorem cited on slide → full derivation in notes)
- Intuition that doesn't fit on a slide
- Edge cases, comparison tables, references
- Look in the `-note.html` for "why does this hold" / "what's the precise statement" detail.

`courses/infotheory/` has notes for every deck. `courses/privacy/lectures/04-mia/` has notes for every deck. `courses/privacy/lectures/02-generative/` has notes for every diffusion lecture (1–5); `llm.html` has no note. `talks/kics260521dllm/`, `talks/math260624dllm/`, and `courses/privacy/lectures/01-dp/` do **not** have companion notes — proof detail is in-deck or in `note/2_difffusion.tex` (under `courses/privacy/lectures/02-generative/`).

## Authoring conventions

- Course lecture decks live at `courses/<course>/lectures/<NN-topic>/<deck>.html` — reference path `../../../../reference/`.
- Research talks live at `talks/<name>/<deck>.html` — reference path `../../reference/`.
- Build: `python3 scripts/bundle.py <path>/<deck>.html` → `<deck>.standalone.html` (gitignored).
- Lint: `python3 scripts/lint-deck.py --all`.
- Outline pointers: `python3 scripts/outline-lint.py` verifies every `file:line` cited in any `OUTLINE.md` still exists and is within the file's length. Run it after edits that shift line numbers.
