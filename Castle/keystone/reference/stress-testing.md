# Architecture Stress Testing

A boundary that has not been actively broken in a test is not an enforced boundary. Before marking an architecture record complete, execute three deliberate structural violations and verify that the fitness functions fail the build.

## Stress Protocol: Three Deliberate Violations

1. **Import infrastructure into domain core:**
   - Add an import from a database driver or web framework into an entity or use case.
   - Run the architectural check.
   - Verify the command fails and names the violating file.
2. **Bypass aggregate boundary:**
   - Directly query an internal entity without traversing its aggregate root, or mutate two aggregates in a single synchronous transaction.
   - Verify the check or domain test fails.
3. **Bypass anti-corruption layer:**
   - Directly use an external third-party model inside the domain without translation.
   - Verify the boundary check fails.

If an attempted violation is **not** caught by any check, mark that rule as `unenforced` in the record and implement an automated check before marking the architecture complete.

---

## Stress Test Record Template

Save at `docs/architecture/<slug>-stress.md`:

```markdown
# Stress Test: <Architecture Slug>

## Provenance
- Target record: [<slug>.md](<slug>.md)
- Commit evaluated: <SHA>
- Date: YYYY-MM-DD

## Attempted Violations

### 1. Inward Infrastructure Leak
- **Action:** Added import of database driver in `core/order.ts`.
- **Command:** `npm run test:arch`
- **Output:** `Error: Forbidden dependency 'infrastructure/db' in 'core/order.ts'`
- **Result:** Caught. Change reverted.

### 2. Direct Aggregate Mutation
- **Action:** Mutated line items without traversing order root.
- **Command:** `npm test`
- **Output:** `InconsistentAggregateStateError`
- **Result:** Caught. Change reverted.

### 3. Direct Upstream Integration
- **Action:** Injected payment vendor schema directly into domain use case.
- **Command:** `npm run lint:deps`
- **Output:** `Failed: Boundary violation`
- **Result:** Caught. Change reverted.

## Structural Limits
- **What force would make this architecture wrong?** <e.g., transition from single tenant to multi-region distributed transactions>
- **Estimated cost to refactor if that occurs:** <honest estimate>
```
