# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 01:55:00
  - Trace: [001-3-component-system.topic.trace](001-component-system.topic.trace.md)
  - Origin:
    - [relative](001-component-system.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:56:00
  - Authors: Olle Tiinus
  - Why: Create one canonical prototype bill of materials.
  - Summary: Prototype component inventory

---
# Prototype component inventory

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted MVP inventory
- Component Manifest ID: components.mvp

| Component | Quantity | Prototype Substitute | Constraint |
|---|---:|---|---|
| Player mat | 6 | paper/player colour zone | visibly separate Action Bank, Ready Ammo, Production |
| Reference card | 6 | paper note | one quick reference per player |
| Optional faction card | 6 | paper note | used only in Faction mode |
| Tower floor | 18 | generic block | 3 per player; identical mechanical envelope |
| Light field cannon | 6 | pawn/token | theme/readability only; no real projectile required |
| D6 | 2 | standard die | one required plus one spare |
| Bell | 1 | obvious goal token | physical bell preferred later |
| Ammo token | 72 | cube/coin | shared supply |
| Reinforcement marker | 72 | numbered token | values 2–5 x 3 floors x 6 players |
| Action tracker | 6 sets | counter/dial | must support banked actions without a small fixed cap |
| Card | 40 | generated prototype deck | deck manifest comes from card lineage |


## Basis

The inventory supports the maximum six-player game while keeping enough visible tokens for all reinforcement positions and a generous shared ammunition pool.

## Consequences

Generated component manifests and CAD/TTS briefs use this table. Quantity changes should land here before regenerated outputs change.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-3-component-system.topic.trace](001-component-system.topic.trace.md)
  - Value: 5o1q-tj4Kry2JGV9fW0-cu5f16qt_e6G1nGCTI08zk8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: KFVa__Wl6U2Ym6Mjt4_EnFSkEZnhn0VJHqVUANpKNTM