# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-19 12:50:13
  - Trace: [Post-playtest TTS surface](001-2-1-post-playtest-tts-surface.presentation.trace.md)
  - Origin:
    - [relative](001-2-1-post-playtest-tts-surface.presentation.trace.md)
- Current
  - Current Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-19 15:09:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Advance the TTS surface to the explicitly approved visual baseline without rewriting the first post-playtest surface.
  - Summary: TTS v0.3 presentation surface using six approved faction boards, shared coin art, and integrated quick reference.

---

# Approved-art TTS Surface

## Surface Identity

- Surface Name: Tower Havoc TTS approved-art playtest table
- Surface ID: tower-havoc.surface.tts-playtest.v3
- Surface Kind: composite
- Stability: experimental

## Surface Role

- Purpose: present the next-session Tower Havoc state using the approved faction boards, shared Action/Ammo coin, integrated quick reference, and current Dud-free card deck
- Primary Audience: playtesters and designer
- Primary Use: play, inspect, and record real-session behavior with lower manipulation and lookup overhead

## Interface Relationship

- Interface Relationship: inside-interface
- Interface Boundary: implemented inside Tabletop Simulator while remaining semantically bounded to the board-game table

## Content Boundary

- May Contain: six approved faction player-board textures; one shared double-sided Action/Ammo coin texture pair; tower floors; D6; shared bell object; current card deck; one shared card back; finished individual Event/Sabotage/Tactic faces when approved; visible persistent Event
- Must Not Contain: separate quick-reference cards; Dud cards; faction-specific coin mechanics; hidden rule state required for legal play; unreviewed generated card text treated as game authority

## Interaction Capability

- Supported Interactions: stack/flip shared coins; mark build/reinforcement/bell state; move tower floors; draw/play cards; roll dice; ring shared bell; record observations
- User Invocation: ordinary TTS interactions
- Write Capability: in-memory-only
- Side Effects: TTS save state only unless a human separately preserves session material

## Disclosure Boundary

- What Is Disclosed: persistent legal-play state plus integrated board quick reference and card-face rules
- What Is Hidden Or Deferred: final physical manufacturing geometry; unfinished individual card-front art; unresolved balance conclusions
- Expansion Path: GitHub Pages-hosted TTS assets and later preserved playtest Evidence

## Implementation Limits

- Does Not Provide: automatic rule correctness, final balance validation, physical handling evidence, or authority to change gameplay rules
- Must Not Be Used To Claim: generated artwork is a rules source, faction appearance creates mechanical asymmetry, or TTS behavior proves physical ergonomics

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Post-playtest TTS surface](001-2-1-post-playtest-tts-surface.presentation.trace.md)
  - Value: qjv1UBS5rSr0Ct4ZloaUKDcmd0hCGm5xYieArJDksSU

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:kHXweCbCboxJdBLRmFU-Htv8Z6-TD7C0XEC5plqzzEA
