# infotheory/ — Information-theory lecture series

Master-level series with paired `<deck>.html` + `<deck>-note.html`. Notes hold full derivations and proof detail; decks hold the rigorous statements + intuition.

## Subfolders

- **`diffusion/`** — Diffusion through the information-theory lens (3 lectures): VAE/ELBO → hierarchical VAE → parameterizations + Tweedie. See `diffusion/OUTLINE.md`.
- **`lossy/`** — Rate–distortion theory + modern LLM compression (4 lectures): foundations → Gaussian/Laplacian + pruning + CROM → lattice codes & QUIP# → TURBOQUANT. See `lossy/OUTLINE.md`.
- **`mi/`** — Mutual-information estimation (2 lectures): variational lower bounds (BA, DV, NWJ, MINE) → InfoNCE & CLIP. See `mi/OUTLINE.md`.

## Themes

- **diffusion** is the *theoretical* side of diffusion (see `privacy/diffusion/` for the from-scratch Bayes-route version).
- **lossy** ramps from classical R(D) (Shannon, Lloyd–Max) to **applied compression of LLM weights and KV caches** (QUIP#, TURBOQUANT). The applied modules ride on the classical theorems established earlier in the series.
- **mi** culminates in the MI view of CLIP — the bridge between the variational-bound theory and contemporary contrastive learning.

## Cross-deck pointers

| Topic | Lecture | Line |
|---|---|---|
| ELBO definition | `diffusion/diff1-vae-elbo.html` | `:101` |
| Reparameterization trick (lemma) | `diffusion/diff1-vae-elbo.html` | `:198` |
| q(x_t\|x_0) closed form | `diffusion/diff2-diffusion.html` | `:76` |
| Tweedie's formula (theorem + proof) | `diffusion/diff3-parameterizations.html` | `:121` (statement), `:130` (proof) |
| Shannon's R(D) theorem | `lossy/lossy1-foundations.html` | `:270` |
| Gaussian R(D) achievability + converse | `lossy/lossy2-gaussian-laplacian.html` | `:71-160` |
| Layer-wise telescoping (pruning) | `lossy/lossy2-gaussian-laplacian.html` | `:215` |
| Lattice packing gain | `lossy/lossy3-lattice-quip.html` | `:119` |
| QUIP# Hadamard step | `lossy/lossy3-lattice-quip.html` | `:180` |
| TURBOQUANT_mse theorem | `lossy/lossy4-turboquant.html` | `:154` |
| QJL lemma | `lossy/lossy4-turboquant.html` | `:233` |
| Barber–Agakov bound | `mi/mi1-bounds.html` | `:107` |
| Donsker–Varadhan representation | `mi/mi1-bounds.html` | `:151` |
| InfoNCE bound | `mi/mi2-infonce-clip.html` | `:91` |

## Pairing convention

Every deck has a `-note.html` companion. The note generally contains:
- Full derivations of theorems stated in the deck.
- Pitfalls, edge cases, comparison tables.
- Forward/backward references to other lectures in the series.
- Connection to the *next* lecture (often at the bottom of the note).

When in doubt: deck = "what is true"; note = "why and how to apply".
