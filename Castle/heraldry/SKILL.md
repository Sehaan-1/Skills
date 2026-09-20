---
name: heraldry
description: "Use when designing, building, redesigning, or polishing any user interface: a page, screen, component, landing page, dashboard, portfolio, design system, or a DESIGN.md. Use when something looks generic, templated, or AI-made; when the user asks for taste, visual direction, typography, color, motion polish, a critique, an audit, reference boards, mood boards, or a design-to-code fidelity loop. Use when a screen must be proven good, not merely called good. Do not use to decide product questions (cuecards), to implement a decided slice (oneslice), or to map multi-workstream shipping (lanes)."
---

# Heraldry

A castle wears one coat of arms. Every tower, gate, and banner carries the same tinctures, the same charges, the same hand. Nobody designed each wall separately.

This skill is that idea, applied to interfaces. Decide what this thing looks like, write it down as **the arms** (`DESIGN.md`), then make every screen wear them. When the interface already exists, this is the loop that renders it, critiques it, fixes the few things that matter, and proves it with fresh evidence.

Cuecards decides *what* to build. Oneslice builds it. Lanes ships the whole destination. Heraldry answers the question lanes explicitly refuses — **what does it look like, and is it actually good?**

Announce at start: `Using heraldry to [read | cast | arm | build | critique | polish | walk | stop].`

## Hard gates

1. **Read the room before you pick a font.** Say one line out loud, in plain words: who this is for, what it should feel like, which family it leans toward. No code until that line exists. If the brief genuinely diverges, ask **one** question, not a questionnaire.
2. **Dial first, default never.** Name `BOLDNESS`, `MOTION`, and `DENSITY` before you build, with a one-clause reason from the read. The baseline is a fallback, not a decision.
3. **No arms, no second screen.** You may build one screen to learn something. You may not build the app on an unwritten direction. Write `DESIGN.md`, commit it, then cut.
4. **The arms are law once written.** Like an ADR: cite them, follow them, and when you must change one, change it deliberately in the same commit as the code and say so. Never quietly drift because a section "looked better" in a different palette.
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

<!-- ── PROVENANCE GATES (a claim is not a check) ─────────────────────────── -->

16. **"It looks good" is a claim. It is not a check.** Before you tell a human an interface is done, five artifacts must exist, made in *this* sitting:

    - **The arms** committed (`DESIGN.md`), and the code matching them. If the code and the arms disagree, the arms are wrong or the code is; say which and fix it.
    - **The board** at `docs/heraldry/<slug>-board.md`, carrying a human's pick, when this is a new product, a page whose look is the question, or a redesign. A one-component fix inside an already-armed product skips it, out loud.
    - **A critique** at `docs/heraldry/<slug>-critique.md`: the Before/After table from the last pass.
    - **A walk** at `docs/heraldry/<slug>-walk.md`: the record below, with **fresh renders** at 375 / 768 / 1440 in both themes, and a reduced-motion pass.
    - **The mechanical pre-flight output**, pasted. Real commands, real output. Not a summary.

    Renders must be new. A screenshot from three sessions ago is not evidence that this diff is good.

17. **An agent may not certify its own taste by assertion.** Writing "audited for accessibility" with no renders, no contrast values, and no keyboard pass is a fabricated check. If you cannot render the interface in this environment, write `unrendered` in the walk record, list exactly what you could not verify, and hand it to the human to look at. `unrendered` is honest and acceptable. A fake pass is not.

18. **Do not call a screen done when the walk would not catch it breaking.** The walk has to be able to fail: if a broken layout, a contrast failure, a missing focus ring, or an overflowing hero would still produce a green walk record, the walk is a slideshow, not a check. Strengthen it.

19. **You cannot pick the direction for them.** A board with no human pick is three files, not a decision. If nobody has pointed at a tile, the direction is not chosen: do not write the arms from your own favorite and carry on. When the human is unavailable, cast the tiles, state the recommendation, and stop there.

<!-- ─────────────────────────────────────────────────────────────────────── -->

## Reading the room

Most machine-made interfaces are bad for one reason: the model jumps to its default aesthetic instead of reading the room. Train yourself out of it. Read these first, in this order:

1. **Page kind.** A landing page, a portfolio, a product screen, a dashboard, something editorial, or a redesign. Each has its own expectations; name which one before you design for it.
2. **Vibe words the human actually used.** "Calm", "Linear-ish", "brutalist", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "dark tech", "warm", "cheap and fast".
3. **References.** Pasted screenshots, linked sites, named competitors. A reference outranks every adjective.
4. **Audience.** A procurement panel and a design-literate consumer do not get the same page. The audience picks the aesthetic, not your taste.
5. **What already exists.** Logo, color, type, photography, existing design system. On a redesign these are starting material, not optional input.
6. **Quiet constraints.** Accessibility-first, public sector, regulated, trust-first commerce, kids, safety. These override aesthetic preference without discussion.

Then say the line, in that many words or fewer:

> A \<kind> for \<audience>: \<vibe>. Register \<name>, leaning toward \<family or system>.

- *"A bookkeeping screen for small-business owners: calm, plain. Register Keep, leaning toward one neutral palette and a real typeface."*
- *"A studio portfolio for hiring managers: kinetic and editorial. Register Masquerade, leaning toward native CSS and a custom display face."*
- *"A public-service form, rebuilt: trust first. Register Keep, leaning toward the design system this sector already uses."*

If the read genuinely forks, ask **one** question: *"Should this feel closer to calm-and-plain or bold-and-experimental?"* If you can infer, infer, say the line, and move. Do not ask permission to have taste.

**No defaults.** Do not reach for: purple-blue gradients, a centered hero over a dark mesh, three equal feature cards, glass on everything, an infinite loop in every tile, Inter plus slate-900. Those are habits, not a direction.

---

## The three dials

Set all three. Every layout, motion, and density decision below is gated by them. Never invent aliases; use these names.

* **`BOLDNESS`** — 1 = perfect symmetry, 10 = artsy chaos. Baseline **8**.
* **`MOTION`** — 1 = static, 10 = cinematic physics. Baseline **6**.
* **`DENSITY`** — 1 = art gallery, 10 = cockpit. Baseline **4**.

### Reading the dials off the brief

| Signal | Boldness | Motion | Density |
| --- | --- | --- | --- |
| "minimal / calm / clean / editorial / Linear-style" | 5-6 | 3-4 | 2-3 |
| "premium consumer / Apple-y / luxury / brand" | 7-8 | 5-7 | 3-4 |
| "playful / wild / experimental / agency / showcase" | 9-10 | 8-10 | 3-4 |
| "landing page / portfolio / marketing" (default) | 7-9 | 6-8 | 3-5 |
| "product screen / dashboard / tool" | 3-5 | 3-5 | 5-8 |
| "trust-first / public sector / regulated / accessibility-critical" | 3-4 | 2-3 | 4-5 |
| "redesign, preserve the brand" | match existing | match +1 | match existing |
| "redesign, start visually fresh" | +2 | +2 | match existing |

Do not ask the human to edit a config file. Overrides happen in conversation.

### What the levels mean

**Boldness.** 1-3: strict grids, equal padding, centered. 4-7: negative-margin overlaps, mixed aspect ratios, a left-aligned header over centered data. 8-10: fractional grids (`2fr 1fr 1fr`), masonry, deliberate empty zones. **Mobile override:** from level 4 up, any asymmetric layout must collapse to a strict single column below 768px. Declare that collapse in the component, not in your head.

**Motion.** 1-3: no automatic motion; `:hover` and `:active` only. 4-7: one motion language, `transform` and `opacity`, short durations, cascades on load. 8-10: scroll-driven reveals, pinning, scrubbed sequences, springs. From level 4 up, `prefers-reduced-motion` is mandatory.

**Density.** 1-3: large section gaps, few elements, expensive emptiness. 4-7: normal product spacing. 8-10: tight padding, cards banned, **all numbers in a tabular mono**, hierarchy from hairlines and gutters rather than boxes.

---

## The nine registers

A register is where the arrows start: dials, palette family, type stance, motion stance, and what that world must never do. Name one per product, in the arms, and let it do the first half of the thinking. It is a starting position, not a costume — the arms may bend it, but you say why.

| Register | Built for | Boldness | Motion | Density | Palette family | Type stance | Never |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Keep** | product UI, tools, dashboards that must feel solid | 3 | 2 | 6 | one neutral ramp, one accent | one grotesk, hierarchy by weight | decoration, gradients, a hero |
| **Scriptorium** | docs, settings, long-form product text | 2 | 2 | 4 | paper neutrals, ink | body serif allowed, mono for code and IDs | card-inside-card, accent sprawl |
| **Cathedral** | editorial, publication, brand storytelling | 6 | 3 | 2 | high contrast, plenty of paper | a display face with real character, tall scale | cards, shadows, icons as ornament |
| **Barbican** | raw tools, builder products, manifesto pages | 5 | 4 | 7 | near-black on off-white, one alert color | heavy grotesk caps against mono | rounding, blur, soft shadows |
| **Armoury** | devtools, telemetry, terminals | 4 | 5 | 9 | off-black surfaces, one restrained emissive accent | mono for numbers and IDs, grotesk for UI | serif, a light theme, pastel |
| **Watchtower** | ops, monitoring, live data | 3 | 4 | 8 | dark or light, semantic status only | tabular numerals everywhere | decorative motion, illustration |
| **Solar** | premium consumer, care, craft, warmth | 5 | 5 | 4 | rotate families; never the warm-craft default | humanist sans, or one justified serif | glow, beige-and-brass as the reflex |
| **Bazaar** | social, playful consumer, events | 9 | 8 | 5 | two saturated hues against honest neutrals | chunky display, weight contrast | monochrome, corporate blue |
| **Masquerade** | agency, portfolio, launch, showcase | 9 | 9 | 2 | bone or black base, one loud accent | display type carrying the composition | cards as filler, stock-photo rows |

Two registers in one product is two brands. A split is legitimate only when the arms say so and the seam is obvious: a marketing site may be Cathedral while the product it sells is Keep. Everything else picks one.

When the read lands between two registers, pick the one that matches how the product is used for hours, not the one that photographs better. A tool that is beautiful for ten seconds and tiring for three hours has the wrong register.

---

## Cast three tiles, one choice

"Premium" and "calm" mean ten different things to ten people. Stop describing the direction. Show three, and let a human point.

**Cast three.** The named register, its closest rival, and one deliberate outlier. Two safe options is a false choice, and the outlier is often the one that wins.

**One tile per direction, one image per tile.** Never a grid, collage, or contact sheet inside a single image; three files, not one. Each tile:

- shows the same real screen moment, with the same real copy, at the real aspect ratio (desktop 16:10, mobile 9:19.5)
- commits to one register completely, with no mixing
- states the palette by role, the type stack, the density, and the register's bans in the prompt that made it
- is a *look*, not a layout document. Nobody builds from it literally, and its invented text is not copy.

Prompt shape:

> A \<desktop|mobile> interface for \<the real product and screen>. Register: \<name>, \<its atmosphere in a phrase>. Colors: \<role by role, with hex>. Type: \<display face> for headings, \<body face> for text. Density: \<level>. The frame implies \<what motion looks like here>. Banned: \<the register's never-list>. Ratio \<n:n>.

**No image tool?** Build one HTML page with three full-bleed sections, one per tile, and screenshot each at the real ratio. You get the board and a head start on the CSS in the same pass. Often the better path.

**A human points.** The agent does not choose the direction, and does not proceed on "they will probably like it". Quote the pick verbatim. If nobody answers, the board stays open and you say so out loud.

**Record it** at `docs/heraldry/<slug>-board.md`:

```markdown
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
<the two or three things the arms should adopt from the comparison>
```

**Then write the arms from the chosen tile**, and hand the builder three things: the tile, the arms, and the register name. The tile is a reference, not a spec. Where the tile and the arms disagree, the arms win — or you amend the arms on purpose, in the same commit, and say so.

**Fidelity is a check, not a feeling.** At the end, put the built screen beside the chosen tile at the same width. If the build landed in a different register than the tile it came from, either the tile was wrong or the build is.

---

## Arm the castle

**The arms are `DESIGN.md` at the repo root.** One file. It is the single source of truth for what this product looks like, readable by any agent, and precise enough to generate new screens from. If the repo already has one, it is law: follow it, and change it on purpose.

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

### Rules for the arms

- **Name colors by role, not appearance.** "Copper" means "the accent", not "a nice brown". Role names survive a palette change; appearance names do not.
- **Always hex, always the number.** "Deep charcoal (#1B1A18)". Radius, spacing, and type scale get numbers too.
- **One accent.** Semantic states are status, not a second accent, and they are desaturated to live inside the neutral system.
- **Write the bans down.** The explicit "never do this" list is what keeps the next screen from drifting back to the default. A design system without bans is a mood board.
- **Lock the register, and cite the board.** Both sit at the top of the file, above the colors, because they are the decisions everything else follows from. A reader should be able to tell which register this is and which tile was chosen without scrolling.
- **Plain language.** "Generously rounded corners (10px)", not `rounded-[10px]`. The arms are read by humans first and agents second.
- **Short.** If the arms are longer than the code they describe, they will not be read. Cut.
- **Rotate between projects.** Never ship the same palette, typeface, and layout family twice in a row. If your last project was beige and brass, this one is not.

---

## The tinctures (color)

* **One accent, used identically everywhere.** Pick it once, lock it. A rose-accented site does not get a teal status badge in the footer. Audit every component before shipping.
* **Saturation under 80%** unless the brand demands otherwise. Desaturated accents sit in a neutral system; saturated ones fight it.
* **No pure black, no pure white.** `#000000` kills depth and reads as a default. Use off-black and off-white.
* **One palette per project.** Do not mix warm and cool grays. Do not invent a new tint for section seven.
* **The purple exemption, not the purple default.** The AI-purple glow is discouraged as a *default*. If the brand is genuinely purple, embrace it and execute with intent: one palette, harmonized neutrals, restrained gradients.
* **Beige and brass is not a brand.** For cookware, wellness, artisan, heritage, or luxury briefs, that warm-craft family (cream page, brass or clay accent, espresso text) is the most-reused palette in existence, and it is banned unless the brief names those colors. Rotate instead: cold luxury (silver, chrome, smoke) · forest (deep green, bone, amber) · black and tan · cobalt and cream · terracotta and slate · monochrome plus one saturated pop.
* **Tint your shadows.** A shadow carries the hue of the background. Pure-black drop shadows on a warm surface look like dirt.
* **Contrast is arithmetic, not opinion.** WCAG AA for body text (4.5:1), 3:1 for large text and interactive borders. Hero copy aims higher. Check the numbers; do not eyeball them.
* **Both themes, one hierarchy.** Whatever pops in light mode pops in dark mode. The brand color stays recognizable. Set `color-scheme` and a matching `theme-color`, and give native controls explicit colors.
* **Status colors are rationed.** A colored dot means real state (a server is down), not decoration on every list row.

---

## The letter (typography)

* **Hierarchy comes from weight, color, and spacing before size.** A page where every headline is enormous has no hierarchy at all.
* **Display**: tight tracking, compressed leading, `clamp()` scale. Body: 65 characters per line, relaxed leading, never below 1rem on mobile.
* **Inter is not the default.** Reach for Geist, Satoshi, Cabinet Grotesk, Outfit, or a brand face first. The override is real: Inter is fine when the brief is explicitly neutral, trust-first, or accessibility-first, and you say so.
* **Serif discipline.** "Creative, so serif" is the most-tested tell there is. A serif is allowed only when the brand names one, or the family is genuinely editorial, luxury, publication, or heritage, and you can say why *this* serif fits *this* product. Default to a sans display. Banned as defaults: Fraunces, Instrument Serif. Banned always: Times, Georgia, Garamond, Palatino as stand-ins for "serif". Serif is banned outright in dashboards and software UI.
* **Emphasis inside a headline uses the same family**: italic or bold, never a random serif word dropped into a sans line.
* **Italic descenders need room.** If an italic display word contains `y g j p q`, leading below 1.1 clips it. Reserve the space.
* **Numbers behave.** `tabular-nums` in any column that gets compared. At density above 7, all numbers are mono.
* **Real typography, not substitutions.** Curly quotes, `…` instead of `...`, non-breaking spaces in units and shortcuts, `text-wrap: balance` on headings.
* **Load fonts properly.** Self-host or `next/font`, `font-display: swap`, preload the critical face. Never a bare Google Fonts `<link>` in production.

---

## The form (layout and components)

### The hero

* **It fits the first viewport.** Headline two lines maximum on desktop, subtext under 20 words and under four lines, primary action visible without scrolling.
* **Four text elements, maximum.** One of: eyebrow / brand strip / nothing. A headline. A subtext. Actions. That is the list. A tagline under the buttons, a trust micro-strip, a pricing teaser, or a feature bullet list inside the hero is a defect; those are separate sections below it.
* **A four-line headline is a size error, not a copy error.** Lower the scale, widen the container, or cut the words. Plan the type size and the hero asset together.
* **Top padding cap: roughly 6rem at desktop.** More than that and the hero floats halfway down the viewport, which reads as a layout bug, not breathing room.
* **Centered heroes are banned above variance 4**, unless the message itself is the design (manifesto, launch, single statement).
* **A hero needs a real visual.** Type over a gradient blob is a placeholder.
* **Buttons must be readable.** White on white, weak ghost buttons over photographs, and accent-on-accent all fail. One primary action, at most one secondary.

### Rhythm

* **Small-caps labels are rationed.** The tiny uppercase, wide-tracked label sitting above a headline is the most overused device in machine-made UI, and it appears above *everything* by reflex. **One per three sections at most, the hero counting as one:** nine sections buy you three. Count them in the diff, not in your memory. The usual right answer is deleting it; a section's position on the page already labels it.
* **A layout family appears once.** Three-column image cards, full-width quote, split text and image: each family gets one appearance per page. Eight sections need at least four families.
* **Zig-zag caps at two.** The third consecutive image-left/text-right split is a fail. Break it with a full-width section, a grid, or a different structure.
* **The split header is banned.** Big headline left, small explainer paragraph floating in the right column. Stack them, or make the right column carry something real.
* **Section numbering, meta-labels, and micro-meta sentences are banned.** `00 / INDEX`, `002 - Capabilities`, `Step 1 of 3`, and a sentence of throat-clearing under a heading all read as filler.
* **Long lists get a different component**, not more rows. Over five items: grouped columns, a card grid, tabs, scroll-snap pills, a carousel, or a marquee for things that do not need individual attention.
* **Content shape per section**: short headline, short paragraph, one asset or one action. Landing pages live on the first impression.
* **CTAs: one label per intent, page-wide.** "Get in touch", "Contact us", and "Let's talk" are the same button; pick one and use it everywhere. A desktop CTA label never wraps to two lines.

### Shape and surface

* **Pick one radius system and document it.** All-sharp, all-soft, or a stated rule ("buttons full-pill, cards 16px, inputs 8px") that holds everywhere. Round buttons in a square layout is broken design.
* **Cards only when elevation means something.** Otherwise group with a top border, a divider, or whitespace. Above density 7, generic card containers are banned: let data breathe in plain layout.
* **Navigation renders on one line at desktop, under 80px tall.** If it does not fit, condense the labels before you wrap them or hide them behind a menu.
* **Grid over flex math.** No `calc(33% - 1rem)`. Use CSS Grid.
* **Contain the page**: a max width, generous horizontal padding that scales with the viewport.
* **`min-h-[100dvh]`, never `h-screen`.** The iOS address bar makes `100vh` wrong.
* **Z-index is a system**, not a pile of `z-50`s. Document the ladder: base, sticky, overlay, modal, grain.
* **No overlap** unless the composition genuinely depends on it. Text over text and text over image edges are the most common self-inflicted readability wound.
* **Mobile collapse is explicit per section.** Write the `< 768px` fallback in the component. "Tailwind will handle it" is not a plan, and horizontal scroll on mobile is a critical failure.

### States (the part that gets skipped)

* **Loading**: skeletons shaped like the layout they replace. Not a spinner.
* **Empty**: composed, with the real action that fills it.
* **Error**: inline and specific, under the field it belongs to.
* **Hover, focus, active, disabled**: all four, on everything interactive. Focus is visible and never removed without a replacement. Use `:focus-visible`.
* **Press feedback**: a subtle scale or a 1px shove, so the interface feels like it heard the click.
* **Forms**: label above the input, error below, helper text optional but present. Never a placeholder standing in for a label. Check placeholder, focus ring, and error text contrast against the section background.
* **Ordinary things that get forgotten**: a way back, a real 404, destructive actions confirmed or undoable, a skip link, legal links, long-content truncation (`min-w-0` on flex children), explicit image dimensions, and empty-string safety everywhere.

### Copy

* **One register per page.** Do not mix terse product voice, editorial prose, and marketing punch in a single composition unless the brand is genuinely that.
* **Re-read every visible string before shipping**: headline, subhead, button, caption, error, alt text, empty state, footer. Flag anything grammatically broken, anything with an unclear referent, anything that sounds like a machine being thoughtful. Rewrite unclear strings as plain functional sentences. Boring and clear beats clever and wrong.
* **Numbers must be honest.** Real data, or explicitly labeled as sample. Invented precision is banned.
* **Quotes**: three lines maximum, attribution with a name and a role. Real typographic quotes or none.
* **No filler verbs.** "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize" are noise. Concrete verbs, specific nouns.
* **Names and data must sound real.** No "User One", no "Example Corp", no round-number performance claims. Invent names that belong to the actual product and the actual region, and let numbers be slightly untidy (`47.2%`) the way measured numbers are.

---

## The motion

Motion is the fastest way to look expensive — and the fastest way to look fake. The rules are not stylistic; they are about intent, physics, and cost.

### Should it animate at all

Ask how often a user will see it.

| Frequency | Decision |
| --- | --- |
| Hundreds of times a day (command palette, keyboard shortcut) | No animation, ever |
| Tens of times a day (hover, list navigation) | Remove it or cut it to almost nothing |
| Occasional (modal, drawer, toast) | Standard animation |
| Rare or first-time (onboarding, first success) | Room to delight |

**Never animate keyboard-initiated actions.** They are repeated constantly, and animation makes them feel slow and disconnected from the keypress.

### Why it animates

Valid reasons: spatial consistency (a toast leaves the way it came in), showing a state change, explaining how something works, answering a press, or softening a change that would otherwise jolt. Invalid: "it looks cool". If you cannot answer in one sentence, drop it.

### How it moves

* **Entering or exiting → ease-out** (starts fast, feels responsive). **Moving on screen → ease-in-out.** **Hover or color change → ease.** **Constant motion → linear.** Never `ease-in` for UI; it delays the exact moment the user is watching.
* **The built-in curves are too weak.** Define your own once and reuse them:

```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);      /* UI interactions */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);     /* on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);      /* drawers and sheets */
```

* **Duration bands**: press feedback 100-160ms, tooltips 125-200ms, dropdowns 150-250ms, modals and drawers 200-500ms. UI work stays under 300ms. A 180ms dropdown feels faster than a 400ms one at identical cost.
* **Springs for anything interruptible**: `stiffness: 100, damping: 20` as a start. Springs carry velocity when interrupted; keyframes restart from zero. For gesture-driven state (a drawer the user might reverse), transitions or springs win; keyframes lose.
* **Never animate from `scale(0)`.** Nothing in the world appears from nothing. Start at `scale(0.95)` with opacity.
* **Nothing animates `top`, `left`, `width`, or `height`.** `transform` and `opacity` only.
* **Popovers are origin-aware.** They scale from their trigger, using the transform-origin value your primitive library exposes (Radix publishes `--radix-popover-content-transform-origin`, for example). Modals stay centered because they are not anchored to anything.
* **Tooltips open instantly once one is already open.** Keep the delay on first hover; skip the animation on the next.
* **Reveal staggered lists with a cap.** Small groups cascade; long lists mount instantly. A slow cascade on a long list feels broken.
* **Blur bridges a bad crossfade.** A 2px `filter: blur()` during the transition hides the moment two states overlap.
* **`transform: translateY(100%)`** beats hardcoded pixels: it is relative to the element, so it survives any height.

### How it costs

* **CSS for predetermined motion, JS for interruptible motion.** CSS runs off the main thread; under load, JS animation frames drop.
* **WAAPI** when you want programmatic control with CSS performance.
* **Motion's shorthand props (`x`, `y`, `scale`) are not hardware-accelerated.** Use the full `transform` string when it matters.
* **Changing an inheritable CSS variable on a parent recalculates every child.** Set the transform on the element, not a variable on the container.
* **Grain and noise go on a fixed, `pointer-events-none` overlay.** Never on a scrolling container.
* **Never `window.addEventListener("scroll")`**, never a `requestAnimationFrame` loop that writes React state, never `useState` for a continuously changing value. Use scroll-driven CSS, `IntersectionObserver`, Motion's `useScroll`, or a `ScrollTrigger`; use motion values for anything driven by the pointer.
* **Clean up.** Every observer, timer, listener, and animation instance gets a teardown.
* **`prefers-reduced-motion` collapses everything** above intensity 3: infinite loops, parallax, scroll hijacks, magnetic pull. Gate it, do not hope.

### Canonical patterns (get these wrong and the page feels broken)

* **Sticky stack**: pin each card at `start: "top top"` with `pin: true`, and drive the shrink of the previous card from the *next* card's trigger. The common failure is a trigger that fires halfway through the scroll instead of pinning at the viewport top.
* **Horizontal pan**: pin the wrapper at `start: "top top"`, set `end: "+=" + distance` where distance is track width minus viewport, `scrub: 1`, `invalidateOnRefresh: true`. The common failure is animating before the pin, so the user sees half a slide.
* **Scroll reveal**: for plain "appear on scroll", Motion's `whileInView` with `once: true` is lighter than GSAP. Save GSAP for real pinning and scrubbing.
* **Never mix GSAP or WebGL with Motion in the same component tree.** They fight for the same frames.

---

## The arsenal

Know these by name. Reach for one when the read calls for it, not by default. **At most one marquee per page**, and no infinite loop in every tile.

* **Heroes**: asymmetric split · editorial manifesto · media mask · kinetic type · curtain reveal · scroll-pinned.
* **Navigation**: dock magnification · magnetic button · gooey menu · morphing status pill · radial menu at the click point · speed dial · full-screen mega menu.
* **Layout**: bento grid · masonry · split-screen scroll · sticky stack · deliberate broken grid.
* **Containers**: tilt card · spotlight border · true glass (inner border plus inner highlight, with a solid fallback) · morphing modal that grows from its trigger · swipe stack.
* **Scroll**: sticky card stack · horizontal pan · zoom parallax · scroll-drawn path · sequence scrub.
* **Media**: coverflow · drag-to-pan canvas · accordion strip that opens on hover · hover image trail.
* **Type**: kinetic marquee · text mask over media · scramble decode · circular path · outlined-to-filled.
* **Micro**: directional hover fill from the entry side · ripple from the click coordinates · skeleton shimmer shaped like the content · focus spotlight · tinted ambient gradient.

Bento rules, if you use a grid: **exactly as many cells as you have content** (`3 items → 3 cells`), `grid-auto-flow: dense`, no dead cells in the middle or at the end, and at least two or three cells carrying real visual variation (an image, a brand-appropriate gradient, a texture) rather than white-on-white text.

---

## The loop (render, critique, fix, prove)

The loop is identical whether you are generating a screen for the first time or tightening one that shipped last year:
look at the pixels, say what is wrong, fix the few things that matter, look again.

1. **Render.** Run the thing. Screenshot it at 375, 768, and 1440 in both themes, and put the chosen tile next to each one. Look at the actual pixels; never critique from the source.
2. **Critique against the arms, then against the bans.** Output **one markdown table**, one row per issue:

   | Before | After | Why |
   | --- | --- | --- |
   | Amounts in the UI sans, left-aligned | Mono, `tabular-nums`, right-aligned | Money gets compared down the page; proportional digits defeat that |
   | A rule above **and** below every table row | One rule under each row | Doubled hairlines make a long table vibrate at 100% |
   | A spinner while the list loads | Skeleton rows at the table's real geometry | The layout stops jumping when the data lands |
   | A status badge borrowing the accent | Status tints desaturated, accent reserved for actions | Two accents means neither one means anything |
   | `z-50` sprinkled wherever something overlapped | The documented stacking ladder | Ad-hoc z-index is how modals end up under tooltips |

   Never a Before/After list. Never a wall of prose. One table, sorted by impact.
3. **Rank, then fix the top few.** Order of leverage: **structure and hierarchy → typography → spacing and rhythm → color → states → motion → nits.** A font swap and a palette cleanup move a page further than fifty small adjustments. Fix the top handful, re-render, look again.
4. **Pick a mode** if the human names one. **Audit**: find the highest-impact problems. **Critique**: explain what feels generic, overdesigned, or inconsistent. **Polish**: edit it. **Animate**: add motion only where it clarifies. **Harden**: mobile overflow, clipping, contrast, missing states, fragile assumptions. **Live**: final QA before someone else sees it.
5. **Prove it.** Pre-flight passes, walk recorded, evidence committed. Then stop.
6. **Stop.** Not "while I'm here". Not a restyle of three other pages nobody asked about. A design pass that never ends is not taste — it is anxiety.

### If the interface already exists

1. **Detect the mode.** Either this is new, or it is a redesign that preserves the existing brand, or it is a redesign starting visually fresh. If it is ambiguous, ask once: *"Preserve the existing brand, or start visually from scratch?"*
2. **Audit before touching anything.** Write down the current tokens (accent, type stack, radii, logo), the information architecture and conversion paths, and which content blocks are doing work versus filler. Note the patterns worth preserving (signature interactions, a recognizable hero, the copy voice) and the ones to retire (the bans, dead links, stock filler, performance traps). Read the dials the existing site is already running at, and capture the SEO baseline, because losing rankings is the number one redesign risk.
3. **Preserve.** Do not change information architecture unasked. Extract the real brand accent *before* applying the color rules; a brand that is already purple stays purple. Keep the copy voice. Do not regress accessibility. Do not rename anything analytics depends on.
4. **Modernize in leverage order**, stopping when the brief is satisfied: typography → spacing and rhythm → color recalibration → motion layer → hero and key sections → full block replacement (only when unsalvageable).
5. **Never change silently**: URL structure, primary nav labels, form field names or order, the logo, legal and consent copy.

---

## Forbidden (the tells)

These are the signatures a machine produces when it tries to look designed. Treat them as hard bans unless the brief explicitly asks for one.

### The single worst one

**The em dash is banned in the interface.** Zero. Not "sparingly" — zero. Not in headlines, eyebrows, pills, buttons, body copy, quotes, attribution, captions, or alt text. Use a period, a comma, a colon, or parentheses. Ranges use a hyphen (`2018-2026`), not an en dash. A user should never see anything but the regular hyphen and the math minus sign. *(This ban governs shipped interface copy. Docs, ADRs, tickets, and skill files are not the interface.)*

### Visual

No neon or outer glow, no pure black, no oversaturated accents, no gradient text on large headings, no custom mouse cursors, and no decorative crosshair or hairline grids drawn just to look designed.

### Hero and labels

No version labels (`v0.6`, BETA, INVITE-ONLY) unless the brief is a launch. No micro-eyebrows that number the brand ("Brand, No. 01"). No section-number eyebrows (`00 / INDEX`, `06 / how it works`), and no `01 / 4` counters on tiles. No scroll cues ("Scroll to explore", bouncing chevrons) and no decoration strips across the bottom of the hero (`BRAND. MOTION. SPATIAL.`). No floating explainer paragraph in the top-right of a section header, no tiny tagline under the hero buttons, and no trust logo row inside the hero.

### Separators and decoration

The middle dot is rationed to one per line, and only inside metadata. No colored status dots on every row, badge, or nav item; a dot that repeats the word beside it is decoration. No pills or tags overlaid on photographs, and no photo-credit captions used as filler. No vertical rotated text unless the brief is genuinely experimental and it organizes real content. No version or build footers (`v1.4.2`, `Build 0048`, `last sync 4s ago`) on marketing pages, and no locale, time, or weather strips. No `<br>`-split-and-italicized headlines.

### Fake things

**No div-built fake screenshots.** A hand-made "product preview" out of styled rectangles, fake dashboards, fake terminals, or fake task lists is the number one tell. Use a real screenshot, a generated image, a real mini-version of the component, or nothing at all. The same goes for fake version footers planted inside an invented preview, performance numbers nobody measured, placeholder names, and invented brand shells. No random remote image URLs that may break; use a seeded placeholder or a real asset. No hand-rolled decorative SVG when a library or a generated asset would do, and no icon drawn by hand from path data; pick one family (Phosphor, HugeIcons, Tabler, or similar) at one stroke width.

### Marketing voice

No coy social-proof headings ("Quietly in use at", "Quietly trusted by"). No poetic section labels ("From the field", "Currently on the bench", "Loose plates") where a plain one would do. No mock-humble nods at other people in the industry, and no throat-clearing sentence under a label. No numbered step labels ("Stage 1", "Phase 02") where the verb would do the job: "Install", "Configure", "Ship".

### Layout

No three equal feature cards. No rule above and below every row of a long list. No filled progress tracks used as decoration for comparisons. No centered hero above Boldness 4. No navigation that wraps to two lines at desktop. No layout family used twice on one page.

### Content

No generic names, stock avatars, or suspiciously round numbers. No filler verbs. No emoji, unless the brief is explicitly playful and social, and then sparingly. One copy register per page.

---

## Real assets

Two different jobs, often confused. **Tiles** (above) choose a direction before anything is built. **Assets** fill the interface once the direction is set: photography, product shots, textures, logos. Same tools, different purpose; a board is not a substitute for the imagery inside the product.

Priority order for assets, and do not skip to the bottom because the top is slower:

1. **Generate it.** If an image tool exists in this environment, use it for hero photography, product shots, textures, and section-specific imagery at the right aspect ratio.
2. **Use a real image.** A brand asset, a real screenshot, or a seeded placeholder (`https://picsum.photos/seed/<descriptive-seed>/1600/1200`) with a seed that describes the section.
3. **Label the hole and say so.** `<!-- TODO: hero product photo, 1600x1200 -->` plus a closing sentence: *"This page needs real images at these three placements; supply or generate them."* Never fill the hole with invented decoration.

**A text-only page is not minimalism — it is unfinished.** Even a restrained editorial page needs two or three real images.

**Logo walls**: real SVG brand marks from a public logo set, or a generated monogram when the brand is invented. Logos only, no category labels under them. Legible in both themes.

---

## The walk (proof, not vibes)

A walk is how you know it is actually good. Record it at `docs/heraldry/<slug>-walk.md`:

```markdown
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

If you cannot render, write `unrendered` and list what you could not check — that is a legitimate, honest record. Claiming a walk you did not run is fabrication, and it is worse than an admitted gap.

---

## Pre-flight (mechanical, paste the output)

Run this before you say anything is done. The mechanical ones have real commands; adapt them to the stack, and paste what they return.

- [ ] **Em dash sweep**: `grep -rn "—\|–" src/` returns nothing (visual dash check too, in the copy block).
- [ ] **Label count**: small-caps labels above headings, at most one per three sections.
- [ ] **Accent count**: exactly one accent value across the whole surface.
- [ ] **Radius count**: matches the arms' documented system, nothing off-scale.
- [ ] **Theme lock**: one theme per page; no section inverts mid-scroll.
- [ ] **No pure black / pure white** tokens.
- [ ] **Contrast**: every text and interactive border measured, AA met, values in the walk.
- [ ] **Focus**: every interactive element reachable by keyboard with a visible focus state; no `outline: none` without a replacement.
- [ ] **Reduced motion**: everything above Motion 3 collapses correctly.
- [ ] **`transition: all`**: `grep -rn "transition: all" src/` returns nothing.
- [ ] **Scroll listeners**: `grep -rn 'addEventListener("scroll"' src/` returns nothing.
- [ ] **Viewport**: `grep -rn "h-screen\|100vh" src/` returns nothing above the fold; `100dvh` used instead.
- [ ] **Mobile collapse**: declared per section, no horizontal scroll at 375.
- [ ] **Targets**: interactive elements at least 44px.
- [ ] **Images**: explicit dimensions, `loading="lazy"` below the fold, `priority` or `fetchpriority="high"` above it.
- [ ] **States**: loading, empty, error, disabled present.
- [ ] **Forms**: label above, error below, no placeholder-as-label, contrast checked.
- [ ] **Icons**: one family, one stroke width, no hand-drawn paths.
- [ ] **Copy self-audit**: every visible string re-read.
- [ ] **Bans**: the Forbidden list walked, item by item, out loud.
- [ ] **Arms match code**: palette, type, radius, and motion in `DESIGN.md` are the ones in the build.
- [ ] **Register**: the build reads as the register named in the arms, and bends it nowhere without a reason in writing.
- [ ] **Board**: the tile a human picked exists in the repo, and the build is recognizable as that same direction.
- [ ] **Motion motivated**: every animation justified in one sentence.

Any unchecked box is a blocker, not a nit. Do not hand over a page with five known fails and a promise. Fix them or name them.

---

## Out of scope

Say so out loud, point at the right tool, and apply only the parts of this skill that fit:

* Dense product UI, admin panels, enterprise dashboards: use the official system for that world (Fluent, Carbon, Material, Atlassian, Polaris), then apply this skill's craft rules where the system is silent.
* Data tables: TanStack Table or AG Grid.
* Multi-step forms and wizards: form-specific patterns.
* Code editors: Monaco or CodeMirror, with their own skinning.
* Native mobile: Apple HIG and Material directly.
* Realtime collaborative UI: presence and cursors are a different problem class.
* **Deciding what to build**: cuecards. **Implementing a decided slice**: oneslice. **Shipping everything in parallel**: lanes.

---

## Approval bar

Do not call an interface done until all of these hold:

* The read was stated, the register named, and the dials chosen, not defaulted.
* A board exists with a human's pick (or the skip was named out loud), and the build landed in the register the tile promised.
* `DESIGN.md` exists, is short, names roles and numbers, and matches the code.
* The pre-flight mechanical output is pasted and clean, or the fails are named as fails.
* The walk exists with fresh renders at 375 / 768 / 1440 in both themes, plus a reduced-motion and a keyboard pass, or it is honestly marked `unrendered`.
* The critique table from the last pass is committed.
* Zero em dashes in the interface. One accent. One radius system. One theme. One icon family.
* Every animation has a reason, and reduced motion collapses it.
* Every visible string was re-read.
* No product decision was made here, and no ADR was silently contradicted.
* A stranger could describe this interface's character in one sentence after ten seconds — if they cannot, it is still a default.

## It's working if

* The human can point at any screen and name what the product looks like without opening the code.
* Two screens built a week apart, by different agents, look like they belong to the same castle and the same register.
* Put the board beside the build and a stranger sees the same product — the tile was a promise, and the screen kept it.
* The things you changed this pass were the few things that mattered, and you stopped.
* The evidence in `docs/heraldry/` is something a stranger could check, and it would fail if you broke the interface tomorrow.
* Nobody had to ask "does this look okay?" because the walk already answered it.
