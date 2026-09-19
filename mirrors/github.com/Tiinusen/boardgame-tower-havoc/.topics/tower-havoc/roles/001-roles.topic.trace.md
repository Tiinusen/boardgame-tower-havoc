# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Trace: [Tower Havoc](../001-tower-havoc.project.trace.md)
  - Origin:
    - [relative](../001-tower-havoc.project.trace.md)
- Current
  - Current Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 12:40:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Make collaboration and gameplay responsibilities explicit without coupling them to concrete people, models, sessions, or implementations.
  - Summary: Reusable Tower Havoc role endpoints for project, continuity, match, and participant responsibilities.
  - Status: ready/local

---

# Tower Havoc Roles

This topic owns the reusable Tower Havoc role endpoints used to separate project authority,
design/continuity work, match adjudication, and player participation from the concrete humans,
LLMs, bots, or runtimes that may hold those capacities.

## Current Read

Tower Havoc needs explicit roles so collaboration and gameplay can be transported without
treating a person name, model identity, chat session, repository account, or bot implementation
as semantic authority. Role identity and holder identity remain separate.

The current reusable roles are:

- Steward — project stewardship, game-design authority, and human acceptance.
- Cartographer — design-system analysis, continuity modelling, and provenance-aware artifact materialization.
- Keeper — match execution, adjudication, integrity review, replay, and simulation.
- Player — bounded match participant and seat decision-maker.

## Design Direction

Keep these roles as sibling Role artifacts under one Roles Topic. Do not encode authority,
delegation, collaboration, or match participation by making one Role the Parent of another.

Concrete holder assignment must follow the active `tiinex.party.role.v1` Holder Relationship
contract and separately qualified binding evidence. A Role reference alone never proves a
current holder, delegation, participation, acceptance, source-mutation authority, or legal
ownership.

## Next Artifacts

- holder/session bindings only when a concrete workflow requires them
- Handoffs or Tasks that target one of these reusable capacities
- match artifacts that bind Player/Keeper participation without turning role identity into seat identity

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc](../001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 9rv6NpjrEL3GEkrga-dhcY8_xpcD9hNCAP6WKDtOnLg
