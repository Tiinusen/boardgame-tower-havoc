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
  - Created At: 2026-09-18 02:15:00
  - Authors: Olle Tiinus
  - Why: Explicitly model the rulebook as a projection surface rather than a competing source of truth.
  - Summary: Generated rulebook projection

---
# Generated rulebook projection

## Surface Identity

- Surface Name: Tower Havoc generated rulebook
- Surface ID: tower-havoc.surface.rulebook.v1
- Surface Kind: print
- Stability: experimental

## Surface Role

- Purpose: render current game rules into a player-readable document from the semantic lineage
- Primary Audience: players and playtesters
- Primary Use: learn and reference current playable rules

## Interface Relationship

- Interface Relationship: interface-independent
- Interface Boundary: Markdown/print projection; not the semantic authority itself

## Content Boundary

- May Contain: current setup, turns, actions, building, attacks, reinforcement, collapse, cards, events, victory, and explicit PLAYTEST markers derived from `.topics/tower-havoc/**`
- Must Not Contain: silently invented rules or claims that generated prose outranks its source artifacts

## Interaction Capability

- Supported Interactions: read, print, navigate to source lineage
- User Invocation: run `python scripts/generate_from_topics.py` or read the committed generated output
- Write Capability: artifact-write
- Side Effects: rewrites generated documentation files only

## Disclosure Boundary

- What Is Disclosed: player-facing current rule projection
- What Is Hidden Or Deferred: detailed rationale and full project-development history
- Expansion Path: source artifact paths are listed in generated headers and remain resolvable from the canonical `.topics/tower-havoc/**` artifact tree

## Implementation Limits

- Does Not Provide: independent rule authority or evidence that the source model is balanced
- Must Not Be Used To Claim: manual edits to generated files changed the canonical game

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-projection-surfaces.topic.trace](001-projection-surfaces.topic.trace.md)
  - Value: 2aCr4OMSfsWgIXVQGWTGfoCE5ti7kavgwh6JwamJxjM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: F1Z-lLKCiaJtf1FssobZY4GHmuesbu3RbjMPIwBoQ-U
