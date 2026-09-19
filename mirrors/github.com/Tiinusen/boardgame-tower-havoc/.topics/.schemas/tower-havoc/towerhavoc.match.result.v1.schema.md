# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Created At: 2026-06-05 11:00:00
  - Trace: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.match.result.v1](towerhavoc.match.result.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: A completed match needs an explicit winner/result bound to the winning resolution and final state rather than a free-form announcement.
  - Summary: Final outcome and audit closure for one Tower Havoc match.

---

# Tower Havoc Match Result

## Summary

Records the terminal outcome of one match and the bounded audit closure supporting it.

## Schema Validation Contract

### Parent Runtime Specialization

Rules

- `towerhavoc.match.result.v1` specializes `tiinex.runtime.v1` for Tower Havoc gameplay provenance.
- The local `Match Result Body` replaces the inherited `Runtime Body` body structure for artifacts whose current schema is `towerhavoc.match.result.v1`.
- Compatible non-structural semantics from `tiinex.runtime.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A match result is a bounded runtime outcome package that closes one match and records replay and audit status.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-match-result-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.runtime.v1
  - Parent Node: Schema Validation Contract / Runtime Body / Required Shape
  - Child Node: Schema Validation Contract / Match Result Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Match Result Body` is authoritative for `towerhavoc.match.result.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Match Result Body
Required Shape
- `## Match Binding`
- `## Completion`
- `## Winner Or Outcome`
- `## Final State`
- `## Audit Closure`
- `## Interpretation Limits`

### Match Binding
Required Fields
- Match Artifact
- Match ID
- Ruleset Artifact

### Completion
Required Fields
- Completion State
- Completion Reason
- Terminal Resolution Artifact
Allowed Completion State
- completed
- abandoned
- invalidated

### Winner Or Outcome
Required Fields
- Outcome
Optional Fields
- Winning Seat

### Final State
Required Fields
- Final State Artifact
- Final State Fingerprint

### Audit Closure
Required Fields
- Unresolved Intents
- Unresolved Random Requests
- State Replay Status
- Hidden Commitment Reveal Status

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create when a terminal game condition is accepted or the match is explicitly abandoned/invalidated.

## Minimal Example

```md
## Winner Or Outcome
- Outcome: bell victory
- Winning Seat: seat-02

## Audit Closure
- Unresolved Intents: 0
- Unresolved Random Requests: 0
- State Replay Status: verified
- Hidden Commitment Reveal Status: complete
```

## Interpretation Notes

The result closes the match lineage but does not prove player identity or social agreement outside the declared runtime boundary.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Value: hzROFN7xQRZUwU_5aLKLar8gKSHEKGFGUjiOhMEfH_A

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: Tb341AhFJ9v83fNePbg8mDh0DUzFngVZSyBcKSHIR_k
