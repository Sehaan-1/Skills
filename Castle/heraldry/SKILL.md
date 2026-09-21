---
name: heraldry
description: "Use when designing, building, redesigning, or polishing user interfaces: pages, screens, components, design systems, or DESIGN.md. Use when something looks generic or AI-made; when establishing visual direction, typography, colors, or motion; or when running a design critique. Do not use to decide product questions (cuecards) or write non-UI backend slices (oneslice)."
---

# Heraldry

Establish a coherent visual identity, record it in `DESIGN.md`, and verify that every screen honors it.

A cohesive product follows one visual identity. Every view, component, and surface carries the same tokens, typography, and aesthetic restraint. Heraldry answers: **what does it look like, and is it actually good?**

Announce at start: `Using heraldry to [read | explore | design-system | build | critique | polish | verify | stop].`

## Hard gates

1. **Read the room before picking fonts.** Define who the product is for, the target mood, and the typographic family before writing code.
2. **Set dials explicitly.** State `BOLDNESS`, `MOTION`, and `DENSITY` (1–10) with clear rationale (see [reference/dials-and-layout.md](reference/dials-and-layout.md)).
3. **No design system, no second screen.** Build one view to learn; write and commit `DESIGN.md` before expanding across the app.
4. **DESIGN.md is law once written.** Treat `DESIGN.md` as an architectural contract. Update it deliberately in the same commit if changes are necessary.
5. **Enforce visual locks.** Maintain one accent color, one border-radius scale, one theme hierarchy, and one icon family.
6. **Eliminate AI tells.** The Forbidden anti-patterns list is mandatory (see [reference/preflight-checklist.md](reference/preflight-checklist.md)).
7. **Every animation must be motivated.** If an animation does not communicate state or hierarchy, remove it (see [reference/motion.md](reference/motion.md)).
8. **Real assets only.** Use real photography, rendered assets, or honest labeled placeholders. Never use empty gray boxes as fake screenshots.
9. **Copy is part of design.** Design headers, empty states, button labels, and error messages with intent.
10. **Accessibility is structural.** Contrast ratios, keyboard reach, visible focus rings, and 44px touch targets must be built in from the start.
11. **Do not decide product scope.** Heraldry identifies UX and visual defects; it does not invent new business features.
12. **Select one style archetype.** Choose one of the 9 archetypes (Keep, Scriptorium, etc.) per product (see [reference/style-archetypes.md](reference/style-archetypes.md)).
13. **Explore three directions before deciding.** When designing a new product or redesign, produce three distinct visual mockups (see [reference/critique-method.md](reference/critique-method.md)).
14. **Human picks the direction.** The user must select the visual direction. An agent cannot self-select the design direction.
15. **Quality requires reproducible proof.** Mark an interface done only when fresh multi-viewport renders, a critique table, and a mechanical pre-flight report exist (see [reference/critique-method.md](reference/critique-method.md)).

## Workflow

1. **Read the room:** State page kind, audience, vibe adjectives, and reference inspirations.
2. **Set dials:** Calibrate `BOLDNESS`, `MOTION`, and `DENSITY` (1–10).
3. **Explore three directions:** Generate 3 distinct mockups of the same key screen (the target style, a close alternative, and an intentional outlier).
4. **User selection:** Have the decider pick their preferred direction. Record in `docs/heraldry/<slug>-directions.md`.
5. **Commit DESIGN.md:** Write role-based color tokens, typography stacks, component rules, and layout constraints at repo root (see [reference/color-and-tokens.md](reference/color-and-tokens.md)).
6. **Implement & Critique:** Build the view, capture screenshots at 375px / 768px / 1440px in both themes, and record a Before/After critique table.
7. **Pre-flight & Verify:** Run mechanical checks (contrast, focus, touch targets, reduced motion) and commit the verification record.

## Direction Exploration Template

Record visual direction choices at `docs/heraldry/<slug>-directions.md`:

```markdown
# Visual Directions: <Product Screen>, <Date>

| Direction | Style Archetype | Preview File | Summary |
| --- | --- | --- | --- |
| A | Keep | docs/heraldry/previews/a.png | Dense, clean, data-focused |
| B | Scriptorium | docs/heraldry/previews/b.png | High-contrast editorial typography |
| C | Masquerade | docs/heraldry/previews/c.png | Stark black/white with bold display text |

## Chosen Direction
Direction <X>, in user's words: "<quote>"

## Key Learnings
- Rationale and tokens to carry forward into DESIGN.md
```

## Reference guides

- [reference/style-archetypes.md](reference/style-archetypes.md) — The 9 visual style presets (Keep, Scriptorium, Cathedral, etc.).
- [reference/dials-and-layout.md](reference/dials-and-layout.md) — Boldness, motion, density dials, and responsive rules.
- [reference/color-and-tokens.md](reference/color-and-tokens.md) — Role-based color tokens, contrast rules, and typography clamp formulas.
- [reference/preflight-checklist.md](reference/preflight-checklist.md) — Banned anti-patterns and mechanical accessibility checks.
- [reference/critique-method.md](reference/critique-method.md) — Viewport screenshot protocol, critique table format, and verification records.
- [reference/motion.md](reference/motion.md) — Animation easing curves, duration bands, and spring physics.
- [reference/arsenal.md](reference/arsenal.md) — Component pattern catalog.
