# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/8145c280093dff5d0b67db2aa72d5f5c12b6c7cb/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Trace: [001-tower-havoc.project.trace](001-tower-havoc.project.trace.md)
  - Origin:
    - [relative](001-tower-havoc.project.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/13991b5a13ab911ed9abd63646f92c8a9362ea01/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 02:18:00
  - Authors: Olle Tiinus
  - Why: Make the experiment intentionally artifact-native rather than using lineage only as a development diary.
  - Summary: Use Tiinex lineage as the canonical game source

---
# Use Tiinex lineage as the canonical game source

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Project Rule ID: continuity.lineage-authority
- Decision: `.topics/tower-havoc/**` is the canonical semantic source for the current game definition and its development continuity. `docs/**`, `data/**`, CAD briefs, TTS helper files, and similar consumable material should be generated or reconciled from that source wherever practical. Raw preserved source material may remain outside `.topics` when a Preservation artifact declares its boundary.

## Basis

This allows the same game definition to produce different views — rulebook, card manifest, CAD brief, TTS setup — without making each view a manually maintained competing authority.

## Consequences

Generated outputs carry a GENERATED header and source references. Manual edits to projections are expected to be overwritten. New game semantics should land as appropriately typed artifacts first.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-tower-havoc.project.trace](001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 1N_nR2U85au4R-cFhYfaQQdDat72dzG6AslRyMRkK9g