# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 12:40:00
  - Trace: [Tower Havoc Roles](001-roles.topic.trace.md)
  - Origin:
    - [relative](001-roles.topic.trace.md)
- Current
  - Current Schema: [tiinex.party.role.v1](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.schemas/party/role/tiinex.party.role.v1.schema.md)
  - Created At: 2026-09-18 12:40:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Represent participant agency separately from person identity, seat identity, faction identity, and match adjudication.
  - Summary: Reusable Tower Havoc match participant and seat decision-maker role.
  - Status: ready/local

---

# Player Role

## Role Identity

- Role Label: Player
- Role Kind: Tower Havoc bounded match participant and seat decision-maker
- Canonical Identifier: tower-havoc.role.player
- Project: Tower Havoc

## Role Boundary

- In Scope: one explicitly bound match seat; choosing among permitted gameplay options; submitting Action Intents; choosing targets/cards/resources where the rules allow; passing; responding to required match prompts; performing a declared physical procedure such as rolling a die when that procedure is assigned to the holder.
- Out Of Scope: self-adjudicating legality or results; mutating authoritative state directly; choosing the outcome of randomness; seeing hidden information belonging to another seat without explicit access; changing the frozen ruleset; project-level design acceptance; licensing/publication authority.
- Context: Player represents participant agency in a match. Seat identity, person/model identity, faction identity, and Role identity remain separate and must be explicitly bound where they matter.

## Authority And Responsibility Boundary

- May Do: select or accept a seat/faction when allowed; choose legal strategy and actions; submit one or more bounded Action Intents according to turn rules; use cards/resources within the rules; perform assigned physical random procedures and report observations through the declared runtime path; request review when an adjudication appears inconsistent.
- Does Not Authorize: accepting its own Action Intent as legal; editing `towerhavoc.state.v1` directly; inventing or rerolling randomness outside the declared procedure; inspecting unauthorized opponent hidden state; changing commitments after publication; declaring itself winner without the governing resolution/result path; changing project rules or rights.
- Required Instrument: Player operation requires an explicit match/session context, one seat binding, the governing frozen ruleset, and the current authorized state/visibility surface.
- Delegation: Player strategy may be assisted by another person/tool/LLM only within the match's allowed assistance boundary. Assistance does not silently transfer seat ownership or create Keeper authority.
- Review Boundary: Player owns strategic choice and expressed intent for the assigned seat. Keeper adjudicates legality/result; Steward owns game-design consequences outside the match.

## Holder Relationship

- Holder State: assignable to one bounded match seat for a declared session, invocation, Handoff, or explicit participation context; no permanent holder asserted.
- Assignment Modes: explicit-session, explicit-user-session, explicit-role-invocation, handoff, explicit-participation
- Possible Holder: a human, LLM, bot, agent, or other participant explicitly bound to one Tower Havoc seat under the match's participation and assistance rules.

## Interpretation Limits

- Does Not Prove: real-world identity, fair play, consent to publication, ownership of Tower Havoc, authority over another seat, that every submitted intent is legal, or that a holder actually participated merely because the Role exists.
- Must Not Be Treated As: Keeper adjudication authority, Steward project authority, omniscient game-state access, repository credential, contributor-rights grant, or evidence that a match action occurred unless the relevant runtime/resolution artifacts support it.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Roles](001-roles.topic.trace.md)
  - Value: jHvHszvvdDaeiWtgMsBFkrpA4qgRhLiumELW1UF6ZIY

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: URTJCC_A7qbyeF8l3YKjbXDQtc2UH3qxlm3_YmXvv08
