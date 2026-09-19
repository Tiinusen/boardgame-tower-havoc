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
  - Created At: 2026-09-19 15:04:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Preserve the approved shared coin visual language separately from faction art.
  - Summary: One approved faction-neutral Action/Ammo coin with normalized TTS textures.

---

# Approved Shared Action Ammo Coin Art

## Decision

- State: accepted next-playtest visual baseline
- Component: one shared double-sided Action/Ammo coin
- Faction Variation: none
- Action Side: weathered industrial coin with Action symbol
- Ammo Side: matching weathered industrial coin with ammunition symbol
- TTS Texture Geometry: 512 × 512 PNG per side; common normalized circular footprint
- Decision: use one common coin appearance for every faction and every seat.

## Basis

The project Steward explicitly approved the reviewed and normalized Action/Ammo coin textures after the original generated coin art was cropped into equal TTS-ready square textures.

## Consequences

Action and Ammo state remains encoded by coin side plus board location. Faction identity is not encoded in coin appearance.

## Review Conditions

Physical coin diameter, thickness, edge treatment, and manufacturing material remain unresolved.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Value: 8q2khIhd68nFOB_FcG1H0HwVVABGuVO4LMB_0qxtZwE

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:Rhf0vJn5r2VFO_JD4ovVIKU4Km8uNgd5M6u3dKF9EVk
