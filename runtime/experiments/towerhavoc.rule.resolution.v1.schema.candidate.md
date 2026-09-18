# Continuity Context

- Envelope Schema: tiinex.root.v1
- Parent
  - Parent Schema: [tiinex.runtime.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Created At: 2026-06-05 11:00:00
  - Trace: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Origin:
    - [browse + git](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
- Current
  - Current Schema: towerhavoc.rule.resolution.v1
  - Created At: 2026-09-18 10:30:00
  - Status: experimental/local candidate
  - Summary: Experimental deterministic automatic rule-resolution Runtime specialization for Tower Havoc.

---

# Tower Havoc Rule Resolution

## Summary

Tower Havoc Rule Resolution records deterministic game effects that occur because a rule trigger fires rather than because a player directly requested that effect.

## Parent Runtime Specialization

- Parent Schema: tiinex.runtime.v1
- Specialization: retain Runtime result semantics while requiring trigger, rules applied, state delta/result, and execution boundary.
- Execution Neutrality: the same rule resolution may be performed through human runtime, machine runtime, or another qualified execution procedure without changing gameplay meaning.

## Required Artifact Shape

- `## Trigger`
- `## Rules Applied`
- `## Result`
- `## Execution Boundary`

## Interpretation Limits

- This schema records Tower Havoc automatic rule effects, not player intent.
- It does not make human or machine execution the gameplay authority by itself; the frozen ruleset and declared adjudication boundary remain material.

---

# Continuity Integrity

- sha256-base64url-c14n-v2
  - Towards: [tiinex.runtime.v1.schema.md](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/tiinex.runtime.v1.schema.md)
  - Value: hzROFN7xQRZUwU_5aLKLar8gKSHEKGFGUjiOhMEfH_A

- sha256-base64url-c14n-v2
  - Towards: self
  - Value: oSG2I3lfpgwEqdn6wxWq8E97plsQHJphTMqk3EiQPao
