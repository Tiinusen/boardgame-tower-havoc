# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Trace: [001-tower-havoc.project.trace](../001-tower-havoc.project.trace.md)
  - Origin:
    - [relative](../001-tower-havoc.project.trace.md)
- Current
  - Current Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 02:14:00
  - Authors: Olle Tiinus
  - Why: Give generated outputs one semantic home without pretending generated documents are game rules.
  - Summary: Projection Surfaces

---
# Projection Surfaces

## Current Read

This branch defines bounded consumable views generated from the canonical Tower Havoc semantic model.

## Design Direction

Keep source authority in typed game artifacts. Projection surfaces declare what they expose, omit, and may rewrite so rulebook, quick-reference, machine manifests, and later views can be regenerated without becoming competing authorities.

## Next Artifacts

Add new Presentation Surface children only when a distinct reusable view has a real audience or tool boundary.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-tower-havoc.project.trace](../001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 2aCr4OMSfsWgIXVQGWTGfoCE5ti7kavgwh6JwamJxjM