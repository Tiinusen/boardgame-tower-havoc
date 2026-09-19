# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Trace: [001-match-provenance-runtime.topic.trace.md](001-match-provenance-runtime.topic.trace.md)
  - Origin:
    - [relative](001-match-provenance-runtime.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Land the runtime authority split before implementing GitHub Issue play so player commands, randomness, adjudication, and state cannot silently collapse into one mutable blob.
  - Summary: Use event-sourced match provenance

---

# Event-Sourced Match Authority

Tower Havoc gameplay should remain reconstructable even if the current UI or generated state snapshot disappears.

## Decision

- State: accepted-for-R&D
- Subject: digital/artifact-native match authority
- Decision: bind each match to a frozen `towerhavoc.ruleset.v1`; preserve player commands as `towerhavoc.action.intent.v1`; generate separate randomness request/result artifacts when needed; preserve authoritative adjudication as `towerhavoc.action.resolution.v1`; generate `towerhavoc.state.v1` checkpoints as replayable projections; close with `towerhavoc.match.result.v1`. Hidden deck/hand state uses commitment/reveal artifacts rather than public plaintext during play.

## Basis

This separation makes it possible to replay a match, distinguish what a player asked for from what the engine accepted, and later generate a UI or documentation from the same provenance. It also prevents ordinary GitHub issue/comment ordering from becoming hidden game semantics.

## Consequences

- current state is convenient but not the sole authority
- an illegal action can be preserved as rejected intent/resolution without mutating game state
- random outcomes require precommitted requests and reproducible result mapping
- full provenance is compatible with temporary secrecy through commitments
- the eventual GitHub runtime can be replaced without rewriting match semantics

## Review Conditions

Revisit after the first real artifact-native match. If the artifact volume makes play impractical, optimize projection/aggregation before weakening provenance boundaries.


---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-match-provenance-runtime.topic.trace.md](001-match-provenance-runtime.topic.trace.md)
  - Value: YGNSdvw4OzdD1k3VWRmMhp0S5U4zHoX4LuaqKDsxe9s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: SGUdrfX9jdzZQgfjnU8J0FbBHAUQHoIh2F_9polctZc
