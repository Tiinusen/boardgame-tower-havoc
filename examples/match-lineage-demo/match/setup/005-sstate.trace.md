# Continuity Context

- Envelope Schema: tiinex.root.v1
- Parent
  - Parent Schema: towerhavoc.match.v1
  - Created At: 2026-09-18 10:30:00
  - Trace: [Tower Havoc Schema Demo Match](../001-match.trace.md)
  - Origin:
    - [relative](../001-match.trace.md)
- Current
  - Current Schema: towerhavoc.state.v1
  - Created At: 2026-09-18 10:30:00

---

# Initial Match State

## State Identity

- State ID: state-000
- Match: TH-DEMO-001
- State Kind: initial materialized gameplay state

## Player State

- seat-01: actions=9; ready-ammo=2; production-ammo=0; tower-floors=0
- seat-02: actions=9; ready-ammo=2; production-ammo=0; tower-floors=0

## Match State

- Active Seat: seat-01
- Next Turn Number: 1
- Winner: none
- Active Global Event: none

## Source Bindings

- Seat 01 Assignment: 001-1
- Seat 02 Assignment: 001-2-1-1-1
- Turn Order: 001-3-1-1-1
- Deck Commitment: 001-4

---

# Continuity Integrity

- sha256-base64url-c14n-v2
  - Towards: [Tower Havoc Schema Demo Match](../001-match.trace.md)
  - Value: rAH_Cwf8ykowkYQJUG9E_apCqQyRwBPeJBeH9xKu1Zs

- sha256-base64url-c14n-v2
  - Towards: self
  - Value: oKya_aECrGpz2Gx59cgkLhG7RxmK1AEeD8Thw2J5Ebw
