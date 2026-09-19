# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:10
  - Trace: [Compact shared-coin prototype inventory](001-1-1-compact-coin-inventory.decision.trace.md)
  - Origin:
    - [relative](001-1-1-compact-coin-inventory.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 15:07:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Reconcile the approved integrated board with the current component inventory without rewriting the prior playtest successor.
  - Summary: PLAYTEST component-inventory successor with integrated board reference and no separate quick-reference card.

---

# Integrated Board Prototype Inventory

## Decision

- State: provisional/PLAYTEST
- Component Manifest ID: components.mvp.v3

| Component | Quantity | Prototype Substitute | Constraint |
|---|---:|---|---|
| Faction player board | 6 | approved TTS board art | identical gameplay layout; integrated quick reference; one visual variant per faction |
| Tower floor | 18 | generic block | 3 per player; identical mechanical envelope |
| Light field cannon | 6 | pawn/token | theme/readability only; no real projectile required |
| D6 | 2 | standard die | one required plus one spare |
| Shared bell | 1 | obvious bell object | theatrical ring object; per-player bell construction state lives on each board |
| Action/Ammo coin | 144 | shared double-sided coin/token | one common visual design; Action face and Ammo face; stack in resource wells |
| Card | 34 | current Dud-free draw deck | one common back and three visual front families |

- Removed Component: separate faction/mode quick-reference card
- Decision: integrate the quick reference into each player board and keep the rest of the compact shared-coin inventory.

## Basis

The approved board layout makes a separate quick-reference card redundant and reduces table handling further.

## Consequences

Generated component projections and TTS setup no longer require a quick-reference card object or slot.

## Review Conditions

Final physical quantities and production dimensions remain subject to later physical handling evidence.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Compact shared-coin prototype inventory](001-1-1-compact-coin-inventory.decision.trace.md)
  - Value: P8BYIxmjuoZIewd6pDN6EF80rNRFjFZhwUyLwYfGaGI

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:SbbjkNq9d0bm9AW60b_XWdLI5GgVTsp6E1VaNjdyZjY
