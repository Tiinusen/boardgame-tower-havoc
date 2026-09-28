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
  - Created At: 2026-09-18 01:57:00
  - Authors: Olle Tiinus
  - Why: Keep delayed and persistent game state inspectable at a glance.
  - Summary: Visible player-state layout

---
# Visible player-state layout

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Component Rule ID: components.player-state
- Required Visible Zones: Action Bank; Ready Ammo; Production
- Additional Visible State: built floors; reinforcement markers; active persistent Event
- Decision: persistent state that matters later should be physically/digitally represented rather than remembered where practical.

## Basis

The project explicitly prefers low start-of-turn process and minimal latent memory bookkeeping.

## Consequences

Player mats and TTS layouts should expose the declared state zones. Hidden automation must not become necessary for understanding the analog game.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-3-component-system.topic.trace](001-component-system.topic.trace.md)
  - Value: 5o1q-tj4Kry2JGV9fW0-cu5f16qt_e6G1nGCTI08zk8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 9aha6Er1bbuZOe6z91r-um7LX91P7vXA-3KVCsmCNj4
