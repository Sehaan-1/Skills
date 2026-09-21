# Pre-Flight Checklist & Forbidden Anti-Patterns

Before approving an interface design or submitting changes, verify that the code passes both the anti-pattern audit and the mechanical checks.

## Forbidden Anti-Patterns (The Tells)

These generic patterns signal uninspired, AI-templated design and are strictly forbidden:

- [ ] **Purple gradient mesh:** Neon purple or indigo radial glows behind a centered dark hero.
- [ ] **The "Three Cards" trap:** Three identical rounded cards with centered icons, a title, and a paragraph.
- [ ] **Decorative floating elements:** Unmotivated floating geometric shapes, 3D blobs, or abstract icons.
- [ ] **Fake product shots:** Generic code editors, fake dashboards, or placeholder rectangles pretending to be real product previews.
- [ ] **Marketing boilerplate:** Vague claims like "Supercharge your workflow" or "Next-generation platform".
- [ ] **Uniform border radii:** Applying `16px` or `24px` radius to every button, tag, card, and image without hierarchy.
- [ ] **Unmotivated micro-animations:** Infinite floating loops, spinning gradient borders, or distracting hover bounces.

---

## Mechanical Pre-Flight Verification

Execute and paste actual command outputs:

1. **Focus Rings:** Ensure every interactive element has a visible `:focus-visible` outline matching the accent token.
2. **Contrast Arithmetic:**
   - Body text against background $\ge 4.5:1$
   - Large headings $\ge 3.0:1$
   - Form field borders and icons $\ge 3.0:1$
3. **Touch Targets:** Verify buttons and interactive targets are at least `44px × 44px` on touch screens.
4. **Reduced Motion:** Ensure all animations are enclosed in `@media (prefers-reduced-motion: no-preference)`.
5. **Horizontal Overflow:** Verify zero horizontal scrollbar on mobile viewport (`375px`).
