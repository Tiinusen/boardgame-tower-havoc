# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 01:32:00
  - Trace: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Origin:
    - [relative](001-core-game-rules.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:38:00
  - Authors: Olle Tiinus
  - Why: Land attack cost and targeting while keeping attack frequency explicitly open.
  - Summary: Attack targeting and cost

---
# Attack targeting and cost

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted with frequency PLAYTEST
- Rule ID: rules.attack
- Weapon Metaphor: light field cannon
- Target: one specific built floor of one opponent
- Cost: 1 Ready Ammo
- Additional Action Cost: 0
- First-Session Attack Limit: maximum 1 attack per player turn
- Long-Term Multi-Attack Rule: unresolved/PLAYTEST
- Decision: attacks consume ammunition and resolve against one chosen built floor. The first session uses a one-attack cap only as a conservative comparison baseline.

## Basis

Ammunition already represents prepaid offensive capacity. A temporary one-attack cap gives the first session a clean starting point without claiming that unlimited or escalating attacks are wrong.

## Consequences

Every playtest must record which multi-attack variant was used. A later Decision may replace the baseline after Evidence exists.

## Review Conditions

Compare max-one, unlimited 1-ammo, and escalating-ammo variants after playtest evidence exists.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Value: RcuOSY4OoNGiBxKMzj46me6BYv99aZL1TSrCTkO9FbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: BwhmeXLyNLdZRv9Topm-QYDyca5lW4W7675bubMPu-s
