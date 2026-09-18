# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.action.intent.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-05 Follow-up Attack Intent](001-2-attack.intent.trace.md)
  - Origin:
    - [relative](001-2-attack.intent.trace.md)
- Current
  - Current Schema: [towerhavoc.random.request.v1](../../../../../../.schemas/tower-havoc/towerhavoc.random.request.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-05 Attack Random Request

## Request Identity
- Request ID: TH-SIM-05-attack
- Request State: open

## Match Binding
- Match ID: TH-SIM-05
- Bound Artifact Or Step: 001-2-attack.intent.trace.md
- Context Fingerprint: bound-artifact-self-digest

## Random Purpose
- Purpose: attack D6

## Outcome Space
- Outcomes: 1;2;3;4;5;6
- Selection Count: 1
- Replacement Policy: not-applicable

## Randomness Source Policy
- Method: physical-or-simulated-d6 observed after request
- Source Must Be Unknown At Request Time: yes

## Deterministic Mapping
- Mapping Method: identity D6 face
- Canonical Input Encoding: UTF-8 normalized scalar observation

## Request State
- State: open

## Interpretation Limits
- Does Not Prove: unpredictability beyond the declared source method
- Must Not Be Inferred: an outcome existed before this request

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-05 Follow-up Attack Intent](001-2-attack.intent.trace.md)
  - Value: j2LtXEI0o7PWXvhyqpdjloEccQY8sVhv60pREskXtS8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: bAxqd7AoaWqiX51sTduSrFcvS7D3PWc00ixJwB7Rkco
