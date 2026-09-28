# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 13:50:00
  - Trace: [Incremental Tower Havoc Match-Lineage Stress](../002-incremental-lineage-stress.topic.trace.md)
  - Origin:
    - [relative](../002-incremental-lineage-stress.topic.trace.md)
- Current
  - Current Schema: [towerhavoc.ruleset.v1](../../../../.schemas/tower-havoc/towerhavoc.ruleset.v1.schema.md)
  - Created At: 2026-09-18 13:50:01
  - Authors: ChatGPT
  - Why: Freeze one deterministic three-seat scenario before incremental execution begins.
  - Summary: Frozen synthetic ruleset for incremental lineage stress.

---

# TH-SIM-09 Frozen Incremental Ruleset

## Ruleset Identity
- Ruleset ID: TH-SIM-09-ruleset
- Game: Tower Havoc
- Edition: Dieselpunk Edition
- Mode: Classic synthetic incremental simulation fixture
- Ruleset State: frozen

## Canonical Rule Binding
- Project Root: ../../../001-tower-havoc.project.trace.md
- Source Commit Or Snapshot: Tower Havoc carrier-006 semantic state plus integrity-repaired carrier-007 workspace
- Bound Rule Artifacts: ../../../rules/**; ../../../cards/**
- Binding Fingerprint: synthetic-fixture:TH-SIM-09

## Runtime Parameters
- Parameters: multi-attack=max-1-per-turn; build-curve=2/3/4; bell-success=1; attack-miss=1,6; hittable=2,3,4,5; fixture-start-actions=seat-01=10,seat-02=0,seat-03=0; fixture-rng=attack:4,bell:1; fixture-purpose=exercise incremental lineage emission

## Adjudication Boundary
- Legal Action Source: canonical Tower Havoc rule Decisions plus the explicit synthetic fixture parameters above
- Randomness Policy: request artifact must verify before the deterministic machine source emits its next value
- Hidden State Policy: no hidden cards are required by this scenario

## Interpretation Limits
- Does Not Prove: canonical balance, ordinary starting resources, player behavior, match duration, or real randomness
- Must Not Be Inferred: fixture values modify canonical Tower Havoc outside this simulation

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Incremental Tower Havoc Match-Lineage Stress](../002-incremental-lineage-stress.topic.trace.md)
  - Value: lM4Pr8d9d2cNCpRP85O1v0QN-L2f2gh2jGuOMujyHBY

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:CLzCIPTqopfa2wR2-XeoUMdykqvDntCqfTfUpNZInQk
