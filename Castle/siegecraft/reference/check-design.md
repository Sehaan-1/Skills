# Algorithmic Check Design & Ticket Splitting

Complex algorithmic tasks must be decomposed into independently verifiable units, each with a test that can genuinely fail.

## Designing Tests That Can Fail

A check that passes on a broken or naive implementation is defective. Algorithmic checks must include:

1. **Known analytical solutions:** Test cases whose expected outcomes are verified mathematically from primary sources.
2. **Boundary stress cases:** Testing zero, negative, maximum integer, empty collections, and extreme floating-point scales ($10^{-9}$ to $10^9$).
3. **Counter-examples:** Test scenarios where naive or heuristic approaches produce incorrect outputs.
4. **Benchmark thresholds:** Latency or memory ceilings measured in execution environments.

---

## Splitting Complex Algorithmic Tickets

Split large algorithmic tickets into discrete child tickets:

```markdown
## Algorithm Ticket N of M: <Spoken Name>

### What this ticket does
<Specific phase of the algorithm: data preparation, core computation, or post-processing>

### Contract Inherited
- Implements: [docs/siegecraft/<slug>-spec.md](docs/siegecraft/<slug>-spec.md)
- Invariants guaranteed: <Pre- and post-conditions>

### Check
- Command: `npm test tests/algo-part-N.test.ts`
- Expected behavior: Confirms invariant under edge cases.
```

---

## Approval Bar

Before marking an algorithm specification or split tickets ready for implementation:

- [ ] All primary claims backed by citations in `docs/research/<slug>-dossier.md`
- [ ] Correctness argument includes explicit invariants and termination logic
- [ ] Time and space complexities formally stated in Big-O notation
- [ ] Numerical precision limits and overflow risks documented
- [ ] Checks include tests capable of catching naive or incorrect implementations
