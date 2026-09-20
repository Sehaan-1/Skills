# Worked example: invoicing

A snapshot of the whole pipeline on one tiny effort: adding customer invoices to a small bookkeeping app.

Read in this order — each file is what the pipeline leaves at that moment:

1. [board.md](invoicing/board.md) — the parent issue cuecards created (the board)
2. [cards/001-who-owes-us.md](invoicing/cards/001-who-owes-us.md) — an ask card, closed
3. [cards/002-where-the-invoice-goes.md](invoicing/cards/002-where-the-invoice-goes.md) — a look card (real evidence), closed
4. [cards/003-does-the-app-take-the-money.md](invoicing/cards/003-does-the-app-take-the-money.md) — a scope ruling, closed as not-this-effort
5. [adr/0001-who-owes-us.md](invoicing/adr/0001-who-owes-us.md) — the durable record of card 001
6. [adr/0002-where-the-invoice-goes.md](invoicing/adr/0002-where-the-invoice-goes.md) — the durable record of card 002
7. [adr/0003-money-moves-outside-the-app.md](invoicing/adr/0003-money-moves-outside-the-app.md) — a "not this effort" ADR
8. [handoff.md](invoicing/handoff.md) — what cuecards wrote when the board was done
9. [map.md](invoicing/map.md) — what lanes committed before round 1

In a real repo these live elsewhere: the board and cards are GitHub issues, ADRs sit in `docs/adr/`, the handoff in `docs/cuecards/`, the map in `docs/lanes/`. The bodies below are the exact shapes from each SKILL.md — copy them as templates.

# Worked example: heraldry

The design side of the same effort. Heraldry produces three files; these are the exact shapes from its SKILL.md.

Read in this order:

1. [heraldry/board.md](heraldry/board.md) — three tiles cast for the same screen in three registers, the owner's pick quoted verbatim, why the other two lost, and the prompt that made the winner
2. [heraldry/DESIGN.md](heraldry/DESIGN.md) — the arms: the register and chosen board at the top, then dials, atmosphere, palette named by role, type, components, layout, motion, bans, and the agent prompt guide
3. [heraldry/critique.md](heraldry/critique.md) — one pass, one table, sorted by impact, plus what the pass deliberately did not touch
4. [heraldry/walk.md](heraldry/walk.md) — the proof: the build against the board tile, fresh renders at three widths in both themes, the pre-flight commands and their output, contrast values, and what could not be verified

In a real repo the arms are `DESIGN.md` at the project root, and the board, critique, and walk live in `docs/heraldry/`. Note how `critique.md` and `walk.md` carry their own admissions: the placeholder still missing, the device we could not test on, the `unrendered` claim. An honest gap is what makes the rest of the record worth reading.
