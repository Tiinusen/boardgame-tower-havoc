# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.v1](../../../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-08 Hidden Deck Commitment And Reveal](../../002-match.match.trace.md)
  - Origin:
    - [relative](../../002-match.match.trace.md)
- Current
  - Current Schema: [towerhavoc.turn.v1](../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-08 Turn 1

## Match Binding
- Match Artifact: ../../002-match.match.trace.md
- Match ID: TH-SIM-08

## Turn Identity
- Round Index: 1
- Turn Index: 1
- Active Seat: seat-01
- Turn State: open

## Opening State
- State Artifact: ../../setup/004-initial-state.trace.md
- State Fingerprint: referenced-state-self-digest

## Action Window
- Legal Actor: seat-01
- Accepted Action Resolutions: none yet

## Closing State
- State Artifact Or Pending: pending
- Next Seat Or Pending: pending

## Interpretation Limits
- Does Not Prove: every submitted intent is legal or that wall-clock ordering defines causality
- Must Not Be Inferred: a turn artifact itself applies automatic rule effects without a Rule Resolution

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-08 Hidden Deck Commitment And Reveal](../../002-match.match.trace.md)
  - Value: Yp_yqGJaUMEcKBy3k1ubtRnYbAZAdD_h0cn4fqummBw

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: MHD6dUELqGVaaqe0xXgVp9CK8GkP8nPaZr4Yw-T8vYc
