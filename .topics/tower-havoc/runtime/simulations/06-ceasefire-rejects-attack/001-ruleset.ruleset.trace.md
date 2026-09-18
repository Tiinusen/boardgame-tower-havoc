# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [Tower Havoc Runtime Simulation Corpus](../001-runtime-simulation-corpus.topic.trace.md)
  - Origin:
    - [relative](../001-runtime-simulation-corpus.topic.trace.md)
- Current
  - Current Schema: [towerhavoc.ruleset.v1](../../../../.schemas/tower-havoc/towerhavoc.ruleset.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT
  - Why: Keep each conformance vector replayable without changing canonical game rules.
  - Summary: Frozen synthetic ruleset for Ceasefire Rejects Attack Then Expires.

---

# TH-SIM-06 Frozen Scenario Ruleset

## Ruleset Identity
- Ruleset ID: TH-SIM-06-ruleset
- Game: Tower Havoc
- Edition: Dieselpunk Edition
- Mode: Classic synthetic simulation fixture
- Ruleset State: frozen

## Canonical Rule Binding
- Project Root: ../../../001-tower-havoc.project.trace.md
- Source Commit Or Snapshot: e9168e4772429834a4b220d3b0b3cd0df485f208
- Bound Rule Artifacts: ../../../rules/**; ../../../cards/**
- Binding Fingerprint: git:e9168e4772429834a4b220d3b0b3cd0df485f208

## Runtime Parameters
- Parameters: multi-attack=max-1-per-turn; build-curve=2/3/4; bell-success=1; attack-miss=1,6; hittable=2,3,4,5; fixture=Ceasefire event is active from seat-01 draw until seat-01 next turn

## Adjudication Boundary
- Legal Action Source: canonical Tower Havoc rule Decisions plus the explicit synthetic fixture parameters above
- Randomness Policy: request must exist before source observation; result mapping is deterministic
- Hidden State Policy: public state exposes counts/commitments, not hidden identities

## Interpretation Limits
- Does Not Prove: canonical balance, match duration, player behavior, or that fixture-only starting values are normal game setup
- Must Not Be Inferred: synthetic fixture parameters modify the canonical game outside this simulation

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Runtime Simulation Corpus](../001-runtime-simulation-corpus.topic.trace.md)
  - Value: 7XG7-ZrEUxfvr__HzZp6MZkn7fZfV_Mcj6pDNcdhtmM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: LYt9kr_NernIQnLJ2fgU0mNmDPmB1me-WybPazOwt4o
