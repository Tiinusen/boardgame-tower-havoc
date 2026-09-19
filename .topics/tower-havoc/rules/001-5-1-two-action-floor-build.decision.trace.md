# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:37:00
  - Trace: [Three-floor building and burst cost](001-5-building.decision.trace.md)
  - Origin:
    - [relative](001-5-building.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:03
  - Authors: Olle Tiinus; ChatGPT
  - Why: Translate the playtest ergonomics finding into a simpler flat floor-build cost while avoiding accidental partial-construction semantics.
  - Summary: PLAYTEST successor: every tower floor costs 2 actions.

---

# Two-action floor construction

This artifact supersedes the 2/3/4 burst-cost curve for the next PLAYTEST iteration.

## Decision

- State: provisional/PLAYTEST
- Rule ID: rules.building
- Tower Floors Per Player: 3
- Build Cost Per Floor: 2 actions
- Same-Turn Multi-Floor Building: allowed when enough banked actions are available
- Three-Floor Burst Total: 6 actions
- Board Representation: each floor row exposes two Build slots sized for the shared Action/Ammo coin; the slots communicate the two-action cost
- Partial Construction State: none; both actions are paid when the floor is built, and the physical tower remains the authoritative visible built-floor state
- Decision: use one flat two-action floor cost so construction is easier to read and manipulate while preserving banked-action burst play.

## Basis

The first TTS playtest found repeated handling of variable build-cost tokens unnecessarily fiddly. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

The 2/3/4 curve is historical baseline material, not the next-session rule. Player-board construction rows show two cost positions for each floor; they do not create a new partially-built-floor state.

## Review Conditions

Review whether the lower total build cost accelerates tower completion too much after the next session.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Three-floor building and burst cost](001-5-building.decision.trace.md)
  - Value: 15EHsw82vMftwRqAqAdtr4WW7EXgc48s3Lo9B7HZll0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:iE0my_T_nWNBJuttXHIheIQM1Qmo6kinvax4TDL_Lac
