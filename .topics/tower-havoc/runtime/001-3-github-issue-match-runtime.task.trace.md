# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Trace: [001-match-provenance-runtime.topic.trace.md](001-match-provenance-runtime.topic.trace.md)
  - Origin:
    - [relative](001-match-provenance-runtime.topic.trace.md)
- Current
  - Current Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Test whether GitHub Issues plus Actions can act as a thin interaction host while repository artifacts remain the game authority.
  - Summary: Prototype GitHub Issue match runtime

---

# Prototype GitHub Issue Match Runtime

## Objective

Build a small R&D runtime where a GitHub Issue can host one Tower Havoc match and players can submit artifact-shaped commands without requiring a custom web game client.

## Done Criteria

- one issue can open a match and bind an exact ruleset
- player comments can submit one `towerhavoc.action.intent.v1` command
- a workflow validates actor/turn/legal-state boundaries and materializes accepted or rejected resolution artifacts
- random actions use request/result separation and a replayable randomness source/mapping
- current state is regenerated from accepted resolutions
- at least one full match can be replayed from repository artifacts without trusting issue comment order
- hidden-card handling is either implemented with commitment/private delivery or explicitly disabled for the first R&D profile

## Scope

- GitHub Issues/Actions are a host experiment, not canonical game semantics.
- Start with Classic mode and, if necessary, open hands to validate the event model before private-card delivery is built.
- Do not claim Actions alone makes cheating impossible. Stronger digital fairness requires precommitted external entropy or multi-party commit/reveal plus protected history.
- No polished UI is required. Markdown comments and generated summaries are sufficient.

## Dependencies

- local gameplay schema family
- frozen match ruleset representation
- repository branch/history protection policy for meaningful tamper evidence
- chosen randomness source for the high-assurance profile


---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-match-provenance-runtime.topic.trace.md](001-match-provenance-runtime.topic.trace.md)
  - Value: YGNSdvw4OzdD1k3VWRmMhp0S5U4zHoX4LuaqKDsxe9s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: dbrE_hP724kJ94SVWJaYOcFYiM1Eu_cIzPcaAZhmuLk
