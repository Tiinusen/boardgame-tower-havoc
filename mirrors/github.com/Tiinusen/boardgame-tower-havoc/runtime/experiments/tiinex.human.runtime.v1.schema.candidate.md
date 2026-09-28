# Continuity Context

- Envelope Schema: tiinex.root.v1
- Parent
  - Parent Schema: [tiinex.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Created At: 2026-06-05 11:00:00
  - Trace: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
- Current
  - Current Schema: tiinex.human.runtime.v1
  - Created At: 2026-09-18 10:30:00
  - Status: experimental/local candidate
  - Summary: Experimental human-executed Runtime specialization for bounded observable procedures and outputs.

---

# Human Runtime

## Summary

Human Runtime specializes Runtime for observable execution performed by a human following a bounded procedure. It does not make the person a machine and it does not treat a human observation as cryptographically trustworthy.

## Parent Runtime Specialization

- Parent Schema: tiinex.runtime.v1
- Specialization: retain Runtime execution/result semantics while requiring human execution, procedure, observed output, and review/witness boundaries to remain explicit.
- Sibling Intent: machine runtime and human runtime should be alternative execution mechanisms when domain semantics do not depend on which performs the procedure.

## Required Artifact Shape

- `## Runtime Identity`
- `## Human Execution Boundary`
- `## Procedure`
- `## Observed Output`
- `## Review Or Witness Boundary`
- `## Interpretation Limits`

## Interpretation Limits

- A Human Runtime artifact records a bounded human-executed procedure and observation.
- It does not prove fairness, identity, competence, authorization, cryptographic unpredictability, or correctness beyond separately declared support.

---

# Continuity Integrity

- sha256-base64url-c14n-v2
  - Towards: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Value: hzROFN7xQRZUwU_5aLKLar8gKSHEKGFGUjiOhMEfH_A

- sha256-base64url-c14n-v2
  - Towards: self
  - Value: F6htLRnN03ZlxhApYDz-ahkoy1QLF4Zk5rOadU1j6YQ
