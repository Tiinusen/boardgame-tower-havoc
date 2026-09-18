# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Created At: 2026-06-05 11:00:00
  - Trace: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.action.resolution.v1](towerhavoc.action.resolution.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: A replayable digital match needs an engine-owned legality/result artifact separate from player-authored intent.
  - Summary: Adjudicated result of one Tower Havoc action intent.

---

# Tower Havoc Action Resolution

## Summary

Records adjudication of one action intent against one ruleset and current state.

## Schema Validation Contract

### Parent Runtime Specialization

Rules

- `towerhavoc.action.resolution.v1` specializes `tiinex.runtime.v1` for Tower Havoc gameplay provenance.
- The local `Action Resolution Body` replaces the inherited `Runtime Body` body structure for artifacts whose current schema is `towerhavoc.action.resolution.v1`.
- Compatible non-structural semantics from `tiinex.runtime.v1` remain inherited unless this schema explicitly narrows them.
- Reason: An action resolution is runtime-produced execution or adjudication output, including legality, costs, state delta, and resulting state binding.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-action-resolution-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.runtime.v1
  - Parent Node: Schema Validation Contract / Runtime Body / Required Shape
  - Child Node: Schema Validation Contract / Action Resolution Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Action Resolution Body` is authoritative for `towerhavoc.action.resolution.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Action Resolution Body
Required Shape
- `## Match And Turn Binding`
- `## Intent Binding`
- `## Adjudication`
- `## Costs Applied`
- `## Randomness Binding`
- `## Outcome And State Delta`
- `## Resulting State`
- `## Adjudication Provenance`
- `## Interpretation Limits`

### Match And Turn Binding
Required Fields
- Match ID
- Turn Artifact
- Ruleset Artifact
- Prior State Artifact

### Intent Binding
Required Fields
- Intent Artifact
- Intent Fingerprint

### Adjudication
Required Fields
- Resolution State
- Legal
- Reason
Allowed Resolution State
- accepted
- rejected
- failed-runtime

### Costs Applied
Required Fields
- Costs

### Randomness Binding
Required Fields
- Randomness Required
Optional Fields
- Random Request Artifact
- Random Result Artifact

Rules
- If randomness is required, an accepted random result must be bound before an accepted outcome is emitted.

### Outcome And State Delta
Required Fields
- Outcome
- State Delta

### Resulting State
Required Fields
- State Artifact
- State Fingerprint

### Adjudication Provenance
Required Fields
- Adjudicator
- Runtime Or Workflow Version
- Rules Validator Version

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

An automated runtime should be the ordinary author in digital play. Rejected intents still get a resolution artifact so the rejection remains provenance.

## Minimal Example

```md
## Adjudication
- Resolution State: accepted
- Legal: yes
- Reason: active seat has 1 ready ammo and attack limit permits one attack

## Randomness Binding
- Randomness Required: yes
- Random Result Artifact: ../../random/...
```

## Interpretation Notes

The action resolution is the durable game event. Human UI summaries are projections of it.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Value: hzROFN7xQRZUwU_5aLKLar8gKSHEKGFGUjiOhMEfH_A

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 68T3y4U7R5S028NJnW-IDAlJpXJVWmXLjxitH32HqGQ
