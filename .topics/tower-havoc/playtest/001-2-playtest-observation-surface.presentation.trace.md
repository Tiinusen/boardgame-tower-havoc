# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-18 02:11:00
  - Trace: [001-8-playtest-program.task.trace](001-playtest-program.task.trace.md)
  - Origin:
    - [relative](001-playtest-program.task.trace.md)
- Current
  - Current Schema: [tiinex.presentation.surface.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/presentation/surface/tiinex.presentation.surface.v1.schema.md)
  - Created At: 2026-09-18 02:13:00
  - Authors: Olle Tiinus
  - Why: Define the observation surface now without fabricating Evidence before a session exists.
  - Summary: Playtest observation checklist

---
# Playtest observation checklist

## Surface Identity

- Surface Name: Tower Havoc playtest observation checklist
- Surface ID: tower-havoc.surface.playtest-observation.v1
- Surface Kind: checklist
- Stability: experimental

## Surface Role

- Purpose: prompt consistent observations without turning player impressions into conclusions
- Primary Audience: designer / session recorder
- Primary Use: recording comparable session observations

## Interface Relationship

- Interface Relationship: interface-independent
- Interface Boundary: may be paper, Markdown, spreadsheet, or digital form

## Content Boundary

- May Contain: player count; duration; rounds; build timing; attacks/hits; fortification; Sabotage use; bell attempts; strategy shifts; unclear rules; downtime; card impressions; post-game answers
- Must Not Contain: invented observations, automatic balance conclusions, or fabricated Evidence

## Interaction Capability

- Supported Interactions: record observations and bounded player feedback
- User Invocation: recorder fills during/after session
- Write Capability: draft-only
- Side Effects: none until a real session artifact is deliberately preserved

## Disclosure Boundary

- What Is Disclosed: the observations requested for comparison
- What Is Hidden Or Deferred: design conclusion and rule-change authority
- Expansion Path: future tiinex.evidence.v1 session artifacts followed by Decisions where warranted

## Implementation Limits

- Does Not Provide: proof of fun, balance, or statistical significance
- Must Not Be Used To Claim: that one player's reaction is representative of all players

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-8-playtest-program.task.trace](001-playtest-program.task.trace.md)
  - Value: D34kCPLAaVs1DZB5tFHPq7jDTei_oPGIZA1RZrqsdG8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: dSLuKXTuw-DDGZHLI2mrgxfwVYnuxAQ_GHgRZu_1cag