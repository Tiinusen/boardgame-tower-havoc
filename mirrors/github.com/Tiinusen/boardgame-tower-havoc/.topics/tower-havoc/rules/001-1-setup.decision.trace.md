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
  - Created At: 2026-09-18 01:33:00
  - Authors: Olle Tiinus
  - Why: Land the current playable setup as a governing rule.
  - Summary: Setup and player boundary

---
# Setup and player boundary

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Rule ID: rules.setup
- Players: 2–6
- Starting Ready Ammo: 2 per player
- Starting Production Ammo: 0
- Starting Banked Actions: 0
- Starting Built Floors: 0
- Start Player: highest D6 roll
- Turn Direction: clockwise
- Decision: Each player takes one player set with three tower floors and the resources required by the selected game mode. Classic mode is the reference setup.

## Basis

This preserves the six-player material boundary from the original design while giving every player the same baseline state in Classic mode.

## Consequences

Generated rules and prototype manifests use these values as the default setup. Faction mode may override only explicitly declared starting advantages.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Value: RcuOSY4OoNGiBxKMzj46me6BYv99aZL1TSrCTkO9FbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: -Q9suohJcG54bqb2tcZRptiK9Tt5TFiLaSmu8cYTcGA
