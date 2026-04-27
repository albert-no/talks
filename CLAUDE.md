# Talks repo

Slide decks for academic talks — conference presentations and master-level lectures. **Math-heavy**: rigorous theorem statement, rigorous proof, plus a high-level intuition pass (where color and controlled build-up earn their place). **Minimal visual design**: short abstract phrases, not full sentences (7×7 rule). Two authoring formats:

- **Custom HTML** (`<talk>/<talk>.html`) — preferred. Single-page deck, one `.active` slide visible at a time, scaled to viewport via JS. Links to `reference/` for CSS/JS/fonts/logo.
- **Marp markdown** — copy `template.md`, run `marp <file>.md --pdf`.

## Visual identity

White background. Yonsei Blue (`#003876`) accent. Yonsei TTFs (`reference/fonts/`) with Noto Sans fallback. Yonsei emblem (`reference/kor-eng2.png`) in the title-slide top-right.

## Repo layout

```
reference/                  canonical CSS/JS/fonts/logo (single source of truth)
  colors_and_type.css       @font-face + CSS tokens
  deck.css                  slide engine + components
  deck.js                   scale / nav / progress / brand-footer
  deck-skeleton.html        starter (cloned by new-talk.sh)
  fonts/                    Yonsei{Light,Bold,Body,Logo}.TTF
  kor-eng2.{png,pdf}        Yonsei emblem
scripts/
  new-talk.sh               scaffold <name>/<name>.html
  bundle.py                 produce <name>.standalone.html for distribution
  lint-deck.py              validate against canonical CSS
<talk>/<talk>.html          authoring source (committed)
<talk>/<talk>-note.html     companion notes for off-slide detail
OUTLINE.md                  per-folder content index — root, every topic folder,
                            and every leaf subfolder. See "Outlines" below.
```

Only the authoring source is committed. `<talk>.standalone.html` is a build artifact (gitignored).

## Design rules

The design rule, type scale, color tokens, components, and recipes live in **`DESIGN_SYSTEM.md`**. Read it before editing slides. The 4 ranked priorities (font sizes → line breaks → overflow → empty space) are non-negotiable.

Pitfalls and lessons learned live in **`GOTCHAS.md`**. Search there when something looks wrong before debugging from scratch.

## Creating a new talk

```bash
scripts/new-talk.sh <talk-name>
```

Creates `<talk-name>/<talk-name>.html` linking to `../reference/`. For Marp, copy `template.md` and run `marp <file>.md --pdf`.

## Editing workflow

1. Edit `<talk>/<talk>.html`.
2. Open the file in Chrome to preview (`reference/` must be alongside, which it is in this repo).
3. `python3 scripts/lint-deck.py --all` catches unknown classes and hardcoded colors.
4. **Update `OUTLINE.md`.** Whenever you add a slide, remove a slide, rename a section, change a section's line range, or add/remove a theorem the outline cites, update the leaf-subfolder `OUTLINE.md` (e.g. `privacy/mia/OUTLINE.md`). If the change introduces a new topic, file, or cross-reference, also update the parent folder's `OUTLINE.md` and the root `OUTLINE.md` quick-lookup table. Line numbers must stay accurate — outlines are read as authoritative pointers.
5. To distribute: `python3 scripts/bundle.py <talk>/<talk>.html` produces `<talk>.standalone.html` — single self-contained file (~4 MB, gitignored), no network deps.

## Outlines

Each folder has an `OUTLINE.md`. Three tiers:

- **Root** (`/OUTLINE.md`): folder map + topic→location quick-lookup table.
- **Folder** (`<topic>/OUTLINE.md`): subfolder map + cross-deck pointers.
- **Leaf** (`<topic>/<sub>/OUTLINE.md`): per-deck section table with line numbers, key theorems with line numbers, paired-note summary.

**Read outlines before writing slides** (full rule in `DESIGN_SYSTEM.md` → "OUTLINE.md → Read-side rule"). Two checks:

- **Series continuity.** When working on a deck, scan the leaf `OUTLINE.md` for earlier decks in the same series — and the parent folder's `OUTLINE.md` for adjacent topics — to see what has already been defined or proved. Refer back; don't redefine.
- **Cross-folder reuse.** When the topic you're writing on may live in another folder (diffusion in `infotheory/` vs `privacy/`; DP in `privacy/dp/` vs `privacy/mia/`; MI bounds in `infotheory/mi/` vs anywhere CLIP comes up), check the root `OUTLINE.md` quick-lookup table first, then the relevant leaf file. Reuse, link, or differentiate — explicit choice.

When a new deck is created (via `scripts/new-talk.sh` or by hand), add a stub for it in the leaf `OUTLINE.md` *immediately* — even before writing slides — so the deck is discoverable.

## Print-to-PDF

`reference/deck.css` includes an `@media print { @page { size: 1280px 720px; margin: 0 } … }` block.

1. Open the deck in Chrome (`<talk>.html` or `<talk>.standalone.html`).
2. `Cmd+P` → Save as PDF.
3. Margins **None**. Headers/footers **off**. Background graphics **on**.
