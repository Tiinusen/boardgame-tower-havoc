# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-06-05 02:00:00
  - Trace: [tiinex.task.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.random.request.v1](towerhavoc.random.request.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Randomness must be requested before the random source is known so a workflow cannot choose a favorable source after seeing results.
  - Summary: Precommitted request for unbiased/replayable randomness.

---

# Tower Havoc Random Request

## Summary

Defines one random choice required by match setup or gameplay before the random source value is available.

## Schema Validation Contract

### Parent Task Specialization

Rules

- `towerhavoc.random.request.v1` specializes `tiinex.task.v1` for Tower Havoc gameplay provenance.
- The local `Random Request Body` replaces the inherited `Task Body` body structure for artifacts whose current schema is `towerhavoc.random.request.v1`.
- Compatible non-structural semantics from `tiinex.task.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A random request is a bounded unit of requested work with explicit constraints and completion criteria before the source value exists.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-random-request-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.task.v1
  - Parent Node: Schema Validation Contract / Task Body / Required Shape
  - Child Node: Schema Validation Contract / Random Request Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Random Request Body` is authoritative for `towerhavoc.random.request.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Random Request Body
Required Shape
- `## Request Identity`
- `## Match Binding`
- `## Random Purpose`
- `## Outcome Space`
- `## Randomness Source Policy`
- `## Deterministic Mapping`
- `## Request State`
- `## Interpretation Limits`

### Request Identity
Required Fields
- Request ID
- Request State

### Match Binding
Required Fields
- Match ID
- Bound Artifact Or Step
- Context Fingerprint

### Random Purpose
Required Fields
- Purpose
Allowed Purpose Examples
- faction assignment
- turn order
- D6 attack roll
- D6 bell roll
- deck shuffle
- random card selection

### Outcome Space
Required Fields
- Outcomes
- Selection Count
- Replacement Policy

### Randomness Source Policy
Required Fields
- Method
- Source Must Be Unknown At Request Time
Optional Fields
- Future Beacon Identifier Or Round
- Commit-Reveal Participants
- Physical Randomizer

Allowed Method
- public-beacon
- commit-reveal
- physical-randomizer
- trusted-host

Rules
- `trusted-host` is lower assurance and must not be described as cheat-proof.
- Digital anti-bias mode should prefer a source whose value was not knowable when the request was sealed.

### Deterministic Mapping
Required Fields
- Mapping Method
- Canonical Input Encoding

Rules
- Mapping must be deterministic and replayable.
- Mapping should avoid avoidable modulo bias; rejection sampling is recommended for bounded integer outcomes.

### Request State
Required Fields
- State
Allowed State
- pending
- fulfilled
- cancelled
- failed

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Seal the request before retrieving the random source. The request may be generated from an accepted action intent or setup step.

## Minimal Example

```md
## Random Purpose
- Purpose: D6 attack roll

## Outcome Space
- Outcomes: 1;2;3;4;5;6
- Selection Count: 1
- Replacement Policy: not-applicable
```

## Interpretation Notes

The request is a precommitment to the question; the result owns the answer.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.task.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Value: SVkacZ6IRAHU68znToXLqDvAKAVRMUqdZHJNAVmmcBc

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: XBhtP0cR9vNdfbwdn7npKawuyEWZ8xkUZoFSBRBRtzk
