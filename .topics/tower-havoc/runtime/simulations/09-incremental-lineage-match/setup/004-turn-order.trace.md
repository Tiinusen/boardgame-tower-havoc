# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.v1](../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 13:50:02
  - Trace: [TH-SIM-09 Incremental Lineage Match](../002-match.match.trace.md)
  - Origin:
    - [relative](../002-match.match.trace.md)
- Current
  - Current Schema: [towerhavoc.turn-order.v1](../../../../../.schemas/tower-havoc/towerhavoc.turn-order.v1.schema.md)
  - Created At: 2026-09-18 13:50:06
  - Authors: ChatGPT

---

# TH-SIM-09 Turn Order

## Match Binding
- Match Artifact: ../002-match.match.trace.md
- Match ID: TH-SIM-09

## Eligible Seats
- Seats: seat-01; seat-02; seat-03

## Ordering Method
- Method: agreed

## Ordered Seats
- Order: seat-01; seat-02; seat-03

## Finality
- State: accepted

## Interpretation Limits
- Does Not Prove: this order was selected by real players
- Must Not Be Inferred: filesystem order or emission time silently determines turn order

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-09 Incremental Lineage Match](../002-match.match.trace.md)
  - Value: Kr3m3te7pzvZGLO0GaCCoPeeii_TRFs12KRqJ_nEKmg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:emTXtabHLrtcouXEDhdMv-g3_hFKMe87rxC-rAW2tn8
