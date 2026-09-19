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
  - Created At: 2026-09-18 02:03:00
  - Authors: Olle Tiinus
  - Why: Keep optional asymmetry distinct from core balance.
  - Summary: Optional Faction Module

---
# Optional Faction Module

## Current Read

Classic mode is the symmetric reference game. Faction mode is an optional later layer with six small asymmetries.

## Design Direction

Keep faction abilities roughly around one action-equivalent or a single-use tactical edge; do not use permanent multipliers to compensate for a weak core game.

## Next Artifacts

First balance tests use Classic. Faction ability Evidence belongs here only after the symmetric core has useful baseline data.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-tower-havoc.project.trace](../001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 2LX_20q7B6zk_nqfcj3e8_PB9Cae3Y6oRMZUWUmtsWg
