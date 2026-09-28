# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-18 02:08:00
  - Trace: [TTS first-playtest surface](001-2-tts-playtest-surface.presentation.trace.md)
  - Origin:
    - [relative](001-2-tts-playtest-surface.presentation.trace.md)
- Current
  - Current Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-19 12:50:13
  - Authors: Olle Tiinus; ChatGPT
  - Why: Represent the redesigned digital table as a successor presentation surface rather than silently changing the first-playtest surface.
  - Summary: TTS v0.2 presentation surface for compact player boards and shared coins.

---

# Post-playtest TTS surface

## Surface Identity

- Surface Name: Tower Havoc TTS post-playtest table
- Surface ID: tower-havoc.surface.tts-playtest.v2
- Surface Kind: composite
- Stability: experimental

## Surface Role

- Purpose: present all analog-visible state required by the current next-session PLAYTEST rules in Tabletop Simulator
- Primary Audience: playtesters and designer
- Primary Use: play, inspect, and record real-session behavior with lower manipulation overhead

## Interface Relationship

- Interface Relationship: inside-interface
- Interface Boundary: implemented inside Tabletop Simulator but semantically limited to the board-game table

## Content Boundary

- May Contain: compact player boards; Action/Ammo coins; faction/mode quick-reference cards; tower blocks; D6; shared bell object; generated card deck; visible persistent Event; generated dieselpunk placeholder graphics
- Must Not Contain: hidden rule state required for legal play; final-art claims; automation that changes analog semantics

## Interaction Capability

- Supported Interactions: stack/flip coins; move tower floors; mark reinforcement positions; draw/play cards; roll dice; ring shared bell; record observations
- User Invocation: ordinary TTS interactions
- Write Capability: in-memory-only
- Side Effects: TTS save state only unless a human separately records playtest Evidence

## Disclosure Boundary

- What Is Disclosed: all persistent game state needed for legal decisions plus concise board helper text
- What Is Hidden Or Deferred: final art, final CAD, unresolved balance conclusions, physical handling results
- Expansion Path: GitHub Pages-hosted assets, future faction graphics, physical prototype Evidence

## Implementation Limits

- Does Not Provide: automatic rule correctness, physical handling evidence, final graphic design, or final balance validation
- Must Not Be Used To Claim: that the TTS surface itself is game authority or that digital coin handling proves physical ergonomics

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TTS first-playtest surface](001-2-tts-playtest-surface.presentation.trace.md)
  - Value: dhRi3HdcHHfd-mLRQEh8pRXdDKbXE9fatZ3SKpuElYs

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:qjv1UBS5rSr0Ct4ZloaUKDcmd0hCGm5xYieArJDksSU
