# Architectural Stress Testing

## 10. Stress — try to break your own shape

Attempt three violations. For each: show what you did, what caught it (paste the failure), and the fix. Restore the tree.

A violation that **nothing** catches is the best possible outcome of this exercise — it means you found a rule the record claimed and the build does not hold. Move that rule to `unenforced` in the record, say what it would take to enforce it, and add the crudest check that catches the obvious recurrence. Do not quietly leave it in the enforced column.

1. **Import a detail into the core.** Add one `import` from the persistence adapter into a domain type, or reference a framework type in an entity. Run the check. It must fail, and the failure must name the file.
2. **Reach across an aggregate.** Write a test or a function that loads an internal entity directly instead of traversing from its root, or that mutates two aggregates in one transaction. Run the check. It must fail.
3. **Cross a context without the layer.** Call the upstream system's shape from the downstream domain — bypass the anti-corruption layer or the published language. Run the check. It must fail.

Then two questions that no tool answers, and both must be answered in writing (they are the part of the stress test a future engineer will actually read):

- **What would make this shape wrong?** Name the change — a scale jump, a team split, a new consistency requirement, a new integration — and say which boundary it would move. If you cannot name one, you have not understood the forces.
- **What is the cost of being wrong?** If the answer is "a day in one package," the boundary was cheap and correctly drawn. If it is "a quarter and a data migration," say so now, while it is still a sentence and not a project.


---

## Stress Test Template

`markdown
# Stress Test: <system or subsystem name>
Tested against Architecture commit: <sha>

## Scenario 1: <Axis of Change>
- **Perturbation**: <What changes 10x or shifts fundamentally>
- **Blast Radius**: <Which contexts/modules are touched>
- **Broken Invariants**: <What contracts are strained>
- **Result**: PASS | WARN | FAIL

## Limits and Boundary Assessment
- **Throughput/Scale ceiling**: ...
- **Failure domains**: ...
`
