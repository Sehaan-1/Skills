# Boundary Enforcement & Fitness Functions

An architectural rule that cannot fail a build is only a suggestion. Every structural rule must be verified mechanically by automated checks wired to CI.

## Automated Fitness Functions

Adapt to the project's stack:

| Rule | Enforcement Tool |
| --- | --- |
| **No circular dependencies** in module graph | `dependency-cruiser` (JS/TS), `ArchUnit` (JVM), `import-linter` (Python), `madge`, `cargo-deny` |
| **Core domain does not import infrastructure** | Linter rules (`no-restricted-imports`), ArchUnit boundary rules |
| **Pure domain logic runs without I/O** | Isolated test target running in environment without network/database |
| **No framework annotations on core entities** | AST lint rules or structural grep checks |
| **Only aggregate roots have repositories** | Path-based structural check |
| **Restricted public API surface** | TypeScript project references, package export maps (`exports`), Go internal packages |

---

## Ports & Adapters Architecture

The upstream (core) defines the port interface; the downstream (infrastructure) implements it.

```text
[Core Business Rules] ──(defines)──▶ (Port Interface)
                                             ▲
                                             │ (implements)
[Infrastructure Layer] ──────────────────────┘
```

1. **Persistence Port:** Named in domain language (`Orders`, not `OrdersRepository`). Core calls it; adapter implements database operations.
2. **Presenter / Output Port:** Use case produces plain data structures; presenter adapter handles display and serialization.
3. **External Service Port:** Isolates third-party APIs behind an intention-revealing contract.
4. **Event Publisher Port:** Core publishes domain events; infrastructure adapter dispatches across message brokers.

---

## The Humble Object Pattern

Where behavior is difficult to test (GUIs, raw sockets, database drivers, framework lifecycles), extract all logic into testable pure objects, leaving the difficult part "humble" — thin, procedural glue with minimal decision logic.

`main` is the primary humble object of the system. It initializes factories, reads environment config, wires dependencies, and injects adapters into the domain before handing execution to high-level policy.
