# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Trace: [001-tower-havoc.project.trace.md](../001-tower-havoc.project.trace.md)
  - Origin:
    - [relative](../001-tower-havoc.project.trace.md)
- Current
  - Current Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Explore a gameplay representation where a complete Tower Havoc match can be reconstructed from typed artifacts and projected into human or automated play surfaces.
  - Summary: Artifact-native match provenance runtime

---

# Match Provenance Runtime

This branch treats gameplay itself as provenance, not only the design process.

## Current Read

Tower Havoc now has enough canonical rule semantics to define project-local match artifacts for setup, seats, turn order, actions, randomness, state, hidden information, and final result.

## Design Direction

Keep player intent separate from adjudicated resolution. Keep random requests separate from random results. Treat current state as a regenerable projection over a frozen ruleset and accepted resolutions. Preserve hidden information with commitments rather than exposing it prematurely.

## Risks

- schema proliferation without clear semantic boundaries
- accidentally treating GitHub comment order as game causality
- describing GitHub Actions RNG as cheat-proof when repository administrators still control workflow/history
- exposing hidden cards in a public event log

## Next Artifacts

- project-local gameplay schema family
- event-sourced match authority decision
- bounded GitHub Issue runtime task


---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-tower-havoc.project.trace.md](../001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: YGNSdvw4OzdD1k3VWRmMhp0S5U4zHoX4LuaqKDsxe9s
