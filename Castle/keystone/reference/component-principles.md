# Dependency and component principles

> Reference for [keystone](../SKILL.md). The one-line defense of each principle the
> method leans on. Load when you must justify a boundary, a packaging choice, or a
> metric position to someone who will otherwise relitigate it.

## Where the dependency rules come from

- **SRP** tells you where to draw boundaries — one reason to change per component.
- **OCP** tells you why the boundary pays — extend without modifying.
- **LSP** is the reason substitutability across a boundary is real rather than nominal; a plugin that needs `instanceof` to work is not a plugin.
- **ISP** keeps a consumer from depending on a fat interface it does not use, which is how accidental coupling enters.
- **DIP** is the mechanism: depend on abstractions the **caller** defines, so the dependency arrow opposes the flow of control.


## The cohesion principles (what pulls components together and apart)

Choose with the cohesion principles, and say which one you are sacrificing:

- **REP** — the granule of reuse is the granule of release. Pulls components **bigger**.
- **CCP** — gather what changes together, for the same reasons, at the same times. Pulls components **bigger**. For most applications maintainability beats reusability; early in a project, CCP dominates.
- **CRP** — don't force users to depend on things they don't need. Pulls components **smaller**.

These fight. That is the job. An architect who optimizes REP and CRP gets too many components touched by a simple change; one who optimizes CCP and REP generates needless releases. Find the position that fits today's concerns and say out loud that it will move as the project matures — early on you sacrifice reuse, later you slide toward it.

Then the coupling principles:

- **ADP** — allow no cycles in the component dependency graph. Cycles are why the build broke overnight. Break them with DIP (both sides depend on an abstraction one of them owns) or by extracting the shared part into a new component both depend on downward.
- **SDP** — depend in the direction of stability. A volatile component must not be depended on by something that is hard to change; the hard-to-change thing makes it hard to change.
- **SAP** — a component should be as abstract as it is stable. SDP and SAP together are DIP for components, with shades of grey.

