# Continuity Context

- Envelope Schema: tiinex.root.v1
- Parent
  - Parent Schema: towerhavoc.match.v1
  - Created At: 2026-09-18 10:30:00
  - Trace: [Tower Havoc Schema Demo Match](../001-match.trace.md)
  - Origin:
    - [relative](../001-match.trace.md)
- Current
  - Current Schema: towerhavoc.hidden.commitment.v1
  - Created At: 2026-09-18 10:30:00

---

# Hidden Deck Commitment

## Commitment Identity

- Commitment ID: deck-commitment-001
- Subject: complete 40-card deck order
- Commitment Method: SHA-256 over UTF-8 compact JSON array

## Commitment

- Digest: 3a03964986aff699ce12e71bbb8bf308f39178738d5dfef72159f7aea6d0d5eb
- Hidden Material State: not disclosed during match

## Binding

- Match: TH-DEMO-001
- Card Count: 40

## Interpretation Limits

- The commitment binds one byte representation.
- It does not prove that a physical player could not privately know the committed order.

---

# Continuity Integrity

- sha256-base64url-c14n-v2
  - Towards: [Tower Havoc Schema Demo Match](../001-match.trace.md)
  - Value: rAH_Cwf8ykowkYQJUG9E_apCqQyRwBPeJBeH9xKu1Zs

- sha256-base64url-c14n-v2
  - Towards: self
  - Value: iXacgR1so_Ok-iW43uwDLwOB_GGjh5m1lnaGyhngQcg
