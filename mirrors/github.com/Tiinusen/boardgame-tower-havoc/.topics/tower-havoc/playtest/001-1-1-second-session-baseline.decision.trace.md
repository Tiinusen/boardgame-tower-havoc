# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 02:12:00
  - Trace: [First-session comparison baseline](001-1-first-session-baseline.decision.trace.md)
  - Origin:
    - [relative](001-1-first-session-baseline.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:16
  - Authors: Olle Tiinus; ChatGPT
  - Why: Freeze one reproducible next-session configuration after the first real playtest.
  - Summary: PLAYTEST baseline.002 for the next TTS session.

---

# Second-session post-playtest baseline

## Decision

- State: provisional/PLAYTEST
- Session Baseline ID: playtest.baseline.002
- Recommended Players: 3–4
- Mode: Classic
- Deck: 34-card dud-free prototype deck
- Floor Build Cost: 2 actions per floor
- Attack Cost: 1 action plus 1 Ready Ammo
- Attack Limit: maximum 1 attack per player turn
- Draw Attempt: 1 action; D6 1 or 6 draws one card; failure may be retried for another action; first success ends card drawing for that turn
- Turn Start: gain 1 action first, then resolve event expiry and Production maturity
- Bell Sequence: build bell for 1 action after completing the tower; survive one full orbit; then spend 1 action for a bell attempt
- Bell Success: D6 result 1
- Bell Attempt Limit: maximum 1 per player turn
- Player Surface: compact stacked board with double-sided Action/Ammo coins and faction/mode quick-reference slot
- Decision: use this complete successor baseline for the next real session so the first-session findings can be tested together rather than mixed with ad-hoc mid-match changes.

## Basis

This baseline responds directly to `001-3-first-tts-playtest.evidence.trace.md` and the successor Decisions under rules, cards, components, and digital surfaces.

## Consequences

New generated docs/assets target baseline.002. The first-session baseline and TH-SIM fixtures remain preserved as historical/frozen material.

## Review Conditions

Record which parts feel better or worse separately; do not promote this bundle of changes to final rules merely because they are coherent on paper.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [First-session comparison baseline](001-1-first-session-baseline.decision.trace.md)
  - Value: q9iYdNXd4ajvg_mkEiToaB0YFMOtZyNXE0vBHQKnz4c

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:DqyjL2PHi9l_6C-STTrr3uaDvXyOqnvVNZrJ8MCuFJo
