# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.claim.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/claim/tiinex.claim.v1.schema.md)
  - Created At: 2026-07-02 00:00:00
  - Trace: [tiinex.claim.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/claim/tiinex.claim.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/claim/tiinex.claim.v1.schema.md)
- Current
  - Current Schema: [towerhavoc.hidden.commitment.v1](towerhavoc.hidden.commitment.v1.schema.md)
  - Created At: 2026-09-18 10:35:00
  - Status: draft/local
  - Why: Card hands and deck order need auditable provenance without making hidden information public before it should be revealed.
  - Summary: Public commitment to hidden match state without revealing it during play.

---

# Tower Havoc Hidden State Commitment

## Summary

Preserves a public cryptographic commitment to hidden game material such as deck order or private hands.

## Schema Validation Contract

### Parent Claim Specialization

Rules

- `towerhavoc.hidden.commitment.v1` specializes `tiinex.claim.v1` for Tower Havoc gameplay provenance.
- The local `Hidden Commitment Body` replaces the inherited `Claim Body` body structure for artifacts whose current schema is `towerhavoc.hidden.commitment.v1`.
- Compatible non-structural semantics from `tiinex.claim.v1` remain inherited unless this schema explicitly narrows them.
- Reason: A hidden-state commitment is a bounded assertion that concealed material is bound to a declared commitment value and method; it is not the secret or proof by itself.
- Parent specialization applies to the artifact body only; it does not alter Root continuity, integrity, Parent, or Origin semantics.

Inheritance Overrides

- towerhavoc-hidden-commitment-v1-body-structure
  - Merge Operation: override
  - Parent Schema: tiinex.claim.v1
  - Parent Node: Schema Validation Contract / Claim Body / Required Shape
  - Child Node: Schema Validation Contract / Hidden Commitment Body / Required Shape
  - Reason: the Tower Havoc artifact has a narrower gameplay-specific readable body while retaining the parent family semantics.
  - Effective Result: `Hidden Commitment Body` is authoritative for `towerhavoc.hidden.commitment.v1` artifact-body structure; compatible inherited semantics remain active outside the overridden structural body.

### Hidden Commitment Body
Required Shape
- `## Match Binding`
- `## Secret Scope`
- `## Commitment Method`
- `## Commitment`
- `## Custody And Delivery`
- `## Reveal Policy`
- `## Interpretation Limits`

### Match Binding
Required Fields
- Match ID
- State Or Setup Binding

### Secret Scope
Required Fields
- Hidden Material Kind
- Affected Seats Or Deck

### Commitment Method
Required Fields
- Algorithm
- Canonical Secret Encoding
- Salt Or Nonce Policy

### Commitment
Required Fields
- Commitment Value
Optional Fields
- Encrypted Payload Reference

### Custody And Delivery
Required Fields
- Secret Custodian
- Player Delivery Method

Rules
- The commitment does not by itself deliver a player's private card identities.
- A public GitHub repository needs a separate private/encrypted delivery path if hidden hands are preserved during play.

### Reveal Policy
Required Fields
- Reveal Trigger
- Required Reveal Material

### Interpretation Limits
Required Fields
- Does Not Prove
- Must Not Be Inferred

## Artifact Creation Contract

Create before hidden material is consumed or selectively revealed.

## Minimal Example

```md
## Secret Scope
- Hidden Material Kind: shuffled deck order
- Affected Seats Or Deck: main-card-deck

## Commitment
- Commitment Value: sha256:<digest>
```

## Interpretation Notes

Full provenance does not require full public plaintext during the match. Commitment now + reveal later preserves both secrecy and auditability.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [tiinex.claim.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/knowledge/claim/tiinex.claim.v1.schema.md)
  - Value: ocv6EBAm4E1aHXW7OlMP2Eu5VvxVaKX3weiTukpFOGc

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: rVhrfDBTg0F3Ou-s39nxoRSDnDjPBJMs2ZnmWOtNya8
