# Dials & Layout Guidelines

Every interface layout is controlled by three explicit dials (1–10). Never design from default habits.

## The Three Dials

* **`BOLDNESS` (1–10):** 1 = strict symmetric grid; 10 = aggressive asymmetry and editorial layouts.
* **`MOTION` (1–10):** 1 = static with basic `:hover`; 10 = continuous scroll-driven choreography and physics springs.
* **`DENSITY` (1–10):** 1 = expansive negative space; 10 = data-dense operational cockpit.

---

## Dial Calibration by Product Signal

| Brief Signal | Boldness | Motion | Density |
| --- | --- | --- | --- |
| "Minimal, calm, editorial, Linear-style" | 5–6 | 3–4 | 2–3 |
| "Premium consumer, luxury, Apple-style" | 7–8 | 5–7 | 3–4 |
| "Playful, experimental, agency showcase" | 9–10 | 8–10 | 3–4 |
| "Landing page, marketing portfolio" | 7–9 | 6–8 | 3–5 |
| "Product screen, dashboard, SaaS tool" | 3–5 | 3–5 | 5–8 |
| "Regulated, government, accessibility-critical" | 3–4 | 2–3 | 4–5 |

---

## What the Levels Mean

### Boldness
- **1–3:** Centered structures, equal padding, standard 12-column grids.
- **4–7:** Negative margin overlaps, varied aspect ratios, offset typographic headers.
- **8–10:** Asymmetrical grid tracks (`2fr 1fr 1fr`), dynamic white space zones.
- **Mobile Rule:** Any layout with Boldness $\ge 4$ must cleanly collapse to a strict single-column flow below `768px`.

### Motion
- **1–3:** Static layout; micro-transitions on `:hover` and `:active` only.
- **4–7:** Staggered load animations, state transitions using `transform` and `opacity` (<300ms).
- **8–10:** Scroll-linked reveals, layout morphing, spring physics.
- **Reduced Motion:** From level 4 up, `prefers-reduced-motion` media queries are mandatory.

### Density
- **1–3:** Large section gaps (`80px+`), generous internal margins.
- **4–7:** Standard web application spacing (`16px–24px` grid gaps).
- **8–10:** Compact table views (`<8px` padding), hairlines instead of bordered cards, all numbers rendered in tabular monospace font.
