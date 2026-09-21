# Color & Typographic Tokens

A complete design system defines color by functional role rather than appearance, and enforces a deliberate typographic scale.

## Role-Based Color Palette

Define each color token by what it does:

- **Paper:** Base application background (e.g. `#F7F6F3` or `#0F1012`). Never pure `#FFFFFF` or `#000000`.
- **Surface:** Elevated component backgrounds, cards, and modal sheets (e.g. `#FFFFFF` or `#18191B`).
- **Ink:** Primary text color with strong contrast against Paper/Surface (e.g. `#1B1A18`).
- **Slate:** Muted secondary text, metadata labels, and timestamps (e.g. `#6B6A66`).
- **Hairline:** Structural 1px division lines (`rgba(27,26,24,0.1)`). Avoid heavy borders.
- **Accent:** The single primary brand color for active states, primary CTA, and focus outlines.
- **Semantic:** Success, Warning, Error indicators. Saturated solely for state alerts, never as general decoration.

### Color Rules
1. **One accent color:** Do not combine multiple unrelated vibrant accents in one view.
2. **Desaturate neutrals:** Keep background and text saturation low to maintain readability.
3. **Tint shadows:** Avoid pure black `#000000` drop shadows. Tint drop shadows with a fraction of the background hue.
4. **WCAG Contrast:** 
   - Minimum 4.5:1 contrast for regular text.
   - Minimum 3:1 for large text (18pt+) and interactive boundaries.
5. **Dark & Light parity:** Ensure hierarchy is consistent across both themes.

---

## Typography Rules

- **Display Face:** Used for main page headers (`h1`, `h2`). Set with tight line-height and fluid scaling (`clamp()`).
- **Body Face:** Clean, highly legible sans or serif for reading paragraphs. Constrain paragraph widths to maximum `65ch`.
- **Monospace Face:** Dedicated to tabular numerals, transaction IDs, code blocks, and financial figures.
- **Serif restraint:** Use serifs only when explicitly part of the brand voice (editorial, luxury, legal). Do not reach for decorative serif as a generic flavor.
