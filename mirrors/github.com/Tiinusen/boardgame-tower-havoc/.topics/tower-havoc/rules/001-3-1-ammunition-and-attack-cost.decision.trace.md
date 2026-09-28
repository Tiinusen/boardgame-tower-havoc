# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:35:00
  - Trace: [Ready and planned ammunition economy](001-3-ammunition.decision.trace.md)
  - Origin:
    - [relative](001-3-ammunition.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:17
  - Authors: Olle Tiinus; ChatGPT
  - Why: Keep ammunition semantics consistent with the playtest-corrected two-resource attack cost.
  - Summary: PLAYTEST ammunition successor with 1-action + 1-ammo attacks.

---

# Ammunition and post-playtest attack cost

This artifact supersedes the first-session ammunition note where attack action cost was recorded as zero.

## Decision

- State: provisional/PLAYTEST
- Rule ID: rules.ammunition
- Emergency Production: 1 action -> 1 Ready Ammo immediately
- Planned Production: 1 action -> 2 Production Ammo
- Planned Maturity: all Production Ammo becomes Ready Ammo at the beginning of that player's next own turn
- Attack Ammo Cost: 1 Ready Ammo
- Attack Action Cost: 1 action
- Decision: Ready Ammo and Production Ammo remain separate visible states; an attack now spends both 1 action and 1 Ready Ammo under the next-session baseline.

## Basis

The first real TTS playtest established the intended played attack cost as 1 action plus 1 ammo. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

Generated rule projections no longer repeat the historical zero-action attack cost from the first-session ammunition baseline.

## Review Conditions

Ammo production rates remain otherwise unchanged for the next session.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Ready and planned ammunition economy](001-3-ammunition.decision.trace.md)
  - Value: H8U38thCKdFNVGhY0O9T7GerFBc3ixZ33IZRYMfSZp0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:PxlbjeFSiWNsHMQeryimrbtlyjaABCYExZqA8HiNh28
