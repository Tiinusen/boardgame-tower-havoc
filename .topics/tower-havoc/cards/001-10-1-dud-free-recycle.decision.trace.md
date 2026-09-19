# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:54:00
  - Trace: [Deck recycle rule](001-10-deck-recycle.decision.trace.md)
  - Origin:
    - [relative](001-10-deck-recycle.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:09
  - Authors: Olle Tiinus; ChatGPT
  - Why: Keep recycle semantics aligned with the dud-free deck.
  - Summary: PLAYTEST successor for ordinary discard-pile recycling.

---

# Dud-free deck recycle rule

## Decision

- State: provisional/PLAYTEST
- Rule ID: cards.recycle
- Decision: when the draw pile is exhausted, shuffle the discard pile to create a new draw pile. No hand purge occurs as part of deck exhaustion.

## Basis

Dud cards are absent from the next PLAYTEST deck, so the original special Dud-return step no longer has a subject.

## Consequences

Generated rules and digital helpers use an ordinary discard reshuffle for the next baseline.

## Review Conditions

If later card families need special recycle behavior, land that as another explicit successor rather than reviving the Dud-specific rule implicitly.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Deck recycle rule](001-10-deck-recycle.decision.trace.md)
  - Value: VXnHijsG7kZKuqgEP4gX2RrQEn5cop0lokksnZfy67I

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:6fimCX0nOk0zyno3U97Jx3ZK52ThZYapYYLdq8l2uQc
