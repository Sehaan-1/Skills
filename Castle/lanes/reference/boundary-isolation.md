# Workstream Isolation & Shared Contracts

Parallel execution requires strict boundaries between workstreams to prevent file collisions, conflicting data models, and integration deadlock.

## Workstream Boundary Rules

1. **Partition by module ownership:** Group handoff slices so each workstream owns a cohesive set of files and directory trees.
2. **Disjoint file sets:** Two parallel workstreams must not write to the same files in the same round. If two tasks must touch the same surface, either serialize them or extract a shared contract.
3. **Single contract ownership:** Every shared interface contract is owned by exactly one workstream. Other streams consume it. A shared interface with two writers creates immediate divergence.

---

## Defining Shared Contracts

When workstreams must interact, define the shared contract in the repository **before** parallel implementation begins:

- **Types and schemas first:** Commit TypeScript types, OpenAPI specs, GraphQL schemas, or protobuf definitions to the branch.
- **Mock implementations / fixtures:** Provide static mock responses or test fixtures so consumers can develop and test without waiting for the provider's backend to land.
- **Additive changes only:** New fields must be optional; existing types and behavior must not change during the round.
- **Strict single versioning:** Do not allow parallel streams to introduce competing `v1` and `v2` endpoints.

---

## Contract Divergence Protocol

If an interface contract proves insufficient during implementation:

1. **Pause consuming workstreams:** Do not allow the consumer to "just adapt" with ad-hoc workarounds.
2. **Update the contract in provider workstream:** Commit updated types and fixtures.
3. **Resume parallel work:** Consuming workstreams update against the new contract.
