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
  - Why: Represent project-level design and acceptance authority as a reusable Role rather than a named person.
  - Summary: Reusable Tower Havoc project stewardship and human acceptance role.
  - Status: ready/local

---

# Steward Role

## Role Identity

- Role Label: Steward
- Role Kind: Tower Havoc project stewardship, game-design authority, and human acceptance
- Canonical Identifier: tower-havoc.role.steward
- Project: Tower Havoc

## Role Boundary

- In Scope: canonical game-design direction; acceptance, rejection, deferral, or reopening of gameplay proposals; classification of current rules as LOCKED or PLAYTEST; project scope and priorities; acceptance of concrete contributions into project state; project-level rights, licensing, publication, and publisher-facing direction when separately within the holder's authority.
- Out Of Scope: rewriting historical provenance; manufacturing playtest Evidence; proving legal ownership, trademark clearance, patent freedom, market demand, or contributor consent merely from Role authority; silently granting another Role source-mutation, publication, or release authority.
- Context: Steward is the project's human acceptance and direction boundary. It is not a generic manager role and does not make preference equivalent to evidence.

## Authority And Responsibility Boundary

- May Do: accept, reject, defer, or reopen design proposals; declare which game definition currently governs; distinguish LOCKED from PLAYTEST; set bounded project priorities; authorize bounded Tasks/Handoffs; accept concrete contributions; decide whether project-level licensing or publication policy should change when the holder has the separate real-world authority to do so.
- Does Not Authorize: fabrication or erasure of provenance; treating synthetic simulations as observed playtest Evidence; assigning authorship or rights to another party without basis; claiming external legal clearance; automatic repository mutation by another Role; interpreting a Role reference as holder identity, consent, acceptance, or delegation.
- Required Instrument: consequential delegated work should be bounded by an explicit Task, Handoff, Decision, or equivalent controlling artifact. Rights/publication changes should be landed as explicit project Decisions rather than inferred from ordinary design acceptance.
- Delegation: Steward may route bounded work to Cartographer, Keeper, or another qualified capacity. Delegation does not transfer Steward's project-acceptance authority unless a separate qualified artifact explicitly says so.
- Review Boundary: Steward owns project-level acceptance of canonical design consequences. Technical validation, simulation, or match adjudication may inform that decision but does not replace it.

## Holder Relationship

- Holder State: no permanent holder is asserted by this Role artifact; a concrete Tower Havoc project steward must be separately and explicitly bound.
- Assignment Modes: explicit-user-session, handoff, explicit-participation
- Possible Holder: a human participant explicitly carrying Tower Havoc project stewardship and acceptance authority within the bounded context.

## Interpretation Limits

- Does Not Prove: legal ownership, authorship of every project artifact, consent from other contributors, publication authority outside the holder's actual rights, correctness of design judgment, or that a concrete person currently holds the Role.
- Must Not Be Treated As: legal title, employment position, universal repository administrator, evidence source, automatic Handoff acceptance, or permission to rewrite historical artifacts.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Roles](001-roles.topic.trace.md)
  - Value: 9rv6NpjrEL3GEkrga-dhcY8_xpcD9hNCAP6WKDtOnLg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/c5c0a8173dcc0816d239a64fa363c7924df216b1/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 86q7qaaQSRyOkvMuihFEOtXZ31OElaZOsiv1SmimX8k
