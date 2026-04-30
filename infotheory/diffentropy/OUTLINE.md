# infotheory/diffentropy/ — Differential entropy and continuous-domain MI (3 lectures)

Three-lecture series. Continuous-domain analogue of the discrete entropy series. Paired with `-note.html` companions.

## Files

| Deck | Note | Topic |
|---|---|---|
| `diffentropy1-foundations.html` | `diffentropy1-foundations-note.html` | Definition, examples, scaling, joint/conditional |
| `diffentropy2-maxent-gaussian.html` | `diffentropy2-maxent-gaussian-note.html` | MaxEnt principle, Gaussian, EPI |
| `diffentropy3-mi-awgn.html` | `diffentropy3-mi-awgn-note.html` | MI, AWGN capacity, water-filling, I-MMSE |

---

## diffentropy1-foundations.html — Foundations

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — Discrete to continuous** | Why a new definition | `:64-130` |
| | Why a new definition | `:72` |
| | **Definition — differential entropy** | `:84` |
| | Discretization bridge | `:96` |
| | Reading the bridge | `:111` |
| **02 — Examples** | Standard families | `:134-220` |
| | Uniform $[a,b]$ | `:142` |
| | Gaussian $\mathcal{N}(\mu,\sigma^2)$ | `:155` |
| | Exponential | `:170` |
| | Laplace | `:182` |
| | Cauchy | `:195` |
| | Multivariate Gaussian | `:206` |
| **03 — Properties** | Scaling, can be negative | `:224-294` |
| | Translation invariance | `:232` |
| | **Scaling — $h(aX) = h(X) + \log\|a\|$** | `:243` |
| | Linear transformation | `:255` |
| | $h$ can be negative | `:267` |
| | What is meaningful | `:277` |
| **04 — Joint and conditional** | Chain rule, KL, MI | `:298-405` |
| | Joint differential entropy | `:306` |
| | Conditional differential entropy | `:317` |
| | Chain rule | `:329` |
| | KL divergence (continuous) | `:340` |
| | Why KL is scale-invariant | `:352` |
| | Conditioning reduces $h$ | `:365` |
| | Mutual information | `:375` |
| | **Theorem — MI scaling invariance** | `:386` |
| | Example — independent Gaussians | `:399` |
| | Example — correlated Gaussians | `:411` |
| Recap / Next | | `:425, :437` |

**Key:** definition `:84`; bridge `:96`; scaling `:243`; KL invariance `:352`; MI invariance `:386`.

### Note (`diffentropy1-foundations-note.html`)
- Discretization bridge proof
- Why $h$ can be negative
- Cauchy entropy computation
- Multivariate Gaussian $h$ derivation
- Linear-transform Jacobian
- KL convexity, Pinsker, DPI
- Mixed discrete/continuous case

---

## diffentropy2-maxent-gaussian.html — MaxEnt and the Gaussian

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — MaxEnt principle** | Lagrangian, exponential family | `:64-153` |
| | The MaxEnt question | `:72` |
| | Lagrangian | `:85` |
| | The MaxEnt density (exp family) | `:97` |
| | Catalogue — three constraint types | `:110` |
| | Why MaxEnt is useful | `:130` |
| **02 — Gaussian = MaxEnt** | Variance constraint | `:157-275` |
| | **Theorem — Gaussian MaxEnt** | `:165` |
| | Proof — KL inequality (setup) | `:177` |
| | Proof — cross-term | `:188` |
| | Proof — combining | `:204` |
| | Proof variant — Lagrangian | `:218` |
| | Numerical examples | `:232` |
| | **Corollary — Hadamard's inequality** | `:248` |
| **03 — Multivariate Gaussian** | Hadamard, conditioning | `:279-340` |
| | **Theorem — multivariate MaxEnt** | `:287` |
| | Conditioning Gaussians | `:300` |
| | MI for Gaussians | `:312` |
| | Translation invariance revisited | `:324` |
| **04 — EPI** | Entropy power inequality | `:344-447` |
| | Definition — entropy power | `:352` |
| | **Theorem — EPI** | `:367` |
| | Equivalent form | `:380` |
| | Special case — both Gaussian | `:391` |
| | Why "Gaussians are hardest" | `:402` |
| | Application — AWGN converse sketch | `:412` |
| | Application — CLT-style | `:425` |
| Recap | | `:439` |

**Key:** Gaussian MaxEnt `:165`; KL-trick proof `:177-216`; Hadamard `:248`; EPI `:367`.

### Note (`diffentropy2-maxent-gaussian-note.html`)
- Variational calculus rigor
- Gaussian via generalized KL trick
- Hadamard direct proof
- Schur complement detail
- EPI proof sketch (Stam)
- Why EPI ⇒ Gaussian-hardest
- Vector Gaussian channel capacity

---

## diffentropy3-mi-awgn.html — MI and the AWGN Channel

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — Continuous MI** | Definition, properties, examples | `:64-152` |
| | Definition (recap) | `:72` |
| | Discretization bridge for MI | `:84` |
| | Properties — all inherited | `:97` |
| | Example — bivariate Gaussian | `:111` |
| | Example — additive Gaussian noise | `:124` |
| **02 — AWGN channel** | $C = \tfrac{1}{2}\log(1+\mathrm{SNR})$ | `:156-258` |
| | Setup | `:164` |
| | **Theorem — Shannon–Hartley** | `:177` |
| | Proof — achievability | `:189` |
| | Proof — converse | `:202` |
| | Numerical examples | `:215` |
| | Bandwidth-limited form | `:230` |
| **03 — Parallel channels** | Water-filling | `:262-360` |
| | Setup | `:270` |
| | Optimization problem | `:282` |
| | **Theorem — water-filling** | `:293` |
| | Water-filling — picture | `:308` |
| | Example — three sub-channels | `:333` |
| | Application — frequency-selective | `:346` |
| **04 — Connections** | I-MMSE, de Bruijn, diffusion | `:364-470` |
| | MMSE | `:372` |
| | **Theorem — I-MMSE** | `:385` |
| | Sanity check — Gaussian input | `:399` |
| | **Theorem — de Bruijn** | `:412` |
| | Application — diffusion models | `:424` |
| Recap series + Connections | | `:437, :451` |

**Key:** Shannon–Hartley `:177`; water-filling `:293`; I-MMSE `:385`; de Bruijn `:412`.

### Note (`diffentropy3-mi-awgn-note.html`)
- AWGN full coding theorem outline
- Bandwidth-limited continuous-time form
- Water-filling KKT derivation
- I-MMSE proof sketch (Guo–Shamai–Verdú)
- de Bruijn via heat equation
- Diffusion-models information-theoretic loss
