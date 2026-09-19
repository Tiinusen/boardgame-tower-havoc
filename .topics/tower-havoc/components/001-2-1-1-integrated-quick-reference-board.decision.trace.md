# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:11
  - Trace: [Stacked compact player-board layout](001-2-1-stacked-player-board.decision.trace.md)
  - Origin:
    - [relative](001-2-1-stacked-player-board.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 15:08:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Land the final reviewed board grammar as a successor to the first compact-board playtest design.
  - Summary: PLAYTEST player-board layout with three persistent floor rows, integrated quick reference, and three stack wells.

---

# Integrated Quick Reference Player Board

## Decision

- State: provisional/PLAYTEST
- Component Rule ID: components.player-state
- Stack Wells: Ready Ammo; Production; Available Actions
- Stack Well Geometry: one coin-sized well per fungible resource; tokens stack vertically
- Quick Reference: printed directly on the board; no card slot
- Tower Section: three permanent floor rows; each row has 2 Build slots plus Reinforcement slots labelled 2, 3, 4, 5
- Build Representation: two Action-face coins placed on a floor's Build slots represent the paid build cost and give each placed marker permanent meaning
- Reinforcement Representation: one Action-face coin on the matching numbered slot records protection against that attack value
- Bell Section: one Bell construction slot; Ring the Bell is an action and needs no separate slot
- Removed Zones: player-card slot; active-card slot; quick-reference-card slot; card-draw-attempt slot; Ring-the-Bell slot
- Decision: use this fixed layout for every faction board; only decorative faction treatment may vary.

## Basis

Iterative visual review found that transient actions do not need board slots, while persistent build/reinforcement/bell state benefits from permanent positions. The project Steward approved the resulting three-floor layout.

## Consequences

All faction boards share one coordinate grammar suitable for common TTS snap points. Quick-reference text becomes part of board presentation rather than a separate component.

## Review Conditions

Physical token diameter and print tolerances remain pending physical prototype review.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Stacked compact player-board layout](001-2-1-stacked-player-board.decision.trace.md)
  - Value: 19bazYZ2tfB8sxl7Ud83itxj4DwaGqqaoaI2_LEjUz0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:qFilBykbFFwvVxQuh6izr2T2xR_42B8SnL4CwW4lSRY
