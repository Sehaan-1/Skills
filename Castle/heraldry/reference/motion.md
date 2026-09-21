# Motion engineering

> Reference for [heraldry](../SKILL.md). The short form lives in the skill file; this is
> the full how-it-moves, how-it-costs, and canonical-patterns material. Load it when a
> pass actually ships motion above level 3.

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

