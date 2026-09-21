# Destination Verification & Approval Bar

Shipping a complete destination requires proving that all integrated workstreams function together end-to-end.

## The Destination Check

The destination check is defined in the initial handoff and locked on the map:

- **End-to-end user scenario:** A complete functional path traversing all integrated workstreams (e.g., user creates an invoice, sends it, webhook receives payment, ledger balance reconciles).
- **Proof artifact:** Saved terminal transcript, test runner report, or screenshot evidence committed to `docs/lanes/proof-<slug>.md`.
- **Automated enforcement:** An integration test or CI suite wired to fail if the end-to-end scenario regresses.

---

## Approval Bar

Do not mark the destination shipped until every item is verified:

- [ ] All workstream branches merged cleanly into `lanes/<slug>`
- [ ] No file or module ownership collisions occurred
- [ ] Shared contracts were honored by all consumers without local monkey-patches
- [ ] Full project test suite and type check are green
- [ ] End-to-end destination scenario executed and passed
- [ ] Map updated at `docs/lanes/map-<slug>.md` with final status and metrics
- [ ] No unaddressed out-of-scope creep introduced
