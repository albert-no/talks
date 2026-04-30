# Talks repo — content outline

Slide decks for Yonsei talks (academic conferences + master-level lectures). Repo conventions in `CLAUDE.md`, design rules in `DESIGN_SYSTEM.md`, pitfalls in `GOTCHAS.md`.

Each topic folder has its own `OUTLINE.md`. Leaf subfolders have detailed per-deck outlines with slide and theorem line numbers. **For specific content, descend into the relevant folder's OUTLINE.md.**

## Folders

- **`dllm/`** — Diffusion LLMs: invited talk on masked-discrete diffusion (Rainbow Padding, A2D, dgMARK, Reversal Curse, DAPD). 1 deck, no notes.
- **`infotheory/`** — Information-theory lecture series (paired decks + `-note.html` companions):
  - `entropy/` — Foundations: entropy, KL, joint/conditional MI, DPI, Fano (2 lectures)
  - `lossless/` — Codes/Kraft/Huffman, AEP/arithmetic, Markov/LZ (3 lectures)
  - `diffentropy/` — Differential entropy, MaxEnt/Gaussian/EPI, AWGN/water-filling/I-MMSE (3 lectures)
  - `diffusion/` — Diffusion as hierarchical VAE (3 lectures)
  - `lossy/` — Rate–distortion + LLM compression (4 lectures)
  - `mi/` — Variational MI bounds, InfoNCE/CLIP (2 lectures)
- **`privacy/`** — Privacy series:
  - `diffusion/` — Diffusion generative models from scratch (5 lectures, no companion notes; `note/2_difffusion.tex` is LaTeX source for Lectures 1–2)
  - `dp/` — Differential privacy + federated learning (1 NeurIPS 2023 talk: RRSC result)
  - `mia/` — Membership inference attacks (5 lectures, paired notes; legacy `old/MIA.html`)

## Quick lookup — where does X live?

| Topic | Location |
|---|---|
| Entropy definition / Gibbs / log-sum | `infotheory/entropy/entropy1-entropy-kl.html:97, :379, :437` |
| Chain rule / DPI / Fano | `infotheory/entropy/entropy2-joint-mi-fano.html:118, :368, :438` |
| Mutual information (discrete) | `infotheory/entropy/entropy2-joint-mi-fano.html:227` |
| Kraft / Kraft–McMillan / Shannon / Huffman | `infotheory/lossless/lossless1-codes.html:157, :198, :268, :413` |
| AEP / source coding theorem / arithmetic coding | `infotheory/lossless/lossless2-aep-arithmetic.html:84, :204, :405` |
| Markov entropy rate / LZ78 | `infotheory/lossless/lossless3-markov-universal.html:188, :355` |
| Differential entropy + bin discretization | `infotheory/diffentropy/diffentropy1-foundations.html:84, :96` |
| Gaussian MaxEnt / Hadamard / EPI | `infotheory/diffentropy/diffentropy2-maxent-gaussian.html:165, :248, :367` |
| Shannon–Hartley / water-filling / I-MMSE | `infotheory/diffentropy/diffentropy3-mi-awgn.html:177, :293, :385` |
| Score function / Tweedie's formula | `privacy/diffusion/diffusion1-foundations.html:362-425`; theorem at `infotheory/diffusion/diff3-parameterizations.html:121` |
| DDPM forward + VLB derivation | `privacy/diffusion/diffusion2-ddpm.html:189-333`; `infotheory/diffusion/diff2-diffusion.html:153-212` |
| SDE / Fokker–Planck / Anderson reverse | `privacy/diffusion/diffusion3-sde-score.html` (FP `:148`, Anderson `:234`, score matching `:339`) |
| DDIM (non-Markovian, deterministic, ODE) | `privacy/diffusion/diffusion4-ddim.html` (marginal invariance `:164`, predicted clean `:234`) |
| Classifier guidance + CFG | `privacy/diffusion/diffusion5-guidance-discrete.html:202-282` |
| Discrete diffusion / score-entropy loss | `privacy/diffusion/diffusion5-guidance-discrete.html:287-425`; `dllm/dllm.html:192-205` (SEDD) |
| Rate–distortion theorem (Shannon) | `infotheory/lossy/lossy1-foundations.html:258-311` |
| Lloyd–Max / scalar quantization | `infotheory/lossy/lossy1-foundations.html:143-199` |
| Gaussian R(D), Shannon lower bound, pruning | `infotheory/lossy/lossy2-gaussian-laplacian.html:63-232` |
| Lattice / E8 / QUIP# | `infotheory/lossy/lossy3-lattice-quip.html` |
| TURBOQUANT (online VQ for KV cache) | `infotheory/lossy/lossy4-turboquant.html` |
| Variational MI lower bounds (BA, DV, NWJ, MINE) | `infotheory/mi/mi1-bounds.html` |
| InfoNCE / CLIP | `infotheory/mi/mi2-infonce-clip.html` |
| MIA foundations (Homer, evaluation metrics) | `privacy/mia/mia1-foundations.html` |
| Shadow models (Shokri / LOGAN / seq2seq) | `privacy/mia/mia2-shadow.html` |
| MIA theory (Yeom / Sablayrolles / ML-Leaks / Nasr) | `privacy/mia/mia3-theory.html` |
| LiRA, RMIA, label-only, attack hierarchy | `privacy/mia/mia4-modern.html` |
| LLM MIA (perplexity, neighbourhood, SPV, InfoRMIA) | `privacy/mia/mia5-llm.html` |
| DP definition / LDP vs central / PrivUnit | `privacy/dp/DP-FL.html:364-569` |
| RRSC + k-closest exact-optimality (NeurIPS 2023) | `privacy/dp/DP-FL.html:571-822` |
| DP-SGD / DP-Diffusion / DP-RDM | `privacy/dp/DP-FL.html:827-1004` |
| Diffusion-LLM safety (A2D) | `dllm/dllm.html:429-522` |
| Rainbow Padding (EOS overflow) | `dllm/dllm.html:323-427` |
| dgMARK (diffusion-LLM watermarking) | `dllm/dllm.html:524-569` |

## Cross-references

Same topic, different decks (use the more recent / more detailed):
- **VAE / ELBO**: rigorous derivation `infotheory/diffusion/diff1-vae-elbo.html`
- **Hierarchical-VAE view of diffusion**: `infotheory/diffusion/diff2-diffusion.html` (information-theoretic, Markov rewrite)
- **Diffusion from-scratch (Bayes route)**: `privacy/diffusion/diffusion1-foundations.html` (Taylor + complete-square proof, less abstract)
- **Tweedie**: brief `privacy/diffusion/diffusion1-foundations.html:374`; with proof `infotheory/diffusion/diff3-parameterizations.html:130`

## Companion notes pattern

`<deck>.html` is the deck. `<deck>-note.html` (where present) holds:
- Long-form proofs (theorem cited on slide → full derivation in notes)
- Intuition that doesn't fit on a slide
- Edge cases, comparison tables, references
- Look in the `-note.html` for "why does this hold" / "what's the precise statement" detail.

`infotheory/` has notes for every deck. `privacy/mia/` has notes for every deck. `privacy/diffusion/` and `dllm/` and `privacy/dp/` do **not** have companion notes — proof detail is in-deck or in `note/2_difffusion.tex` (privacy/diffusion only).

## Authoring conventions

- Decks live at `<topic>/<deck>.html`.
- Reference assets in `reference/`: paths from depth-1 decks (`infotheory/foo.html`) use `../reference/`; depth-2 decks (`privacy/mia/foo.html`) use `../../reference/`.
- Build: `python3 scripts/bundle.py <path>/<deck>.html` → `<deck>.standalone.html` (gitignored).
- Lint: `python3 scripts/lint-deck.py --all`.
