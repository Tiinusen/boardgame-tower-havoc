# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.action.resolution.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.resolution.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-05 Sabotage Resolution](001-1-1-sabotage.resolution.trace.md)
  - Origin:
    - [relative](001-1-1-sabotage.resolution.trace.md)
- Current
  - Current Schema: [towerhavoc.hidden.reveal.v1](../../../../../../.schemas/tower-havoc/towerhavoc.hidden.reveal.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-05 Played Sabotage Reveal

## Commitment Binding
- Commitment Artifact: ../../setup/005-hand-commitment.trace.md
- Commitment Value: sha256:1750c9f4ba25ec9b59711c35c737794706f9d4458e463ea533ab4beb129bdda0

## Revealed Material
- Canonical Secret Payload Or Preserved Reference: ["Sabotage"]
- Salt Or Nonce: th-sim-05-nonce

## Verification
- Recomputed Commitment: sha256:1750c9f4ba25ec9b59711c35c737794706f9d4458e463ea533ab4beb129bdda0
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
  - Towards: [TH-SIM-05 Sabotage Resolution](001-1-1-sabotage.resolution.trace.md)
  - Value: F2tfyjwn_LoUeN5Nq0UdR_LplDU3Xyv3gQzEZO4D2EU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: t-4RkFxlddOBSORaDN7UkDuT9vjPdZh8lcQYa-uw7_w
