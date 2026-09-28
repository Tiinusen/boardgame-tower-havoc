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
  - Created At: 2026-09-18 01:42:00
  - Authors: Olle Tiinus
  - Why: Lock the exposure requirement while keeping the bell probability provisional.
  - Summary: Bell victory after one full orbit

---
# Bell victory after one full orbit

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted structure; probability PLAYTEST
- Rule ID: rules.victory
- Required Tower: 3 built floors
- Exposure Requirement: the complete three-floor tower must already exist at the beginning of the player's own turn
- Bell Attempt Cost: 1 action
- First-Session Success: D6 result 1
- First-Session Attempt Limit: maximum 1 bell attempt per player turn
- Decision: A player cannot build the third floor and attempt victory in the same turn. The tower must survive a full table orbit before the first legal bell attempt.

## Basis

The exposure orbit creates a clear response window for opponents. The 1-in-6 success rate is only a starting hypothesis for ending tension.

## Consequences

The prototype must visibly distinguish tower completion from legal bell eligibility. Bell probability and repeat-attempt rules remain easy to alter after testing.

## Review Conditions

Review bell probability and attempt limit after observing whether endings feel tense or merely slow.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Value: RcuOSY4OoNGiBxKMzj46me6BYv99aZL1TSrCTkO9FbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: H_8VW-zjAUzjiNme7nbylQ-ymWUXAsJaMdYNWiydBz0
