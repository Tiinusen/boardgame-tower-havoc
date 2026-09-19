# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:38:00
  - Trace: [001-1-6-attack.decision.trace](001-6-attack.decision.trace.md)
  - Origin:
    - [relative](001-6-attack.decision.trace.md)
- Current
  - Current Schema: [tiinex.condition.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/condition/tiinex.condition.v1.schema.md)
  - Created At: 2026-09-18 01:39:00
  - Authors: Olle Tiinus
  - Why: Express the attack branch as a Condition rather than burying an if/else gate inside prose.
  - Summary: Attack hit resolution condition

---
# Attack hit resolution condition

## Condition Identity

- Condition Name: Tower Havoc attack hit resolution
- Condition Kind: gate
- Condition State: not-evaluated
- Canonical Identifier: tower-havoc.condition.attack-hit.v1

## Condition Statement

- Condition: After an attack targets a built floor and rolls D6, the shot destroys that floor only when the result is 2, 3, 4, or 5 and the target floor does not currently have reinforcement for that exact value.
- Plain-Language Meaning: 1 and 6 miss automatically; a side value hits only when that side is open.

## Evaluation Boundary

- Evaluation Scope: one paid attack against one chosen built floor
- Inputs Needed: D6 result and visible reinforcement state of the target floor
- Evaluation State: not-evaluated

## Branch Outcomes

- If Satisfied: destroy the targeted floor and apply the collapse rule to every floor above it.
- If Not Satisfied: the attack causes no tower destruction.
- If Unknown: do not resolve destruction until the die result and reinforcement state are readable.

## Interpretation Limits

- Does Not Prove: that the attack-frequency balance is correct or that physical geometry literally simulates ballistic physics.
- Must Not Be Inferred: reinforcement on another floor or another value protects the target result.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-6-attack.decision.trace](001-6-attack.decision.trace.md)
  - Value: BwhmeXLyNLdZRv9Topm-QYDyca5lW4W7675bubMPu-s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: pKAAdYMidBIyrgxerJ4OralHpy0ZCammC1Qbim1XHmI
