# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 02:03:00
  - Trace: [001-5-faction-module.topic.trace](001-faction-module.topic.trace.md)
  - Origin:
    - [relative](001-faction-module.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 02:04:00
  - Authors: Olle Tiinus
  - Why: Preserve a chess-like mechanically pure reference mode.
  - Summary: Classic mode is the balance reference

---
# Classic mode is the balance reference

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Mode ID: mode.classic
- Decision: In Classic mode every player set is mechanically identical. Use Classic mode for the first playtests and as the reference when judging whether the core game itself works.

## Basis

Symmetric testing isolates core economic and timing behavior from faction-specific noise.

## Consequences

Faction powers are not required for a valid Tower Havoc match and must not become hidden dependencies of balance.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-5-faction-module.topic.trace](001-faction-module.topic.trace.md)
  - Value: 2LX_20q7B6zk_nqfcj3e8_PB9Cae3Y6oRMZUWUmtsWg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: IKN7zsSfBwGaCMUf8mHnN6yUgy2wocGCpaq4ijLtcvI
