# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.v1](../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 13:50:02
  - Trace: [TH-SIM-09 Incremental Lineage Match](../../002-match.match.trace.md)
  - Origin:
    - [relative](../../002-match.match.trace.md)
- Current
  - Current Schema: [towerhavoc.turn.v1](../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 13:50:47
  - Authors: ChatGPT

---

# TH-SIM-09 Turn 4

## Match Binding
- Match Artifact: ../../002-match.match.trace.md
- Match ID: TH-SIM-09

## Turn Identity
- Round Index: 2
- Turn Index: 4
- Active Seat: seat-01
- Turn State: open

## Opening State
- State Artifact: ../turn-003/001-3-1-state.trace.md
- State Fingerprint: referenced-state-self-digest

## Action Window
- Legal Actor: seat-01
- Accepted Action Resolutions: none yet

## Closing State
- State Artifact Or Pending: pending
- Next Seat Or Pending: pending

## Interpretation Limits
- Does Not Prove: every submitted intent is legal or that wall-clock order defines causality
- Must Not Be Inferred: this Turn artifact itself mutates state without Rule/Action Resolution artifacts

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-09 Incremental Lineage Match](../../002-match.match.trace.md)
  - Value: Kr3m3te7pzvZGLO0GaCCoPeeii_TRFs12KRqJ_nEKmg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:20q5SXSPBBBrMEoZySKJG4mxWVZ3O-nKdk6YjgYRQCc
