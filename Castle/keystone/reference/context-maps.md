# Context-map patterns

> Reference for [keystone](../SKILL.md). One pattern per pair of touching contexts —
> named, out loud, in the record. Unnamed relationships are where integrations rot.

| Pattern | Use when | It costs | It breaks when |
| --- | --- | --- | --- |
| **Shared kernel** | Two teams agree to share a small, carefully chosen subset of model + code + schema | Coordination on every change; joint test suites must both pass | The subset grows, or one team changes it without the other |
| **Customer / supplier** | One context feeds another; dependencies run one way | Downstream must be treated as a customer in upstream planning | No automated acceptance tests from downstream in upstream CI — then every upstream change is a surprise |
| **Conformist** | Downstream has no leverage, or the upstream model is good enough and translation isn't worth it | Downstream gives up its own model in that area | Upstream changes; downstream has no say and no insulation |
| **Anti-corruption layer** | Downstream must keep its own model clean while integrating with a legacy, external, or badly-factored upstream | A translation layer to build and maintain — one place, deliberately | The layer starts leaking upstream concepts, or everyone routes around it |
| **Open host service** | Many consumers need to integrate; one-off translation per consumer is worse | You own a published protocol and must evolve it compatibly | The protocol becomes a second model nobody owns, or gets per-consumer special cases |
| **Published language** | The translation itself is the hard part, or parties must interoperate independently | Adopting (or writing and documenting) a shared interchange language | The language is underspecified — then independent implementations diverge |
| **Separate ways** | Integration is not worth the coordination cost | Duplication, deliberately | Someone quietly re-couples them through a shared database |

