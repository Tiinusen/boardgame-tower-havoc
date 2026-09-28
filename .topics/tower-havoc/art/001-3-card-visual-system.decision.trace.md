# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-19 15:02:00
  - Trace: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Origin:
    - [relative](001-visual-asset-system.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 15:05:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Separate card presentation families from gameplay card semantics before individual face production.
  - Summary: One common back plus Event, Sabotage, and Tactic front-design references.

---

# Approved Card Visual System

## Decision

- State: accepted visual baseline
- Draw Piles: one
- Common Back: one shared card-back design for every card in the draw pile
- Front Families: Event; Sabotage; Tactic
- Event Visual Accent: brass/gold global-event treatment
- Sabotage Visual Accent: red disruption treatment
- Tactic Visual Accent: blue/cool tactical treatment
- Dud Visual Family: none
- Gameplay Binding: card name, effect, timing, quantity, and current inclusion remain governed by `../cards/**`
- Reference Status: the approved Event, Sabotage, and Tactic front images are visual references; their example names/effects are not gameplay authority
- Decision: use the approved common back and three front references as the visual source for producing the individual current-deck faces.

## Basis

The project Steward explicitly approved the common back and all three front-design references after review.

## Consequences

One shared back is sufficient for TTS because the game has one draw pile. The current 34-card Dud-free deck requires fifteen unique front faces across the three visual families; duplicate copies reuse the same face art.

## Review Conditions

Individual face artwork remains pending until each current gameplay card variant has been rendered against the appropriate approved visual reference.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Value: 8q2khIhd68nFOB_FcG1H0HwVVABGuVO4LMB_0qxtZwE

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:6B02XH07aZFLZd7QMtbcu9wjmedQ6VQb3RK6WGbOeBo
