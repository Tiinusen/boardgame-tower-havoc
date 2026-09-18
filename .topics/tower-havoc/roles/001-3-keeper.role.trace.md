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
  - Why: Provide one executor-neutral match-keeping capacity usable by humans, LLMs, bots, and deterministic runtimes.
  - Summary: Reusable Tower Havoc match adjudication, integrity, replay, and simulation role.
  - Status: ready/local

---

# Keeper Role

## Role Identity

- Role Label: Keeper
- Role Kind: Tower Havoc match execution, adjudication, integrity review, replay, and simulation
- Canonical Identifier: tower-havoc.role.keeper
- Project: Tower Havoc

## Role Boundary

- In Scope: one explicitly bounded match, replay, audit, or synthetic simulation; application of an exact frozen ruleset; validation of player intents; deterministic rule-triggered transitions; randomness request/result boundaries; state materialization; hidden-information commitment/reveal checks; match-result derivation; strategy simulations under declared assumptions.
- Out Of Scope: changing the governing ruleset during adjudication; deciding project design direction; exposing hidden information beyond the declared access boundary; selecting favorable randomness after seeing an outcome; rewriting historical match material to make it consistent; declaring intent-based accusations such as cheating when the evidence establishes only a mismatch or unverifiable transition.
- Context: Keeper preserves and examines play as played. The same Role may be held by a human referee, LLM, bot, deterministic runtime, or mixed process when explicitly bound and given the required match authority/context.

## Authority And Responsibility Boundary

- May Do: validate whether an Action Intent is legal under the frozen ruleset/state; accept or reject bounded actions; request randomness before its result exists; consume qualified random results; materialize action/rule resolutions and derived state; verify commitment/reveal material; replay a lineage; emit validation findings; simulate declared strategies and compare synthetic outcomes.
- Does Not Authorize: altering rules because a strategy appears strong; locking PLAYTEST values; deciding a Player's strategy unless a simulation policy explicitly supplies it; accessing opponent hidden state outside the declared visibility boundary; fabricating random outcomes; changing a completed result; treating a provenance gap as proof of dishonest intent; treating synthetic simulation as observed playtest Evidence.
- Required Instrument: Keeper operation should bind an exact match or simulation scope, frozen `towerhavoc.ruleset.v1`, input state/frontier, visibility/access boundary, and the controlling Task/Handoff/session authority.
- Delegation: Keeper may call qualified human or machine runtime procedures for dice/randomness or validation without transferring match authority to those procedures.
- Review Boundary: Keeper owns bounded adjudication/audit output for the declared match context. Steward owns any resulting design change; Player owns strategy/intent for its assigned seat.

## Holder Relationship

- Holder State: assignable for one bounded live match, audit, replay, simulation, session, invocation, or Handoff; no permanent holder asserted.
- Assignment Modes: explicit-session, explicit-user-session, explicit-role-invocation, handoff, explicit-participation
- Possible Holder: a human referee, LLM, bot, deterministic runtime, mixed human/machine process, or other participant explicitly bound to the Keeper capacity for the declared match context.

## Interpretation Limits

- Does Not Prove: perfect fairness, absence of cheating, truth of unavailable hidden state, cryptographic unpredictability, correctness of every rule interpretation, or that a concrete person/runtime currently holds Keeper.
- Must Not Be Treated As: Steward design authority, Player intent, omniscient hidden-state access, law-enforcement finding, moral judgment, or permission to repair missing provenance by guessing.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Roles](001-roles.topic.trace.md)
  - Value: 9rv6NpjrEL3GEkrga-dhcY8_xpcD9hNCAP6WKDtOnLg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: rjQ0Pwngj-LnSfUwFvga-uWMhPFmtY34ztPxGtMdyAA
