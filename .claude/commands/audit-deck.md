# /audit-deck

Audit a deck against the talks design system. Produces a report — does not edit.

## Inputs
- Target deck path (HTML file). Default to the single `.html` under the current deck folder if none given.

## Workflow

1. **Read canonical references**: `reference/deck.css`, `reference/deck.js`, `DESIGN_SYSTEM.md`, `CLAUDE.md`.
2. **Run `python3 scripts/lint-deck.py <deck>`** and capture the output verbatim.
3. **Inspect every slide** and rate it on:
   - Consistency with design system (classes used, accent patterns, divider placement).
   - Style priorities from `CLAUDE.md`: one idea per slide, `**strong**` / `*em*`, highlight usage, math-block usage.
   - Visual hierarchy: is `h2 → divider → body → optional highlight` respected?
   - Accessibility lightweight check: contrast on gray text, reasonable font sizes, no class overflow.
4. **Draft a report** with these sections:
   - **Summary** — pass/fail, total warnings, overall score out of 100.
   - **Token & class coverage** — anything hardcoded, unknown classes.
   - **Slide-by-slide findings** — only flag slides with issues; list the slide number, a one-line diagnosis, and a one-line fix.
   - **Priority actions** — top 3 fixes, ranked by impact.
5. **Offer** to fix the priority actions via `/upgrade-deck` or direct edits, but do not edit without explicit user approval.

## Output format

Use the audit output template from the design-system skill (§ Output — Audit). Keep it tight — no slide-by-slide entry for clean slides.

## Do not

- Make any edits. This command is read-only.
- Fabricate lint warnings the script didn't actually produce.
