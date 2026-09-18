# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-06-05 01:00:00
  - Trace: [tiinex.decision.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.turn-order.v1](towerhavoc.turn-order.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Turn order is mechanically material and must preserve whether it was selected or randomized and the result that produced it.
  - Summary: Authoritative ordered seat list used to start a Tower Havoc match.

---

# Tower Havoc Turn Order

## Summary

Defines the accepted initial turn order for a match.

## Schema Validation Contract

### Parent Decision Specialization

Rules

- `towerhavoc.turn-order.v1` specializes `tiinex.decision.v1` for Tower Havoc gameplay provenance.
- The local `Turn Order Body` replaces the inherited `Decision Body` body structure for artifacts whose current schema is `towerhavoc.turn-order.v1`.
- Compatible non-structural semantics from `tiinex.decision.v1` remain inherited unless this schema explicitly narrows them.
- Reason: Accepted turn order is a landed governing configuration, whether its basis was agreement, rules, or audited randomness.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-turn-order-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.decision.v1
  - Parent Node: Schema Validation Contract / Decision Body / Required Shape
  - Child Node: Schema Validation Contract / Turn Order Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Turn Order Body` is authoritative for `towerhavoc.turn-order.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Turn Order Body
Required Shape
- `## Match Binding`
- `## Eligible Seats`
- `## Ordering Method`
- `## Ordered Seats`
- `## Finality`
- `## Interpretation Limits`

### Match Binding
Required Fields
- Match Artifact
- Match ID

### Eligible Seats
Required Fields
- Seats

### Ordering Method
Required Fields
- Method
Allowed Method
- randomized
- agreed
- rules-derived
Optional Fields
- Random Request Artifact
- Random Result Artifact

Rules
- `randomized` requires an accepted random result bound to the same seat set.

### Ordered Seats
Required Fields
- Order

### Finality
Required Fields
- State
Allowed State
- proposed
- accepted
- superseded

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create once all participating seats are accepted and before the initial gameplay state becomes active.

## Minimal Example

```md
## Ordered Seats
- Order: seat-03; seat-01; seat-02
```

## Interpretation Notes

Issue-comment arrival order must never silently become turn order.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.decision.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Value: BlXrn7NlflHc7UzQ4j98mD4Yj9qOyoNwxaRw-PQO-ps

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: pZ1syqmVqDSlSb-28abTNBjVfyry1iRUABGdealXMEc
