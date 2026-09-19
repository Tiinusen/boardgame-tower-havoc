# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 02:07:00
  - Trace: [First TTS implementation baseline](001-1-first-tts-baseline.decision.trace.md)
  - Origin:
    - [relative](001-1-first-tts-baseline.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:12
  - Authors: Olle Tiinus; ChatGPT
  - Why: Advance the TTS prototype using the first real session instead of continuing the deliberately ugly v0.1 surface.
  - Summary: PLAYTEST TTS v0.2 baseline with compact board and Pages-hosted assets.

---

# Post-playtest TTS baseline

## Decision

- State: provisional/PLAYTEST
- Prototype ID: tts.v0.2
- Tower Floors: generic blocks remain sufficient while visual replacements are explored
- Cannon: generic pawn/token remains sufficient
- Resources: one double-sided Action/Ammo coin vocabulary
- Player Board: compact stacked layout with printed construction and reinforcement positions
- Quick Reference: faction/mode-specific quick-reference card seated in the board slot
- Cards: generated 34-card dud-free deck
- Asset Delivery: load generated public assets from the repository GitHub Pages publication rather than GitHub repository permalink URLs
- Scripting Required: no
- Hidden Automation: avoid
- Decision: keep rule state analog-visible while improving ergonomics and presentation enough for the next real session.

## Basis

The first TTS session succeeded as a rules test but exposed asset-hosting, player-mat, token-handling, quick-reference, and visual-presentation weaknesses. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

The TTS asset generator now produces the compact board, coin faces, and a Classic mode quick-reference card; GitHub Pages exposes stable HTTP paths for those outputs.

## Review Conditions

Do not treat better graphics as gameplay validation; keep visual iteration replaceable.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [First TTS implementation baseline](001-1-first-tts-baseline.decision.trace.md)
  - Value: ZXqiw05dWyYzvbega-xJql6MX6k29Ffgr1KYNnWfvUQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:FJodxMYZQmaIKZ2QVbI3Mq_FXz_SE-8990l7vZXfWMs
