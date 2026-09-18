# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:42:00
  - Trace: [001-1-9-victory.decision.trace](001-9-victory.decision.trace.md)
  - Origin:
    - [relative](001-9-victory.decision.trace.md)
- Current
  - Current Schema: [tiinex.condition.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/condition/tiinex.condition.v1.schema.md)
  - Created At: 2026-09-18 01:43:00
  - Authors: Olle Tiinus
  - Why: Make the victory exposure gate independently inspectable and generatable.
  - Summary: Bell attempt eligibility condition

---
# Bell attempt eligibility condition

## Condition Identity

- Condition Name: Tower Havoc bell eligibility
- Condition Kind: prerequisite
- Condition State: not-evaluated
- Canonical Identifier: tower-havoc.condition.bell-eligibility.v1

## Condition Statement

- Condition: A player may attempt the bell only if that player had a complete three-floor tower when the current own turn began and still has all three floors at the moment of the attempt.
- Plain-Language Meaning: completing the tower does not immediately unlock victory; it must survive the other players' turns first.

## Evaluation Boundary

- Evaluation Scope: one player immediately before spending an action on a bell attempt
- Inputs Needed: tower state at start of current turn and current tower state
- Evaluation State: not-evaluated

## Branch Outcomes

- If Satisfied: the player may spend 1 action and make the current bell roll.
- If Not Satisfied: the player may not attempt the bell this turn.
- If Unknown: do not allow the attempt until start-of-turn tower state is established.

## Interpretation Limits

- Does Not Prove: that the current 1-in-6 success probability is balanced.
- Must Not Be Inferred: rebuilding the third floor during the current turn restores eligibility immediately.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-1-9-victory.decision.trace](001-9-victory.decision.trace.md)
  - Value: H_8VW-zjAUzjiNme7nbylQ-ymWUXAsJaMdYNWiydBz0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: FYbZwCrDf1NJr-nzmgLe7YHbq3nJOcpfueWS7Tcy8Hs
