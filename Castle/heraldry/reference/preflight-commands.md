# Mechanical Pre-Flight Commands

## Pre-flight (mechanical, paste the output)

Run this before you say anything is done. The mechanical ones have real commands; adapt them to the stack, and paste what they return.

- [ ] **Em dash sweep**: `grep -rn "â€”" src/` returns nothing in product-authored copy; visual check the rendered copy block too.
- [ ] **En dash sweep**: `grep -rn "â€“" src/` â€” every hit must be a numeric range (`2018â€“2026`); any other hit is a fail.
- [ ] **Label count**: small-caps labels above headings, at most one per three sections.
- [ ] **Accent count**: exactly one accent value across the whole surface.
- [ ] **Radius count**: matches the design system (DESIGN.md)' documented system, nothing off-scale.
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
- [ ] **Register**: the build reads as the register named in the design system (DESIGN.md), and bends it nowhere without a reason in writing.
- [ ] **Board**: the tile a human picked exists in the repo, and the build is recognizable as that same direction.
- [ ] **Motion motivated**: every animation justified in one sentence.

Any unchecked box is a blocker, not a nit. Do not hand over a page with five known fails and a promise. Fix them or name them.

---

