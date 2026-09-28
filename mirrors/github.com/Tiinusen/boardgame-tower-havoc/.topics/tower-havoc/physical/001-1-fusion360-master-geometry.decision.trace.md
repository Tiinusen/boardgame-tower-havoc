# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-18 02:09:00
  - Trace: [001-7-physical-prototype-and-cad.task.trace](001-physical-prototype-and-cad.task.trace.md)
  - Origin:
    - [relative](001-physical-prototype-and-cad.task.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 02:10:00
  - Authors: Olle Tiinus
  - Why: Prevent aesthetic work from hard-coding untested mechanics.
  - Summary: Fusion 360 neutral master before faction variants

---
# Fusion 360 neutral master before faction variants

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- CAD Rule ID: cad.master
- Decision: Begin physical modeling from one parametric mechanically neutral tower-floor master. Preserve shared bounding box, footprint, stacking/contact area, height, alignment, stability envelope, reinforcement interfaces, and access. Create cosmetic faction variants only after the master survives physical stacking tests.
- Reinforcement Interface Options: slots; holes; pegs; clips; magnets; adjacent marker positions
- First Prototype Priority: visibility and easy removal over realism

## Basis

The most expensive mistake would be sculpting six visually rich factions before the mechanical interface is known to work.

## Consequences

CAD parameters remain editable. Final dimensions, connector technology, board size, decorative mass distribution, and packaging tolerances stay open until physical evidence exists.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-7-physical-prototype-and-cad.task.trace](001-physical-prototype-and-cad.task.trace.md)
  - Value: UePhDkLfbGUTAqOj-UY4rkMpTUsr58ocrCH11jQTIAw

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: x7iQ8yV_SdsGn26kFbATS4xgdgji6bxHZ_npw_Gmylc
