
> [!IMPORTANT]
> **The walk has to be able to fail.**
> If a broken layout, a contrast failure, a missing focus ring, or an overflowing hero would still produce a green walk record, the walk is a slideshow, not a check. Strengthen it.
> If you cannot render in the current environment, record unrendered honestly with the list of unverified checks. Never fabricate a pass.


# Visual Verification Walk Protocol

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

If you cannot render, write `unrendered` and list what you could not check â€” that is a legitimate, honest record. Claiming a walk you did not run is fabrication, and it is worse than an admitted gap.

---


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
* A stranger could describe this interface's character in one sentence after ten seconds â€” if they cannot, it is still a default.

## It's working if

* The human can point at any screen and name what the product looks like without opening the code.
* Two screens built a week apart, by different agents, look like they belong to the same castle and the same register.
* Put the board beside the build and a stranger sees the same product â€” the tile was a promise, and the screen kept it.
* The things you changed this pass were the few things that mattered, and you stopped.
* The evidence in `docs/heraldry/` is something a stranger could check, and it would fail if you broke the interface tomorrow.
* Nobody had to ask "does this look okay?" because the walk already answered it.
 something a stranger could check, and it would fail if you broke the interface tomorrow.
* Nobody had to ask "does this look okay?" because the walk already answered it.
