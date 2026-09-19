# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-06-05 02:00:00
  - Trace: [tiinex.task.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.action.intent.v1](towerhavoc.action.intent.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Player intent must stay distinct from adjudicated legality, random result, and resulting state.
  - Summary: Player-authored request to perform one Tower Havoc action.

---

# Tower Havoc Action Intent

## Summary

Records what a player asked to do. An intent is not proof that the action is legal or occurred.

## Schema Validation Contract

### Parent Task Specialization

Rules

- `towerhavoc.action.intent.v1` specializes `tiinex.task.v1` for Tower Havoc gameplay provenance.
- The local `Action Intent Body` replaces the inherited `Task Body` body structure for artifacts whose current schema is `towerhavoc.action.intent.v1`.
- Compatible non-structural semantics from `tiinex.task.v1` remain inherited unless this schema explicitly narrows them.
- Reason: An action intent is a bounded request for work to be adjudicated or executed; it is not the outcome itself.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-action-intent-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.task.v1
  - Parent Node: Schema Validation Contract / Task Body / Required Shape
  - Child Node: Schema Validation Contract / Action Intent Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Action Intent Body` is authoritative for `towerhavoc.action.intent.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Action Intent Body
Required Shape
- `## Match And Turn Binding`
- `## Actor`
- `## Requested Action`
- `## Parameters`
- `## Intent State`
- `## Interpretation Limits`

### Match And Turn Binding
Required Fields
- Match ID
- Turn Artifact
- Opening Or Current State Artifact

### Actor
Required Fields
- Seat
- Host Actor Or Submission Source

### Requested Action
Required Fields
- Action Kind
Allowed Action Kind
- pass
- emergency-ammo
- planned-ammo
- reinforce
- build
- draw-card
- attack
- play-card
- bell-attempt

### Parameters
Required Fields
- Parameters

Rules
- Parameters must contain target seat, target floor, reinforcement value, card reference, or other values required by the action kind.
- Parameters must not self-assert a random outcome.

### Intent State
Required Fields
- State
Allowed State
- submitted
- cancelled
- expired

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create from a player command/comment. The player authors intent; adjudication belongs to `towerhavoc.action.resolution.v1`.

## Minimal Example

```md
## Requested Action
- Action Kind: attack

## Parameters
- Parameters: target-seat=seat-03; target-floor=2
```

## Interpretation Notes

Separating intent from resolution is the core anti-cheat boundary for issue-driven play.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.task.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Value: SVkacZ6IRAHU68znToXLqDvAKAVRMUqdZHJNAVmmcBc

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: pPFmY_KJJl8Ssuqft5U6liSVFAC3LskAmdA4CqZLv1w
