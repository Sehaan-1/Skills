# Shared Contracts Between Lanes

# shared contracts

shared contracts are how parallel workstreams stay honest.

- Write the contract in the repo (types, schema, event shape, fixture) **before** both implement. Oneslice interface rules apply: one error shape, validate at the edge, additive fields, idempotency honoured if you accept a key.
- One owner. Everyone else consumes. A seam with two writers is not a seam.
- Version is "one version." Do not let Lane A ship `v1` and Lane B ship `v2` of the same call "for now."
- If implementing the contract would change a product decision, stop â€” cuecards.
- When a seam must change after both sides have started: **stop both lanes**, update the contract, unstick the map, then continue. Do not let one side "just adapt."
- shared contracts are also how you cut latency: a written contract is what lets two agents start instead of waiting on each other.

---

