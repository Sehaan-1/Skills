# DESIGN.md Specification

## build the design system (DESIGN.md)

**The design system (DESIGN.md) are `DESIGN.md` at the repo root.** One file. It is the single source of truth for what this product looks like, readable by any agent, and precise enough to generate new screens from. If the repo already has one, it is law: follow it, and change it on purpose.

### Required shape

```markdown
# Design System: <Product>

## Register
<name> — and the one clause that chose it.

## Chosen board
<path to the tile a human picked> — "<their words>"

## Dials
Boldness <n> · Motion <n> · Density <n> (and the one line that produced them)

## 1. Atmosphere
Two or three sentences of plain description. What does it feel like to use?
"Calm, dense, and slightly old-fashioned, like a good paper ledger."

## 2. Color, named by role
- **Paper** (#F7F6F3) - primary background
- **Surface** (#FFFFFF) - raised fills
- **Ink** (#1B1A18) - primary text (off-black, never #000000)
- **Slate** (#6B6A66) - secondary text
- **Hairline** (rgba(27,26,24,0.10)) - structural 1px lines
- **Copper** (#A2542E) - THE accent: primary actions, active state, focus ring
- **Semantic** - Paid/Moss, Overdue/Clay, Draft/Slate. Status only, never decoration.
- **Banned**: pure black, pure white, neon, the AI purple family, any second accent.

## 3. Typography
- Display: <family> - weight-driven hierarchy, tight tracking, scale via clamp()
- Body: <family> - 65ch max, relaxed leading
- Mono: <family> - code, IDs, and all numbers when density > 7
- Banned: <the specific faces you are not allowed to reach for>

## 4. Components
Buttons, cards, inputs, navigation, tables, loaders, empty states, errors,
each with its shape, its states, and its radius in the number.

## 5. Layout
Grid, max width, section rhythm, mobile collapse rule, what may never overlap.

## 6. Motion
The one easing curve, the duration bands, what springs, what never animates,
the reduced-motion story.

## 7. Pre-flight bans
The short list from the Forbidden section that applies to THIS product.

## 8. Agent prompt guide
Three or four plain sentences an agent can paste to generate a new screen
that will match. Name the accent, the typeface, the density, and the mood.
```

### Rules for the design system (DESIGN.md)

- **Name colors by role, not appearance.** "Copper" means "the accent", not "a nice brown". Role names survive a palette change; appearance names do not.
- **Always hex, always the number.** "Deep charcoal (#1B1A18)". Radius, spacing, and type scale get numbers too.
- **One accent.** Semantic states are status, not a second accent, and they are desaturated to live inside the neutral system.
- **Write the bans down.** The explicit "never do this" list is what keeps the next screen from drifting back to the default. A design system without bans is a mood board.
- **Lock the register, and cite the board.** Both sit at the top of the file, above the colors, because they are the decisions everything else follows from. A reader should be able to tell which register this is and which tile was chosen without scrolling.
- **Plain language.** "Generously rounded corners (10px)", not `rounded-[10px]`. The design system (DESIGN.md) are read by humans first and agents second.
- **Short.** If the design system (DESIGN.md) are longer than the code they describe, they will not be read. Cut.
- **Rotate between projects.** Never ship the same palette, typeface, and layout family twice in a row. If your last project was beige and brass, this one is not.

---

