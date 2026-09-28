# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.derivation.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/derivation/tiinex.derivation.v1.schema.md)
  - Created At: 2026-07-02 00:00:00
  - Trace: [tiinex.derivation.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/derivation/tiinex.derivation.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/derivation/tiinex.derivation.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.random.result.v1](towerhavoc.random.result.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: A random outcome should be derivable from a precommitted request plus inspectable source material rather than simply asserted by a player or workflow.
  - Summary: Replayable result and proof material for one random request.

---

# Tower Havoc Random Result

## Summary

Records the source value, verification boundary, deterministic mapping, and outcome for one random request.

## Schema Validation Contract

### Parent Derivation Specialization

Rules

- `towerhavoc.random.result.v1` specializes `tiinex.derivation.v1` for Tower Havoc gameplay provenance.
- The local `Random Result Body` replaces the inherited `Derivation Body` body structure for artifacts whose current schema is `towerhavoc.random.result.v1`.
- Compatible non-structural semantics from `tiinex.derivation.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A random result is a reviewable deterministic derivation from a precommitted request plus source material through a declared mapping.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-random-result-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.derivation.v1
  - Parent Node: Schema Validation Contract / Derivation Body / Required Shape
  - Child Node: Schema Validation Contract / Random Result Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Random Result Body` is authoritative for `towerhavoc.random.result.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Random Result Body
Required Shape
- `## Request Binding`
- `## Source Material`
- `## Source Verification`
- `## Mapping`
- `## Result`
- `## Runtime Provenance`
- `## Interpretation Limits`

### Request Binding
Required Fields
- Random Request Artifact
- Request Fingerprint

### Source Material
Required Fields
- Source Method
- Source Identifier
- Raw Source Value Or Observation
Optional Fields
- Public Proof Or Signature
- Source URL Or Reference

### Source Verification
Required Fields
- Verification State
- Verification Method
Allowed Verification State
- verified
- observed
- unavailable
- failed

### Mapping
Required Fields
- Mapping Method
- Canonical Mapping Input
- Mapping Steps Or Algorithm ID

### Result
Required Fields
- Outcome

### Runtime Provenance
Required Fields
- Produced By
- Workflow Or Runtime Version
- Produced At

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Generate only after the corresponding request is sealed. For public-beacon mode, preserve enough source proof/reference for an independent replay.

## Minimal Example

```md
## Result
- Outcome: 4
```

## Interpretation Notes

GitHub Actions may materialize the artifact, but GitHub Actions alone is not a trustless random oracle. Stronger assurance comes from precommitment plus external/public entropy or multi-party commit-reveal.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.derivation.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/derivation/tiinex.derivation.v1.schema.md)
  - Value: uWngIm-KlgHyD3gTLEvsyHgStLSXNX56kK0HW2FKbgQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: ypJighFy9nEUEwCAgdCgqNuvR4jQEzpA-LFFF0I3FCA
