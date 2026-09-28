# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.evidence.v1](https://github.com/Tiinex/docs/blob/e713557f8be630967571d11a73f9ecd05ae329ce/.topics/.schemas/core/evidence/tiinex.evidence.v1.schema.md)
  - Created At: 2026-09-19 16:10:00
  - Trace: [Pre-Pilot Manual Card Generation Evidence](001-pre-pilot-manual-generation.evidence.trace.md)
  - Origin:
    - [relative](001-pre-pilot-manual-generation.evidence.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/e713557f8be630967571d11a73f9ecd05ae329ce/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 16:11:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Record the bounded source-review outcome from the first manual card batch without erasing rejected geometry or promoting it into final acceptance.
  - Summary: Three 5:7 source candidates retained, three 4:7 candidates routed to explicit retry, and Offensive Reroll — 2 selected as the next Tactic production reference.
  - Status: ready/local

---

# Pre-Pilot Card Source Review

## Decision

- State: production-review disposition; not final project acceptance
- Reusable Source Candidates:
  - `001-generated-sabotage.png` — 1060×1484, exact 5:7; text/layout reviewed as matching current Sabotage semantics
  - `001-generated-offensive-reroll-2.png` — 1060×1484, exact 5:7; text/layout reviewed as matching current printed-value 2 semantics
  - `001-generated-offensive-reroll-3.png` — 1060×1484, exact 5:7; text/layout reviewed as matching current printed-value 3 semantics
- Retry Required:
  - `001-generated-defensive-reroll.png` — returned 948×1659 (4:7 rather than 5:7)
  - `001-generated-offensive-reroll-4.png` — returned 948×1659 (4:7 rather than 5:7)
  - `001-generated-offensive-reroll-5.png` — returned 948×1659 (4:7 rather than 5:7)
- Production Reference For Remaining Tactic Routes: `001-generated-offensive-reroll-2.png`
- Deterministic Stretch/Crop Of 4:7 Candidates: rejected for current production because it would either distort the accepted layout or remove source content.

## Basis

The 5:7 candidates preserve the intended production geometry and the reviewed current card text. The 4:7 candidates are visually useful but cannot be normalized to the same production frame without a material crop or non-uniform stretch.

## Consequences

Remaining Tactic generation routes use the exact Offensive Reroll — 2 source as their strict visual reference. The three 4:7 outputs remain Evidence rather than being overwritten or silently repaired. Event production begins with one new Ammunition Shortage route against the approved Event design reference; a successful 5:7 Event result may become the later Event production reference.

## Review Conditions

Steward project-level source acceptance remains separate. Final TTS normalization and deck-sheet assembly remain later deterministic derivative work.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Pre-Pilot Manual Card Generation Evidence](001-pre-pilot-manual-generation.evidence.trace.md)
  - Value: o1-d-axFzTxY7mqX9VlQQwxjVuc2uaMHyf3oYLbixC8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:R-tDODuS2IKe1ycM2eBQzwsrbbYZIliUOEUCdfu0kBE
