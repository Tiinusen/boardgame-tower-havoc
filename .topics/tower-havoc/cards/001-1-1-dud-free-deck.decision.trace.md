# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:45:00
  - Trace: [Forty-card prototype deck](001-1-deck-composition.decision.trace.md)
  - Origin:
    - [relative](001-1-deck-composition.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:08
  - Authors: Olle Tiinus; ChatGPT
  - Why: Create a clean next-session deck baseline after the first real playtest.
  - Summary: PLAYTEST deck successor with Duds removed and 34 total cards.

---

# Dud-free thirty-four-card deck

## Decision

- State: provisional/PLAYTEST
- Rule ID: cards.deck
- Total Cards: 34

| Family | Quantity | Type |
|---|---:|---|
| Sabotage | 6 | tactic |
| Offensive Reroll | 8 | tactic |
| Defensive Reroll | 4 | tactic |
| Upper Hand | 2 | tactic |
| Plunder | 4 | tactic |
| Overtime | 4 | tactic |
| Global Events | 6 | event |

- Decision: remove all six Dud cards and test the remaining 34-card composition before adding replacements.

## Basis

The first TTS playtest reported that Duds reduced motivation to engage with card draw. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

Generated manifests, TTS deck sheets, component counts, and recycle behavior use 34 cards for the next baseline.

## Review Conditions

Evaluate draw frequency and card-family pressure before deciding whether the deck should return to 40 cards.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Forty-card prototype deck](001-1-deck-composition.decision.trace.md)
  - Value: F0v-M4ghximtaqMcZXq4nDLYVvA8nS5FTy2fT6gMAa8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:2RR1icIdCIRulNrffkiV3ltSgIeZI5USzmzu4VXE6B4
