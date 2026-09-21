# Git Branching & Merge Discipline

Parallel streams must coordinate git branches to prevent merge conflicts and maintain deployable integrity.

## Branch Topology

```text
main (default branch)
  └── lanes/<slug> (coordination integration branch)
        ├── lane/a-<slug> (workstream A)
        ├── lane/b-<slug> (workstream B)
        └── lane/c-<slug> (workstream C)
```

1. **Integration Branch (`lanes/<slug>`):** Branched off `main` at the start of the session. All parallel workstreams merge into this branch during rounds.
2. **Workstream Feature Branches (`lane/<letter>-<slug>`):** Isolated short-lived branches branched off `lanes/<slug>`.

---

## Merge Protocol

- **Dependency Order:** Merge upstream provider workstreams (shared contracts, core schemas) before merging dependent consumer workstreams.
- **Rebase before merge:** Individual workstreams rebase against `lanes/<slug>` before integrating to ensure clean fast-forward or non-conflicting merge commits.
- **Run verification test on integration:** Execute project test suites and linter on `lanes/<slug>` after every workstream merge.
- **Final PR to main:** When the destination Check passes on `lanes/<slug>`, open a single consolidated pull request to `main`.
