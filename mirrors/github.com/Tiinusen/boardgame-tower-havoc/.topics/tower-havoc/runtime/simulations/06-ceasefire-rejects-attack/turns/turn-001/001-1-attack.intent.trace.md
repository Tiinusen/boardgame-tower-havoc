# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.turn.v1](../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-06 Turn 1](001-turn.trace.md)
  - Origin:
    - [relative](001-turn.trace.md)
- Current
  - Current Schema: [towerhavoc.action.intent.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-06 Attack During Ceasefire Intent

## Match And Turn Binding
- Match ID: TH-SIM-06
- Turn Artifact: 001-turn.trace.md
- Opening Or Current State Artifact: ../../setup/004-initial-state.trace.md

## Actor
- Seat: seat-02
- Host Actor Or Submission Source: synthetic player command

## Requested Action
- Action Kind: attack

## Parameters
- Parameters: target-seat=seat-01; target-floor=1

## Intent State
- State: submitted

## Interpretation Limits
- Does Not Prove: legality, successful execution, resource availability, or random outcome
- Must Not Be Inferred: submission order alone determines accepted game causality

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-06 Turn 1](001-turn.trace.md)
  - Value: JDF9qWF1OkbI8xYJRdu4lGU0xjiIuJezp2bf-YTSTq4

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: aXLey95rlNXQzNE5UXF68pSwhirx8iNAirGhDi_srXU
