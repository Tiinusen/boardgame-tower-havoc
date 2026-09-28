# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 12:40:06
  - Trace: [001-discussions.trace.md](001-discussions.trace.md)
  - Origin:
    - [relative](001-discussions.trace.md)
- Current
  - Current Schema: [tiinex.handoff.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/handoff/tiinex.handoff.v1.schema.md)
  - Created At: 2026-09-28 15:14:16
  - Summary: New Bootstrap
  - Status: draft/local

---

# New Bootstrap

## Handoff Parties

- Purpose: Open an interactive bounded conversation with the receiving role about the subject described by this Handoff.
- From: Cartographer
- From Kind: role
- To: Steward
- To Kind: role
- From Reference: [Cartographer](tiinusen-boardgame-tower-havoc::.topics/tower-havoc/roles/001-2-cartographer.role.trace.md)
- To Reference: [Steward](tiinusen-boardgame-tower-havoc::.topics/tower-havoc/roles/001-1-steward.role.trace.md)

## Transfers

- bounded-conversation
  - Transfer Kind: work
  - Description: Participate in the bounded live conversation or brainstorm. Respond conversationally; do not turn the exchange into a durable result artifact unless explicitly requested.

## Required Context

- none

## Reference Context

- none

## Retained Responsibilities

- none

## Exclusions And Dependencies

- none

## Completion Expectation

- Signal Kind: none
- Signal Meaning: This Handoff opens a live conversation. No automatic completion artifact, disposition, or return package is expected; continue the conversation until the participants explicitly choose a next action.
- Return To: Cartographer
- Return To Reference: [Cartographer](tiinusen-boardgame-tower-havoc::.topics/tower-havoc/roles/001-2-cartographer.role.trace.md)

## Interpretation Limits

- Does Not Mean: Opening the conversation does not transfer implementation authority or require the receiving role to manufacture a durable discussion result.
- Must Not Be Used To Claim: Do not infer implementation, acceptance, completion, or a required return artifact from conversational participation alone.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-discussions.trace.md](001-discussions.trace.md)
  - Value: eQEvX93MT5TgnqqUZtoevdwIP39i-YbmPv4OA9RFqWY

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: fsZZueFoJ57lr1B2dkejhDuFgXwsMlMwtW_V52n3zNs