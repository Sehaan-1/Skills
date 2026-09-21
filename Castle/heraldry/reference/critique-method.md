# Critique Method & Verification Walk

Visual quality is verified through reproducible inspection artifacts, not subjective claims.

## The Inspection Loop

1. **Render at three viewports:** Capture fresh screenshots at `375px` (mobile), `768px` (tablet), and `1440px` (desktop) in both light and dark themes.
2. **Tab navigation test:** Tab through interactive elements with keyboard only, checking focus indicators.
3. **Generate critique table:** Detail issues identified against `DESIGN.md` tokens.
4. **Fix the high-leverage issues:** Refactor layout, type, and spacing.
5. **Re-render and verify:** Capture updated screenshots to prove the issues are resolved.

---

## Critique Table Format

Record findings in `docs/heraldry/<slug>-critique.md`:

| View / Component | Issue Identified | Violates Rule | Action Taken | Verified Status |
| --- | --- | --- | --- | --- |
| Header Nav | Low contrast on secondary links (2.8:1) | WCAG AA 4.5:1 | Darkened text token to `#52525B` | Resolved (4.8:1) |
| Feature Grid | Overflows viewport horizontally on mobile | Single column rule | Stacked items to single column below 768px | Resolved |
| Primary CTA | Missing visible focus ring | Accessibility gate | Added `focus-visible:ring-2` outline | Resolved |

---

## Verification Record Template

Commit to `docs/heraldry/<slug>-verification.md`:

```markdown
# Verification Record: <Feature or Screen>

- **Target screen:** <URL or local component route>
- **Design system:** [DESIGN.md](../../DESIGN.md)
- **Date:** YYYY-MM-DD
- **Evaluated commit:** <SHA>

## Renders Captured
- Mobile (375px): `docs/heraldry/renders/<slug>-375.png`
- Tablet (768px): `docs/heraldry/renders/<slug>-768.png`
- Desktop (1440px): `docs/heraldry/renders/<slug>-1440.png`

## Pre-Flight Output
- Contrast check: Passed (all text $\ge 4.5:1$)
- Keyboard tab order: Verified
- Reduced motion check: Verified

## Status
Verified — matches DESIGN.md specifications.
```
