# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 15:06:00
  - Trace: [Produce Individual Card Fronts](../001-3-1-individual-card-front-production.task.trace.md)
  - Origin:
    - [relative](../001-3-1-individual-card-front-production.task.trace.md)
- Current
  - Current Schema: [tiinex.evidence.v1](https://github.com/Tiinex/docs/blob/e713557f8be630967571d11a73f9ecd05ae329ce/.topics/.schemas/core/evidence/tiinex.evidence.v1.schema.md)
  - Created At: 2026-09-19 16:10:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Preserve the first human-operated generation batch and its reported execution method before introducing Pilot-mediated Handoff transport.
  - Summary: Byte-exact evidence for six manually returned card-front generation candidates and the reported clean-project execution method.
  - Status: captured/local

---

# Pre-Pilot Manual Card Generation Evidence

## Supported Claim Or Question

- Supported Claim Or Question: six exact card-front PNG outputs were returned from a human-operated external generation process before the project-local Pilot route was introduced, and their observable byte/dimension identities can be preserved for review.
- Evidence Role: execution-result preservation and process-observation evidence only.
- Claim Reference: [Produce Individual Card Fronts](../001-3-1-individual-card-front-production.task.trace.md)
- Review Context: determine which exact outputs can be reused as current production source/reference and which require a successor generation route.

## Evidence Material

| Preserved file | Dimensions | Bytes | SHA-256 |
|---|---:|---:|---|
| `001-generated-defensive-reroll.png` | 948×1659 | 2450582 | `8a0f7284692d746160264e67b4b91c129e385613b44d447091956b84421a6deb` |
| `001-generated-offensive-reroll-2.png` | 1060×1484 | 2555146 | `0cb88ac850d034f02819fb60fda3e8c2241d081c30aee12a3c277d33e235e3ca` |
| `001-generated-offensive-reroll-3.png` | 1060×1484 | 2523740 | `fb4f2fe31111457c17ced7169782dfb324865a7e67d74d81d21b4b8dbc5ac417` |
| `001-generated-offensive-reroll-4.png` | 948×1659 | 2660049 | `ec3b0c1fef72f27a0b29e4593d3132dc73d656f7dedd5cbad7b2c35522356283` |
| `001-generated-offensive-reroll-5.png` | 948×1659 | 2573034 | `7adf2d3fcee3bd5662114dcee2ffe586f3cbd99d829e178ec4bb5e235f1e92f0` |
| `001-generated-sabotage.png` | 1060×1484 | 2440272 | `dc62e49fbdd0463a695a182f6df52e87b8768583ad717cacda6d73565e26503b` |

## Observation

The human reported this execution method for each accepted download:

- create a new ChatGPT project without a project preprompt;
- provide exactly the requested single visual reference for that generation;
- paste the exact generation text prepared by Cartographer;
- inspect the provider result;
- when the result looked good, manually download the image;
- collect the downloaded files into the returned archive.

The returned archive also carried the three reference-image files used during this work. Equivalent approved reference bytes already exist elsewhere in the Tower Havoc Workspace, so this Evidence does not duplicate those reference files into this execution directory.

## Preservation And Fidelity

- Preservation State: byte-exact/local copies of the six returned generated PNGs.
- Transformation: none after extraction into the lineage-local execution directory.
- Known Limits: provider-internal prompt compilation, hidden model/tool state, generation seed/state, and exact hidden preprocessing are not observable and are not claimed.
- User-visible input fidelity: reported as the exact prepared text and single requested reference per generation; this Evidence preserves the report but does not claim unseen provider-side identity.

## Interpretation Limits

- Does Not Prove: final visual acceptance, TTS suitability, print suitability, gameplay correctness, or that any generated text supersedes card lineage.
- Not Yet Used As: final approved card-face runtime assets.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Produce Individual Card Fronts](../001-3-1-individual-card-front-production.task.trace.md)
  - Value: X87JAQyNubj8HT-nr9NjLDasdHTI3kFAWBYur5HYrP0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:o1-d-axFzTxY7mqX9VlQQwxjVuc2uaMHyf3oYLbixC8
