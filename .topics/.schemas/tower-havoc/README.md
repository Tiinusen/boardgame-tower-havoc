# Tower Havoc local gameplay schemas

These are **project-local schema proposals** for representing a Tower Havoc match as artifact-native provenance. They do not claim to be generic Tiinex game schemas.

The local `towerhavoc.*` namespace is a **domain grouping**, not a semantic inheritance parent. Each local schema extends the nearest existing Tiinex schema whose main artifact role matches the gameplay artifact. The project-level Schema Family artifact groups the domain without flattening those semantic parents.

## Semantic inheritance map

| Tower Havoc schema | Direct parent schema | Why that parent owns the main role |
|---|---|---|
| `towerhavoc.ruleset.v1` | `tiinex.instrument.v1` | frozen governing terms/boundaries for adjudication |
| `towerhavoc.match.v1` | `tiinex.event.session.v1` | one bounded gameplay session |
| `towerhavoc.match.seat.v1` | `tiinex.party.role.v1` | bounded seat/role with a holder relationship |
| `towerhavoc.turn-order.v1` | `tiinex.decision.v1` | accepted configuration that governs play order |
| `towerhavoc.turn.v1` | `tiinex.event.window.v1` | bounded action window for one active seat |
| `towerhavoc.action.intent.v1` | `tiinex.task.v1` | bounded requested action awaiting resolution |
| `towerhavoc.action.resolution.v1` | `tiinex.runtime.v1` | execution/adjudication result and state delta |
| `towerhavoc.random.request.v1` | `tiinex.task.v1` | precommitted bounded work request for randomness |
| `towerhavoc.random.result.v1` | `tiinex.derivation.v1` | replayable mapping from source material to outcome |
| `towerhavoc.state.v1` | `tiinex.runtime.v1` | derived runtime checkpoint/projection |
| `towerhavoc.hidden.commitment.v1` | `tiinex.claim.v1` | bounded assertion binding concealed material to a commitment value |
| `towerhavoc.hidden.reveal.v1` | `tiinex.validation.report.v1` | verification of revealed material against commitment |
| `towerhavoc.match.result.v1` | `tiinex.runtime.v1` | bounded terminal result package and audit closure |

Every child schema explicitly declares a body-structure inheritance override. This keeps the generic Tiinex parent semantics while allowing a narrow gameplay-specific artifact body.

## Intended match flow

```text
ruleset
  -> match
     -> seat(s)
     -> turn-order
     -> initial state
     -> turn
        -> action intent
        -> [random request -> random result]
        -> action resolution
        -> state
        -> ...
     -> match result
```

Hidden information uses `hidden.commitment` during play and `hidden.reveal` when policy allows.

## Important distinction

Artifact lineage and schema inheritance are different graphs:

- **Artifact Parent** answers which concrete prior artifact this artifact directly continues.
- **Schema Parent** answers which semantic contract this schema specializes.
- **Schema Family** groups related schemas for discovery and extension policy; it is not automatically their direct parent schema.
- **Relations/bindings** connect match artifacts that depend on each other without abusing `Parent` as a generic graph edge.

The path is navigation. Each schema note owns its own identity and contract.
## Review-sensitive parent choices

Most mappings are fairly direct (`match -> Event Session`, `turn -> Event Window`, `seat -> Party Role`, requests -> `Task`). Three are intentionally provisional until exercised by real match artifacts:

- `towerhavoc.ruleset.v1 -> tiinex.instrument.v1`: chosen because the ruleset is the terms-bearing governing record for adjudication. If future artifacts primarily preserve a frozen snapshot rather than govern play, a Preservation-shaped split may be cleaner.
- `towerhavoc.action.resolution.v1 -> tiinex.runtime.v1`: chosen because the artifact owns execution/adjudication output and state delta, not merely the legality decision. If adjudication and execution become separate artifacts, the adjudication part may narrow Decision or Validation while execution remains Runtime/Event.
- `towerhavoc.hidden.commitment.v1 -> tiinex.claim.v1`: chosen because the commitment is a bounded assertion awaiting later verification. This is the least settled mapping and should be revisited if Tiinex gains a generic cryptographic-commitment primitive.

The family records these as current design choices, not claims that the Tiinex ontology has only one possible valid decomposition.

