# Security & Trust Boundaries

If the slice handles user input, authentication, sessions, PII, payment flows, file uploads, webhooks, external APIs, or LLM output: conduct a five-minute threat model before implementing.

## Five-Minute Threat Model

Identify:
1. **Trust boundaries** (trust follows who *wrote* the value, not who passes it along).
2. **Assets** (tokens, customer records, database integrity, file storage).
3. **STRIDE** risks (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).
4. At least one explicit **abuse case** alongside the normal use case.

If you cannot clearly name the trust boundaries, do not begin coding.

---

## Core Rules

### Always
- Validate and sanitize input at the boundary.
- Parameterize database queries (no string interpolation into SQL).
- Encode output to prevent XSS.
- Enforce HTTPS and transport security.
- Hash passwords using modern key-derivation algorithms (bcrypt, scrypt, argon2).
- Configure strict security headers.
- Set `httpOnly`, `secure`, and `sameSite` flags on authentication cookies.
- Audit dependency lockfiles before release.

### Ask the human first
- Creating or changing authentication/authorization mechanisms.
- Storing new PII, credit cards, or financial details.
- Adding third-party external integrations or OAuth scopes.
- Relaxing CORS policies.
- Adding file upload endpoints.
- Modifying rate-limiting or firewall thresholds.
- Introducing elevated administrative privileges.

### Never
- Never commit or log secrets, API keys, or plaintext passwords.
- Never rely solely on client-side validation as the security boundary.
- Never use `eval` or unsafe HTML rendering (`innerHTML`, `dangerouslySetInnerHTML`) with untrusted data.
- Never store session secrets or authentication tokens in `localStorage`.
- Never expose stack traces or raw database error messages to end-users.
- Never fetch user-supplied URLs without an explicit domain allowlist (SSRF prevention).
- Never treat raw LLM output as a verified command or trusted SQL/shell input.

---

## Key Scenarios

- **Authorization vs Authentication:** Authenticating who a caller is does not authorize them to act on *this specific resource*. Always verify resource-level tenancy/ownership.
- **Rate limiting:** Rate-limit authentication endpoints using a shared cache/store if multiple process instances handle traffic.
- **PII compliance:** Collect data only against a stated purpose; ensure complete deletion mechanisms exist.
- **LLM security:** LLM output is untrusted input. Do not inject sensitive credentials into context prompts. Require human verification for destructive tool invocations.
- **Filesystem & Path Traversal:** When a file path is derived from user input, resolve symlinks and verify the final canonical path is inside an allowlisted root directory before reading or writing.
- **Secret leaks:** If a secret is pushed to any remote repository, **rotate the credential immediately**, then purge git history. Simply removing the line in a subsequent commit does not mitigate the leak.
