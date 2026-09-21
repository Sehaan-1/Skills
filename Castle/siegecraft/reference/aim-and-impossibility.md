# Aim and the Impossibility Pass

# Aim

Read the ticket, every ADR it cites, the board's Notes and standing rules, the handoff slice if one exists, and any look-card proof it depends on. Then name the wall in one line:

> The wall: <what is too hard> under <the constraint that makes it hard>.

Fill in the shape of the problem before you scout:

- **What is decided** â€” ADRs by name, the destination, the slice Check.
- **The real n** â€” data sizes, rates, latencies, dimensions. From the ticket, the codebase, or measurement. Not from vibes.
- **The tolerance** â€” exact, or approximate within a stated bound? "Fast enough" is not a tolerance; a number is.
- **The environment** â€” memory, single machine or distributed, latency budget, determinism requirements, what language the builder will cut.
- **What "solved" looks like** â€” the walk and proof this engine must eventually survive.

If you cannot name the wall, the ticket is still fuzzy. Back to cuecards â€” say so out loud.

---


---

# Aim again (the impossibility pass)

Before designing anything, spend five minutes trying to dissolve the wall. The hardest-engineered solution to a mis-stated problem is still the wrong answer.

1. **Is there an easier way?** Does the task secretly not need this? Is a dumber engine, run at a different time, indistinguishable at the real n?
2. **Question the premise.** Try each constraint on for size. Is n really 10^7 â€” measured, or assumed? Is exactness really required, or is a stated error bound acceptable? Is the deadline real? Is the data actually adversarial, or just big?
3. **Dig under the ticket.** The stated method is often one dig too shallow. What is the ticket *for*? Would a reformulation â€” different coordinates, precompute once and amortize, stream instead of batch, trade memory for time â€” serve the same need for a tenth of the engine?
4. **Renegotiate the shape, not the destination.** If one line changed in the ticket collapses the wall â€” a tolerance, a precompute step, a weaker guarantee that nobody would notice â€” that is a *decision*. Take it back to the board as a cuecards card with your recommendation. Do not silently weaken what was decided.

The pass ends one of two ways: **the wall stands** (proceed to design), or **the wall moves** (back to the board, with a card). Say which, out loud.

---

