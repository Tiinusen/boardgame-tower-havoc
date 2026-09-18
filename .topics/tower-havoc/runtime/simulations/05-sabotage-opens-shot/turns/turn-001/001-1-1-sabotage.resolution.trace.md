# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.action.intent.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-05 Sabotage Intent](001-1-sabotage.intent.trace.md)
  - Origin:
    - [relative](001-1-sabotage.intent.trace.md)
- Current
  - Current Schema: [towerhavoc.action.resolution.v1](../../../../../../.schemas/tower-havoc/towerhavoc.action.resolution.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-05 Sabotage Resolution

## Match And Turn Binding
- Match ID: TH-SIM-05
- Turn Artifact: 001-turn.trace.md
- Ruleset Artifact: ../../001-ruleset.ruleset.trace.md
- Prior State Artifact: ../../setup/004-initial-state.trace.md

## Intent Binding
- Intent Artifact: 001-1-sabotage.intent.trace.md
- Intent Fingerprint: referenced-intent-self-digest

## Adjudication
- Resolution State: accepted
- Legal: yes
- Reason: Sabotage may remove one reinforcement from chosen opponent floor

## Costs Applied
- Costs: card consumed

## Randomness Binding
- Randomness Required: yes

## Outcome And State Delta
- Outcome: reinforcement 3 removed from seat-01 floor1
- State Delta: seat-02 hand -1; seat-01 floor1 reinforcement 3 removed

## Resulting State
- State Artifact: 001-1-1-1-state.trace.md
- State Fingerprint: referenced-state-self-digest

## Adjudication Provenance
- Adjudicator: simulation-adjudicator
- Runtime Or Workflow Version: simulation-corpus-v1
- Rules Validator Version: tower-havoc-rule-check-v1

## Interpretation Limits
- Does Not Prove: source code correctness outside the declared scenario or real human agreement
- Must Not Be Inferred: accepted synthetic adjudication is playtest Evidence

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-05 Sabotage Intent](001-1-sabotage.intent.trace.md)
  - Value: nNe2UqYNfqBwLcdhm5EDKyx272bnedWincSwVyhKA80

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: cRqF3nedCuugQ9eNjANRCnXBl7rM2urXAA2F2mnhVJI
