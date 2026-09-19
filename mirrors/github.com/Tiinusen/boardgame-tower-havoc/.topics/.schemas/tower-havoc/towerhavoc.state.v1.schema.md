# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Created At: 2026-06-05 11:00:00
  - Trace: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.state.v1](towerhavoc.state.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Issue-driven play needs a convenient current-state projection while preserving that accepted resolutions and ruleset are the reconstructable authority.
  - Summary: Generated checkpoint of public and committed hidden Tower Havoc state.

---

# Tower Havoc State Snapshot

## Summary

Defines one deterministic match-state checkpoint. The snapshot is a cache/projection of the accepted event chain, not independent gameplay authority.

## Schema Validation Contract

### Parent Runtime Specialization

Rules

- `towerhavoc.state.v1` specializes `tiinex.runtime.v1` for Tower Havoc gameplay provenance.
- The local `State Body` replaces the inherited `Runtime Body` body structure for artifacts whose current schema is `towerhavoc.state.v1`.
- Compatible non-structural semantics from `tiinex.runtime.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A state snapshot is a runtime projection or checkpoint derived from the authoritative match event chain.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-state-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.runtime.v1
  - Parent Node: Schema Validation Contract / Runtime Body / Required Shape
  - Child Node: Schema Validation Contract / State Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `State Body` is authoritative for `towerhavoc.state.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### State Body
Required Shape
- `## Match Binding`
- `## State Identity`
- `## Public State`
- `## Hidden State Commitments`
- `## Derivation Binding`
- `## Verification State`
- `## Interpretation Limits`

### Match Binding
Required Fields
- Match ID
- Ruleset Artifact

### State Identity
Required Fields
- State ID
- Sequence
- Active Seat Or Setup State

### Public State
Required Fields
- Seat States
- Action Banks
- Ready Ammo
- Production Ammo
- Tower Floors
- Reinforcements
- Hand Counts
- Deck Count
- Discard State
- Active Global Event
- Bell Eligibility

### Hidden State Commitments
Required Fields
- Commitments

Rules
- Secret card identities or deck order should not appear in public state while hidden information matters.

### Derivation Binding
Required Fields
- Previous State Or Initial Setup
- Producing Resolution Or Setup Step

### Verification State
Required Fields
- State
- Regeneration Method
Allowed State
- generated
- verified
- stale
- invalid

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Generate after setup and after every accepted action resolution. A state snapshot should be reproducible by replaying the ruleset plus accepted prior resolutions.

## Minimal Example

```md
## Public State
- Seat States: seat-01=active; seat-02=active
- Action Banks: seat-01=3; seat-02=1
- Ready Ammo: seat-01=2; seat-02=4
- Production Ammo: seat-01=0; seat-02=2
- Tower Floors: seat-01=2; seat-02=1
```

## Interpretation Notes

The snapshot makes play convenient; the event chain makes it auditable.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Value: hzROFN7xQRZUwU_5aLKLar8gKSHEKGFGUjiOhMEfH_A

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: wFMv4JV21PyLXTD9Y61rrAmDweqK1ZrsDKiV-T6YKSU
