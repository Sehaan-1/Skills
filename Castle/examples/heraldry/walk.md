# Walk: Invoices screen, 2026-09-18

Rendered from commit `9f4c1ab` after the fixes in [critique.md](critique.md). Renders made this sitting.

## Render

- **375 / 768 / 1440, light and dark:** `docs/heraldry/shots/invoices-375-light.png`, `-768-light`, `-1440-light`, and the same three in dark.
- **Reduced motion on:** the detail panel appears instantly, hover colors unchanged, nothing else moves. Correct at Motion 3.
- **Keyboard only:** tab order is skip link, nav, "New invoice", table rows, detail panel controls. Focus ring visible on all of them (Copper, 2px, 2px offset). Escape closes the panel and returns focus to the row that opened it. Enter on a row opens it.
- **Zoom 200%:** no clipping; the table drops to name, amount, status exactly as declared, and no horizontal scrollbar appears.

## Pre-flight

```
$ grep -rn "—\|–" src/ ; echo "grep exited $?"
grep exited 1               # 1 means nothing matched: zero em dashes in the interface

$ grep -rn "transition: all" src/
(no output)

$ grep -rn 'addEventListener("scroll"' src/
(no output)

$ grep -rn "h-screen\|100vh" src/
(no output)

$ grep -rnc "uppercase.*tracking" src/screens/Invoices*.tsx
2                           # 2 labels on a screen with 6 sections: under ceil(6/3) = 2. At the cap, not over.
```

Accent audit: `#A2542E` appears in the token file and in Copper usages only. No other accent value exists in the tree.

## Render vs board

`boards/invoices-a.png` and the built screen at 1440, side by side. Same paper, same copper, same table rhythm; the build adds the empty state the tile never showed and drops the tile's invented column for "Notes", which the real schema does not have. Everything else matches, and the divergence is written down here rather than discovered by the owner.

## Contrast spot checks

| Pair | Ratio | Threshold |
| --- | --- | --- |
| Ink #1B1A18 on Paper #F7F6F3 | 16.1:1 | 4.5 (body) |
| Slate #6B6A66 on Paper #F7F6F3 | 5.0:1 | 4.5 (body) |
| Slate #6B6A66 on Surface #FFFFFF | 5.4:1 | 4.5 (body) |
| Paper #F7F6F3 on Copper #A2542E, the primary button label | 5.1:1 | 4.5 (body) |
| Copper #A2542E on Paper #F7F6F3, focus ring and interactive border | 5.1:1 | 3.0 (border) |
| Overdue #A33B2A on its 10% tint (#EFE3DF over Paper) | 5.2:1 | 4.5 (status text) |

Measured with the WCAG relative-luminance formula, compositing the status tints over Paper before measuring.

## What I could not verify

- **Real iOS Safari.** The `100dvh` behaviour was verified by zoom and by resizing, not on a device. Marked `unrendered` for that specific claim.
- **Print output.** The invoice PDF is generated server-side and is out of this screen's scope.
- **Screen reader pass.** Semantics and `aria-live` on the status changes were reviewed in the code; no VoiceOver or NVDA run was possible in this environment.

## Still open

- Empty state illustration is a labeled placeholder (`<!-- TODO: empty state image, 600x400 -->`). The screen is correct without it; it is not finished looking.
- Mobile sheet drag has no damping at the top boundary (motion work, not layout).
- ~~Double hairline under each row~~ fixed in this pass.
- ~~Spinner on first load~~ replaced with skeleton rows in this pass.
