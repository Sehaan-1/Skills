# Color System and Typography

## Color System and Palette

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

## Typography System

* **Hierarchy comes from weight, color, and spacing before size.** A page where every headline is enormous has no hierarchy at all.
* **Display**: tight tracking, compressed leading, `clamp()` scale. Body: 65 characters per line, relaxed leading, never below 1rem on mobile.
* **Inter is not the default.** Reach for Geist, Satoshi, Cabinet Grotesk, Outfit, or a brand face first. The override is real: Inter is fine when the brief is explicitly neutral, trust-first, or accessibility-first, and you say so.
* **Serif discipline.** "Creative, so serif" is the most-tested tell there is. The default is a sans display. A serif is allowed when the brand names one, or the family is genuinely editorial, luxury, publication, or heritage, and you can say why *this* serif fits *this* product — and in dashboards and software UI that bar is deliberately high, because serif-as-flavor is the tell. Banned as *unchosen defaults*: Fraunces, Instrument Serif, and the stand-ins (Times, Georgia, Garamond, Palatino). If one of those is genuinely the right face for this brand, say so in the design system (DESIGN.md) and ship it on purpose; never reach for it as a reflex.
* **Emphasis inside a headline uses the same family**: italic or bold, never a random serif word dropped into a sans line.
* **Italic descenders need room.** If an italic display word contains `y g j p q`, leading below 1.1 clips it. Reserve the space.
* **Numbers behave.** `tabular-nums` in any column that gets compared. At density above 7, all numbers are mono.
* **Real typography, not substitutions.** Curly quotes, `…` instead of `...`, non-breaking spaces in units and shortcuts, `text-wrap: balance` on headings.
* **Load fonts properly.** Self-host or `next/font`, `font-display: swap`, preload the critical face. Never a bare Google Fonts `<link>` in production.

---

