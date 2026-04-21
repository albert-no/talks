# /new-slide

Add one or more slides to an existing deck, strictly following the talks design system.

## Inputs
- Target deck path (HTML file).
- Topic, structure, and any specific components desired (cards, math, table, diagram, etc.).

## Workflow (follow every time)

1. **Read the canonical style definitions first** — do not skip:
   - `reference/deck.css` — defines every class and token available.
   - `reference/deck.js` — understand the engine (brand-footer auto-inject, nav).
   - `DESIGN_SYSTEM.md` — tokens, components, recipes, and do/don'ts.
2. **Read `CLAUDE.md`** for repo conventions (Style priorities).
3. **Open the target deck** and find the insertion point. Respect existing slide numbering comments; renumber if needed so the sequence stays consistent.
4. **Draft the new slide(s)** using only classes defined in `reference/deck.css`. If a desired pattern is not in the system, do **not** invent ad-hoc classes — either compose existing ones with inline `style=` (no hardcoded colors, use `var(--…)`) or stop and propose a design-system extension.
5. **Insert**, then verify:
   - No new classes outside the canonical set.
   - One `.highlight` per slide max.
   - Math goes in `.math-block` (display) or inline `$…$`.
   - Follow Style priorities: one idea per slide, `**blue**` / `*muted*`, `>` / `.highlight` for insights.
6. **Run `python3 scripts/lint-deck.py <deck>`** and fix any warnings.
7. **Confirm** the `@media print` block and DECK STYLE/ENGINE markers are intact.

## Output

Summarize which slides were added, the recipes used, and the lint result. Do not re-paste the full file; show only the new slide markup (diff-style) so the user can eyeball it before refreshing Chrome.

## Do not

- Edit `reference/deck.css` or `reference/deck.js` from this command — those changes belong in `/upgrade-deck` or direct canonical edits followed by `scripts/sync-style.py`.
- Hardcode colors or typography values inline. Use CSS variables.
- Add `<link>`s to external stylesheets — decks stay self-contained.
