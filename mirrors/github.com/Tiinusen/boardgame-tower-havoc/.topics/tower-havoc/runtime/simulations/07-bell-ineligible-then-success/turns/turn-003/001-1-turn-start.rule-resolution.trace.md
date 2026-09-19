# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.turn.v1](../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-07 Turn 3](001-turn.trace.md)
  - Origin:
    - [relative](001-turn.trace.md)
- Current
  - Current Schema: [towerhavoc.rule.resolution.v1](../../../../../../.schemas/tower-havoc/towerhavoc.rule.resolution.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-07 Bell Eligibility Turn Start

## Match And Turn Binding
- Match ID: TH-SIM-07
- Turn Artifact Or Setup Step: 001-turn.trace.md
- Ruleset Artifact: ../../001-ruleset.ruleset.trace.md
- Prior State Artifact: ../turn-002/001-1-1-1-state.trace.md

## Trigger
- Trigger Kind: turn-start
- Trigger Source: declared scenario/game rule boundary

## Rules Applied
- Rule Artifacts: ../../../../../rules/001-9-victory.decision.trace.md; ../../../../../rules/001-9-1-bell-eligibility.condition.trace.md
- Evaluation: deterministic against prior state

## Outcome And State Delta
- Outcome: bell eligibility becomes active; seat-01 gains action
- State Delta: seat-01 actions +1; bell eligibility=yes

## Resulting State
- State Artifact: 001-1-1-state.trace.md
- State Fingerprint: referenced-state-self-digest

## Execution Provenance
- Executed By: synthetic deterministic procedure
- Procedure Or Runtime Version: simulation-corpus-rule-runtime-v1

## Interpretation Limits
- Does Not Prove: the executor is infallible or that a real match occurred
- Must Not Be Inferred: automatic resolution was requested by a player

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-07 Turn 3](001-turn.trace.md)
  - Value: EL8sjkKaAl_Lu1BsBnTP1dsnY7yGYHBe-_l2jQcXDKA

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: -xKM4wIgsr9Qp6w9I0ZVE5ujzf_Cf07UnhBT-WSebg8
