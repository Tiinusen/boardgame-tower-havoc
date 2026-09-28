# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:12
  - Trace: [Post-playtest TTS baseline](001-1-1-post-playtest-tts-baseline.decision.trace.md)
  - Origin:
    - [relative](001-1-1-post-playtest-tts-baseline.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 15:11:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Advance the next TTS baseline to the explicitly approved art without rewriting the earlier v0.2 prototype decision.
  - Summary: PLAYTEST TTS v0.3 baseline with six approved faction boards, shared coin art, integrated quick reference, and card art pending individual faces.

---

# Approved-art TTS Baseline

## Decision

- State: provisional/PLAYTEST
- Prototype ID: tts.v0.3
- Tower Floors: generic blocks remain sufficient until approved tower-floor geometry/art exists
- Cannon: generic pawn/token remains sufficient
- Resources: one shared double-sided Action/Ammo coin using the approved common texture pair
- Player Boards: six approved faction board textures with identical gameplay layout
- Quick Reference: printed directly on every player board; no separate quick-reference card object
- Cards: current 34-card Dud-free draw deck; one common back; Event/Sabotage/Tactic front families
- Card Art State: common back and three front-family visual references approved; individual current-deck faces still pending review
- Asset Delivery: load published TTS assets from the repository GitHub Pages surface
- Scripting Required: no
- Hidden Automation: avoid
- Decision: use the approved-art player boards and shared coin for the next TTS session while keeping unfinished individual card faces explicitly provisional.

## Basis

The project Steward explicitly approved the six faction boards, shared coin art, and card visual references after iterative review.

## Consequences

The TTS asset surface no longer generates or exposes the obsolete generic player mat or separate quick-reference card. Faction identity is visual only; all six boards share one state layout.

## Review Conditions

Individual card faces must be produced and checked against card lineage before the card deck is considered visually complete.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Post-playtest TTS baseline](001-1-1-post-playtest-tts-baseline.decision.trace.md)
  - Value: FJodxMYZQmaIKZ2QVbI3Mq_FXz_SE-8990l7vZXfWMs

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:BgosNcQiDve2SlHQ9wW8wFairF1-tLgSaWoRr7OGbk0
