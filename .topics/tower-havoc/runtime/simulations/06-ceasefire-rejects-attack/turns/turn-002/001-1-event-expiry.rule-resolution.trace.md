# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.turn.v1](../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-06 Turn 2](001-turn.trace.md)
  - Origin:
    - [relative](001-turn.trace.md)
- Current
  - Current Schema: [towerhavoc.rule.resolution.v1](../../../../../../.schemas/tower-havoc/towerhavoc.rule.resolution.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-06 Ceasefire Expiry Rule Resolution

## Match And Turn Binding
- Match ID: TH-SIM-06
- Turn Artifact Or Setup Step: 001-turn.trace.md
- Ruleset Artifact: ../../001-ruleset.ruleset.trace.md
- Prior State Artifact: ../turn-001/001-1-1-1-state.trace.md

## Trigger
- Trigger Kind: event-expiry
- Trigger Source: declared scenario/game rule boundary

## Rules Applied
- Rule Artifacts: ../../../../../cards/001-9-global-events.decision.trace.md; ../../../../../rules/001-4-turn-structure.decision.trace.md
- Evaluation: deterministic against prior state

## Outcome And State Delta
- Outcome: Ceasefire expires at drawer seat-01 next turn start
- State Delta: active global event -> none; seat-01 actions +1

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
  - Towards: [TH-SIM-06 Turn 2](001-turn.trace.md)
  - Value: 9-nBAvADsRksRiByBQCkwsgW5YYedstjkR7Jk_EJqgA

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: EqAkUM4UhX6HTJpTLNoaFk_a_RPy0pvBaGzNGE1PdP4
