# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 15:05:00
  - Trace: [Approved Card Visual System](001-3-card-visual-system.decision.trace.md)
  - Origin:
    - [relative](001-3-card-visual-system.decision.trace.md)
- Current
  - Current Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 15:06:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Define the bounded production queue for the fifteen unique card faces needed by the current deck.
  - Summary: Pending production task for all fifteen unique current-deck card-front images.

---

# Produce Individual Card Fronts

## Objective

Create one production-ready card-front image for every unique face in the current 34-card Dud-free deck, using the accepted visual reference for its presentation family and preserving the exact current gameplay text.

## Done Criteria

- one Sabotage face exists
- four Offensive Reroll faces exist for printed values 2, 3, 4, and 5
- one Defensive Reroll face exists
- one Upper Hand face exists
- one Plunder face exists
- one Overtime face exists
- six Event faces exist: Ammunition Shortage, Production Boom, Panic Production, Damp Powder, Ceasefire, Building Strike
- all fifteen unique faces use the correct Event, Sabotage, or Tactic reference
- generated face text is checked against `../cards/**` before TTS deck-sheet materialization
- duplicate physical cards reuse the corresponding approved face

## Scope

- Preserve the accepted frame geometry, typography hierarchy, color family, and illustration placement from the supplied reference image.
- Generate a single isolated card per image, not a montage, contact sheet, mockup, or combined card set.
- Do not invent new effects, flavor rules, costs, timing, quantities, card families, or Dud cards.
- The reference image controls visual style; the card lineage controls gameplay text.
- Final TTS face normalization and deck-sheet packing happen only after the individual images are reviewed.

## Dependencies

- `001-3-card-visual-system.decision.trace.md`
- `../cards/001-1-1-dud-free-deck.decision.trace.md`
- `../cards/001-2-sabotage.decision.trace.md`
- `../cards/001-3-offensive-reroll.decision.trace.md`
- `../cards/001-4-defensive-reroll.decision.trace.md`
- `../cards/001-6-upper-hand.decision.trace.md`
- `../cards/001-7-plunder.decision.trace.md`
- `../cards/001-8-overtime.decision.trace.md`
- `../cards/001-9-global-events.decision.trace.md`
- `../../../art/approved/card-references/card-back-reference.png`
- `../../../art/approved/card-references/event-front-reference.png`
- `../../../art/approved/card-references/sabotage-front-reference.png`
- `../../../art/approved/card-references/tactic-front-reference.png`

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Approved Card Visual System](001-3-card-visual-system.decision.trace.md)
  - Value: 6B02XH07aZFLZd7QMtbcu9wjmedQ6VQb3RK6WGbOeBo

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:X87JAQyNubj8HT-nr9NjLDasdHTI3kFAWBYur5HYrP0
