# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-18 02:06:00
  - Trace: [001-6-tabletop-simulator-prototype.task.trace](001-tabletop-simulator-prototype.task.trace.md)
  - Origin:
    - [relative](001-tabletop-simulator-prototype.task.trace.md)
- Current
  - Current Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-18 02:08:00
  - Authors: Olle Tiinus
  - Why: Model the digital table as a presentation surface rather than treating TTS itself as game authority.
  - Summary: TTS first-playtest surface

---
# TTS first-playtest surface

## Surface Identity

- Surface Name: Tower Havoc TTS first-playtest table
- Surface ID: tower-havoc.surface.tts-first-playtest.v1
- Surface Kind: composite
- Stability: experimental

## Surface Role

- Purpose: present all state required to play the analog rules in Tabletop Simulator
- Primary Audience: playtesters and designer
- Primary Use: play, inspect, and record first-session behavior

## Interface Relationship

- Interface Relationship: inside-interface
- Interface Boundary: implemented inside Tabletop Simulator but semantically limited to the board-game table

## Content Boundary

- May Contain: player mats; tower blocks; counters; D6; bell object; generated card deck; visible active Event
- Must Not Contain: hidden rule state required to understand legal play; final-art claims; automation that changes analog semantics

## Interaction Capability

- Supported Interactions: move pieces; draw/play cards; roll dice; count resources; record observations
- User Invocation: ordinary TTS interactions
- Write Capability: in-memory-only
- Side Effects: TTS save state only unless a human separately records a playtest artifact

## Disclosure Boundary

- What Is Disclosed: all persistent game state needed for legal decisions
- What Is Hidden Or Deferred: final art, final CAD, unresolved balance conclusions
- Expansion Path: generated rulebook, playtest task, and later Evidence artifacts

## Implementation Limits

- Does Not Provide: automatic rule correctness, balance validation, physical handling evidence, or final presentation quality
- Must Not Be Used To Claim: that a digital session reproduces every tactile property of the physical game

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-6-tabletop-simulator-prototype.task.trace](001-tabletop-simulator-prototype.task.trace.md)
  - Value: PwHnOq22J1ij6hTnodRn4sJffaXh2UGhbngkCes2oPM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: dhRi3HdcHHfd-mLRQEh8pRXdDKbXE9fatZ3SKpuElYs
