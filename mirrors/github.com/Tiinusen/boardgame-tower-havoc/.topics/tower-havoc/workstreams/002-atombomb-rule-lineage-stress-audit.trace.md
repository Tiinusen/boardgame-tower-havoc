# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: tiinex.decision.v1
  - Created At: 2026-09-28 16:04:09
  - Trace: [001-9-1-atombomb-global-events.decision.trace.md](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Origin:
    - [relative](../cards/001-9-1-atombomb-global-events.decision.trace.md)
- Current
  - Current Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-28 16:15:56
  - Authors: Steward
  - Why: Exercise Atombomb rule interactions independently from implementation and visual production before the next real playtest.
  - Summary: Bounded Keeper synthetic adjudication and integrity audit for the accepted Atombomb Event.
  - Status: ready/local

---

# Atombomb Rule-Lineage Stress Audit

## Objective

Keeper is an explicitly required participant in this current work because the new Atombomb Event needs executor-neutral synthetic adjudication and integrity review before the next real playtest.

Stress-test the accepted Atombomb semantics against the current frozen Tower Havoc rules through a compact lineage-first synthetic audit. Prefer explicit states, intents/triggers, rule resolutions, and resulting states over aggregate statistics.

## Done Criteria

- audit at least these bounded cases: multiple built floors with mixed reinforcements; partially built towers; a player with Bell-related state; Atombomb while a persistent Event is active; simultaneous destruction across multiple players; and a post-Atombomb next-turn recovery/build sequence;
- apply only the accepted effect: destroy all tower floors and all reinforcements belonging to every player;
- preserve the Steward Decision that Atombomb adds no direct Bell, hand, Ready Ammo, Production, Available Actions, or persistent-Event reset effect;
- identify any state inconsistency, ambiguous transition, or rule interaction as a finding rather than silently repairing the rules;
- distinguish illegal/inconsistent/unverifiable transitions from claims about cheating or intent;
- preserve every scenario as SYNTHETIC audit material, never real playtest Evidence or balance proof;
- return concise findings plus enough lineage to replay the cases deterministically under the supplied rules;
- return one qualified Keeper-to-Steward Handoff Package and do not mutate canonical gameplay rules.

## Scope

Synthetic Keeper adjudication/audit only. No gameplay-design acceptance, card-art generation, deck projection implementation, publication, rights change, or real playtest claim.

## Dependencies

- `../cards/001-9-1-atombomb-global-events.decision.trace.md`
- `../rules/001-core-game-rules.topic.trace.md`
- `../runtime/001-match-provenance-runtime.topic.trace.md`
- `../roles/001-3-keeper.role.trace.md`

## Visibility Boundary

Use public-state-only unless a declared scenario explicitly supplies additional state. Do not invent hidden cards, deck order, or unavailable commitments to make a scenario convenient.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-1-atombomb-global-events.decision.trace.md](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Value: 1b5UA56LeOHMixichDk6Jr5f6NG0CCLmL01pln9Yxdo

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: D7bbF6Ru-t81qjpG-X3kkmnejG_sOhKYvfCAcsdrEDc