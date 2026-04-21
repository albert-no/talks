# /upgrade-deck

Interactively pull a deck back in line with the current design system: sync inline style/script blocks from canonical sources and propose structural updates (TOC slide, left-numbered section dividers, brand-footer opt-outs, end-slide) where appropriate.

## Inputs
- Target deck path (HTML file).

## Workflow

1. **Read canonical references first**: `reference/deck.css`, `reference/deck.js`, `DESIGN_SYSTEM.md`, `CLAUDE.md`.
2. **Check deck is self-contained**: confirm DECK STYLE/ENGINE markers are present. If missing, insert them around the existing inline style/script blocks and proceed.
3. **Dry-run sync**: `python3 scripts/sync-style.py --check <deck>` → report drift.
4. **Apply sync**: `python3 scripts/sync-style.py <deck>`. Confirm with user if the style block size changes significantly (possible design-system change since last sync).
5. **Structural audit** — list candidates for upgrade, each with a one-line rationale:
   - Is there a Contents slide? If not, propose one matching the deck's section structure.
   - Are `.section-slide` instances using the left-numbered variant? Propose conversions.
   - Does the deck end with a `.end-slide` Q&A closer? If not, propose adding one.
   - Are the title-slide + closer correctly tagged `.no-footer` where needed?
6. **Confirm each proposal with the user** — apply one at a time, show the diff, wait for approval.
7. **Re-lint**: `python3 scripts/lint-deck.py <deck>` → zero warnings is the goal.

## Reversibility

Each structural edit is one `Edit` call, so the user can ask to revert specific changes by referencing them. Git is the backstop.

## Output

After each phase, print a short status line:
```
[sync]     style + engine re-inlined (Δ +48 lines)
[propose]  add Contents slide → accepted
[propose]  convert section dividers (3 instances) → 2 accepted, 1 skipped
[lint]     0 warnings, 0 errors
```

## Do not

- Bulk-edit without user approval, even for small changes. The point of this command is interactivity.
- Alter slide content (prose, math, diagrams) without being asked. Only structural/style changes.
- Introduce new CSS classes — those belong in a `reference/deck.css` edit + re-sync.
