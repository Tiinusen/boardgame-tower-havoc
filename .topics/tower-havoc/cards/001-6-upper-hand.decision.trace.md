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
  - Created At: 2026-09-18 01:50:00
  - Authors: Olle Tiinus
  - Why: Keep card-family semantics independently editable and traceable.
  - Summary: Upper Hand card family

---
# Upper Hand card family

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted prototype baseline
- Card Family ID: cards.upper-hand
- Name: Upper Hand
- Type: tactic
- Quantity: 2
- Effect: Take two random cards from one chosen opponent hand.
- Timing: Play on your turn.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Basis

The hand swing is intentionally rare because it changes options for both players at once.

## Consequences

The generator emits the declared number of physical/digital card instances from this family Decision.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-2-card-system.topic.trace](001-card-system.topic.trace.md)
  - Value: ywUmCrjm4NqLH3dV7cxuR0d3O2F3c0XuuCvjThA9LbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: zX0re3O_0XwhrDR-pmkuBUymOnRdMum1VAJtfljEmGM