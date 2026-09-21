# Critique and Iterative Refinement

## The loop (render, critique, fix, prove)

The loop is identical whether you are generating a screen for the first time or tightening one that shipped last year:
look at the pixels, say what is wrong, fix the few things that matter, look again.

### How much proof this pass owes

Evidence scales with the size of the claim, not to zero and not past need:

* **Full pass** â€” a new product, a new page, or a redesign: everything gate 16 lists. Board, fresh renders at three widths in both themes, reduced-motion and keyboard passes, zoom, contrast values, pasted pre-flight, walk record.
* **Spot pass** â€” a fix inside an product with an existing design system that touches one component or one region of one screen. Say `spot pass` out loud, then owe exactly this:
  * fresh renders of the affected region at the widths it actually appears at (both themes if it touches color or tokens; one if the design system (DESIGN.md) make variation impossible),
  * contrast values for any token that changed,
  * the critique table â€” still one table, before/after/why,
  * the pre-flight rows the change could plausibly break â€” all of them, not the convenient ones,
  * the walk record appended, or a dated spot record beside it.
  
  No board. No keyboard or zoom pass unless interaction changed.
* What no pass may skip: **fresh** renders (never reused from a previous sitting), the honest `unrendered`, and the bans. "Small" changes the amount of evidence, never its freshness.

1. **Render.** Run the thing. Screenshot it at 375, 768, and 1440 in both themes, and put the chosen tile next to each one. Look at the actual pixels; never critique from the source. *(A spot pass renders the affected region at the widths it appears at instead â€” say which you ran.)*
2. **Critique against the design system (DESIGN.md), then against the bans.** Output **one markdown table**, one row per issue:

   | Before | After | Why |
   | --- | --- | --- |
   | Amounts in the UI sans, left-aligned | Mono, `tabular-nums`, right-aligned | Money gets compared down the page; proportional digits defeat that |
   | A rule above **and** below every table row | One rule under each row | Doubled hairlines make a long table vibrate at 100% |
   | A spinner while the list loads | Skeleton rows at the table's real geometry | The layout stops jumping when the data lands |
   | A status badge borrowing the accent | Status tints desaturated, accent reserved for actions | Two accents means neither one means anything |
   | `z-50` sprinkled wherever something overlapped | The documented stacking ladder | Ad-hoc z-index is how modals end up under tooltips |

   Never a Before/After list. Never a wall of prose. One table, sorted by impact.
3. **Rank, then fix the top few.** Order of leverage: **structure and hierarchy â†’ typography â†’ spacing and rhythm â†’ color â†’ states â†’ motion â†’ nits.** A font swap and a palette cleanup move a page further than fifty small adjustments. Fix the top handful, re-render, look again.
4. **Pick a mode** if the human names one. **Audit**: find the highest-impact problems. **Critique**: explain what feels generic, overdesigned, or inconsistent. **Polish**: edit it. **Animate**: add motion only where it clarifies. **Harden**: mobile overflow, clipping, contrast, missing states, fragile assumptions. **Live**: final QA before someone else sees it.
5. **Prove it.** Pre-flight passes, walk recorded, evidence committed. Then stop.
6. **Stop.** Not "while I'm here". Not a restyle of three other pages nobody asked about. A design pass that never ends is not taste â€” it is anxiety.

### If the interface already exists

1. **Detect the mode.** Either this is new, or it is a redesign that preserves the existing brand, or it is a redesign starting visually fresh. If it is ambiguous, ask once: *"Preserve the existing brand, or start visually from scratch?"*
2. **Audit before touching anything.** Write down the current tokens (accent, type stack, radii, logo), the information architecture and conversion paths, and which content blocks are doing work versus filler. Note the patterns worth preserving (signature interactions, a recognizable hero, the copy voice) and the ones to retire (the bans, dead links, stock filler, performance traps). Read the dials the existing site is already running at, and capture the SEO baseline, because losing rankings is the number one redesign risk.
3. **Preserve.** Do not change information architecture unasked. Extract the real brand accent *before* applying the color rules; a brand that is already purple stays purple. Keep the copy voice. Do not regress accessibility. Do not rename anything analytics depends on.
4. **Modernize in leverage order**, stopping when the brief is satisfied: typography â†’ spacing and rhythm â†’ color recalibration â†’ motion layer â†’ hero and key sections â†’ full block replacement (only when unsalvageable).
5. **Never change silently**: URL structure, primary nav labels, form field names or order, the logo, legal and consent copy.

---

