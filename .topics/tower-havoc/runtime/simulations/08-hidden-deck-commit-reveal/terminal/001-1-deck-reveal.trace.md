# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.result.v1](../../../../../.schemas/tower-havoc/towerhavoc.match.result.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-08 Simulation Result](001-result.trace.md)
  - Origin:
    - [relative](001-result.trace.md)
- Current
  - Current Schema: [towerhavoc.hidden.reveal.v1](../../../../../.schemas/tower-havoc/towerhavoc.hidden.reveal.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-08 Deck Reveal

## Commitment Binding
- Commitment Artifact: ../setup/005-deck-commitment.trace.md
- Commitment Value: sha256:786f0d09e5741b553a206b75985dc9c00bf17fda8c503483825e05381e75af3f

## Revealed Material
- Canonical Secret Payload Or Preserved Reference: ["Ceasefire","Sabotage","Nitlott","...remaining committed deck..."]
- Salt Or Nonce: th-sim-08-nonce

## Verification
- Recomputed Commitment: sha256:786f0d09e5741b553a206b75985dc9c00bf17fda8c503483825e05381e75af3f
- Matches: yes
- Verification Method: SHA-256 over canonical payload + nonce

## Reveal Timing
- Trigger: synthetic scenario terminal result
- Revealed At: 2026-09-18 11:35:00

## Interpretation Limits
- Does Not Prove: the secret was unknown to every participant before reveal
- Must Not Be Inferred: commitment verification proves fairness beyond byte binding

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-08 Simulation Result](001-result.trace.md)
  - Value: x_FNBwfjuMnJPXezy6e-3vTw4gp-LeIWrr-9c5RGB6I

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: FFiK3hvCrWV80itSEwm8KY8JznMAAoxNX9Q_i4oLBKk
