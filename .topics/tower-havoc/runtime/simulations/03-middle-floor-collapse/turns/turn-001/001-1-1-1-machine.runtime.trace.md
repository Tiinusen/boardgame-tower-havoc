# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [towerhavoc.random.request.v1](../../../../../../.schemas/tower-havoc/towerhavoc.random.request.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Trace: [TH-SIM-03 Attack Random Request](001-1-1-attack.random-request.trace.md)
  - Origin:
    - [relative](001-1-1-attack.random-request.trace.md)
- Current
  - Current Schema: [tiinex.machine.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/machine/tiinex.machine.runtime.v1.schema.md)
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT

---

# TH-SIM-03 Machine Random Source Runtime

## Metadata
- Runtime Family: machine simulation runtime
- Bound Random Request: 001-1-1-attack.random-request.trace.md
- Status: completed

## Outcome
- Preserved Result: 3

## Technical Details
- Procedure: deterministic simulation source emits value only after request
- Interpretation: this artifact preserves source observation/execution only; Tower Havoc mapping belongs to the following Random Result artifact

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [TH-SIM-03 Attack Random Request](001-1-1-attack.random-request.trace.md)
  - Value: yyyiCXs4uX11R3UzElDtUGfdmb2SzezlOzbhTvnfhU8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 31ZzGRl-fnocmdmgu-prkA6qG9NTmAWzh130Rq0Ss5I
