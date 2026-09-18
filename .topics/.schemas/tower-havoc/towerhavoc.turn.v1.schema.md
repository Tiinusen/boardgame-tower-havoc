# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.event.window.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/window/tiinex.event.window.v1.schema.md)
  - Created At: 2026-06-30 00:00:00
  - Trace: [tiinex.event.window.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/window/tiinex.event.window.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/window/tiinex.event.window.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.turn.v1](towerhavoc.turn.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: A match replay needs explicit active actor, opening state, action window, and closing state rather than inferring turns from timestamps.
  - Summary: Lifecycle envelope for one player turn.

---

# Tower Havoc Turn

## Summary

Defines one bounded player turn in one Tower Havoc match.

## Schema Validation Contract

### Parent Event Window Specialization

Rules

- `towerhavoc.turn.v1` specializes `tiinex.event.window.v1` for Tower Havoc gameplay provenance.
- The local `Turn Body` replaces the inherited `Event Window Body` body structure for artifacts whose current schema is `towerhavoc.turn.v1`.
- Compatible non-structural semantics from `tiinex.event.window.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A turn is a bounded gameplay window during which one seat may perform allowed actions.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-turn-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.event.window.v1
  - Parent Node: Schema Validation Contract / Event Window Body / Required Shape
  - Child Node: Schema Validation Contract / Turn Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Turn Body` is authoritative for `towerhavoc.turn.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Turn Body
Required Shape
- `## Match Binding`
- `## Turn Identity`
- `## Opening State`
- `## Action Window`
- `## Closing State`
- `## Interpretation Limits`

### Match Binding
Required Fields
- Match Artifact
- Match ID

### Turn Identity
Required Fields
- Round Index
- Turn Index
- Active Seat
- Turn State
Allowed Turn State
- open
- closed
- interrupted

### Opening State
Required Fields
- State Artifact
- State Fingerprint

### Action Window
Required Fields
- Legal Actor
- Accepted Action Resolutions

### Closing State
Required Fields
- State Artifact Or Pending
- Next Seat Or Pending

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

The runtime opens a Turn from an accepted state and closes it only after all accepted action resolutions for that turn have produced the closing state.

## Minimal Example

```md
## Turn Identity
- Round Index: 2
- Turn Index: 5
- Active Seat: seat-02
- Turn State: open
```

## Interpretation Notes

A Turn owns the action window, not the legality of each individual action.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.event.window.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/window/tiinex.event.window.v1.schema.md)
  - Value: 5NlPIJaGR3UakPrNW1Ja66b5jSQNxJTpbAmm5zUXBCg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: H6XxddYh1em2_lsUBnbpkv8KJOlcFeHAPdBf-9nT1Gs
