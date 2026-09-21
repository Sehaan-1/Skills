# Layout, Components, Copy, and Assets

## Layout and Component System

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


---

## Real assets

Two different jobs, often confused. **Tiles** (above) choose a direction before anything is built. **Assets** fill the interface once the direction is set: photography, product shots, textures, logos. Same tools, different purpose; a board is not a substitute for the imagery inside the product.

Priority order for assets, and do not skip to the bottom because the top is slower:

1. **Generate it.** If an image tool exists in this environment, use it for hero photography, product shots, textures, and section-specific imagery at the right aspect ratio.
2. **Use a real image.** A brand asset, a real screenshot, or a seeded placeholder (`https://picsum.photos/seed/<descriptive-seed>/1600/1200`) with a seed that describes the section.
3. **Label the hole and say so.** `<!-- TODO: hero product photo, 1600x1200 -->` plus a closing sentence: *"This page needs real images at these three placements; supply or generate them."* Never fill the hole with invented decoration.

**A text-only page is not minimalism â€” it is unfinished.** Even a restrained editorial page needs two or three real images.

**Logo walls**: real SVG brand marks from a public logo set, or a generated monogram when the brand is invented. Logos only, no category labels under them. Legible in both themes.

---

