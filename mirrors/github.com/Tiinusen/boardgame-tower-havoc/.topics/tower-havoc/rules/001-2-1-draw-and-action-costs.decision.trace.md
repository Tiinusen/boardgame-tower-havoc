# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:34:00
  - Trace: [Bankable action economy](001-2-action-economy.decision.trace.md)
  - Origin:
    - [relative](001-2-action-economy.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:01
  - Authors: Olle Tiinus; ChatGPT
  - Why: Land the first playtest-driven action-cost and card-draw revision without rewriting the original baseline.
  - Summary: PLAYTEST successor for attack and card-draw action economy.

---

# Post-playtest action and draw economy

This artifact supersedes the earlier action-cost baseline for the next PLAYTEST iteration.

## Decision

- State: provisional/PLAYTEST
- Rule ID: rules.actions
- Actions Gained Per Own Turn: 1
- General Action Bank Cap: none
- Pass Cost: 0
- Draw Attempt Cost: 1 action
- Draw Attempt Die: D6
- Draw Attempt Success: 1 or 6
- Draw Attempt Failure: 2, 3, 4, or 5; the player may spend another action to attempt again during the same turn
- Draw Success Limit: after the first successful draw, that player may not make another draw attempt during the same turn
- Reinforce Cost: 1 action
- Attack Cost: 1 action plus 1 Ready Ammo
- Bell Construction Cost: 1 action
- Bell Attempt Cost: 1 action
- Draw Phrase: `Ah, hmmm, mmmm`
- Decision: keep banked actions as strategic capital while making attacks and card access visibly compete for that same capital.

## Basis

The first TTS playtest reported low incentive and low drama around drawing cards, plus a quick-reference mismatch that exposed the intended attack cost. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

The quick reference, generated constants, runtime legality checks, and TTS player surface must expose the draw roll and the 1-action attack cost. A failed draw may be retried for another action; a successful draw closes card drawing for that turn.

## Review Conditions

Review draw frequency and attack pressure after the next real session; success on 1/6 and the one-success-per-turn limit remain PLAYTEST values.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Bankable action economy](001-2-action-economy.decision.trace.md)
  - Value: wWB7QrbYv9718G5SmKzqQucBMPWbrKPTbGQTGqZcvZs

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:-EFDP99mk0SpMSbeDDoRG-qF06l4-tbFHPgfx-T-6lg
