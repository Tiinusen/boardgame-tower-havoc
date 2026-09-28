# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:36:00
  - Trace: [Own-turn structure](001-4-turn-structure.decision.trace.md)
  - Origin:
    - [relative](001-4-turn-structure.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:02
  - Authors: Olle Tiinus; ChatGPT
  - Why: Make the guaranteed own-turn action gain impossible to miss in physical and digital play.
  - Summary: PLAYTEST successor placing +1 action first in every own turn.

---

# Action-first own-turn structure

This artifact supersedes the earlier start-step ordering for the next PLAYTEST iteration.

## Decision

- State: provisional/PLAYTEST
- Rule ID: rules.turn
- Start Step 1: gain 1 action; every own turn begins with this gain before any other start-of-turn game effect resolves
- Start Step 2: expire any persistent global event owned by this player from the previous orbit
- Start Step 3: move all of this player's Production Ammo to Ready Ammo
- Action Phase: spend any legal combination of available actions/resources in any legal order
- End: remaining actions stay banked; play passes clockwise
- Decision: the action gain is the first explicit event of every own turn and is never skipped because another start-of-turn effect also resolves.

## Basis

The first TTS playtest showed that the guaranteed action gain was easy to miss when it appeared after other processing. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

Rulebook, quick reference, board helper text, and digital runtimes should all render the action gain first.

## Review Conditions

This revision clarifies sequencing rather than claiming a balance change; review only if another rule later needs an explicit pre-action interrupt.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Own-turn structure](001-4-turn-structure.decision.trace.md)
  - Value: iL2Vlm3lCLESiYLjLu-CcMPwx-QuAaal8j4zq_p7LZc

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:D9bxlTD_EJ-mlz9jxMQN1BlTiIB6Rpwr0blwfeeujmY
