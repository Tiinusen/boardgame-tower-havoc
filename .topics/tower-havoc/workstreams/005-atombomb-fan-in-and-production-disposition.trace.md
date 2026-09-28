# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: tiinex.decision.v1
  - Created At: 2026-09-28 18:07:30
  - Trace: [001-9-1-1-atombomb-event-with-bell-destruction.trace.md](../cards/001-9-1-1-atombomb-event-with-bell-destruction.trace.md)
  - Origin:
    - [relative](../cards/001-9-1-1-atombomb-event-with-bell-destruction.trace.md)
- Current
  - Current Schema: tiinex.decision.v1
  - Created At: 2026-09-28 18:08:17
  - Authors: Steward
  - Why: The parallel fan-out exposed one real Bell ambiguity, one historical-parent authoring blocker, useful synthetic strategy/audit findings, and a Pilot return-path discipline defect that require Steward disposition before the next stable production tranche.
  - Summary: Reconcile the Atombomb parallel returns, explicitly destroy built Bells, and establish qualified Pilot return invariants.
  - Status: ready/local

---

# Atombomb Fan-In And Production Disposition

## Decision

- State: accepted-for-implementation
- Subject: reconcile the bounded Cartographer, Keeper, Player, and Pilot work around the one-copy Atombomb Event and define the next production frontier.
- Decision: keep Atombomb as exactly one immediate global Event, explicitly destroy Bell construction together with all tower floors and reinforcements, retain the synthetic audit/player results only within their stated evidence boundaries, preserve the historical-deck authoring blocker without reparenting, and require Pilot returns to use the qualified Tiinex return path rather than manually reconstructing carrier structure.

## Atombomb Production Semantics

- Quantity: exactly 1 card in the shared draw pile.
- Type: Event.
- Timing: resolve immediately.
- Production-facing rule text: `Destroy all tower floors, all reinforcements, and all built Bells.`
- Resolution scope: the effect applies to every player simultaneously as one global Event resolution.
- Bell consequence: any Bell construction/marker, maturity, readiness, or previously satisfied Bell survival state is destroyed with the tower. Rebuilding floors does not restore the Bell; the player must construct a new Bell and satisfy the ordinary Bell readiness/survival rules again.
- Non-effects: Atombomb does not itself alter hands, Ready Ammo, Production, Available Actions, or unrelated persistent Events unless another qualified rule separately says so.

## Fan-In Disposition

### Keeper

Accept the Keeper synthetic audit as bounded rule-lineage analysis, not playtest Evidence. The audit correctly exposed the prior Bell-lifecycle ambiguity and also supports an implementation constraint: Atombomb must materialize atomically, without observable per-seat interleaving or reaction windows. Partial floor-payment state remains illegal under the current two-action atomic floor build rule. Reinforcement protection does not resist Atombomb.

### Player

Retain the Player strategy probe as synthetic participant-intent material only. It usefully exposes that the one-copy global reset can change draw incentives by public position, but it does not establish balance, fun, frequency, or observed player behavior and does not justify another gameplay change by itself.

### Cartographer

Accept the returned historical-parent authoring blocker as genuine fail-closed behavior under the prior bootstrap. The current bootstrap has since demonstrated identifier-only qualification for historical Decision parents, so Cartographer should retry the exact Dud-free deck Parent through current Tooling. Do not rewrite or reparent the sealed 34-card Dud-free deck Decision merely to obtain a 35-card projection. A canonical 35-card successor remains required before deck-derived manifests, component counts, TTS deck material, or generated documentation may truthfully move to 35 cards.

### Pilot

The generated Atombomb image is visually promising and the human-mediated generation/approval interaction worked, but the returned carrier was not qualified. Do not promote that failed return package as canonical provenance. The process defect is now understood: human approval is a human gate, not the Tooling-qualified return transition. After exact-result preservation, Pilot must use `qualify-return`; only a qualified result may proceed through `prepare-return`, Tiinex authoring/manufacture, exact-carrier qualification, and human-visible package delivery.

## Pilot Return Invariants

- Handoff Package is the canonical human transport/recovery surface for Tiinex role returns; loose JSON receipts are diagnostic/machine evidence, not the normal operator completion payload.
- Pilot must not synthesize Tiinex Handoff Package traces, pointer chains, carrier dimensions, statuses, or Workspace archives from precedent.
- When grounding projects a required transition operation such as `qualify-return`, descriptive Task/Process prose or a human approval phrase does not replace that operation.
- Runtime-only `.tiinex/*` state must not be carried as canonical Workspace source.
- A package may be called qualified only when the exact carrier bytes have a successful Tooling manufacture/qualification receipt.
- Future independent card-generation Handoffs should reference the reusable Pilot production process as Required Context rather than becoming semantic children of the historical Defensive Reroll test-Handoff chain.

## Stable-Major Boundary

This Decision accepts the design/process disposition above. It does not claim that the 35-card deck successor, corrected Pilot process artifact, Atombomb stable art asset, deterministic projections, or remote repository state already exist. Those are implementation work for the next Cartographer tranche under an explicit Handoff.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-1-1-atombomb-event-with-bell-destruction.trace.md](../cards/001-9-1-1-atombomb-event-with-bell-destruction.trace.md)
  - Value: _jZsDCcoNgpgX6b1aaJSMzj9iw1XGY8YePQoZ8zypjk

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: HiV6Vo02ixasyMPe0zITYMenLIU6xpRFn3G5sZ-ce04