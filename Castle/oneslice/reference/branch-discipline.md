# Branch Discipline & Git Hygiene

The default branch (`main`) must remain deployable at all times. All slice implementation happens on short-lived branches with atomic commits.

## Branch Workflow

1. Create a short-lived branch off `main`:
   ```bash
   git checkout -b feature/<slice-slug>
   # or
   git checkout -b fix/<slice-slug>
   ```
2. Keep branches focused: merge in days, not weeks.
3. If an increment must be deployed before the whole slice is user-visible, guard it behind a feature flag rather than letting a branch stagnate.

---

## Thin Vertical Increments

Inside a slice, implement in small vertical steps (DB + API + minimal UI) rather than wide horizontal layers:

```text
Implement ──→ Test ──→ Verify ──→ Commit ──→ Next increment
```

- **Simplest working code:** Three explicit lines beat premature abstractions. Abstract on the third real use, not the first.
- **One logical change per increment:** Do not mix a new endpoint, an architectural refactor, and dependency bumps in one commit.
- **Keep it compilable:** Never leave the test suite or build broken between increments.
- **Save-point pattern:** Increment passes tests → commit → continue. Increment fails → revert to last commit → investigate. You never lose more than one small step.

---

## Atomic Commits

Aim for ~100 lines per commit (up to ~300 lines for a cohesive logical change). If a change approaches 1000 lines, split into smaller steps.

### Commit message format

```text
<type>: <short description>

<why, not what. Reference the slice and ADR-NNNN if applicable.>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`.

### Pre-commit checklist

1. Run `git diff --staged` to verify exactly what is staged.
2. Scan staged changes for secrets or tokens (`api_key`, `token`, `password`).
3. Run the project's tests, linter, and type checker.
4. Verify `.gitignore` rules prevent committing `node_modules/`, `.env`, or build artifacts.

---

## Progress Updates

After each increment, note:
- **Changes made:** files touched and rationale.
- **Things left untouched:** nearby mess intentionally left for later scope.
- **Open concerns:** any assumption that needs human confirmation.

---

## Releases & Worktrees

- **Releases:** Semantic versioning (`MAJOR.MINOR.PATCH`). Tags are the source of truth; changelogs describe user impact, not raw `git log` dumps.
- **Worktrees:** Git worktrees are permitted when parallel tasks must avoid interfering with a shared working tree.
