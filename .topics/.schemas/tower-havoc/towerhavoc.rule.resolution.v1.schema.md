# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Created At: 2026-06-05 11:00:00
  - Trace: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.rule.resolution.v1](towerhavoc.rule.resolution.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Status: draft/local
  - Why: Some game state changes are caused by deterministic rules rather than a player Action Intent, especially turn-start maturation, event expiry, and other automatic transitions.
  - Summary: Project-local schema for deterministic Tower Havoc rule-trigger resolution without fabricating player intent.

---

# Tower Havoc Rule Resolution

## Summary

A Rule Resolution records a deterministic gameplay transition caused by a declared rule trigger rather than by a player command. It preserves the same host-neutral execution boundary as other Runtime artifacts: a person, bot, GitHub Action, or later engine may perform the procedure without changing the gameplay meaning of the resulting resolution.

## Schema Validation Contract

### Parent Runtime Specialization

Rules
- `towerhavoc.rule.resolution.v1` specializes `tiinex.runtime.v1`.
- It is used only when the state transition is caused by game rules rather than a player-authored `towerhavoc.action.intent.v1`.
- It must not invent an Action Intent merely to fit automatic state changes into an action pipeline.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-rule-resolution-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.runtime.v1
  - Parent Node: Schema Validation Contract / Runtime Body / Required Shape
  - Child Node: Schema Validation Contract / Rule Resolution Body / Required Shape
  - Reason: automatic Tower Havoc rule execution needs explicit trigger, rule, delta, and state bindings while retaining generic Runtime semantics.
  - Effective Result: `Rule Resolution Body` is authoritative for `towerhavoc.rule.resolution.v1` artifact-body structure; compatible inherited Runtime semantics remain active outside the overridden structural body.

### Rule Resolution Body
Required Shape
- `## Match And Turn Binding`
- `## Trigger`
- `## Rules Applied`
- `## Outcome And State Delta`
- `## Resulting State`
- `## Execution Provenance`
- `## Interpretation Limits`

### Match And Turn Binding
Required Fields
- Match ID
- Turn Artifact Or Setup Step
- Ruleset Artifact
- Prior State Artifact

### Trigger
Required Fields
- Trigger Kind
- Trigger Source

Allowed Trigger Kind
- setup
- turn-start
- turn-end
- event-expiry
- production-maturation
- collapse-follow-up
- other

### Rules Applied
Required Fields
- Rule Artifacts
- Evaluation

### Outcome And State Delta
Required Fields
- Outcome
- State Delta

### Resulting State
Required Fields
- State Artifact
- State Fingerprint

### Execution Provenance
Required Fields
- Executed By
- Procedure Or Runtime Version

Rules
- `Executed By` may identify a human procedure, machine runtime, bot, GitHub workflow, or another bounded executor.
- Executor identity does not change the gameplay semantics of the resolution.

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create when a deterministic rule changes or confirms gameplay state without a player Action Intent. Do not use for player commands; those must begin with `towerhavoc.action.intent.v1` and resolve through `towerhavoc.action.resolution.v1`.

## Minimal Example

```md
## Trigger
- Trigger Kind: turn-start
- Trigger Source: active seat begins own turn

## Outcome And State Delta
- Outcome: planned ammunition matured
- State Delta: production-ammo seat-01 -2; ready-ammo seat-01 +2
```

## Interpretation Notes

This schema lets the same game event be executed manually at a physical table or automatically by a bot without inventing two different games.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Value: hzROFN7xQRZUwU_5aLKLar8gKSHEKGFGUjiOhMEfH_A

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 4enO3Ot2PSdqMvqnEx04gS3qFc5KT-HBfZOuBNM-QZc
