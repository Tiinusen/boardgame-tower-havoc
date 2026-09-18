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
  - Created At: 2026-09-18 01:35:00
  - Authors: Olle Tiinus
  - Why: Give ammunition a distinct economic role and represent delayed state physically.
  - Summary: Ready and planned ammunition economy

---
# Ready and planned ammunition economy

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Rule ID: rules.ammunition
- Emergency Production: 1 action -> 1 Ready Ammo immediately
- Planned Production: 1 action -> 2 Production Ammo
- Planned Maturity: all Production Ammo becomes Ready Ammo at the beginning of that player's next own turn
- Attack Cost: 1 Ready Ammo
- Attack Action Cost: 0
- Decision: Ready Ammo and Production Ammo are separate visible states. Ammunition is prepaid offensive capacity, not a second copy of the action currency.

## Basis

If one action always produced one ammunition and every attack also consumed an action, ammunition risked becoming a dominated currency. Delayed 2-for-1 production rewards planning while emergency 1-for-1 preserves immediate flexibility.

## Consequences

Every player board/prototype needs separate Ready and Production zones. Attack-rate balance should be tested through ammunition supply and the multi-attack rule rather than silently restoring a second action cost.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Value: RcuOSY4OoNGiBxKMzj46me6BYv99aZL1TSrCTkO9FbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: H8U38thCKdFNVGhY0O9T7GerFBc3ixZ33IZRYMfSZp0