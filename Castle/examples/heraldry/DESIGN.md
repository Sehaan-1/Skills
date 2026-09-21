# Design System: Saltbox

The design system for the invoicing effort from the [pipeline example](../README.md). Small-business bookkeeping, two people, desktop-first, used by owners who dislike accounting.

## Register

**Keep** - a tool that must feel solid, used at a kitchen table next to a paper folder. The ranking against Scriptorium came down to how the money scans in a column.

## Chosen board

`docs/heraldry/boards/invoices-a.png` - *"the other two look like someone else's product. I want the one that looks like my paperwork."*

## Dials

Boldness **4** · Motion **3** · Density **6**

A bookkeeping screen for small-business owners: calm and plain. Register Keep, leaning toward one neutral palette, a real typeface, and a table that behaves like paper.

## 1. Atmosphere

Quiet, legible, and slightly old-fashioned, like a good paper ledger. The screen should feel like it is on the owner's side. Nothing is decoration: no gradients, no glow, no mascots. Density is product-level, so hierarchy comes from hairlines and spacing rather than boxes.

## 2. Color, named by role

- **Paper** (#F7F6F3) - page background. Warm-neutral on purpose; the whole product uses this one neutral family.
- **Surface** (#FFFFFF) - raised fills: the detail panel, popovers, the row under the cursor.
- **Ink** (#1B1A18) - primary text. Off-black, never #000000.
- **Slate** (#6B6A66) - secondary text, labels, timestamps.
- **Hairline** (rgba(27,26,24,0.10)) - every structural line in the table.
- **Copper** (#A2542E) - THE accent. One. Primary buttons, active nav, focus ring, links. Nothing else.
- **Paid** (#4C6B4F) / **Overdue** (#A33B2A) / **Draft** (#6B6A66) - status only, always paired with the word, never a bare dot.

**Banned:** pure black, pure white, any second accent, neon, glow shadows, the AI purple family, warm and cool grays mixed in one screen.

## 3. Typography

- **Display and UI:** Geist. Tight tracking on headings, weight-driven hierarchy. Headings are 1.15 leading.
- **Body:** Geist, 15px/1.55, 65ch max on prose. Table cells are 14px.
- **Amounts, dates, invoice IDs:** Geist Mono with `tabular-nums`. Money is a mono column, always, so the eye can compare down the page.
- **Scale:** `clamp()` for the page title only; everything else is a fixed step (13 / 14 / 15 / 18 / 24 / 32).
- **Banned:** Inter, Roboto, any serif face, Fraunces, Instrument Serif, gradient text.

## 4. Components

- **Buttons:** flat. Radius 10px. Primary is Copper fill with Paper text; secondary is a Surface fill with a Hairline border. `:active` scales 0.98. Focus ring is Copper at 2px with 2px offset. Labels stay on one line.
- **Inputs:** radius 8px, label above, error below in Overdue, focus ring Copper. No placeholders standing in for labels.
- **The invoice table:** no card, no border box. Rows separated by a single Hairline under each row. Numeric columns right-aligned and mono. Header row is Slate, uppercase at 0.08em tracking, one instance on the screen.
- **Status badges:** full pill, tinted background from the status color at 10%, Ink text. The word is always inside; there is never a colored dot on its own.
- **Loaders:** a skeleton of the exact table rows. No spinner.
- **Empty state:** one sentence and the "New invoice" button, centered in the table area.
- **Errors:** inline, next to the field that caused them.

## 5. Layout

- 12-column grid, max width 1200px, 24px gutters. Content column is 8 wide, detail panel 4.
- One page title per screen, no eyebrow. The screen's own nav already says "Invoices".
- Below 768px the grid collapses to a single column, the detail panel becomes a full-screen sheet, and the table drops to name + amount + status. Declared in each component, not assumed.
- Nothing overlaps. `min-h-100dvh` for full-height areas, never `100vh`.

## 6. Motion

- Motion is deliberately low. Hover states, focus rings, the detail panel, and the row cursor only.
- One curve for everything: `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`. 140ms for controls, 180ms for the panel.
- Nothing animates on keyboard-driven actions. No springs at this intensity. No infinite loops.
- Every transition names its properties. No `transition: all`.
- `prefers-reduced-motion` removes the panel transition; hover colors stay, because a color change is feedback, not motion.

## 7. Pre-flight bans

Zero em dashes anywhere in the interface. No second accent. No card boxes around table data. No colored dots without a word. No spinner. No scroll-triggered reveals on a data screen. No emoji.

## 8. Agent prompt guide

> Build screens for Saltbox: a calm small-business bookkeeping tool. Use Paper #F7F6F3 for the page, Surface #FFFFFF for raised fills, Ink #1B1A18 for text, Slate #6B6A66 for secondary text, and Copper #A2542E as the single accent for actions, focus, and links. Type is Geist, with Geist Mono and tabular numerals for every amount and date. Radius is 10px for controls and cards, 8px for inputs. Density is high: prefer hairlines and spacing over cards. Motion is minimal, 140-180ms, ease-out, transform and opacity only. Never use a second accent color, a spinner, an em dash, or a card around table data.
