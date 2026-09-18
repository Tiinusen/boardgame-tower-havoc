# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.instrument.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/instrument/tiinex.instrument.v1.schema.md)
  - Created At: 2026-06-29 00:00:00
  - Trace: [tiinex.instrument.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/instrument/tiinex.instrument.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/instrument/tiinex.instrument.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.ruleset.v1](towerhavoc.ruleset.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: A replayable match must know exactly which rules and provisional playtest values governed it.
  - Summary: Frozen match-time binding to one exact Tower Havoc rules frontier.

---

# Tower Havoc Ruleset Binding

## Summary

Defines a match-time ruleset snapshot/binding. It does not replace the canonical game-design lineage; it freezes the exact rule frontier a match is adjudicated against.

## Core Semantics

- One match binds to exactly one ruleset artifact.
- The ruleset points to exact canonical rule artifacts or a commit-pinned projection plus fingerprints.
- A ruleset may intentionally bind PLAYTEST values.
- Later rule changes do not retroactively change an already-bound match.

## Schema Validation Contract

### Parent Instrument Specialization

Rules

- `towerhavoc.ruleset.v1` specializes `tiinex.instrument.v1` for Tower Havoc gameplay provenance.
- The local `Ruleset Body` replaces the inherited `Instrument Body` body structure for artifacts whose current schema is `towerhavoc.ruleset.v1`.
- Compatible non-structural semantics from `tiinex.instrument.v1` remain inherited unless this schema explicitly narrows them.
- Reason: Tower Havoc rulesets are match-governing terms and adjudication boundaries, so the local schema narrows Instrument rather than inventing a parallel root-level rules contract.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-ruleset-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.instrument.v1
  - Parent Node: Schema Validation Contract / Instrument Body / Required Shape
  - Child Node: Schema Validation Contract / Ruleset Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Ruleset Body` is authoritative for `towerhavoc.ruleset.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Ruleset Body
Required Shape
- `## Ruleset Identity`
- `## Canonical Rule Binding`
- `## Runtime Parameters`
- `## Adjudication Boundary`
- `## Interpretation Limits`

### Ruleset Identity
Required Fields
- Ruleset ID
- Game
- Edition
- Mode
- Ruleset State

### Canonical Rule Binding
Required Fields
- Project Root
- Source Commit Or Snapshot
- Bound Rule Artifacts
- Binding Fingerprint

Rules
- References should be commit-pinned or content-fingerprinted when possible.
- A generated rulebook alone is not sufficient if stronger canonical artifact references are available.

### Runtime Parameters
Required Fields
- Parameters

Rules
- Parameters must include every provisional value that can change match adjudication, including multi-attack policy, burst build curve, and bell success rule.

### Adjudication Boundary
Required Fields
- Legal Action Source
- Randomness Policy
- Hidden State Policy

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create one ruleset binding before match setup is finalized. Do not mutate it after the first accepted match action; create a new ruleset for a new match or explicit restart.

## Minimal Example

```md
## Ruleset Identity
- Ruleset ID: th-ruleset-2026-09-18-a
- Game: Tower Havoc
- Edition: Dieselpunk Edition
- Mode: Classic
- Ruleset State: frozen

## Canonical Rule Binding
- Project Root: .topics/tower-havoc/001-tower-havoc.project.trace.md
- Source Commit Or Snapshot: <commit>
- Bound Rule Artifacts: .topics/tower-havoc/rules/**
- Binding Fingerprint: <digest>
```

## Interpretation Notes

The ruleset is a frozen match input, not competing design authority.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.instrument.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/instrument/tiinex.instrument.v1.schema.md)
  - Value: QEwNHCf03xsYGHv3bpz0r3MIVwqhq7xQj5GNCauhKLA

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 438OXNuTKYyfuOVQ3E2bkYTHDx2l1SMZaZ_F4qSIQNM
