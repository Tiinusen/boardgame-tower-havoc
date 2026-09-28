# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Trace: [001-match-provenance-runtime.topic.trace.md](001-match-provenance-runtime.topic.trace.md)
  - Origin:
    - [relative](001-match-provenance-runtime.topic.trace.md)
- Current
  - Current Schema: [tiinex.schema.family.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/schema/family/tiinex.schema.family.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Make local game-runtime schema roles explicit without claiming that Tiinex needs generic game schemas.
  - Summary: Tower Havoc gameplay provenance schema family

---

# Tower Havoc Gameplay Provenance Schema Family

## Family Identity

- Family Name: Tower Havoc gameplay provenance
- Base Schema: tiinex.root.v1
- Family Role: group project-local Tower Havoc gameplay schemas across several existing Tiinex semantic families without making the Tower Havoc family itself their inheritance parent
- Abstract Family: yes
- Stable Children: none yet; all local schemas are draft/local until exercised by real matches
- Candidate Children: towerhavoc.ruleset.v1; towerhavoc.match.v1; towerhavoc.match.seat.v1; towerhavoc.turn-order.v1; towerhavoc.turn.v1; towerhavoc.action.intent.v1; towerhavoc.action.resolution.v1; towerhavoc.rule.resolution.v1; towerhavoc.random.request.v1; towerhavoc.random.result.v1; towerhavoc.state.v1; towerhavoc.hidden.commitment.v1; towerhavoc.hidden.reveal.v1; towerhavoc.match.result.v1

## Inheritance Model

- Extends: tiinex.root.v1 as the domain-family grouping boundary only; individual local schemas must extend the nearest suitable Tiinex semantic parent
- Intended Children: Tower Havoc-specific gameplay schemas whose direct semantic parents may come from different Tiinex schema families
- Allowed Descendant Pattern: local schemas specialize the nearest existing semantic parent and explicitly declare body inheritance overrides when their body shape narrows that parent
- Disallowed Descendant Pattern: using `towerhavoc.*` or this Schema Family as an inheritance umbrella merely because an artifact belongs to the game; generic Tiinex-wide game semantics inferred from this one board game
- Override Policy: each local schema owns only its declared gameplay specialization; compatible parent-family semantics and Root continuity/integrity remain inherited

## Direct Parent Map

- `towerhavoc.ruleset.v1` -> `tiinex.instrument.v1`
- `towerhavoc.match.v1` -> `tiinex.event.session.v1`
- `towerhavoc.match.seat.v1` -> `tiinex.party.role.v1`
- `towerhavoc.turn-order.v1` -> `tiinex.decision.v1`
- `towerhavoc.turn.v1` -> `tiinex.event.window.v1`
- `towerhavoc.action.intent.v1` -> `tiinex.task.v1`
- `towerhavoc.action.resolution.v1` -> `tiinex.runtime.v1`
- `towerhavoc.rule.resolution.v1` -> `tiinex.runtime.v1`
- `towerhavoc.random.request.v1` -> `tiinex.task.v1`
- `towerhavoc.random.result.v1` -> `tiinex.derivation.v1`
- `towerhavoc.state.v1` -> `tiinex.runtime.v1`
- `towerhavoc.hidden.commitment.v1` -> `tiinex.claim.v1`
- `towerhavoc.hidden.reveal.v1` -> `tiinex.validation.report.v1`
- `towerhavoc.match.result.v1` -> `tiinex.runtime.v1`

This map is schema inheritance, not match-artifact Parent lineage. Concrete match artifacts still use `Parent` only for direct continuity ancestry; other gameplay dependencies remain explicit body bindings or relations.

## Parent Mapping Review Boundary

- High-confidence mappings: Match -> Event Session; Match Seat -> Party Role; Turn -> Event Window; Action Intent -> Task; Random Request -> Task; Random Result -> Derivation; Hidden Reveal -> Validation Report.
- Current but review-sensitive mappings: Ruleset -> Instrument; Action Resolution -> Runtime; Hidden Commitment -> Claim; Match Result -> Runtime.
- Review trigger: material real-match evidence shows the artifact's primary role differs from the selected parent, or Tiinex introduces a narrower generic schema that owns the role better.
- Must Not Be Inferred: project-local parent choices are universal board-game ontology or requirements for Tiinex Core.

## Creatability Policy

- Manually Creatable: advanced
- Creatable As Continuation: advanced
- Creatable As Reference: yes
- Recommended Contexts: match runtime, replay, audit, GitHub Issue experiment, automated playtest capture
- Advanced Contexts: public-beacon randomness; commitment/reveal hidden state
- Not Suitable Contexts: ordinary design discussion, rulebook prose, CAD design, generic Tiinex projects
- Rationale: gameplay artifacts are operational records, not replacements for the existing design lineage

## Extension Guidance

- Add New Descendant When: a recurring gameplay role has its own validation and provenance boundary that cannot be expressed by the current family without ambiguity
- Do Not Add Descendant When: an existing Tiinex Task, Decision, Evidence, Condition, Preservation, Relation, or other generic schema already owns the main role
- Prefer Existing Schema: use generic Tiinex artifacts for design/development work; use local gameplay schemas only inside match execution
- Review Questions: does the new schema distinguish actor intent from authoritative game outcome; does it preserve replayability; does it leak hidden information; does it invent trust that the host cannot provide

## Boundary Notes

- This family is project-local to Tower Havoc.
- It does not claim universal board-game semantics.
- It does not make GitHub Actions a trusted random oracle by itself.
- It does not replace the canonical game-design lineage under `.topics/tower-havoc/**`.


---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-match-provenance-runtime.topic.trace.md](001-match-provenance-runtime.topic.trace.md)
  - Value: YGNSdvw4OzdD1k3VWRmMhp0S5U4zHoX4LuaqKDsxe9s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: _Uy63HyLmNFK7R-_2aRwOUFzJdSDt2LsLeqve_ODCGY
