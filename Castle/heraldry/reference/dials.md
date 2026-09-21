# The Three Dials: Boldness, Motion, Density

## The three dials

Set all three. Every layout, motion, and density decision below is gated by them. Never invent aliases; use these names.

* **`BOLDNESS`** â€” 1 = perfect symmetry, 10 = artsy chaos.
* **`MOTION`** â€” 1 = static, 10 = cinematic physics.
* **`DENSITY`** â€” 1 = art gallery, 10 = cockpit.

There is no fixed default. The table below is the baseline: find the brief's row, take its numbers, adjust with a stated reason. If the brief matches no row, take the product/tool row â€” the most common thing agents are asked to build â€” and say you did. Numbers from habit are how every product ends up at the same three settings.

### Reading the dials off the brief

| Signal | Boldness | Motion | Density |
| --- | --- | --- | --- |
| "minimal / calm / clean / editorial / Linear-style" | 5-6 | 3-4 | 2-3 |
| "premium consumer / Apple-y / luxury / brand" | 7-8 | 5-7 | 3-4 |
| "playful / wild / experimental / agency / showcase" | 9-10 | 8-10 | 3-4 |
| "landing page / portfolio / marketing" | 7-9 | 6-8 | 3-5 |
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

