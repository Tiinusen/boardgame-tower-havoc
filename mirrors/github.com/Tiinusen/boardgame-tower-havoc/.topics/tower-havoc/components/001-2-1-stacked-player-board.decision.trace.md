# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:57:00
  - Trace: [Visible player-state layout](001-2-visible-player-state.decision.trace.md)
  - Origin:
    - [relative](001-2-visible-player-state.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:11
  - Authors: Olle Tiinus; ChatGPT
  - Why: Turn the playtest handling observations into one compact board grammar before investing in final art.
  - Summary: PLAYTEST player-board successor using stack wells and printed floor/reinforcement positions.

---

# Stacked compact player-board layout

## Decision

- State: provisional/PLAYTEST
- Component Rule ID: components.player-state
- Stack Wells: Action Bank; Ready Ammo; Production
- Stack Well Geometry: each well uses the same coin-sized footprint and permits vertical stacking
- Quick Reference Slot: one faction or mode quick-reference card
- Tower Section: three floor rows; each row has 2 Build slots plus reinforcement positions labelled 2, 3, 4, and 5
- Reinforcement Representation: place one Action-face coin on the matching reinforcement position after paying the reinforcement action cost
- Bell Section: one Bell Build slot using an Action-face coin to show constructed/pending bell state
- Removed Zones: dedicated player-card slot; active-card slot; separate generic-reference-card slot
- Helper Text: concise turn start, draw attempt, attack cost, build cost, and bell sequence reminders may be printed where they reduce lookup
- Decision: use board location plus coin face to communicate persistent state, and stack fungible resources instead of spreading many tokens across large zones.

## Basis

The first TTS playtest showed that broad dedicated zones and handling several 2–5 markers were more cumbersome than useful. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

The board becomes substantially smaller. Built floors remain visible in the physical tower; Build slots are cost cues rather than partial-construction state. Reinforcement values become printed board positions, removing numbered reinforcement tokens.

## Review Conditions

Test legibility with generated TTS art first, then validate coin diameter and slot spacing in a physical prototype.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Visible player-state layout](001-2-visible-player-state.decision.trace.md)
  - Value: 9aha6Er1bbuZOe6z91r-um7LX91P7vXA-3KVCsmCNj4

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:19bazYZ2tfB8sxl7Ud83itxj4DwaGqqaoaI2_LEjUz0
