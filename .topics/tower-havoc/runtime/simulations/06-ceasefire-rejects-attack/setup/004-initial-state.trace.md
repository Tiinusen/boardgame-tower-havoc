# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.v1](../../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-06 Ceasefire Rejects Attack Then Expires](../002-match.match.trace.md)
  - Origin:
    - [relative](../002-match.match.trace.md)
- Current
  - Current Schema: [towerhavoc.state.v1](../../../../../.schemas/tower-havoc/towerhavoc.state.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-06 Initial State

## Match Binding
- Match ID: TH-SIM-06
- Ruleset Artifact: ../001-ruleset.ruleset.trace.md

## State Identity
- State ID: s000
- Sequence: 0
- Active Seat Or Setup State: seat-01

## Public State
- Seat States: seat-01=active; seat-02=active
- Action Banks: seat-01=0; seat-02=1
- Ready Ammo: seat-01=2; seat-02=1
- Production Ammo: seat-01=0; seat-02=0
- Tower Floors: seat-01=1; seat-02=1
- Reinforcements: none
- Hand Counts: seat-01=0; seat-02=0
- Deck Count: 40
- Discard State: none
- Active Global Event: Ceasefire drawn by seat-01; expires at seat-01 next turn
- Bell Eligibility: seat-01=no; seat-02=no

## Hidden State Commitments
- Commitments: none

## Derivation Binding
- Previous State Or Initial Setup: initial synthetic setup
- Producing Resolution Or Setup Step: scenario setup

## Verification State
- State: verified
- Regeneration Method: replay scenario ruleset plus accepted action/rule resolutions in sequence

## Interpretation Limits
- Does Not Prove: real-world play, hidden-card identity beyond declared commitments, or balance
- Must Not Be Inferred: this checkpoint is authority independent of the event chain

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-06 Ceasefire Rejects Attack Then Expires](../002-match.match.trace.md)
  - Value: xIAi-0kohiMmB_Z6CdWZtert33tzuhxV6oq_GfLLC3A

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 7N-11WI23IZ66A-4566r8nSFSoJH0DPHtNIF3kJSBh8
