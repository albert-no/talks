# dllm/ — Diffusion LLMs (single talk)

Invited talk: **Why Diffusion LLMs Behave Differently, and How to Control Them.** Surveys five control surfaces for masked-discrete-diffusion language models. No companion notes — all proof/intuition is in-deck.

## Files

- `dllm.html` — the deck

## dllm.html

**Topic:** Inductive biases, failure modes, and control surfaces of masked discrete diffusion LLMs.

### Sections (line numbers)

- **Title / contents / framing** (`:21-180`)
  - `:21` Title slide
  - `:34` Contents (5-part outline)
  - `:84` From toy to competitive (SEDD 2023 → LLaDA 2.0 2025)
  - `:109` Masked diffusion at a glance (forward/reverse on tokens)
  - `:138` AR vs diffusion LLMs comparison table
  - `:159` Two key inductive biases (bidirectional + any-order)

- **Part I — Recent progress in field** (`:182-291`)
  - `:192` SEDD: score-entropy loss (formula `:196`)
  - `:208` RADD: absorbing diffusion = any-order AR (bridge result `:213`)
  - `:226` LLaDA: 8B-scale dLLM
  - `:244` Dream 7B + LLaDA 2.0
  - `:269` Field milestones table

- **Part II–V — Five control surfaces** (`:292-718`)

  | Surface | Lines | Result | Citation |
  |---|---|---|---|
  | **Rainbow Padding** (robustness) | `:323-427` | Cyclic distinct pad tokens fix EOS overflow | Kim et al., ICLR 2026 (`:423`) |
  | **A2D** (safety) | `:429-522` | Token-level [EOS] refusal at any masked position; DIJA neutralized | Jeung et al., ICLR 2026 (`:518`) |
  | **dgMARK** (attribution) | `:524-569` | Watermark via unmasking-order channel; never reweights probs | Hong & No, arXiv 2025 (`:565`) |
  | **Reversal Curse** (understanding) | `:571-649` | Bidirectional attn + weight sharing → gradient alignment mitigates | Shin et al., arXiv 2025 (`:645`) |
  | **DAPD** (decoding) | `:651-714` | Dependency-aware parallel unmasking; training-free | Kim et al., arXiv 2025 (`:680`) |

- **Synthesis** (`:719-829`)
  - `:719` Five surfaces, one thread
  - `:742` Practical guidance
  - `:776` Open problems
  - `:814` Key takeaways

### Key formulas / claims

| Item | Line |
|---|---|
| SEDD score-entropy loss `L_SE = E[Σ s_θ(y\|x_t,t) − log s_θ(x_0\|x_t,t)]` | `:196` |
| RADD bridge: optimal absorbing-diffusion denoiser ≡ any-order AR | `:213` |
| EOS positional-bias formula | `:357` |
| A2D alignment `p_θ([EOS] \| x_t, pos_i) ↑` if harmful | `:452` |
| Attention-weight-sharing equation `α_{A→B}` | `:604` |
| Forward/reverse gradient alignment `∇L_fwd · ∇L_rev > 0` | `:609` |

### Companion content

None. All material on slide. For deeper diffusion theory, see `infotheory/diffusion/` (VAE/ELBO derivations, parameterizations) and `privacy/diffusion/` (Bayes-route, SDE, score-matching theorem, discrete diffusion).
