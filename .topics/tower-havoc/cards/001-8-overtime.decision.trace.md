# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 01:44:00
  - Trace: [001-2-card-system.topic.trace](001-card-system.topic.trace.md)
  - Origin:
    - [relative](001-card-system.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:52:00
  - Authors: Olle Tiinus
  - Why: Keep card-family semantics independently editable and traceable.
  - Summary: Overtime card family

---
# Overtime card family

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted prototype baseline
- Card Family ID: cards.overtime
- Name: Overtime
- Type: tactic
- Quantity: 4
- Effect: Gain 1 action.
- Timing: Play on your turn.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Basis

A simple temporary action gain interacts cleanly with the bankable action economy.

## Consequences

The generator emits the declared number of physical/digital card instances from this family Decision.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-2-card-system.topic.trace](001-card-system.topic.trace.md)
  - Value: ywUmCrjm4NqLH3dV7cxuR0d3O2F3c0XuuCvjThA9LbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: dfHujybcdKV2lFvI2XbuaVj4ILbiLH95j4yYP9Md6HU
