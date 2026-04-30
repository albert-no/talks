# infotheory/entropy/ — Entropy and basic information-theoretic quantities

Two-lecture foundation series. Discrete-domain definitions, properties, and inequalities. Paired with `-note.html` companions.

## Files

| Deck | Note | Topic |
|---|---|---|
| `entropy1-entropy-kl.html` | `entropy1-entropy-kl-note.html` | Entropy, $H_b$, KL divergence |
| `entropy2-joint-mi-fano.html` | `entropy2-joint-mi-fano-note.html` | Joint, conditional, MI, DPI, Fano |

---

## entropy1-entropy-kl.html — Entropy and KL Divergence

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — Entropy** | Self-information, definition, examples | `:64-149` |
| | Three desiderata for information | `:72` |
| | Self-information $i_X(x) = -\log p_X(x)$ | `:84` |
| | **Definition of entropy** | `:97` |
| | Reading the definition | `:109` |
| | Example — Bernoulli($p$) | `:120` |
| | Example — Uniform($n$) | `:132` |
| | Example — Geometric($p$) | `:142` |
| | Example — three-symbol source | `:152` |
| | Continuity (dyadic vs nearby) | `:161` |
| | Why $\log$? — additivity for independence | `:174` |
| **02 — Properties** | Bounds, concavity, max at uniform | `:188-256` |
| | **Theorem — non-negativity & uniform max** | `:196` |
| | Proof — $H(X)\ge 0$ | `:206` |
| | Recall — Jensen's inequality | `:216` |
| | **Theorem — $H(X)\le\log\|\mathcal{X}\|$** | `:227` |
| | **Concavity of entropy** | `:239` |
| | Proof — concavity | `:248` |
| | Example — mixing two coins | `:260` |
| **03 — Binary entropy** | $H_b(p)$, computations, plot | `:273-333` |
| | Definition + plot | `:281` |
| | Concavity from $H_b''$ | `:301` |
| | Worked values | `:311` |
| | Recursive identity (binary $\to$ general) | `:323` |
| **04 — KL divergence** | Definition, Gibbs, log-sum, examples | `:335-485` |
| | Motivation | `:343` |
| | **Definition of KL** | `:355` |
| | Reading the definition | `:367` |
| | **Theorem — Gibbs $D(p\|q)\ge 0$** | `:379` |
| | Proof — Gibbs via Jensen | `:389` |
| | Corollary — max entropy from Gibbs | `:402` |
| | Example — two Bernoullis (asymmetry) | `:413` |
| | Example — mismatch cost in coding | `:425` |
| | **Theorem — log-sum inequality** | `:437` |
| | Proof — log-sum | `:447` |
| | Corollary — joint convexity of KL | `:459` |
| | Pinsker's inequality (statement) | `:469` |
| Recap / Next | | `:481, :493` |

**Key:** entropy definition `:97`; $H(X)\ge 0$ proof `:206`; $H(X)\le\log\|\mathcal{X}\|$ `:227`; concavity `:239`; KL definition `:355`; Gibbs theorem `:379`; log-sum `:437`.

### Note (`entropy1-entropy-kl-note.html`)
- Khinchin's axiomatic characterization
- Functional-equation justification of $-\log$
- Concavity via second derivative on the simplex
- Worked $H_b(1/4)$ derivation
- Recursive splitting identity proof
- KL asymmetry — operational interpretation
- Gibbs via $\ln t \le t-1$
- Pinsker proof sketch (Csiszár reduction)

---

## entropy2-joint-mi-fano.html — Joint, conditional, MI, Fano

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — Joint and conditional** | $H(X,Y)$, $H(X\mid Y)$, chain rule | `:64-188` |
| | Joint entropy definition | `:72` |
| | Example — two coin flips | `:84` |
| | **Conditional entropy — two definitions** | `:96` |
| | Reading the definition | `:108` |
| | **Theorem — chain rule** | `:118` |
| | Proof — chain rule | `:130` |
| | Example — two correlated coins | `:142` |
| | **Theorem — conditioning reduces entropy** | `:158` |
| | Proof | `:170` |
| | $H(X\mid Y=y) > H(X)$ — concrete case | `:182` |
| | Functional dependence lemma | `:195` |
| | Subadditivity | `:207` |
| **02 — Mutual information** | Definition, Venn, examples | `:219-328` |
| | **Definition of MI** | `:227` |
| | Reading the definition | `:239` |
| | Venn picture | `:250` |
| | Example — Bernoulli pair (BSC) | `:269` |
| | Example — erasure channel | `:282` |
| | Bounds on MI | `:295` |
| | **Theorem — chain rule for MI** | `:306` |
| **03 — Conditional MI & DPI** | Markov, data processing | `:322-415` |
| | Conditional MI definition | `:330` |
| | Conditioning can increase MI (XOR) | `:342` |
| | Markov chain definition | `:355` |
| | **Theorem — DPI** | `:368` |
| | Proof — DPI | `:379` |
| | Corollary — function of $Y$ | `:391` |
| | Example — cascade of BSCs | `:403` |
| **04 — Fano's inequality** | Error lower bound, applications | `:419-518` |
| | Setup — inferring $X$ from $Y$ | `:427` |
| | **Theorem — Fano** | `:438` |
| | Proof — Fano (Step 1) | `:451` |
| | Proof — Fano (Step 2) | `:463` |
| | Application — channel coding converse | `:475` |
| | Example — binary estimation | `:487` |
| | Example — $M$-ary hypothesis testing | `:497` |
| | Equality in Fano | `:507` |
| Recap / Next | | `:519, :533` |

**Key:** chain rule `:118`; conditioning reduces entropy `:158`; MI definition `:227`; DPI `:368`; Fano `:438`.

### Note (`entropy2-joint-mi-fano-note.html`)
- Joint table example — full numbers
- Why $H(X\mid Y=y)$ can exceed $H(X)$
- Subadditivity → total correlation
- Three faces of MI (operational, KL, variational)
- Erasure channel capacity sketch
- XOR collider-bias detail
- DPI equality = sufficient statistic
- Cascade-BSC crossover composition
- Fano two forms
- Channel-coding converse full sketch
- Minimax statistical estimation via Fano
