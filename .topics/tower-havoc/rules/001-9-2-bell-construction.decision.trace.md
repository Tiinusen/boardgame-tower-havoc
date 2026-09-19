# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:42:00
  - Trace: [Bell victory after one full orbit](001-9-victory.decision.trace.md)
  - Origin:
    - [relative](001-9-victory.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:05
  - Authors: Olle Tiinus; ChatGPT
  - Why: Give the endgame a visible build state and explicit response window suited to the redesigned player board.
  - Summary: PLAYTEST successor adding 1-action bell construction and one-orbit maturity.

---

# Bell construction before victory attempt

This artifact supersedes the original immediate post-orbit bell-eligibility structure for the next PLAYTEST iteration.

## Decision

- State: provisional/PLAYTEST
- Rule ID: rules.victory
- Required Tower: 3 built floors
- Bell Construction Requirement: a player with all three floors built may spend 1 action to construct the bell
- Bell Construction Time: one full table orbit; the bell becomes ready only at the beginning of that player's next own turn if the three-floor tower still exists
- Bell Attempt Cost: 1 action
- Bell Attempt Success: D6 result 1
- Bell Attempt Limit: maximum 1 bell attempt per player turn for the next-session baseline
- Decision: completing the tower unlocks bell construction, not immediate victory. The constructed bell must survive one orbit with the complete tower before a ring attempt is legal.

## Basis

The player-board redesign benefits from a distinct visible bell-build state, and the first playtest motivated a clearer physical progression toward victory. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

Player boards need a Bell Build position. A shared physical bell may remain a theatrical table prop, while each player's board tracks whether their own bell has been constructed and matured.

## Review Conditions

Review whether the extra orbit produces tension or excessive delay after the next session; probability remains 1-in-6 PLAYTEST.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Bell victory after one full orbit](001-9-victory.decision.trace.md)
  - Value: H_8VW-zjAUzjiNme7nbylQ-ymWUXAsJaMdYNWiydBz0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:OnBO8nXvWA2xnNs9UHADf1G_TDuIlgzoBuz4oQNWbvU
