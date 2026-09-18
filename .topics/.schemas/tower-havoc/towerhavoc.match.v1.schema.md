# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.event.session.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/session/tiinex.event.session.v1.schema.md)
  - Created At: 2026-06-30 00:00:00
  - Trace: [tiinex.event.session.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/session/tiinex.event.session.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/session/tiinex.event.session.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.match.v1](towerhavoc.match.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: A complete match needs one bounded identity, ruleset, participant set, runtime policy, and lifecycle root.
  - Summary: Root artifact for one replayable Tower Havoc match.

---

# Tower Havoc Match

## Summary

Defines one Tower Havoc match as a bounded gameplay provenance root.

## Core Semantics

- The match binds participants, ruleset, runtime policy, and lifecycle.
- Match state is reconstructed from accepted gameplay artifacts, not inferred from issue text or comment order alone.
- Human-friendly GitHub Issues may host interaction, but host UI is not match authority.

## Schema Validation Contract

### Parent Event Session Specialization

Rules

- `towerhavoc.match.v1` specializes `tiinex.event.session.v1` for Tower Havoc gameplay provenance.
- The local `Match Body` replaces the inherited `Event Session Body` body structure for artifacts whose current schema is `towerhavoc.match.v1`.
- Compatible non-structural semantics from `tiinex.event.session.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A match is a bounded activity session with participants, lifecycle, context, and outcomes.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-match-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.event.session.v1
  - Parent Node: Schema Validation Contract / Event Session Body / Required Shape
  - Child Node: Schema Validation Contract / Match Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Match Body` is authoritative for `towerhavoc.match.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Match Body
Required Shape
- `## Match Identity`
- `## Ruleset Binding`
- `## Participants And Seats`
- `## Runtime Policy`
- `## Lifecycle`
- `## Interpretation Limits`

### Match Identity
Required Fields
- Match ID
- Match State
- Game
- Created By

Allowed Match State
- setup
- ready
- active
- completed
- abandoned

### Ruleset Binding
Required Fields
- Ruleset Artifact
- Ruleset Fingerprint

### Participants And Seats
Required Fields
- Expected Seats
- Seat Artifacts

### Runtime Policy
Required Fields
- Adjudication Mode
- Randomness Mode
- Hidden State Mode
- Canonical Event Store

Rules
- `Adjudication Mode` must distinguish human adjudication from workflow/runtime adjudication.
- A digital no-cheat profile should not accept actor-authored random outcomes as authoritative.

### Lifecycle
Required Fields
- Setup State
- Start Condition
- Completion Condition

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create before seats, faction assignment, turn order, or gameplay actions. The Match ID should remain stable for the entire match.

## Minimal Example

```md
## Match Identity
- Match ID: TH-2026-001
- Match State: setup
- Game: Tower Havoc
- Created By: Olle

## Runtime Policy
- Adjudication Mode: github-action
- Randomness Mode: public-beacon
- Hidden State Mode: commitment-and-reveal
- Canonical Event Store: repository match lineage
```

## Interpretation Notes

The match root groups the game instance; it is not itself a record that every later action was legal.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.event.session.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/event/session/tiinex.event.session.v1.schema.md)
  - Value: xFU3PkkfdogWxou7nItvfXEluxYbY-Mz_TaF9Fl3oAk

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: TPm2nnUq9MI51WoDV1co42TVGV4T4bzJCy1fvpedJCw
