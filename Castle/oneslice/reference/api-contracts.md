# API & Interface Contracts

If the slice designs or changes an API, module boundary, component props, schema, or frontend/backend contract: write the contract **before** implementation.

## Principles

- **Contract first.** Typed input (what the caller sends) vs output (including server-generated fields). Discriminated unions for variants. Branded IDs so a `UserId` is not interchangeable with a `TaskId`. Types are the specification.
- **Hyrum's Law.** Every observable behavior is a potential commitment. Do not leak internal data structures or error details. Plan deprecation paths when adding features, not after regrets arise.
- **One version.** Extend cleanly; do not fork a second API endpoint "temporarily."
- **One error shape everywhere.** Do not mix thrown exceptions, `null`, and `{ error }`. For REST, use consistent body format (`code` + `message` + optional `details`):
  - `400`: Invalid format / bad syntax
  - `401`: Unauthenticated
  - `403`: Forbidden / unauthorized
  - `404`: Missing resource
  - `409`: State conflict
  - `422`: Semantically invalid entity
  - `500`: Server failure (never leak internals or stack traces)
- **Validate at the edge.** Validate at HTTP inputs, forms, environment variables, and especially **third-party responses**. Trust internal layers that already conform to the contract. Avoid repetitive defensive validation between trusted internal functions.
- **Additive changes only.** Add optional fields. Do not alter existing types or delete fields in minor updates.
- **Naming standards.** REST paths: plural nouns, no verbs (`GET /api/tasks`, not `/api/createTask`). JSON fields: `camelCase`; booleans prefixed with `is`/`has`/`can`; enums: `UPPER_SNAKE_CASE`. Use `PATCH` for partial updates; use `PUT` only when the client provides the complete resource. Paginate list endpoints from the start (`data` + `pagination`).
- **Idempotency.** Accepting a key is not the same as honouring it:
  - Client supplies the idempotency key, stable across retries of one intent.
  - Claim the key **atomically** (e.g. database unique constraint, not check-then-act).
  - Same key with a different request payload must fail loudly (`422`).
  - In-flight duplicate requests return a deliberate `409 Conflict`, `202 Accepted`, or wait.
  - Key retention must outlive the longest potential retry loop (including dead-letter queues).
  - Timeouts represent an **unknown** state, not a failure.
  - State-changing endpoints either honour idempotency or are explicitly marked unsafe to retry.

If a contract change would break an ADR or external consumer, stop — escalate to cuecards or plan an explicit major version upgrade.
