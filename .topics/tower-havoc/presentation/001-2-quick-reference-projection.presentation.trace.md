# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 02:14:00
  - Trace: [001-9-projection-surfaces.topic.trace](001-projection-surfaces.topic.trace.md)
  - Origin:
    - [relative](001-projection-surfaces.topic.trace.md)
- Current
  - Current Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-18 02:16:00
  - Authors: Olle Tiinus
  - Why: Keep the at-table quick reference as an explicit bounded projection.
  - Summary: Generated quick-reference projection

---
# Generated quick-reference projection

## Surface Identity

- Surface Name: Tower Havoc quick reference
- Surface ID: tower-havoc.surface.quick-reference.v1
- Surface Kind: card
- Stability: experimental

## Surface Role

- Purpose: present the minimum recurring turn/action/attack rules at the table
- Primary Audience: active players
- Primary Use: fast lookup during play

## Interface Relationship

- Interface Relationship: interface-independent
- Interface Boundary: printable card or TTS image generated from the same rule lineage

## Content Boundary

- May Contain: start-of-turn order; action costs; ammo production; attack D6 map; bell eligibility summary
- Must Not Contain: full rationale, hidden exceptions, or unrepresented rules

## Interaction Capability

- Supported Interactions: read
- User Invocation: generated with docs/TTS assets
- Write Capability: artifact-write
- Side Effects: regenerated helper output only

## Disclosure Boundary

- What Is Disclosed: compact recurring rules
- What Is Hidden Or Deferred: full card wording, rationale, playtest methodology
- Expansion Path: generated RULEBOOK.md and source lineage

## Implementation Limits

- Does Not Provide: a replacement for full rules when an edge case is disputed
- Must Not Be Used To Claim: omitted material does not exist

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-projection-surfaces.topic.trace](001-projection-surfaces.topic.trace.md)
  - Value: 2aCr4OMSfsWgIXVQGWTGfoCE5ti7kavgwh6JwamJxjM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: l1wRYUUMPDkqOCTp9PRZuQogoXxSqvNDDDZuVYJ-_cc