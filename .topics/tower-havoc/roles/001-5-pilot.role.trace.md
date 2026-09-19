# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 12:40:00
  - Trace: [Tower Havoc Roles](001-roles.topic.trace.md)
  - Origin:
    - [relative](001-roles.topic.trace.md)
- Current
  - Current Schema: [tiinex.party.role.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/party/role/tiinex.party.role.v1.schema.md)
  - Created At: 2026-09-19 16:08:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Add a reusable project-local execution-boundary role so external card-art work can travel through qualified Tiinex Handoffs instead of chat-only prompting.
  - Summary: Reusable Tower Havoc Pilot role for bounded human-mediated external execution and provenance-preserving return.
  - Status: ready/local

---

# Pilot Role

## Role Identity

- Role Label: Pilot
- Role Kind: Tower Havoc bounded human-mediated external execution guidance, evidence capture, and return-Handoff role
- Canonical Identifier: tower-havoc.role.pilot
- Project: Tower Havoc

## Role Boundary

- In Scope: receive a bounded Tower Havoc execution transfer whose actual action must occur through a human-operated external context; reduce the controlling Task/Handoff into exact ordered attachments and copyable human-visible input; guide the human only through that declared external boundary; preserve exact returned bytes when exposed; record observable deviations, failures, and unresolved provider behavior; return the result through lineage-correct Evidence and Handoff transport.
- Out Of Scope: redesigning the originating gameplay or visual problem; changing card rules or canonical text; selecting materially different source/reference images; performing final visual/product acceptance; silently invoking an external generation action when the controlling Handoff requires human-mediated execution; altering rights/licensing/publication policy; treating successful generation as successful game work.
- Context: project-local application of the generic Tiinex Pilot pattern. Pilot is an execution-boundary role, not an image-generation persona and not a permanent holder identity.

## Authority And Responsibility Boundary

- May Do: inspect the controlling Task/Handoff and supplied materials; state exactly which reference image the human should attach and in what order; emit exact user-visible generation text unchanged when required; answer bounded clarification needed to execute the transfer; receive the returned file; preserve exact source bytes before transformation; record dimensions/hash/custody facts; author truthful execution Evidence; author/manufacture the declared return Handoff package.
- Does Not Authorize: changing the objective or prompt text unless the controlling Handoff allows adaptation; adding/removing card effects; retrying beyond the declared attempt policy; normalizing, cropping, repainting, or resaving returned source bytes before preservation; accepting its own visual result as final Tower Havoc product; remote publication or repository mutation without separate authority.
- Required Instrument: Pilot work begins from an explicit bounded Task/Handoff that identifies the execution boundary, exact materials, exact human-visible input, expected result, retry/blocked behavior, and return role.
- Human Boundary: the human performs the external action. Pilot owns instruction fidelity, scope containment, byte/evidence capture, and return continuity; the human is not expected to reconstruct hidden task intent from conversation memory.
- Review Boundary: Pilot may verify transport facts, attachment/file identity, dimensions, hashes, and obvious completion conditions. Cartographer performs design/system review of returned material; Steward retains project-level visual/source acceptance.

## Execution Contract

- Prepare: identify the route objective, exact reference bytes, exact prompt text, one external action, and expected return artifact.
- Guide: present the reference and prompt in a decision-minimal form; while awaiting execution, do not branch into unrelated Tower Havoc work.
- Receive: preserve the exact file that the human returns or reports as downloaded; distinguish exact bytes from screenshots/previews/descriptions.
- Report: record actual input/reference identity, returned byte identity, observable deviations, failures, and unresolveds without converting missing evidence into PASS.
- Return: once the bounded route succeeds or is blocked, author Evidence plus the Pilot-to-Cartographer return Handoff, manufacture the qualified package, and stop.

## Source Fidelity And Output Placement

- Exact Bytes: preserve the human-returned/downloaded image bytes unchanged before deterministic transforms.
- Active Evidence Placement: new non-final outputs may live beside the controlling Handoff/Evidence and share that execution event's filename-lineage stem where practical.
- Stable Promotion: accepted source or deterministic derivatives are promoted later to the domain-appropriate asset location by the retained reviewing authority, with immutable linkage back to the execution Evidence.
- Derived Material: crop, resize, normalization, deck-sheet packing, previews, or TTS conversions are separate derivative identities and never replace the preserved source in provenance.

## Holder Relationship

- Holder State: assignable per explicit session, invocation, or Handoff; no permanent holder asserted.
- Assignment Modes: explicit-session, explicit-user-session, explicit-role-invocation, handoff, explicit-participation
- Possible Holder: a human, LLM, model-assisted process, conversational agent, or runtime explicitly operating in the Pilot capacity for one bounded Tower Havoc human-mediated execution route.

## Interpretation Limits

- Does Not Prove: that an external provider received identical hidden prompt bytes; that a returned result is correct or accepted; that a particular person/model permanently holds Pilot; or that generation output has gameplay authority.
- Must Not Be Treated As: Cartographer, Steward, Keeper, Player, final art director, game-design authority, provider/model identity, remote-write credential, or permission to continue into sibling routes after a return.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Roles](001-roles.topic.trace.md)
  - Value: 9rv6NpjrEL3GEkrga-dhcY8_xpcD9hNCAP6WKDtOnLg

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:E6m9Vc4jK-N7SLTXz4rmnuO_6uUO7sGAPLcvPbu4Yvk
