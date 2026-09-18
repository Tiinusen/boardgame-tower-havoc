# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Trace: [Match Provenance Runtime](../001-match-provenance-runtime.topic.trace.md)
  - Origin:
    - [relative](../001-match-provenance-runtime.topic.trace.md)
- Current
  - Current Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT
  - Why: Give humans and implementers concrete end-to-end examples without treating synthetic execution as playtest evidence.
  - Summary: Synthetic replay/conformance corpus for the Tower Havoc gameplay provenance schemas.

---

# Tower Havoc Runtime Simulation Corpus

This branch contains deterministic synthetic match traces used as executable-style examples of the gameplay provenance schemas.

## Current Read

Eight small simulations cover the main runtime branches: ordinary actions, attack randomness, reinforcement blocking, structural collapse, delayed ammunition, Sabotage, global-event rejection/expiry, bell eligibility, and hidden commitment/reveal.

These simulations are **not playtest Evidence** and must not be used to claim balance, fun, match duration, or player behavior. Their purpose is schema/runtime conformance and implementation comprehension.

## Design Direction

Keep each scenario small enough that a human or LLM can replay it from Markdown. Freeze a scenario-specific ruleset or fixture, preserve player intent separately from adjudication, use random request/result separation, materialize state after accepted transitions, and close each scenario with an explicit result.

A Discord bot, GitHub Action, CLI, physical-table recorder, or later GUI should be able to implement the same semantics without changing the match artifact vocabulary.

## Scenario Set

- `01-basic-build-bell/` — build three floors, survive the orbit boundary, legal bell attempt succeeds
- `02-reinforcement-block/` — attack rolls a protected value and is blocked
- `03-middle-floor-collapse/` — successful hit on floor 2 removes floor 2 and floor 3
- `04-planned-ammo-matures/` — delayed ammunition moves from production to ready stock at next own turn
- `05-sabotage-opens-shot/` — Sabotage removes one reinforcement and a matching attack then lands
- `06-ceasefire-rejects-attack/` — attack intent is rejected while Ceasefire is active, then event expiry is automatic
- `07-bell-ineligible-then-success/` — same-turn bell attempt after third floor is rejected; next-own-turn attempt is legal
- `08-hidden-deck-commit-reveal/` — hidden deck order is committed, consumed, then revealed and verified

## Next Artifacts

- real match Evidence only after actual players play
- implementation-specific conformance reports when a bot/runtime replays these vectors
- schema revisions only where these traces expose unclear or missing semantics
## Schema Coverage

- `tiinex.decision.v1`: 1 synthetic artifact(s)
- `tiinex.machine.runtime.v1`: 1 synthetic artifact(s)
- `tiinex.runtime.v1`: 4 synthetic artifact(s)
- `towerhavoc.action.intent.v1`: 17 synthetic artifact(s)
- `towerhavoc.action.resolution.v1`: 17 synthetic artifact(s)
- `towerhavoc.hidden.commitment.v1`: 2 synthetic artifact(s)
- `towerhavoc.hidden.reveal.v1`: 2 synthetic artifact(s)
- `towerhavoc.match.result.v1`: 8 synthetic artifact(s)
- `towerhavoc.match.seat.v1`: 16 synthetic artifact(s)
- `towerhavoc.match.v1`: 8 synthetic artifact(s)
- `towerhavoc.random.request.v1`: 5 synthetic artifact(s)
- `towerhavoc.random.result.v1`: 5 synthetic artifact(s)
- `towerhavoc.rule.resolution.v1`: 4 synthetic artifact(s)
- `towerhavoc.ruleset.v1`: 8 synthetic artifact(s)
- `towerhavoc.state.v1`: 29 synthetic artifact(s)
- `towerhavoc.turn-order.v1`: 8 synthetic artifact(s)
- `towerhavoc.turn.v1`: 15 synthetic artifact(s)

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Match Provenance Runtime](../001-match-provenance-runtime.topic.trace.md)
  - Value: YGNSdvw4OzdD1k3VWRmMhp0S5U4zHoX4LuaqKDsxe9s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: NiWrlJtCZeAMK8OnRDcbtuLNnP3mNp0nhFV5CkKaWQI
