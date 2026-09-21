# Critique: Invoices screen, 2026-09-18

One pass, rendered first, one table, sorted by impact. Source of truth for the "before" column: the render at commit `9f4c1ab`. The design system is [DESIGN.md](DESIGN.md).

| Before | After | Why |
| --- | --- | --- |
| Page title 44px over a 5-word subtitle, with an eyebrow above it reading `INVOICES / 2026` | 32px title, eyebrow deleted | The eyebrow was one of seven on the page; nothing labels a section better than its position |
| Every row carried a top **and** a bottom hairline (24 rows, 48 rules) | One Hairline under each row; the header is separated by spacing instead | Double rules on every row is the laziest table there is, and the pair vibrated at 100% zoom |
| `transition: all 300ms ease` on the detail panel | `transition: transform 180ms var(--ease-out)` | `all` animates properties nobody meant to animate; naming them also made it faster |
| Amounts rendered in the UI sans, left-aligned | Geist Mono, `tabular-nums`, right-aligned | Money is compared down the page; proportional digits make that impossible |
| Accent used for the "Draft" badge (a second accent in practice) | Draft is Slate; Copper is only actions, focus, and links | One accent, everywhere, or it stops meaning anything |
| `transform: scale(0)` on the panel opening | `transform: scale(0.98); opacity: 0` | Nothing real appears from nothing; the pop was the tell |
| Colored status dot next to each row | The word itself, in its status color | A dot that repeats the word beside it is decoration |
| Loading state was a 24px circular spinner | Skeleton rows matching the table's real geometry | The layout stops jumping when the data lands |
| Body copy used an em dash in the empty state ("No invoices yet — create your first") | "No invoices yet. Create the first one." | Zero em dashes in the interface. Always. |

## What this pass deliberately did not touch

- The table's column order (the owner's own words in the interview: "who owes me, how much, when").
- The `InvoiceTable` component's props. Analytics reads `data-invoice-status` and it stays.
- The paper-warm neutral (`#F7F6F3`). It is the brand, not a default; changing it would break the printed invoice PDFs to match.

## Still open after this pass

- The empty state has no illustration or generated image yet; [walk.md](walk.md) lists the placement. The human supplies or approves it.
- Mobile sheet drag has no damping at the top boundary.
