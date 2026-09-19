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
  - Created At: 2026-09-18 01:40:00
  - Authors: Olle Tiinus
  - Why: Map defense directly to visible D6 side values.
  - Summary: Visible number-specific reinforcement

---
# Visible number-specific reinforcement

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Rule ID: rules.reinforcement
- Cost: 1 action per reinforcement
- Allowed Values: 2, 3, 4, 5
- Placement: one marker protects one value on one built floor
- Duplicate Value On Same Floor: not allowed/has no additional effect
- Full Protection: a floor protected on 2, 3, 4, and 5 is immune to normal fire
- Countermeasure: Sabotage may remove one reinforcement
- Decision: full fortification is intentionally legal; the game uses tactical removal rather than an artificial protection cap.

## Basis

Each reinforcement removes exactly one possible hit result, creating a visible linear protection curve. Allowing complete protection creates a reason for Sabotage to matter.

## Consequences

Every floor must expose readable positions for 2–5. Physical handling must allow one marker to be removed without accidentally collapsing the tower.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Value: RcuOSY4OoNGiBxKMzj46me6BYv99aZL1TSrCTkO9FbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: cejBmnAwHo9L-Cab32sc8hsgskvJn8o53RvOTW2p910
