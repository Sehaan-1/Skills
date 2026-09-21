# License compatibility guide

You are not a lawyer and the report should never read like legal advice — but you *can* reliably flag the common, well-understood combinations and tell the user when to check with legal. The question is always two-sided: **what license is the SDK under, and what is the user's project?**

## SDK license families

| Family | Examples | What it means for users |
|---|---|---|
| Permissive | MIT, BSD-2/3-Clause, ISC, Zlib, Unlicense, CC0 | Do almost anything; keep attribution. Safest for commercial/closed source. |
| Permissive + patents | Apache-2.0 | Like MIT plus an explicit patent grant (a plus for companies). Note: Apache-2.0 is **incompatible with GPL-2.0-only** (fine with GPL-3.0). |
| Weak copyleft | LGPL-2.1/3.0, MPL-2.0, EPL-2.0, CDDL | Changes *to the library itself* must be shared. Proprietary apps can usually still use it: LGPL via dynamic linking (or providing relinkable objects), MPL at file granularity. |
| Strong copyleft | GPL-2.0/3.0 | Derivative works must be GPL too. Incompatible with closed-source *distribution*. Fine if the user's project is itself GPL-compatible open source. |
| Network copyleft | AGPL-3.0 | GPL plus: serving it over a network counts as distribution. Modifications used in a SaaS must be released. Often a dealbreaker for commercial SaaS. |
| Dual-licensed | e.g., "AGPL or commercial license" | The free side is listed first; a paid license may remove copyleft. Note both sides. |
| Unknown / custom | "Proprietary", missing LICENSE, bespoke text | Treat as a risk. Do not assume permissive. Flag for verification. |

## Compatibility matrix (SDK license ↓ × project type →)

| SDK license | Closed-source / commercial | MIT/BSD/Apache OSS | GPL OSS | SaaS (no distribution) |
|---|---|---|---|---|
| MIT/BSD/ISC | ✅ | ✅ | ✅ | ✅ |
| Apache-2.0 | ✅ | ✅ | ✅ (⚠️ GPL-2.0-only conflict) | ✅ |
| LGPL | ⚠️ dynamic linking + relinkability | ✅ | ✅ | ✅ |
| MPL-2.0 | ⚠️ file-level copyleft | ✅ | ✅ | ✅ |
| GPL-2/3 | ❌ | ❌ (for MIT/Apache projects — copyleft spreads) | ✅ | ⚠️ only if unmodified and not combined |
| AGPL-3.0 | ❌ | ❌ | ✅ | ❌ if modified (release source or buy commercial license) |
| Unknown | ❌ until verified | ⚠️ | ⚠️ | ⚠️ |

✅ fine · ⚠️ usable with conditions worth documenting · ❌ effectively incompatible

## Practical rules for the report

1. **Incompatibility is a hard gate**, not a score deduction: a GPL SDK is not "the top pick with a caveat" for a closed-source product — it's disqualified, with the reason stated plainly.
2. **State the exact SPDX identifier** from live data when you have it (`MIT`, `Apache-2.0`), and note when it came from the registry vs. memory.
3. **Flag transitive risk briefly** — an MIT SDK wrapping a GPL native library inherits the problem (rare, but it happens; e.g., some bindings around GPL engines).
4. **Dual licensing is an opportunity, not a blocker** — mention the commercial-license option when it exists.
5. **When in doubt, escalate**: "the license field says X but the repo header says Y — have legal confirm before shipping." Users trust the report; license mistakes are the most expensive kind.
6. **User's project license unknown**: assume permissive/commercial (the common case) but list it as an assumption — and if the leading candidate is copyleft, that's one of the rare cases worth asking before recommending.
