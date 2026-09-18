# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.match.v1](../../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-05 Sabotage Opens A Protected Hit Value](../002-match.match.trace.md)
  - Origin:
    - [relative](../002-match.match.trace.md)
- Current
  - Current Schema: [towerhavoc.hidden.commitment.v1](../../../../../.schemas/tower-havoc/towerhavoc.hidden.commitment.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-05 Hand Commitment

## Match Binding
- Match ID: TH-SIM-05
- State Or Setup Binding: 004-initial-state.trace.md

## Secret Scope
- Hidden Material Kind: seat hand
- Affected Seats Or Deck: seat-02

## Commitment Method
- Algorithm: SHA-256
- Canonical Secret Encoding: compact UTF-8 JSON plus explicit simulation nonce
- Salt Or Nonce Policy: fixed nonce is preserved only in post-terminal reveal for this synthetic demonstration

## Commitment
- Commitment Value: sha256:1750c9f4ba25ec9b59711c35c737794706f9d4458e463ea533ab4beb129bdda0

## Custody And Delivery
- Secret Custodian: synthetic simulation harness
- Player Delivery Method: not delivered; scenario emulates hidden state only

## Reveal Policy
- Reveal Trigger: scenario terminal result
- Required Reveal Material: exact canonical payload plus nonce

## Interpretation Limits
- Does Not Prove: secrecy against a real repository administrator or that real players lacked out-of-band knowledge
- Must Not Be Inferred: SHA-256 commitment encrypts the hidden material

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-05 Sabotage Opens A Protected Hit Value](../002-match.match.trace.md)
  - Value: 9tozi9_0StCoc_Hw6_cQm573R0DlsRYHBatuwiS5iBU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: RBA0TffBlaQkneEnYDnQMKhTzTQWXCyYho_t22-2uDU
