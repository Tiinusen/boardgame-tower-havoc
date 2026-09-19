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
  - Created At: 2026-09-18 01:54:00
  - Authors: Olle Tiinus
  - Why: Preserve the deck reset behavior that gives Dud cards a bounded lifetime in hand.
  - Summary: Deck recycle rule

---
# Deck recycle rule

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted prototype baseline
- Rule ID: cards.recycle
- Decision: When the draw pile is exhausted, every player discards Dud cards from hand. Combine those Duds with the discard pile, shuffle, and create a new draw pile.

## Basis

The original design used Dud cards as persistent hand friction but allowed them to return to circulation when the deck resets.

## Consequences

Generated rulebooks include this recycle rule. Card instances are not permanently removed from the match by ordinary deck exhaustion.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-2-card-system.topic.trace](001-card-system.topic.trace.md)
  - Value: ywUmCrjm4NqLH3dV7cxuR0d3O2F3c0XuuCvjThA9LbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: VXnHijsG7kZKuqgEP4gX2RrQEn5cop0lokksnZfy67I
