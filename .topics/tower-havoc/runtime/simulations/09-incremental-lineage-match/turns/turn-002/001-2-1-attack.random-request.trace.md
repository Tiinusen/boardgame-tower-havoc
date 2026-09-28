# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.action.intent.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md)
  - Created At: 2026-09-18 13:50:31
  - Trace: [TH-SIM-09 Attack Intent](001-2-attack.intent.trace.md)
  - Origin:
    - [relative](001-2-attack.intent.trace.md)
- Current
  - Current Schema: [towerhavoc.random.request.v1](../../../../../../.schemas/tower-havoc/towerhavoc.random.request.v1.schema.md)
  - Created At: 2026-09-18 13:50:32
  - Authors: ChatGPT

---

# TH-SIM-09 Attack Random Request

## Request Identity
- Request ID: TH-SIM-09-attack
- Request State: pending

## Match Binding
- Match ID: TH-SIM-09
- Bound Artifact Or Step: 001-2-attack.intent.trace.md
- Context Fingerprint: bound-artifact-self-digest

## Random Purpose
- Purpose: D6 attack roll

## Outcome Space
- Outcomes: 1;2;3;4;5;6
- Selection Count: 1
- Replacement Policy: not-applicable

## Randomness Source Policy
- Method: trusted-host
- Source Must Be Unknown At Request Time: yes

## Deterministic Mapping
- Mapping Method: 1,6=miss;2-5=potential hit; reinforcement matching value blocks
- Canonical Input Encoding: UTF-8 normalized scalar observation

## Request State
- State: pending

## Interpretation Limits
- Does Not Prove: trustless unpredictability or physical randomness quality
- Must Not Be Inferred: the harness may consume or choose the source value before this request artifact verifies

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-09 Attack Intent](001-2-attack.intent.trace.md)
  - Value: OxgRh8vG7S0z3kPN1ytz08kvUmvztnOfiDXmDx5o26s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:yqlJoDup4U-AXNAkDdEe0uoEgx8kvT-i4f100B6sbpY
