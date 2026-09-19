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
  - Created At: 2026-09-18 02:17:00
  - Authors: Olle Tiinus
  - Why: Make machine-readable output an explicit projection rather than a second manual source of truth.
  - Summary: Generated machine-manifest projections

---
# Generated machine-manifest projections

## Surface Identity

- Surface Name: Tower Havoc machine manifests
- Surface ID: tower-havoc.surface.machine-manifests.v1
- Surface Kind: table
- Stability: experimental

## Surface Role

- Purpose: materialize card, component, and prototype-constant data for scripts and TTS asset generation
- Primary Audience: prototype tooling and maintainers
- Primary Use: machine-readable projection

## Interface Relationship

- Interface Relationship: tool-facing
- Interface Boundary: generated JSON/CSV files consumed by local scripts

## Content Boundary

- May Contain: card instances; component inventory; current prototype constants; source artifact references
- Must Not Contain: independent semantic authority or untraceable constants

## Interaction Capability

- Supported Interactions: read by scripts; regenerate from lineage
- User Invocation: `python scripts/generate_from_topics.py`
- Write Capability: artifact-write
- Side Effects: rewrites generated data files

## Disclosure Boundary

- What Is Disclosed: normalized data needed by prototype tooling
- What Is Hidden Or Deferred: full rationale and project history
- Expansion Path: each generated record includes or is backed by a source trace path

## Implementation Limits

- Does Not Provide: a license to edit JSON/CSV as canonical game design
- Must Not Be Used To Claim: a generated manifest supersedes its source Decision

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-projection-surfaces.topic.trace](001-projection-surfaces.topic.trace.md)
  - Value: 2aCr4OMSfsWgIXVQGWTGfoCE5ti7kavgwh6JwamJxjM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: p7wV77bMnWXvzgMJk_to7S8TNLduRi1QCPEMFi3wCAw
