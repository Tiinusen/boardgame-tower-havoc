# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:56:00
  - Trace: [Prototype component inventory](001-1-component-inventory.decision.trace.md)
  - Origin:
    - [relative](001-1-component-inventory.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:10
  - Authors: Olle Tiinus; ChatGPT
  - Why: Reduce token vocabulary and board footprint in response to actual TTS handling friction.
  - Summary: PLAYTEST component inventory centered on one double-sided Action/Ammo coin.

---

# Compact shared-coin prototype inventory

## Decision

- State: provisional/PLAYTEST
- Component Manifest ID: components.mvp.v2

| Component | Quantity | Prototype Substitute | Constraint |
|---|---:|---|---|
| Compact player board | 6 | printed/TTS board | coin-sized stack wells plus tower-construction rows and faction/mode quick-reference slot |
| Faction or mode quick-reference card | 6 | printed/TTS card | one per player; Classic uses a Classic-mode card instead of a separate generic reference card |
| Tower floor | 18 | generic block | 3 per player; identical mechanical envelope |
| Light field cannon | 6 | pawn/token | theme/readability only; no real projectile required |
| D6 | 2 | standard die | one required plus one spare |
| Shared bell | 1 | obvious bell object | theatrical ring object; per-player bell construction state lives on each board |
| Action/Ammo coin | 144 | double-sided coin/token | Action face on one side; Ammo face on the other; one shared physical vocabulary for Action Bank, Ready Ammo, Production, build/reinforcement markers, and bell construction |
| Card | 34 | generated prototype deck | next PLAYTEST deck manifest comes from card lineage |

## Basis

The first TTS playtest found the broad mat and multiple token families cumbersome. Reusing the former combined ammo/reinforcement token budget as one 144-coin pool avoids prematurely optimizing an exact physical quantity. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

Separate Ammo tokens, reinforcement markers, action trackers, generic reference cards, player-card slots, and active-card slots are removed from the next prototype inventory.

## Review Conditions

Physical coin diameter, thickness, final pool quantity, and production material remain unresolved until a physical handling test exists.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Prototype component inventory](001-1-component-inventory.decision.trace.md)
  - Value: KFVa__Wl6U2Ym6Mjt4_EnFSkEZnhn0VJHqVUANpKNTM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:P8BYIxmjuoZIewd6pDN6EF80rNRFjFZhwUyLwYfGaGI
