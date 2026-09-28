# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 13:50:00
  - Trace: [Incremental Tower Havoc Match-Lineage Stress](../002-incremental-lineage-stress.topic.trace.md)
  - Origin:
    - [relative](../002-incremental-lineage-stress.topic.trace.md)
- Current
  - Current Schema: [towerhavoc.match.v1](../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 13:50:02
  - Authors: ChatGPT
  - Why: Bound the live synthetic execution before setup artifacts are emitted.
  - Summary: Three-seat synthetic match emitted artifact-by-artifact during execution.

---

# TH-SIM-09 Incremental Lineage Match

## Match Identity
- Match ID: TH-SIM-09
- Match State: active
- Game: Tower Havoc
- Created By: incremental synthetic simulation harness

## Ruleset Binding
- Ruleset Artifact: 001-ruleset.ruleset.trace.md
- Ruleset Fingerprint: resolved from frozen scenario ruleset self digest

## Participants And Seats
- Expected Seats: 3
- Seat Artifacts: seat-01; seat-02; seat-03

## Runtime Policy
- Adjudication Mode: deterministic incremental simulation harness
- Randomness Mode: machine source value emitted only after the bound request artifact verifies
- Hidden State Mode: no hidden material in this scenario
- Canonical Event Store: artifacts emitted by this scenario directory as execution proceeds

## Lifecycle
- Setup State: synthetic fixture declared by initial state artifact
- Start Condition: required seat, order, ruleset, and initial-state artifacts exist and verify
- Completion Condition: seat-01 survives one full three-seat orbit with three floors and resolves a successful bell attempt

## Interpretation Limits
- Does Not Prove: real play occurred, player preferences, balance, fun, physical randomness quality, or production readiness
- Must Not Be Inferred: machine-generated fixture outcomes are empirical playtest Evidence

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Incremental Tower Havoc Match-Lineage Stress](../002-incremental-lineage-stress.topic.trace.md)
  - Value: lM4Pr8d9d2cNCpRP85O1v0QN-L2f2gh2jGuOMujyHBY

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:Kr3m3te7pzvZGLO0GaCCoPeeii_TRFs12KRqJ_nEKmg
