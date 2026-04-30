# infotheory/lossless/ — Lossless compression (3 lectures)

Three-lecture series. Variable-length codes, AEP and Shannon source coding, Markov sources and universal compression. Paired with `-note.html` companions.

## Files

| Deck | Note | Topic |
|---|---|---|
| `lossless1-codes.html` | `lossless1-codes-note.html` | Variable-length codes, Kraft, Shannon, Huffman |
| `lossless2-aep-arithmetic.html` | `lossless2-aep-arithmetic-note.html` | AEP, source coding theorem, arithmetic coding |
| `lossless3-markov-universal.html` | `lossless3-markov-universal-note.html` | Markov, entropy rate, LZ78, universal coding |

---

## lossless1-codes.html — Codes, Kraft, Huffman

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — Codes & rate** | UD, prefix-free, trees | `:64-145` |
| | Setup | `:72` |
| | Expected rate | `:84` |
| | Example — UD code | `:97` |
| | Example — non-UD code | `:108` |
| | Prefix-free codes as trees | `:118` |
| **02 — Kraft inequality** | Existence statement | `:149-244` |
| | **Theorem — Kraft** | `:157` |
| | Proof — necessity | `:171` |
| | Proof — sufficiency | `:184` |
| | **Theorem — Kraft–McMillan** | `:198` |
| | Proof — Kraft–McMillan | `:213` |
| | Corollary — $L \ge H(X)$ | `:230` |
| **03 — Shannon code** | $\lceil\log 1/p\rceil$, mismatch | `:248-330` |
| | Shannon code definition | `:256` |
| | **Theorem — entropy bound $H \le L < H+1$** | `:268` |
| | Example — dyadic | `:281` |
| | Example — non-dyadic | `:298` |
| | Mismatch — coding for wrong distribution | `:309` |
| | Example — mismatch cost | `:322` |
| **04 — Huffman code** | Optimal prefix-free | `:334-450` |
| | Huffman algorithm | `:342` |
| | Worked example — step by step | `:354` |
| | Worked example — codewords | `:367` |
| | Optimality — two lemmas | `:382` |
| | Proof — Lemma 1 | `:395` |
| | Proof — Lemma 2 | `:404` |
| | **Theorem — Huffman is optimal** | `:413` |
| | Huffman vs entropy — 1-bit gap | `:425` |
| | Block coding — preview | `:434` |
| Recap | | `:451` |

**Key:** Kraft `:157`; Kraft–McMillan `:198`; entropy bound proof `:268`; Huffman optimality `:413`.

### Note (`lossless1-codes-note.html`)
- UD vs prefix-free with example
- Greedy Kraft sufficiency walk
- Why $T^k$ in Kraft–McMillan
- Entropy-bound clean derivation
- Shannon worst case
- Operational reading of mismatch
- Huffman optimality proof detail
- Block coding cost tradeoff

---

## lossless2-aep-arithmetic.html — AEP, Source coding, Arithmetic

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — AEP** | Typical sets, three properties | `:64-180` |
| | Motivation | `:72` |
| | **Theorem — AEP** | `:84` |
| | **Definition — typical set** | `:96` |
| | Three properties of $A_\varepsilon^{(n)}$ | `:108` |
| | Proof — property 1 (high probability) | `:122` |
| | Proof — property 2 (upper bound) | `:132` |
| | Proof — property 3 (lower bound) | `:142` |
| | Picture — volume counting | `:152` |
| | Example — Bernoulli source | `:166` |
| **02 — Source coding theorem** | Achievability + converse | `:184-280` |
| | Block code — setup | `:192` |
| | **Theorem — Shannon source coding** | `:204` |
| | Achievability — idea | `:218` |
| | Achievability — error → 0 | `:230` |
| | Converse — $R<H$ fails | `:241` |
| | Converse — continued | `:252` |
| | Zero-error case | `:267` |
| **03 — Arithmetic coding** | Map sequence to interval | `:284-368` |
| | Why arithmetic coding | `:292` |
| | Construction — recursive subdivision | `:303` |
| | Example — encoding "AB" | `:316` |
| | From interval to bits | `:328` |
| | Example — decoding | `:339` |
| **04 — Optimality** | $L \le H + 2$ per block | `:372-452` |
| | **Lemma — truncation length** | `:380` |
| | Proof — truncation length | `:392` |
| | **Theorem — arithmetic coding bound** | `:405` |
| | Comparison — three codes | `:419` |
| Recap / Next | | `:435, :447` |

**Key:** AEP `:84`; typical set `:96`; source coding theorem `:204`; arithmetic coding bound `:405`.

### Note (`lossless2-aep-arithmetic-note.html`)
- Strong AEP (Birkhoff/SMB)
- Method of types
- Why "equipartition"
- Bernoulli numerical bounds
- Source coding theorem — both directions detail
- Arithmetic coding length proof
- Practical implementation issues
- Connection to LLM-based compression

---

## lossless3-markov-universal.html — Markov, Universal Coding

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:23, :34` |
| **01 — Sources with memory** | Markov chains, stationarity | `:64-150` |
| | i.i.d. is not enough | `:72` |
| | **First-order Markov definition** | `:82` |
| | Example — two-state chain | `:95` |
| | Joint entropy of Markov chain | `:108` |
| | $k$-th order Markov | `:120` |
| **02 — Entropy rate** | Fundamental limit | `:154-235` |
| | **Definition — entropy rate** | `:162` |
| | **Theorem — limits exist and agree** | `:175` |
| | Stationary Markov — closed form | `:188` |
| | Example — two-state chain | `:200` |
| | Coding a Markov source | `:213` |
| **03 — Universal coding** | Two-pass schemes, redundancy | `:239-303` |
| | The universal problem | `:247` |
| | Two-pass scheme | `:259` |
| | Redundancy = mismatch cost | `:272` |
| | Lower bound on redundancy | `:283` |
| **04 — Lempel–Ziv** | LZ78, optimality | `:307-405` |
| | The LZ idea | `:315` |
| | LZ78 algorithm | `:329` |
| | Worked example | `:340` |
| | **Theorem — asymptotic optimality** | `:355` |
| | Proof idea — LZ78 | `:368` |
| | Practical note — what real codecs do | `:380` |
| Recap series + Next | | `:395, :409` |

**Key:** Markov definition `:82`; entropy rate `:162`; Markov entropy rate closed form `:188`; LZ78 algorithm `:329`; LZ78 optimality `:355`.

### Note (`lossless3-markov-universal-note.html`)
- Stationarity vs ergodicity
- Both-limits-agree detail
- Two-state chain $\pi$ verification
- KT mixture universal code
- Context tree weighting
- LZ78 proof sketch
- LZ77 vs LZ78 in practice
- Modern LLM-based compression
