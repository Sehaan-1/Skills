# Provenance & Verification Gates

Claims without artifacts are red flags. The building agent cannot self-certify completion merely by asserting that a check passed.

## Research Artifact Gate

When a slice depends on external APIs, documentation, or specifications outside the repository:

1. The research artifact (Markdown file citing primary sources) must be committed to the branch **before or in the same commit** as the code that depends on it.
2. A commit message stating "research TBD" or "will verify later" is a defect.
3. The research file path must appear in the GitHub issue comment that records the increment.

---

## Reproducible Check Artifact Gate

When setting ticket status to `Check passed`, you must provide:

- The specific **commit SHA** the Check ran against.
- Either:
  - A CI run URL demonstrating passing status, **or**
  - A timestamped terminal transcript showing the check command and its exact output, saved at `docs/research/<slice-slug>-check.md`.

"I ran it and it passed" with no linked artifact remains `In progress`. If automated CI is not yet configured for this slice, commit the terminal transcript before updating the ticket.
