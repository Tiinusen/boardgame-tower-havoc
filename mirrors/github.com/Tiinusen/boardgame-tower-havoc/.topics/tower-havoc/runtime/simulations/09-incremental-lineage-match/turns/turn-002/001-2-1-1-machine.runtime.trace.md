# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.random.request.v1](../../../../../../.schemas/tower-havoc/towerhavoc.random.request.v1.schema.md)
  - Created At: 2026-09-18 13:50:32
  - Trace: [TH-SIM-09 Attack Random Request](001-2-1-attack.random-request.trace.md)
  - Origin:
    - [relative](001-2-1-attack.random-request.trace.md)
- Current
  - Current Schema: [tiinex.machine.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/machine/tiinex.machine.runtime.v1.schema.md)
  - Created At: 2026-09-18 13:50:33
  - Authors: ChatGPT

---

# TH-SIM-09 Machine Attack Roll Runtime

## Metadata
- Runtime Family: machine simulation runtime
- Bound Random Request: 001-2-1-attack.random-request.trace.md
- Status: completed

## Outcome
- Preserved Result: 4

## Technical Details
- Procedure: deterministic fixture source releases the next predeclared value only after the bound request artifact exists and verifies
- Interpretation: source observation for attack roll; Tower Havoc mapping belongs to the following Random Result artifact

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-09 Attack Random Request](001-2-1-attack.random-request.trace.md)
  - Value: yqlJoDup4U-AXNAkDdEe0uoEgx8kvT-i4f100B6sbpY

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:286Mys0GUne5ZCchYvrXdo1FWN9LqcQjeXqUNY_0Ldw
