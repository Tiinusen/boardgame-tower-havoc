# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.validation.report.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/validation/report/tiinex.validation.report.v1.schema.md)
  - Created At: 2026-06-30 00:00:00
  - Trace: [tiinex.validation.report.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/validation/report/tiinex.validation.report.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/validation/report/tiinex.validation.report.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.hidden.reveal.v1](towerhavoc.hidden.reveal.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Post-match or authorized reveal is needed to prove that committed deck/hand material was not changed after the fact.
  - Summary: Reveal and verify previously committed hidden Tower Havoc state.

---

# Tower Havoc Hidden State Reveal

## Summary

Reveals material bound by a prior hidden-state commitment and records verification against that commitment.

## Schema Validation Contract

### Parent Validation Report Specialization

Rules

- `towerhavoc.hidden.reveal.v1` specializes `tiinex.validation.report.v1` for Tower Havoc gameplay provenance.
- The local `Hidden Reveal Body` replaces the inherited `Validation Report Body` body structure for artifacts whose current schema is `towerhavoc.hidden.reveal.v1`.
- Compatible non-structural semantics from `tiinex.validation.report.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A reveal primarily validates disclosed secret material against a prior commitment and records the bounded verification result.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-hidden-reveal-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.validation.report.v1
  - Parent Node: Schema Validation Contract / Validation Report Body / Required Shape
  - Child Node: Schema Validation Contract / Hidden Reveal Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Hidden Reveal Body` is authoritative for `towerhavoc.hidden.reveal.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Hidden Reveal Body
Required Shape
- `## Commitment Binding`
- `## Revealed Material`
- `## Verification`
- `## Reveal Timing`
- `## Interpretation Limits`

### Commitment Binding
Required Fields
- Commitment Artifact
- Commitment Value

### Revealed Material
Required Fields
- Canonical Secret Payload Or Preserved Reference
- Salt Or Nonce

### Verification
Required Fields
- Recomputed Commitment
- Matches
- Verification Method

### Reveal Timing
Required Fields
- Trigger
- Revealed At

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create only when the match policy permits reveal, ordinarily after match completion or when a rule requires a specific hidden item to become public.

## Minimal Example

```md
## Verification
- Recomputed Commitment: sha256:<digest>
- Matches: yes
- Verification Method: canonical-payload-sha256
```

## Interpretation Notes

A matching reveal proves commitment consistency for the disclosed payload, not that an external custodian never saw or leaked the secret earlier.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.validation.report.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/validation/report/tiinex.validation.report.v1.schema.md)
  - Value: ek24us3jtUoLRyUcK4FNBX60fvg4UbW1KFrI4nBB3VI

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 8K6uRNaSgq11s-RmAiRilCe40UCaVmn7BbJurVAenqU
