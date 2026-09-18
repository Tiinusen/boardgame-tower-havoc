# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.party.role.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/party/role/tiinex.party.role.v1.schema.md)
  - Created At: 2026-06-30 00:00:00
  - Trace: [tiinex.party.role.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/party/role/tiinex.party.role.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/party/role/tiinex.party.role.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.match.seat.v1](towerhavoc.match.seat.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Faction choice or random assignment must be explicit and replayable without confusing person identity, seat, and faction.
  - Summary: Binds one participant to one match seat and faction assignment.

---

# Tower Havoc Match Seat

## Summary

Defines one participant seat inside one match, including faction assignment and how that assignment was obtained.

## Schema Validation Contract

### Parent Party Role Specialization

Rules

- `towerhavoc.match.seat.v1` specializes `tiinex.party.role.v1` for Tower Havoc gameplay provenance.
- The local `Seat Body` replaces the inherited `Party Role Body` body structure for artifacts whose current schema is `towerhavoc.match.seat.v1`.
- Compatible non-structural semantics from `tiinex.party.role.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A match seat is a bounded gameplay role or capacity whose holder and faction assignment must remain distinct.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-match-seat-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.party.role.v1
  - Parent Node: Schema Validation Contract / Party Role Body / Required Shape
  - Child Node: Schema Validation Contract / Seat Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Seat Body` is authoritative for `towerhavoc.match.seat.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Seat Body
Required Shape
- `## Match Binding`
- `## Participant Binding`
- `## Faction Assignment`
- `## Seat State`
- `## Interpretation Limits`

### Match Binding
Required Fields
- Match Artifact
- Match ID
- Seat ID

### Participant Binding
Required Fields
- Participant
- Participant Reference Or Label

Rules
- A GitHub username is a host identity, not automatically a legal or real-world identity.

### Faction Assignment
Required Fields
- Faction
- Assignment Method

Allowed Assignment Method
- chosen
- randomized
- assigned

Optional Fields
- Random Result Artifact
- Choice Artifact Or Comment

Rules
- `randomized` requires a referenced accepted `towerhavoc.random.result.v1`.

### Seat State
Required Fields
- State
Allowed State
- proposed
- accepted
- active
- completed
- withdrawn

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create one accepted seat per player before turn order is finalized.

## Minimal Example

```md
## Faction Assignment
- Faction: Arsenal prototype
- Assignment Method: randomized
- Random Result Artifact: ../random/001-3-2-random-result.trace.md
```

## Interpretation Notes

Player, seat, and faction remain distinct identities.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.party.role.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/party/role/tiinex.party.role.v1.schema.md)
  - Value: 7Uks6PbkiAVbdB0MOVxDnj6wg1-9r-3iVaHLvzVVhMA

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: Dp6k0d744nBTClji2bxh9uq_L40_1pczQoUVBUbR0MU
