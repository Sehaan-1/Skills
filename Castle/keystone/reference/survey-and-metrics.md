# Architectural Survey & Coupling Metrics

Estimate structure from observable evidence in code and change logs, not aspirational diagrams.

## Six Survey Inputs

1. **Domain vocabulary:** Gather nouns and verbs domain experts use and correct you on.
2. **System forces:** Team topology, deploy cadences, consistency bounds, latency budgets, compliance.
3. **Existing dependencies:** Run analyzers to count cycles and map existing package graphs.
4. **Change log clusters:** Review the last 20 non-trivial changes to identify true coupling.
5. **Pain points:** Identify slow test suites, high-risk deploys, or frequent regression areas.
6. **Ownership boundaries:** Map team knowledge and module ownership.

---

## Component Coupling Metrics

For each component or package, calculate:

- **Fan-in ($C_a$):** Number of incoming dependencies from outside the component.
- **Fan-out ($C_e$):** Number of outgoing dependencies to outside the component.
- **Instability ($I$):** 
  $$I = \frac{C_e}{C_a + C_e}$$
  Range: $0$ (maximally stable, difficult to change) to $1$ (maximally unstable, easy to change).
- **Abstractness ($A$):** 
  $$A = \frac{N_a}{N_c}$$
  ($N_a$ = abstract classes/interfaces, $N_c$ = total types). Range: $0$ (completely concrete) to $1$ (completely abstract).
- **Distance from Main Sequence ($D$):** 
  $$D = |A + I - 1|$$
  Measures balance between stability and abstractness. Lower is better ($0$ sits on the optimal line).

### Characteristic Zones

- **Zone of Pain ($I=0, A=0$):** Concrete and stable. Highly rigid and painful to change (e.g. core database schema).
- **Zone of Uselessness ($I=1, A=1$):** Abstract and unused. Unnecessary speculative interfaces.
- **The Main Sequence:** The healthy diagonal between $(1, 0)$ and $(0, 1)$.

---

## Architecture Smells & Remedies

| Smell | Root Cause | Structural Remedy |
| --- | --- | --- |
| Every change touches multiple packages | Packaging by layer without component encapsulation | Package by component or aggregate root |
| Cannot test domain without DB or HTTP | High-level business logic imports infrastructure | Invert dependency: domain defines port, infrastructure implements it |
| Circular dependencies across modules | Blurry boundary or missing intermediate abstraction | Extract shared contract or invert one dependency direction |
| Model terms have conflicting meanings | Single model forced across multiple distinct contexts | Split into bounded contexts with an Anti-Corruption Layer |
