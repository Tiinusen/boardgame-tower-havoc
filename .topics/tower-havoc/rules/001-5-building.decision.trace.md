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
  - Created At: 2026-09-18 01:37:00
  - Authors: Olle Tiinus
  - Why: Provide a first burst-building baseline without falsely locking its balance.
  - Summary: Three-floor building and burst cost

---
# Three-floor building and burst cost

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: provisional/PLAYTEST
- Rule ID: rules.building
- Tower Floors Per Player: 3
- Build Cost — first floor built this turn: 2 actions
- Build Cost — second floor built this turn: 3 actions
- Build Cost — third floor built this turn: 4 actions
- Three-Floor Burst Total: 9 actions
- Decision: A player may build multiple floors in one turn if enough banked actions are available; successive builds currently use the 2/3/4 cost curve.

## Basis

The curve preserves a burst response to aggression while making a one-turn tower less action-efficient than gradual construction.

## Consequences

The prototype must make the cost curve easy to change. CAD geometry must not depend on 2/3/4 being final.

## Review Conditions

Review after real sessions; 2/3/4 is a playtest constant, not a final balance claim.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-core-game-rules.topic.trace](001-core-game-rules.topic.trace.md)
  - Value: RcuOSY4OoNGiBxKMzj46me6BYv99aZL1TSrCTkO9FbU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 15EHsw82vMftwRqAqAdtr4WW7EXgc48s3Lo9B7HZll0
