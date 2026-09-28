#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timedelta
import argparse, base64, hashlib, os, re, shutil

ROOT_SCHEMA = "https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md"
TOPIC_SCHEMA = "https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md"
MACHINE_RUNTIME_SCHEMA = "https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/runtime/machine/tiinex.machine.runtime.v1.schema.md"
VALIDATOR = "https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md"

SCENARIO = "09-incremental-lineage-match"
MATCH_ID = "TH-SIM-09"
BASE_TIME = datetime(2026, 9, 18, 13, 50, 1)
RNG_VALUES = iter([4, 1])

def normalize(md: str) -> str:
    md = md.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip(" \t") for line in md.split("\n")).rstrip()

def strip_link(value: str) -> str:
    m = re.match(r"^\[([^\]]+)\]\([^)]+\)$", value.strip())
    return (m.group(1) if m else value).strip()

def self_state(md: str):
    norm = normalize(md)
    lines = norm.split("\n")
    try:
        ih = lines.index("# Continuity Integrity")
    except ValueError:
        raise RuntimeError("integrity footer missing")
    entries, cur = [], None
    def finish():
        nonlocal cur
        if cur is not None:
            entries.append(cur)
            cur = None
    for idx in range(ih + 1, len(lines)):
        line = lines[idx]
        if re.match(r"^#\s+", line):
            finish()
            break
        m = re.match(r"^-\s+(.+?)\s*$", line)
        if m:
            finish()
            cur = {"method": strip_link(m.group(1)), "towards": "", "vals": []}
            continue
        if cur is None:
            continue
        m = re.match(r"^\s+-\s+Towards:\s*(.*?)\s*$", line)
        if m:
            cur["towards"] = strip_link(m.group(1))
        m = re.match(r"^(\s+-\s+Value:)([ \t]*)(.*)$", line)
        if m:
            cur["vals"].append((idx, m.group(1), m.group(2), m.group(3).strip()))
    finish()
    selfs = [e for e in entries if e["method"] == "sha256-base64url-c14n-v2" and e["towards"] == "self"]
    if len(selfs) != 1 or len(selfs[0]["vals"]) != 1:
        raise RuntimeError("ambiguous self integrity")
    idx, label, spacing, declared = selfs[0]["vals"][0]
    canonical = lines[:]
    canonical[idx] = label + spacing
    computed = base64.urlsafe_b64encode(hashlib.sha256("\n".join(canonical).encode("utf-8")).digest()).decode().rstrip("=")
    return lines, idx, declared, computed

def seal(md: str) -> str:
    lines, idx, declared, computed = self_state(md)
    m = re.match(r"^(\s+-\s+Value:)([ \t]*)(.*)$", lines[idx])
    lines[idx] = m.group(1) + m.group(2) + computed
    return "\n".join(lines) + "\n"

def declared_self(path: Path) -> str:
    lines, idx, declared, computed = self_state(path.read_text(encoding="utf-8"))
    if declared != computed:
        raise RuntimeError(f"parent self-integrity invalid: {path}")
    return declared

def artifact_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    body = text.split("---", 1)[1]
    m = re.search(r"^# (.+)$", body, re.M)
    if not m:
        raise RuntimeError(f"title missing: {path}")
    return m.group(1).strip()

def current_created(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    cur = text.split("- Current", 1)[1].split("---", 1)[0]
    m = re.search(r"^\s+- Created At: (.+)$", cur, re.M)
    if not m:
        raise RuntimeError(f"Current Created At missing: {path}")
    return m.group(1).strip()

def current_schema(path: Path):
    text = path.read_text(encoding="utf-8")
    cur = text.split("- Current", 1)[1].split("---", 1)[0]
    m = re.search(r"^\s+- Current Schema: \[([^\]]+)\]\(([^)]+)\)", cur, re.M)
    if not m:
        raise RuntimeError(f"Current Schema missing: {path}")
    return m.group(1), m.group(2)

class Clock:
    def __init__(self):
        self.value = BASE_TIME
    def next(self):
        v = self.value
        self.value += timedelta(seconds=1)
        return v.strftime("%Y-%m-%d %H:%M:%S")

class Emitter:
    def __init__(self, source_root: Path, target_root: Path):
        self.source_root = source_root.resolve()
        self.target_root = target_root.resolve()
        self.clock = Clock()
        self.emitted = []
    def write(self, rel: str, schema_id: str, schema_target: str, title: str, body: str,
              parent_path: Path, parent_link: str | None = None,
              why: str | None = None, summary: str | None = None):
        out = self.target_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            raise RuntimeError(f"refusing to overwrite emitted artifact: {out}")
        parent_path = parent_path.resolve()
        if parent_link is None:
            parent_link = os.path.relpath(parent_path, out.parent).replace(os.sep, "/")
        parent_schema_id, parent_schema_target = current_schema(parent_path)
        parent_created = current_created(parent_path)
        parent_title = artifact_title(parent_path)
        parent_digest = declared_self(parent_path)
        created = self.clock.next()
        env = [
            "# Continuity Context", "",
            f"- Envelope Schema: [tiinex.root.v1]({ROOT_SCHEMA})",
            "- Parent",
            f"  - Parent Schema: [{parent_schema_id}]({parent_schema_target})",
            f"  - Created At: {parent_created}",
            f"  - Trace: [{parent_title}]({parent_link})",
            "  - Origin:",
            f"    - [relative]({parent_link})",
            "- Current",
            f"  - Current Schema: [{schema_id}]({schema_target})",
            f"  - Created At: {created}",
            "  - Authors: ChatGPT",
        ]
        if why:
            env.append(f"  - Why: {why}")
        if summary:
            env.append(f"  - Summary: {summary}")
        env += ["", "---", "", f"# {title}", "", body.strip(), "", "---", "", "# Continuity Integrity", "",
                f"- [sha256-base64url-c14n-v2]({VALIDATOR})",
                f"  - Towards: [{parent_title}]({parent_link})",
                f"  - Value: {parent_digest}", "",
                f"- [sha256-base64url-c14n-v2]({VALIDATOR})",
                "  - Towards: self",
                "  - Value: ", ""]
        out.write_text(seal("\n".join(env)), encoding="utf-8")
        # Verify immediately; next child cannot exist before this passes.
        declared_self(out)
        self.emitted.append(out)
        return out

def schema(depth: int, name: str) -> str:
    return "../" * depth + f".schemas/tower-havoc/{name}.schema.md"

def fmt_map(d):
    return "; ".join(f"{k}={d[k]}" for k in sorted(d))

def fmt_reinf(reinf, seats):
    parts=[]
    any_reinf=False
    for s in seats:
        floors=[]
        for floor in sorted(reinf[s]):
            vals=sorted(reinf[s][floor])
            if vals:
                floors.append(f"floor{floor}=[" + ",".join(str(v) for v in vals) + "]")
                any_reinf=True
        parts.append(f"{s} " + " ".join(floors) if floors else f"{s}=none")
    return "; ".join(parts) if any_reinf else "none"

def state_body(state, state_id, seq, ruleset_ref, previous_ref, producing):
    return f"""## Match Binding
- Match ID: {MATCH_ID}
- Ruleset Artifact: {ruleset_ref}

## State Identity
- State ID: {state_id}
- Sequence: {seq}
- Active Seat Or Setup State: {state['active']}

## Public State
- Seat States: {fmt_map(state['seat_states'])}
- Action Banks: {fmt_map(state['actions'])}
- Ready Ammo: {fmt_map(state['ready'])}
- Production Ammo: {fmt_map(state['production'])}
- Tower Floors: {fmt_map(state['floors'])}
- Reinforcements: {fmt_reinf(state['reinforcements'], state['seats'])}
- Hand Counts: {fmt_map(state['hands'])}
- Deck Count: {state['deck']}
- Discard State: {state['discard']}
- Active Global Event: {state['event']}
- Bell Eligibility: {fmt_map(state['bell'])}

## Hidden State Commitments
- Commitments: none

## Derivation Binding
- Previous State Or Initial Setup: {previous_ref}
- Producing Resolution Or Setup Step: {producing}

## Verification State
- State: verified
- Regeneration Method: replay frozen ruleset plus accepted incremental resolutions in emission order

## Interpretation Limits
- Does Not Prove: real-world play, hidden-card identity, strategy quality, or balance
- Must Not Be Inferred: this checkpoint has authority independent of the preceding event lineage"""

def ruleset_body():
    return """## Ruleset Identity
- Ruleset ID: TH-SIM-09-ruleset
- Game: Tower Havoc
- Edition: Dieselpunk Edition
- Mode: Classic synthetic incremental simulation fixture
- Ruleset State: frozen

## Canonical Rule Binding
- Project Root: ../../../001-tower-havoc.project.trace.md
- Source Commit Or Snapshot: Tower Havoc carrier-006 semantic state plus integrity-repaired carrier-007 workspace
- Bound Rule Artifacts: ../../../rules/**; ../../../cards/**
- Binding Fingerprint: synthetic-fixture:TH-SIM-09

## Runtime Parameters
- Parameters: multi-attack=max-1-per-turn; build-curve=2/3/4; bell-success=1; attack-miss=1,6; hittable=2,3,4,5; fixture-start-actions=seat-01=10,seat-02=0,seat-03=0; fixture-rng=attack:4,bell:1; fixture-purpose=exercise incremental lineage emission

## Adjudication Boundary
- Legal Action Source: canonical Tower Havoc rule Decisions plus the explicit synthetic fixture parameters above
- Randomness Policy: request artifact must verify before the deterministic machine source emits its next value
- Hidden State Policy: no hidden cards are required by this scenario

## Interpretation Limits
- Does Not Prove: canonical balance, ordinary starting resources, player behavior, match duration, or real randomness
- Must Not Be Inferred: fixture values modify canonical Tower Havoc outside this simulation"""

def match_body():
    return """## Match Identity
- Match ID: TH-SIM-09
- Match State: active
- Game: Tower Havoc
- Created By: incremental synthetic simulation harness

## Ruleset Binding
- Ruleset Artifact: 001-ruleset.ruleset.trace.md
- Ruleset Fingerprint: resolved from frozen scenario ruleset self digest

## Participants And Seats
- Expected Seats: 3
- Seat Artifacts: seat-01; seat-02; seat-03

## Runtime Policy
- Adjudication Mode: deterministic incremental simulation harness
- Randomness Mode: machine source value emitted only after the bound request artifact verifies
- Hidden State Mode: no hidden material in this scenario
- Canonical Event Store: artifacts emitted by this scenario directory as execution proceeds

## Lifecycle
- Setup State: synthetic fixture declared by initial state artifact
- Start Condition: required seat, order, ruleset, and initial-state artifacts exist and verify
- Completion Condition: seat-01 survives one full three-seat orbit with three floors and resolves a successful bell attempt

## Interpretation Limits
- Does Not Prove: real play occurred, player preferences, balance, fun, physical randomness quality, or production readiness
- Must Not Be Inferred: machine-generated fixture outcomes are empirical playtest Evidence"""

def seat_body(seat, label):
    return f"""## Match Binding
- Match Artifact: ../002-match.match.trace.md
- Match ID: {MATCH_ID}
- Seat ID: {seat}

## Participant Binding
- Participant: synthetic participant
- Participant Reference Or Label: {label}

## Faction Assignment
- Faction: Classic faction slot
- Assignment Method: assigned

## Seat State
- State: active

## Interpretation Limits
- Does Not Prove: real-world identity, attendance, consent, or durable Player-role holder identity
- Must Not Be Inferred: the synthetic participant label identifies an actual person"""

def turn_order_body():
    return """## Match Binding
- Match Artifact: ../002-match.match.trace.md
- Match ID: TH-SIM-09

## Eligible Seats
- Seats: seat-01; seat-02; seat-03

## Ordering Method
- Method: agreed

## Ordered Seats
- Order: seat-01; seat-02; seat-03

## Finality
- State: accepted

## Interpretation Limits
- Does Not Prove: this order was selected by real players
- Must Not Be Inferred: filesystem order or emission time silently determines turn order"""

def turn_body(turn_index, round_index, seat, opening_ref):
    return f"""## Match Binding
- Match Artifact: ../../002-match.match.trace.md
- Match ID: {MATCH_ID}

## Turn Identity
- Round Index: {round_index}
- Turn Index: {turn_index}
- Active Seat: {seat}
- Turn State: open

## Opening State
- State Artifact: {opening_ref}
- State Fingerprint: referenced-state-self-digest

## Action Window
- Legal Actor: {seat}
- Accepted Action Resolutions: none yet

## Closing State
- State Artifact Or Pending: pending
- Next Seat Or Pending: pending

## Interpretation Limits
- Does Not Prove: every submitted intent is legal or that wall-clock order defines causality
- Must Not Be Inferred: this Turn artifact itself mutates state without Rule/Action Resolution artifacts"""

def intent_body(seat, turn_ref, state_ref, kind, params):
    return f"""## Match And Turn Binding
- Match ID: {MATCH_ID}
- Turn Artifact: {turn_ref}
- Opening Or Current State Artifact: {state_ref}

## Actor
- Seat: {seat}
- Host Actor Or Submission Source: synthetic Player-capacity strategy policy inside incremental harness

## Requested Action
- Action Kind: {kind}

## Parameters
- Parameters: {params}

## Intent State
- State: submitted

## Interpretation Limits
- Does Not Prove: the requested action is legal or accepted
- Must Not Be Inferred: Player intent directly mutates authoritative state"""

def action_resolution_body(turn_ref, ruleset_ref, prior_state_ref, intent_ref, legal, reason, costs,
                           randomness_required, outcome, delta, state_ref, random_request=None, random_result=None):
    random_lines = [f"- Randomness Required: {'yes' if randomness_required else 'no'}"]
    if random_request: random_lines.append(f"- Random Request Artifact: {random_request}")
    if random_result: random_lines.append(f"- Random Result Artifact: {random_result}")
    return f"""## Match And Turn Binding
- Match ID: {MATCH_ID}
- Turn Artifact: {turn_ref}
- Ruleset Artifact: {ruleset_ref}
- Prior State Artifact: {prior_state_ref}

## Intent Binding
- Intent Artifact: {intent_ref}
- Intent Fingerprint: referenced-intent-self-digest

## Adjudication
- Resolution State: accepted
- Legal: {'yes' if legal else 'no'}
- Reason: {reason}

## Costs Applied
- Costs: {costs}

## Randomness Binding
{chr(10).join(random_lines)}

## Outcome And State Delta
- Outcome: {outcome}
- State Delta: {delta}

## Resulting State
- State Artifact: {state_ref}
- State Fingerprint: referenced-state-self-digest

## Adjudication Provenance
- Adjudicator: deterministic incremental simulation harness operating in Keeper-capacity semantics
- Runtime Or Workflow Version: tower-havoc-incremental-lineage-v1
- Rules Validator Version: TH-SIM-09-ruleset

## Interpretation Limits
- Does Not Prove: real-world play, perfect implementation, or Player intent beyond the bound Intent artifact
- Must Not Be Inferred: synthetic adjudication changes canonical game rules"""

def rule_resolution_body(turn_ref, ruleset_ref, prior_state_ref, kind, source, rules, evaluation,
                         outcome, delta, state_ref):
    return f"""## Match And Turn Binding
- Match ID: {MATCH_ID}
- Turn Artifact Or Setup Step: {turn_ref}
- Ruleset Artifact: {ruleset_ref}
- Prior State Artifact: {prior_state_ref}

## Trigger
- Trigger Kind: {kind}
- Trigger Source: {source}

## Rules Applied
- Rule Artifacts: {rules}
- Evaluation: {evaluation}

## Outcome And State Delta
- Outcome: {outcome}
- State Delta: {delta}

## Resulting State
- State Artifact: {state_ref}
- State Fingerprint: referenced-state-self-digest

## Execution Provenance
- Executed By: deterministic incremental simulation harness
- Procedure Or Runtime Version: tower-havoc-incremental-lineage-v1

## Interpretation Limits
- Does Not Prove: the executor is infallible or that a real match occurred
- Must Not Be Inferred: automatic rule resolution was requested by a Player"""

def random_request_body(req_id, bound_ref, purpose, mapping):
    return f"""## Request Identity
- Request ID: {req_id}
- Request State: pending

## Match Binding
- Match ID: {MATCH_ID}
- Bound Artifact Or Step: {bound_ref}
- Context Fingerprint: bound-artifact-self-digest

## Random Purpose
- Purpose: {purpose}

## Outcome Space
- Outcomes: 1;2;3;4;5;6
- Selection Count: 1
- Replacement Policy: not-applicable

## Randomness Source Policy
- Method: trusted-host
- Source Must Be Unknown At Request Time: yes

## Deterministic Mapping
- Mapping Method: {mapping}
- Canonical Input Encoding: UTF-8 normalized scalar observation

## Request State
- State: pending

## Interpretation Limits
- Does Not Prove: trustless unpredictability or physical randomness quality
- Must Not Be Inferred: the harness may consume or choose the source value before this request artifact verifies"""

def machine_runtime_body(req_ref, value, purpose):
    return f"""## Metadata
- Runtime Family: machine simulation runtime
- Bound Random Request: {req_ref}
- Status: completed

## Outcome
- Preserved Result: {value}

## Technical Details
- Procedure: deterministic fixture source releases the next predeclared value only after the bound request artifact exists and verifies
- Interpretation: source observation for {purpose}; Tower Havoc mapping belongs to the following Random Result artifact"""

def random_result_body(req_ref, value, mapping_id, outcome):
    return f"""## Request Binding
- Random Request Artifact: {req_ref}
- Request Fingerprint: referenced-request-self-digest

## Source Material
- Source Method: trusted-host deterministic fixture source
- Source Identifier: TH-SIM-09-sequential-rng
- Raw Source Value Or Observation: {value}

## Source Verification
- Verification State: observed
- Verification Method: request-before-consumption assertion plus preserved machine runtime artifact

## Mapping
- Mapping Method: {mapping_id}
- Canonical Mapping Input: {value}
- Mapping Steps Or Algorithm ID: {mapping_id}

## Result
- Outcome: {outcome}

## Runtime Provenance
- Produced By: incremental simulation harness
- Workflow Or Runtime Version: tower-havoc-incremental-lineage-v1
- Produced At: synthetic execution sequence

## Interpretation Limits
- Does Not Prove: cryptographic unpredictability, fairness against a malicious trusted host, or real-world randomness quality
- Must Not Be Inferred: trusted-host mode is cheat-proof"""

def match_result_body(final_resolution_ref, final_state_ref):
    return f"""## Match Binding
- Match Artifact: ../002-match.match.trace.md
- Match ID: {MATCH_ID}
- Ruleset Artifact: ../001-ruleset.ruleset.trace.md

## Completion
- Completion State: completed
- Completion Reason: seat-01 survived the full three-seat orbit with three floors and resolved a successful bell attempt
- Terminal Resolution Artifact: {final_resolution_ref}

## Winner Or Outcome
- Outcome: bell victory
- Winning Seat: seat-01

## Final State
- Final State Artifact: {final_state_ref}
- Final State Fingerprint: referenced-final-state-self-digest

## Audit Closure
- Unresolved Intents: 0
- Unresolved Random Requests: 0
- State Replay Status: verified by incremental harness
- Hidden Commitment Reveal Status: not-applicable

## Interpretation Limits
- Does Not Prove: playtest result, balance, fun, real winner, or strategy superiority
- Must Not Be Inferred: this synthetic match is empirical game Evidence"""

def run(source_root: Path, target_root: Path, force=False):
    source_root = source_root.resolve()
    target_root = target_root.resolve()
    scenario = target_root / ".topics/tower-havoc/runtime/simulations" / SCENARIO
    if scenario.exists():
        if not force:
            raise RuntimeError(f"{scenario} already exists; use --force only for deterministic regeneration")
        shutil.rmtree(scenario)

    emitter = Emitter(source_root, target_root)
    stress_parent = source_root / ".topics/tower-havoc/runtime/simulations/002-incremental-lineage-stress.topic.trace.md"
    # When target == source, Parent is already present. For temp regeneration, parent bytes come from source.
    ruleset = emitter.write(
        f".topics/tower-havoc/runtime/simulations/{SCENARIO}/001-ruleset.ruleset.trace.md",
        "towerhavoc.ruleset.v1", "../../../../.schemas/tower-havoc/towerhavoc.ruleset.v1.schema.md",
        "TH-SIM-09 Frozen Incremental Ruleset", ruleset_body(), stress_parent,
        parent_link="../002-incremental-lineage-stress.topic.trace.md",
        why="Freeze one deterministic three-seat scenario before incremental execution begins.",
        summary="Frozen synthetic ruleset for incremental lineage stress."
    )
    match = emitter.write(
        f".topics/tower-havoc/runtime/simulations/{SCENARIO}/002-match.match.trace.md",
        "towerhavoc.match.v1", "../../../../.schemas/tower-havoc/towerhavoc.match.v1.schema.md",
        "TH-SIM-09 Incremental Lineage Match", match_body(), stress_parent,
        parent_link="../002-incremental-lineage-stress.topic.trace.md",
        why="Bound the live synthetic execution before setup artifacts are emitted.",
        summary="Three-seat synthetic match emitted artifact-by-artifact during execution."
    )

    setup = scenario / "setup"
    seats = ["seat-01", "seat-02", "seat-03"]
    for idx, (seat, label) in enumerate(zip(seats, ["Synthetic Player A","Synthetic Player B","Synthetic Player C"]), start=1):
        emitter.write(
            f".topics/tower-havoc/runtime/simulations/{SCENARIO}/setup/{idx:03d}-{seat}.seat.trace.md",
            "towerhavoc.match.seat.v1", "../../../../../.schemas/tower-havoc/towerhavoc.match.seat.v1.schema.md",
            f"TH-SIM-09 {seat}", seat_body(seat, label), match
        )
    order = emitter.write(
        f".topics/tower-havoc/runtime/simulations/{SCENARIO}/setup/004-turn-order.trace.md",
        "towerhavoc.turn-order.v1", "../../../../../.schemas/tower-havoc/towerhavoc.turn-order.v1.schema.md",
        "TH-SIM-09 Turn Order", turn_order_body(), match
    )

    state = {
        "seats": seats,
        "seat_states": {s:"active" for s in seats},
        "actions": {"seat-01":10,"seat-02":0,"seat-03":0},
        "ready": {s:2 for s in seats},
        "production": {s:0 for s in seats},
        "floors": {s:0 for s in seats},
        "reinforcements": {s:{} for s in seats},
        "hands": {s:0 for s in seats},
        "deck": 40,
        "discard": "none",
        "event": "none",
        "bell": {s:"no" for s in seats},
        "active": "seat-01",
        "winner": None,
    }
    seq = 0
    initial = emitter.write(
        f".topics/tower-havoc/runtime/simulations/{SCENARIO}/setup/005-initial-state.trace.md",
        "towerhavoc.state.v1", "../../../../../.schemas/tower-havoc/towerhavoc.state.v1.schema.md",
        "TH-SIM-09 Initial State",
        state_body(state,"s000",seq,"../001-ruleset.ruleset.trace.md","initial synthetic setup","scenario setup"),
        match
    )
    current_state = initial

    def rel_from_turn(path: Path):
        return os.path.relpath(path, path.parent).replace(os.sep,"/")

    def emit_state(turn_dir: Path, filename: str, parent_resolution: Path, producing: str):
        nonlocal seq, current_state
        seq += 1
        out = turn_dir / filename
        prev_ref = os.path.relpath(current_state, out.parent).replace(os.sep,"/")
        ruleset_ref = os.path.relpath(ruleset, out.parent).replace(os.sep,"/")
        current_state = emitter.write(
            out.relative_to(target_root).as_posix(),
            "towerhavoc.state.v1", "../../../../../../.schemas/tower-havoc/towerhavoc.state.v1.schema.md",
            f"TH-SIM-09 State s{seq:03d}",
            state_body(state,f"s{seq:03d}",seq,ruleset_ref,prev_ref,producing),
            parent_resolution
        )
        return current_state

    def turn_start(turn_path: Path, turn_dir: Path, prefix: str, seat: str):
        nonlocal current_state
        prior = current_state
        state["actions"][seat] += 1
        matured = state["production"][seat]
        if matured:
            state["ready"][seat] += matured
            state["production"][seat] = 0
        state["bell"][seat] = "yes" if state["floors"][seat] == 3 else "no"
        delta = f"{seat} actions +1"
        outcome = "turn-start resources applied"
        trigger = "turn-start"
        if matured:
            delta += f"; {seat} production ammo -{matured}; ready ammo +{matured}"
            outcome += "; planned ammunition matured"
            trigger = "production-maturation"
        res = emitter.write(
            (turn_dir / f"{prefix}-turn-start.rule-resolution.trace.md").relative_to(target_root).as_posix(),
            "towerhavoc.rule.resolution.v1", "../../../../../../.schemas/tower-havoc/towerhavoc.rule.resolution.v1.schema.md",
            f"TH-SIM-09 Turn Start {seat}",
            rule_resolution_body(
                "001-turn.trace.md",
                "../../001-ruleset.ruleset.trace.md",
                os.path.relpath(prior, turn_dir).replace(os.sep,"/"),
                trigger,
                "active seat begins own turn",
                "../../../../../rules/001-2-action-economy.decision.trace.md; ../../../../../rules/001-3-ammunition.decision.trace.md; ../../../../../rules/001-9-victory.decision.trace.md",
                "deterministic against prior state",
                outcome, delta,
                f"{prefix}-1-state.trace.md"
            ),
            turn_path
        )
        emit_state(turn_dir, f"{prefix}-1-state.trace.md", res, f"turn-start rule resolution for {seat}")

    def turn_end(turn_path: Path, turn_dir: Path, prefix: str, next_seat: str):
        nonlocal current_state
        prior = current_state
        old = state["active"]
        state["active"] = next_seat
        res = emitter.write(
            (turn_dir / f"{prefix}-turn-end.rule-resolution.trace.md").relative_to(target_root).as_posix(),
            "towerhavoc.rule.resolution.v1", "../../../../../../.schemas/tower-havoc/towerhavoc.rule.resolution.v1.schema.md",
            f"TH-SIM-09 Turn End {old}",
            rule_resolution_body(
                "001-turn.trace.md","../../001-ruleset.ruleset.trace.md",
                os.path.relpath(prior,turn_dir).replace(os.sep,"/"),
                "turn-end","active seat ends action window",
                "../../../../../rules/001-4-turn-structure.decision.trace.md",
                "deterministic turn-order progression",
                f"active seat advances from {old} to {next_seat}",
                f"active seat {old}->{next_seat}",
                f"{prefix}-1-state.trace.md"
            ), turn_path
        )
        emit_state(turn_dir, f"{prefix}-1-state.trace.md", res, f"turn-end rule resolution from {old} to {next_seat}")

    def simple_action(turn_path, turn_dir, prefix, seat, kind, params, mutate, outcome, delta, costs, reason):
        nonlocal current_state
        prior = current_state
        intent_name = f"{prefix}-{kind}.intent.trace.md"
        res_name = f"{prefix}-1-{kind}.resolution.trace.md"
        state_name = f"{prefix}-1-1-state.trace.md"
        intent = emitter.write(
            (turn_dir/intent_name).relative_to(target_root).as_posix(),
            "towerhavoc.action.intent.v1","../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md",
            f"TH-SIM-09 {kind.replace('-',' ').title()} Intent",
            intent_body(seat,"001-turn.trace.md",os.path.relpath(prior,turn_dir).replace(os.sep,"/"),kind,params),
            turn_path
        )
        mutate()
        res = emitter.write(
            (turn_dir/res_name).relative_to(target_root).as_posix(),
            "towerhavoc.action.resolution.v1","../../../../../../.schemas/tower-havoc/towerhavoc.action.resolution.v1.schema.md",
            f"TH-SIM-09 {kind.replace('-',' ').title()} Resolution",
            action_resolution_body(
                "001-turn.trace.md","../../001-ruleset.ruleset.trace.md",
                os.path.relpath(prior,turn_dir).replace(os.sep,"/"),
                intent_name,True,reason,costs,False,outcome,delta,state_name
            ), intent
        )
        emit_state(turn_dir,state_name,res,f"{kind} resolution")
        return res

    # TURN 1 — seat-01 builds the tower, schedules ammo, and reinforces value 4.
    t1dir = scenario/"turns/turn-001"
    turn1 = emitter.write(
        (t1dir/"001-turn.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.turn.v1","../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md",
        "TH-SIM-09 Turn 1",turn_body(1,1,"seat-01","../../setup/005-initial-state.trace.md"),match
    )
    turn_start(turn1,t1dir,"001-1","seat-01")

    def planned():
        assert state["actions"]["seat-01"] >= 1
        state["actions"]["seat-01"] -= 1
        state["production"]["seat-01"] += 2
    simple_action(turn1,t1dir,"001-2","seat-01","planned-ammo","quantity=2; delivery=next-own-turn",
                  planned,"planned ammunition entered production","seat-01 actions -1; production ammo +2",
                  "1 action","seat-01 has at least 1 banked action")

    for idx, floor in enumerate([1,2,3], start=3):
        cost={1:2,2:3,3:4}[floor]
        def make_build(f=floor,c=cost):
            def _m():
                assert state["floors"]["seat-01"] == f-1
                assert state["actions"]["seat-01"] >= c
                state["actions"]["seat-01"] -= c
                state["floors"]["seat-01"] = f
                state["bell"]["seat-01"] = "no"
            return _m
        simple_action(turn1,t1dir,f"001-{idx}","seat-01","build",f"floor={floor}",
                      make_build(),f"tower floor {floor} built",
                      f"seat-01 actions -{cost}; tower floors {floor-1}->{floor}",
                      f"{cost} actions",f"seat-01 can build floor {floor} and has {cost} actions")

    def reinforce():
        assert state["actions"]["seat-01"] >= 1 and state["floors"]["seat-01"] >= 1
        state["actions"]["seat-01"] -= 1
        state["reinforcements"]["seat-01"].setdefault(1,set()).add(4)
    simple_action(turn1,t1dir,"001-6","seat-01","reinforce","floor=1; value=4",
                  reinforce,"floor 1 protected against attack value 4",
                  "seat-01 actions -1; reinforcement floor1 value4 added",
                  "1 action","seat-01 has floor 1 and one banked action")
    assert state["actions"]["seat-01"] == 0
    turn_end(turn1,t1dir,"001-7","seat-02")

    # TURN 2 — seat-02 attacks. The random request must exist before fixture value 4 is consumed.
    t2dir=scenario/"turns/turn-002"
    turn2=emitter.write(
        (t2dir/"001-turn.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.turn.v1","../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md",
        "TH-SIM-09 Turn 2",turn_body(2,1,"seat-02","../turn-001/001-7-1-state.trace.md"),match
    )
    turn_start(turn2,t2dir,"001-1","seat-02")
    prior=current_state
    attack_intent=emitter.write(
        (t2dir/"001-2-attack.intent.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.action.intent.v1","../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md",
        "TH-SIM-09 Attack Intent",
        intent_body("seat-02","001-turn.trace.md",os.path.relpath(prior,t2dir).replace(os.sep,"/"),
                    "attack","target-seat=seat-01; target-floor=1"),
        turn2
    )
    request=emitter.write(
        (t2dir/"001-2-1-attack.random-request.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.random.request.v1","../../../../../../.schemas/tower-havoc/towerhavoc.random.request.v1.schema.md",
        "TH-SIM-09 Attack Random Request",
        random_request_body("TH-SIM-09-attack","001-2-attack.intent.trace.md","D6 attack roll",
                            "1,6=miss;2-5=potential hit; reinforcement matching value blocks"),
        attack_intent
    )
    # Only after request verification do we consume the next fixture value.
    declared_self(request)
    attack_roll=next(RNG_VALUES)
    assert attack_roll == 4
    runtime=emitter.write(
        (t2dir/"001-2-1-1-machine.runtime.trace.md").relative_to(target_root).as_posix(),
        "tiinex.machine.runtime.v1",MACHINE_RUNTIME_SCHEMA,
        "TH-SIM-09 Machine Attack Roll Runtime",
        machine_runtime_body("001-2-1-attack.random-request.trace.md",attack_roll,"attack roll"),
        request
    )
    result=emitter.write(
        (t2dir/"001-2-1-1-1-attack.random-result.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.random.result.v1","../../../../../../.schemas/tower-havoc/towerhavoc.random.result.v1.schema.md",
        "TH-SIM-09 Attack Random Result",
        random_result_body("001-2-1-attack.random-request.trace.md",attack_roll,
                           "tower-havoc-attack-d6-v1",str(attack_roll)),
        runtime
    )
    assert state["ready"]["seat-02"] >= 1
    state["ready"]["seat-02"] -= 1
    blocked = attack_roll in state["reinforcements"]["seat-01"].get(1,set())
    assert blocked
    attack_res=emitter.write(
        (t2dir/"001-2-1-1-1-1-attack.resolution.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.action.resolution.v1","../../../../../../.schemas/tower-havoc/towerhavoc.action.resolution.v1.schema.md",
        "TH-SIM-09 Attack Resolution",
        action_resolution_body(
            "001-turn.trace.md","../../001-ruleset.ruleset.trace.md",
            os.path.relpath(prior,t2dir).replace(os.sep,"/"),
            "001-2-attack.intent.trace.md",True,
            "seat-02 has ready ammo; roll 4 is a potential hit but target floor 1 protects value 4",
            "1 ready ammo",
            True,"attack blocked by reinforcement",
            "seat-02 ready ammo -1; tower unchanged",
            "001-2-1-1-1-1-1-state.trace.md",
            "001-2-1-attack.random-request.trace.md","001-2-1-1-1-attack.random-result.trace.md"
        ), result
    )
    emit_state(t2dir,"001-2-1-1-1-1-1-state.trace.md",attack_res,"attack resolution blocked by reinforcement")
    turn_end(turn2,t2dir,"001-3","seat-03")

    # TURN 3 — seat-03 passes.
    t3dir=scenario/"turns/turn-003"
    turn3=emitter.write(
        (t3dir/"001-turn.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.turn.v1","../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md",
        "TH-SIM-09 Turn 3",turn_body(3,1,"seat-03","../turn-002/001-3-1-state.trace.md"),match
    )
    turn_start(turn3,t3dir,"001-1","seat-03")
    simple_action(turn3,t3dir,"001-2","seat-03","pass","none",
                  lambda: None,"seat-03 passes with no state cost","no gameplay resources changed",
                  "none","pass is always available")
    turn_end(turn3,t3dir,"001-3","seat-01")

    # TURN 4 — seat-01 reaches its own turn with three surviving floors; ammo matures and bell becomes eligible.
    t4dir=scenario/"turns/turn-004"
    turn4=emitter.write(
        (t4dir/"001-turn.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.turn.v1","../../../../../../.schemas/tower-havoc/towerhavoc.turn.v1.schema.md",
        "TH-SIM-09 Turn 4",turn_body(4,2,"seat-01","../turn-003/001-3-1-state.trace.md"),match
    )
    turn_start(turn4,t4dir,"001-1","seat-01")
    assert state["bell"]["seat-01"] == "yes"
    assert state["production"]["seat-01"] == 0 and state["ready"]["seat-01"] == 4
    assert state["actions"]["seat-01"] == 1

    prior=current_state
    bell_intent=emitter.write(
        (t4dir/"001-2-bell-attempt.intent.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.action.intent.v1","../../../../../../.schemas/tower-havoc/towerhavoc.action.intent.v1.schema.md",
        "TH-SIM-09 Bell Attempt Intent",
        intent_body("seat-01","001-turn.trace.md",os.path.relpath(prior,t4dir).replace(os.sep,"/"),
                    "bell-attempt","tower=seat-01"),
        turn4
    )
    bell_req=emitter.write(
        (t4dir/"001-2-1-bell.random-request.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.random.request.v1","../../../../../../.schemas/tower-havoc/towerhavoc.random.request.v1.schema.md",
        "TH-SIM-09 Bell Random Request",
        random_request_body("TH-SIM-09-bell","001-2-bell-attempt.intent.trace.md","D6 bell roll","1=success;2-6=fail"),
        bell_intent
    )
    declared_self(bell_req)
    bell_roll=next(RNG_VALUES)
    assert bell_roll == 1
    bell_runtime=emitter.write(
        (t4dir/"001-2-1-1-machine.runtime.trace.md").relative_to(target_root).as_posix(),
        "tiinex.machine.runtime.v1",MACHINE_RUNTIME_SCHEMA,
        "TH-SIM-09 Machine Bell Roll Runtime",
        machine_runtime_body("001-2-1-bell.random-request.trace.md",bell_roll,"bell roll"),
        bell_req
    )
    bell_result=emitter.write(
        (t4dir/"001-2-1-1-1-bell.random-result.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.random.result.v1","../../../../../../.schemas/tower-havoc/towerhavoc.random.result.v1.schema.md",
        "TH-SIM-09 Bell Random Result",
        random_result_body("001-2-1-bell.random-request.trace.md",bell_roll,"tower-havoc-bell-d6-v1","success"),
        bell_runtime
    )
    assert state["actions"]["seat-01"] >= 1
    state["actions"]["seat-01"] -= 1
    state["winner"]="seat-01"
    bell_res=emitter.write(
        (t4dir/"001-2-1-1-1-1-bell.resolution.trace.md").relative_to(target_root).as_posix(),
        "towerhavoc.action.resolution.v1","../../../../../../.schemas/tower-havoc/towerhavoc.action.resolution.v1.schema.md",
        "TH-SIM-09 Bell Attempt Resolution",
        action_resolution_body(
            "001-turn.trace.md","../../001-ruleset.ruleset.trace.md",
            os.path.relpath(prior,t4dir).replace(os.sep,"/"),
            "001-2-bell-attempt.intent.trace.md",True,
            "seat-01 has three floors at own turn start, survived the full orbit, has 1 action, and bell roll is 1",
            "1 action",True,"bell victory",
            "seat-01 actions -1; match terminal winner=seat-01",
            "001-2-1-1-1-1-1-state.trace.md",
            "001-2-1-bell.random-request.trace.md","001-2-1-1-1-bell.random-result.trace.md"
        ), bell_result
    )
    final_state=emit_state(t4dir,"001-2-1-1-1-1-1-state.trace.md",bell_res,"successful bell resolution")

    result_path=emitter.write(
        f".topics/tower-havoc/runtime/simulations/{SCENARIO}/terminal/001-result.trace.md",
        "towerhavoc.match.result.v1","../../../../../.schemas/tower-havoc/towerhavoc.match.result.v1.schema.md",
        "TH-SIM-09 Match Result",
        match_result_body("../turns/turn-004/001-2-1-1-1-1-bell.resolution.trace.md",
                          "../turns/turn-004/001-2-1-1-1-1-1-state.trace.md"),
        bell_res
    )
    assert state["winner"]=="seat-01"
    # Exhaust fixture RNG: no hidden unconsumed outcome is allowed.
    try:
        next(RNG_VALUES)
        raise AssertionError("unexpected extra RNG fixture value")
    except StopIteration:
        pass
    return emitter.emitted

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--target-root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--force", action="store_true")
    args=ap.parse_args()
    emitted=run(args.source_root,args.target_root,args.force)
    print(f"TH-SIM-09 incremental emission complete: {len(emitted)} artifacts")
    for p in emitted:
        print(p.relative_to(args.target_root.resolve()).as_posix())

if __name__=="__main__":
    main()
