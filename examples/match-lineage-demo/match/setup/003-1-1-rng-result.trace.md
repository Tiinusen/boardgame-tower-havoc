# Continuity Context

- Envelope Schema: tiinex.root.v1
- Parent
  - Parent Schema: tiinex.human.runtime.v1
  - Created At: 2026-09-18 10:30:00
  - Trace: [Human Runtime — Turn Order Roll](003-1-roll.trace.md)
  - Origin:
    - [relative](003-1-roll.trace.md)
- Current
  - Current Schema: towerhavoc.random.result.v1
  - Created At: 2026-09-18 10:30:00

---

# Turn Order Random Result

## Request Binding

- Random Request: rng-turn-order

## Source Material

- Raw Observation: 3
- Source Method: physical D6 via human runtime

## Mapping

- Rule: odd = seat-01 first; even = seat-02 first
- Observation 3: odd

## Result

- Outcome: seat-01 first

---

# Continuity Integrity

- sha256-base64url-c14n-v2
  - Towards: [Human Runtime — Turn Order Roll](003-1-roll.trace.md)
  - Value: Rl3J36Nl0MTfIF5aKDmEexWTWWAslfl-njOnBb6mPkA

- sha256-base64url-c14n-v2
  - Towards: self
  - Value: YbnBtKqSyRX4OppCFSAp8gsyzpOY3C0BtZU8zKFfRIQ
