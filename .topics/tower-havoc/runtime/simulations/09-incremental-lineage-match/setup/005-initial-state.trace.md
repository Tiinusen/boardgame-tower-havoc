# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.v1](../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 13:50:02
  - Trace: [TH-SIM-09 Incremental Lineage Match](../002-match.match.trace.md)
  - Origin:
    - [relative](../002-match.match.trace.md)
- Current
  - Current Schema: [towerhavoc.state.v1](../../../../../.schemas/tower-havoc/towerhavoc.state.v1.schema.md)
  - Created At: 2026-09-18 13:50:07
  - Authors: ChatGPT

---

# TH-SIM-09 Initial State

## Match Binding
- Match ID: TH-SIM-09
- Ruleset Artifact: ../001-ruleset.ruleset.trace.md

## State Identity
- State ID: s000
- Sequence: 0
- Active Seat Or Setup State: seat-01

## Public State
- Seat States: seat-01=active; seat-02=active; seat-03=active
- Action Banks: seat-01=10; seat-02=0; seat-03=0
- Ready Ammo: seat-01=2; seat-02=2; seat-03=2
- Production Ammo: seat-01=0; seat-02=0; seat-03=0
- Tower Floors: seat-01=0; seat-02=0; seat-03=0
- Reinforcements: none
- Hand Counts: seat-01=0; seat-02=0; seat-03=0
- Deck Count: 40
- Discard State: none
- Active Global Event: none
- Bell Eligibility: seat-01=no; seat-02=no; seat-03=no

## Hidden State Commitments
- Commitments: none

## Derivation Binding
- Previous State Or Initial Setup: initial synthetic setup
- Producing Resolution Or Setup Step: scenario setup

## Verification State
- State: verified
- Regeneration Method: replay frozen ruleset plus accepted incremental resolutions in emission order

## Interpretation Limits
- Does Not Prove: real-world play, hidden-card identity, strategy quality, or balance
- Must Not Be Inferred: this checkpoint has authority independent of the preceding event lineage

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-09 Incremental Lineage Match](../002-match.match.trace.md)
  - Value: Kr3m3te7pzvZGLO0GaCCoPeeii_TRFs12KRqJ_nEKmg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:tXZ6cXLmuFT0vSOWIZEkNPOz2bmKUxFmUABOEgWfFVQ
