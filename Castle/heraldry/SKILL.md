---
name: heraldry
description: Aesthetic direction, design systems (DESIGN.md), visual verification walks, and design review for software interfaces.
disable-model-invocation: true
---

# Heraldry

Heraldry defines the aesthetic direction, establishes the design system (DESIGN.md), runs iterative critiques, and executes visual verification walks.

## Hard gates

1. **Read the room before you pick a font.** Say one line out loud, in plain words: who this is for, what it should feel like, which family it leans toward. No code until that line exists. If the brief genuinely diverges, ask **one** question, not a questionnaire.
2. **Dial first, default never.** Name `BOLDNESS`, `MOTION`, and `DENSITY` before you build, with a one-clause reason from the read. The table row is the fallback, not a decision.
3. **No arms, no second screen.** You may build one screen to learn something. You may not build the app on an unwritten direction. Write `DESIGN.md`, commit it, then cut.
4. **The design system is law once written.** Like an ADR: cite them, follow them, and when you must change one, change it deliberately in the same commit as the code and say so. Never quietly drift because a section "looked better" in a different palette.
5. **Locks are locks.** One accent, one radius system, one theme per page, one icon family, one copy register. Drift across sections is the most visible tell that a machine made this.
6. **Bans are bans.** The Forbidden list is not a preference. If the pre-flight finds one, the work is not done.
7. **Motion claimed is motion shown.** If you claim `MOTION` above 4, the interface moves. If you cannot ship working motion this sitting, drop the dial and ship a clean static page. Half-built motion is worse than none.
8. **Everything that animates is motivated.** One sentence per animation: what does it communicate? If the answer is "it felt alive", delete it.
9. **Real assets or an honest hole.** Real image, generated image, or a labeled placeholder plus a sentence telling the human what to supply. Never a `<div>` pretending to be a screenshot.
10. **Copy is designed, not filled.** Headlines, buttons, empty states, errors, and alt text are part of the design. Re-read every visible string before you call it done.
11. **Accessibility is structural, not a pass at the end.** Contrast, keyboard reach, visible focus, reduced motion, and 44px targets are built in, not retrofitted.
12. **On a redesign, the existing brand is an input, not a casualty.** Never silently change slugs, nav labels, form field names, logo, legal copy, or anything analytics depends on.
13. **One pass, one thing.** Fix the top handful of issues, re-render, look again. Never a two-hundred-file cosmetic sweep. A pass that cannot be described in a sentence is thrashing.
14. **Heraldry does not decide product.** A new product question is a cuecards card. Heraldry is allowed to say "this screen has no working empty state"; it is not allowed to decide what the empty state should sell.
15. **Name the register before the first pixel.** Nine registers, one choice, on the record. "I will know it when I see it" is not a direction; it is how a product ends up in five of them.

<!-- â”€â”€ PROVENANCE GATES (a claim is not a check) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ -->

16. **"It looks good" is a claim. It is not a check.** Before you tell a human an interface is done, five artifacts must exist, made in *this* sitting:

    - **The design system (DESIGN.md)** committed (`DESIGN.md`), and the code matching them. If the code and the design system (DESIGN.md) disagree, the design system (DESIGN.md) are wrong or the code is; say which and fix it.
    - **The board** at `docs/heraldry/<slug>-board.md`, carrying a human's pick, when this is a new product, a page whose look is the question, or a redesign. A one-component fix inside an product with an existing design system skips it, out loud.
    - **A critique** at `docs/heraldry/<slug>-critique.md`: the Before/After table from the last pass.
    - **A walk** at `docs/heraldry/<slug>-walk.md`: the record below, with **fresh renders** at 375 / 768 / 1440 in both themes, and a reduced-motion pass. (A one-component fix inside an product with an existing design system owes the spot pass instead â€” see *How much proof this pass owes* â€” said out loud.)
    - **The mechanical pre-flight output**, pasted. Real commands, real output. Not a summary.

    Renders must be new. A screenshot from three sessions ago is not evidence that this diff is good.

17. **An agent may not certify its own taste by assertion.** Writing "audited for accessibility" with no renders, no contrast values, and no keyboard pass is a fabricated check. If you cannot render the interface in this environment, write `unrendered` in the walk record, list exactly what you could not verify, and hand it to the human to look at. `unrendered` is honest and acceptable. A fake pass is not.

18. **Do not call a screen done when the walk would not catch it breaking.** The walk has to be able to fail: if a broken layout, a contrast failure, a missing focus ring, or an overflowing hero would still produce a green walk record, the walk is a slideshow, not a check. Strengthen it.

19. **You cannot pick the direction for them.** A board with no human pick is three files, not a decision. If nobody has pointed at a tile, the direction is not chosen: do not write the design system (DESIGN.md) from your own favorite and carry on. When the human is unavailable, explore the directions, state the recommendation, and stop there.

<!-- â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ -->


## Core Lifecycle

`
[Direction Discovery: board.md] -> [Design System: DESIGN.md] -> [Critique: critique.md] -> [Verification: walk.md]
`

1. **Direction Discovery (docs/heraldry/<slug>-board.md)**: Explore three candidate design directions at real aspect ratio. Await human selection.
2. **Design System Specification (DESIGN.md)**: Document the 8 required sections: Register, Atmosphere, Color Tokens (by role), Typography, Components, Layout, Motion, Pre-flight Bans, and Agent Prompt Guide. See [reference/design-md-spec.md](reference/design-md-spec.md).
3. **Iterative Critique (docs/heraldry/<slug>-critique.md)**: Render, critique top issues, fix, and record diff table. See [reference/critique-and-refinement.md](reference/critique-and-refinement.md).
4. **Visual Verification Walk (docs/heraldry/<slug>-walk.md)**: Run mechanical pre-flight checks, verify contrast and mobile responsiveness, and capture renders. See [reference/walk-protocol.md](reference/walk-protocol.md).

## Artifact Contracts

### Board (docs/heraldry/<slug>-board.md)
`markdown
# Board: <what is being designed>, <date>
Tiles cast: <register A>, <register B>, <register C (outlier)>. Ratio <n:n>.

| Tile | Register | File | One line |
| --- | --- | --- | --- |
| A | Keep | docs/heraldry/boards/<slug>-a.png | ... |
| B | Scriptorium | ... | ... |
| C | Masquerade | ... | ... |

## Chosen
Tile <X>, in the human's words: "<quote>"
Rejected: <one line each, and why>

## What the tiles taught us
<the two or three things the design system (DESIGN.md) should adopt from the comparison>
```

**Then write the design system (DESIGN.md) from the chosen tile**, and hand the builder three things: the tile, the design system (DESIGN.md), and the register name. The tile is a reference, not a spec. Where the tile and the design system (DESIGN.md) disagree, the design system (DESIGN.md) win â€” or you amend the design system (DESIGN.md) on purpose, in the same commit, and say so.

`

### Walk Record (docs/heraldry/<slug>-walk.md)
`markdown
# Walk: <what was walked>, <ISO date>
Rendered from commit <sha>, fresh this sitting.

## Render
- 375 / 768 / 1440, light and dark: <paths to the screenshots>
- Reduced motion on: <what changed, or "nothing moves, correct">
- Keyboard only: <tab order, visible focus, escape and enter behavior>
- Zoom 200%: <result>

## Pre-flight
<the mechanical command output, pasted>

## Render vs board
<the chosen tile and the built screen side by side at equal width: where they match, and where they diverge on purpose>

## Contrast spot checks
<foreground on background, measured ratio, threshold>

## What I could not verify
<unrendered, or the specific gap - honest, not empty>

## Still open
<the known-bad things, with the fixed ones crossed off>
```
`

## Reference Index

- [reference/registers.md](reference/registers.md) - The 9 design registers, tone matching, and rotation rules.
- [reference/dials.md](reference/dials.md) - Boldness, Motion, Density dials and mobile collapse rules.
- [reference/design-md-spec.md](reference/design-md-spec.md) - Complete 8-section DESIGN.md specification and downstream agent prompt guide.
- [reference/color-and-typography.md](reference/color-and-typography.md) - Color role taxonomy, contrast math, typographic hierarchy, and font pairing.
- [reference/components-and-layout.md](reference/components-and-layout.md) - Hero standards, rhythm, surfaces, states, copy guidelines, and asset sourcing.
- [reference/forbidden-tells.md](reference/forbidden-tells.md) - Comprehensive catalog of AI layout and styling tells.
- [reference/critique-and-refinement.md](reference/critique-and-refinement.md) - Loop discipline, anti-thrashing rules, and redesign preservation.
- [reference/preflight-commands.md](reference/preflight-commands.md) - Greppable shell commands and pre-flight validation checklist.
- [reference/walk-protocol.md](reference/walk-protocol.md) - Walk record protocol, honest provenance, failure standards, and scope boundaries.
- [reference/arsenal.md](reference/arsenal.md) - Named UI patterns catalog (bento grids, navigation layouts, heroes).
- [reference/motion.md](reference/motion.md) - Motion curves, duration tables, spring physics, and interaction timings.
