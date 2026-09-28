# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Trace: [Tower Havoc](../001-tower-havoc.project.trace.md)
  - Origin:
    - [relative](../001-tower-havoc.project.trace.md)
- Current
  - Current Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-19 15:02:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Give approved generated artwork a dedicated semantic owner without making image-generation output the game-rule source.
  - Summary: Approved visual-system branch for faction boards, shared coin art, and the three-family card design.

---

# Tower Havoc Visual Asset System

## Current Read

This branch owns accepted Tower Havoc visual material and its bounded design system without making generated image bytes into gameplay authority.

The approved visual state currently consists of six faction player-board variants sharing one fixed information layout, one shared double-sided Action/Ammo coin design, one common card-back design reference, and three card-front design references for Event, Sabotage, and Tactic presentation.

## Design Direction

Keep mechanics and layout invariant across faction boards. Faction differentiation may change illustration, emblem, palette, and decorative treatment only.

Keep Action/Ammo coin art shared across all factions.

Keep one draw pile with one common card back. Card fronts use exactly three presentation families: Event, Sabotage, and Tactic. Dud cards are absent from the current deck baseline and therefore have no active visual family.

Generated artwork is preserved material and presentation input. Gameplay Decisions under `cards/`, `rules/`, and `components/` remain semantic authority for effects, costs, timing, and quantities.

## Next Artifacts

- approved exact-byte preservation of the current visual files
- card-front production from the three accepted visual references
- TTS materialization of finished individual card faces

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc](../001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:8q2khIhd68nFOB_FcG1H0HwVVABGuVO4LMB_0qxtZwE
