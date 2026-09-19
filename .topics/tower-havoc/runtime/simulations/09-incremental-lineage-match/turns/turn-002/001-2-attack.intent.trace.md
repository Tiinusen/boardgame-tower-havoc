# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.turn.v1](../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 13:50:28
  - Trace: [TH-SIM-09 Turn 2](001-turn.trace.md)
  - Origin:
    - [relative](001-turn.trace.md)
- Current
  - Current Schema: [towerhavoc.action.intent.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md)
  - Created At: 2026-09-18 13:50:31
  - Authors: ChatGPT

---

# TH-SIM-09 Attack Intent

## Match And Turn Binding
- Match ID: TH-SIM-09
- Turn Artifact: 001-turn.trace.md
- Opening Or Current State Artifact: 001-1-1-state.trace.md

## Actor
- Seat: seat-02
- Host Actor Or Submission Source: synthetic Player-capacity strategy policy inside incremental harness

## Requested Action
- Action Kind: attack

## Parameters
- Parameters: target-seat=seat-01; target-floor=1

## Intent State
- State: submitted

## Interpretation Limits
- Does Not Prove: the requested action is legal or accepted
- Must Not Be Inferred: Player intent directly mutates authoritative state

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-09 Turn 2](001-turn.trace.md)
  - Value: 5nKlkpM8cPa-pHYLdiPjnvX1uwAkxdrf33SqUMt7-XI

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:OxgRh8vG7S0z3kPN1ytz08kvUmvztnOfiDXmDx5o26s
