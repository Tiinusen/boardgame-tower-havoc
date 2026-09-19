# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.condition.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/condition/tiinex.condition.v1.schema.md)
  - Created At: 2026-09-18 01:43:00
  - Trace: [Bell attempt eligibility condition](001-9-1-bell-eligibility.condition.trace.md)
  - Origin:
    - [relative](001-9-1-bell-eligibility.condition.trace.md)
- Current
  - Current Schema: [tiinex.condition.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/knowledge/condition/tiinex.condition.v1.schema.md)
  - Created At: 2026-09-19 12:50:06
  - Authors: Olle Tiinus; ChatGPT
  - Why: Make the new bell-construction timing gate independently inspectable.
  - Summary: Condition for the post-playtest bell-construction sequence.

---

# Constructed bell readiness condition

## Condition Identity

- Condition Name: Tower Havoc constructed-bell readiness
- Condition Kind: prerequisite
- Condition State: not-evaluated
- Canonical Identifier: tower-havoc.condition.bell-eligibility.v2

## Condition Statement

- Condition: a player may attempt the bell only if that player previously spent 1 action to construct the bell while owning a complete three-floor tower, then began a later own turn after one full table orbit with all three floors still built and the bell construction still present.
- Plain-Language Meaning: first finish the tower, then build the bell, then survive the table before trying to ring it.

## Evaluation Boundary

- Evaluation Scope: one player immediately before spending an action on a bell attempt
- Inputs Needed: complete-tower state when bell construction was paid; bell construction state; current-turn start state; current tower state
- Evaluation State: not-evaluated

## Branch Outcomes

- If Satisfied: the player may spend 1 action and make the current bell roll.
- If Not Satisfied: the player may not attempt the bell this turn.
- If Unknown: do not allow the attempt until bell-construction timing and tower survival are established.

## Interpretation Limits

- Does Not Prove: the current 1-in-6 success probability or added orbit is balanced.
- Must Not Be Inferred: rebuilding destroyed floors during the same turn restores a matured bell automatically.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Bell attempt eligibility condition](001-9-1-bell-eligibility.condition.trace.md)
  - Value: FYbZwCrDf1NJr-nzmgLe7YHbq3nJOcpfueWS7Tcy8Hs

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:62buPrJKBol2p8DooZPtuzOBfTnS2InPd60TMZmJmj8
