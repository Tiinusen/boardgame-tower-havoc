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
  - Created At: 2026-09-18 01:47:00
  - Authors: Olle Tiinus
  - Why: Preserve the value-specific reaction card distribution.
  - Summary: Offensive Reroll card family

---
# Offensive Reroll card family

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted prototype baseline
- Card Family ID: cards.offensive-reroll
- Name: Offensive Reroll
- Type: tactic
- Quantity: 8
- Timing: Reaction
- Effect: When another player rolls the value printed on this card for an attack, force that attack die to be rerolled.

| Printed Value | Quantity |
|---:|---:|
| 2 | 2 |
| 3 | 2 |
| 4 | 2 |
| 5 | 2 |


## Basis

Only hittable side values need offensive reroll cards because 1 and 6 are already misses.

## Consequences

The deck generator emits two cards for each value 2–5. Exact timing interaction with other rerolls remains a playtest wording item.

## Review Conditions

Clarify reroll ordering after actual ambiguous cases appear in play.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-2-card-system.topic.trace](001-card-system.topic.trace.md)
  - Value: ywUmCrjm4NqLH3dV7cxuR0d3O2F3c0XuuCvjThA9LbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: TkyjzdKxkdyCeCxfDGFVIXhDkJsZ2Ef5mOS37CDGO8A
