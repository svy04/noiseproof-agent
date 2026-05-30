# Direct evidence-to-gate/report cross-link review

Status: Phase 30.5 review-only gate.

This is a review-only gate. It asks whether the project should now add direct evidence -> gate -> report foreign-key links after Phase 30 added a workflow parent detail endpoint.

## Current State

The repo now has:

- a `workflow_runs` parent table
- `POST /workflow-runs/execute-preview`
- nullable `workflow_run_id` on retrieval, Evidence Ledger, Noise Gate, and Report records
- `GET /workflow-runs/{id}` to inspect the parent and its linked child records
- shared `workflow_trace_id` for local correlation

The deterministic workflow currently executes this sequence:

```text
workflow_runs parent
  -> retrieval run
  -> Evidence Ledger preview
  -> persisted Evidence Ledger rows
  -> Noise Gate preview from evidence-shaped entries
  -> persisted Noise Gate record
  -> Report preview from evidence-shaped entries
  -> persisted Report record
```

This proves that child records can share a workflow parent. It does not yet prove that a persisted Noise Gate record consumed specific persisted Evidence Ledger row ids, or that a persisted Report record consumed a specific persisted Noise Gate record id.

## Decision

Do not add direct evidence -> gate -> report foreign-key links in this review gate.

The service should not add columns such as:

```text
noise_gate_records.input_evidence_ledger_entry_ids
report_records.input_evidence_ledger_entry_ids
report_records.input_noise_gate_record_id
```

until runtime execution order explicitly passes persisted upstream row ids into downstream persistence.

Adding those links now would create a false sense of stage-level causality. The current workflow has a parent id, but the Noise Gate and Report preview services still consume evidence-shaped values rather than persisted Evidence Ledger row identities.

## Why The Parent Is Not Enough

`workflow_run_id` proves common workflow membership.

It does not prove:

- this Noise Gate record consumed these exact persisted Evidence Ledger rows
- this Report record consumed this exact persisted Noise Gate record
- downstream records were impossible to create without upstream persisted ids
- the dashboard can present evidence -> gate -> report links as execution order rather than grouping

`GET /workflow-runs/{id}` is the correct inspection surface for the current state. It shows the tree of local child records, but it should not be rebranded as direct stage-level lineage.

## Alternatives Considered

### Add JSON id arrays now

Rejected for this gate.

JSON arrays such as `input_evidence_ledger_entry_ids` would be easy to add, but they should be populated only from actual persisted upstream rows passed into downstream creation. Without that execution order, they are just copied metadata.

### Add strict foreign-key join tables now

Rejected for this gate.

Join tables such as `noise_gate_evidence_entries` and `report_evidence_entries` imply stronger relational lineage than the current deterministic preview proves.

### Treat `workflow_run_id` as sufficient direct lineage

Rejected as a stage-level claim.

`workflow_run_id` is useful local workflow provenance. It is not direct evidence -> gate -> report causality.

### Keep parent-level inspection and add a later stage-input manifest

Accepted as the next safest direction.

The next implementation should record downstream stage inputs from persisted upstream ids inside the deterministic workflow execution path. The smallest honest version is a stage-input manifest that records which persisted evidence row ids and gate record ids were handed to the next stage.

## Acceptance Criteria For Direct Links Later

Direct cross-stage links become justified only when:

- persisted Evidence Ledger rows are created first
- the Noise Gate input is built from those persisted rows or their ids
- the persisted Noise Gate record stores the upstream evidence row ids it consumed
- the Report input is built from the persisted Evidence Ledger rows and persisted Noise Gate record
- the persisted Report record stores the upstream evidence row ids and gate record id it consumed
- tests prove the links come from execution order, not text matching
- `GET /workflow-runs/{id}` exposes these links as local workflow provenance
- dashboard or docs label the links as local deterministic workflow lineage, not distributed tracing

## Boundary

This review does not add migrations.
It does not add columns.
It does not add endpoints.
It does not change runtime behavior.
It does not claim direct evidence -> gate -> report foreign-key links exist.

The current honest claim is:

```text
WorkflowRun detail now shows retrieval, Evidence Ledger, Noise Gate, and Report child records under one workflow parent. Direct evidence -> gate -> report links remain unimplemented because downstream stages do not yet consume persisted upstream row ids.
```

## Next Gate

Recommended next implementation:

```text
Workflow stage input manifest v0
```

That gate should add the smallest runtime evidence needed to prove downstream stages consumed persisted upstream ids before adding stronger foreign-key or join-table claims.

## Follow-up status after Phase 31

Phase 31 implemented `stage_input_manifest` on deterministic workflow-created Noise Gate and Report records.

The manifest records persisted Evidence Ledger row ids consumed by the gate preview, plus persisted Evidence Ledger row ids and the persisted Noise Gate record id consumed by the report preview. This is enough to show local stage input provenance for the deterministic preview, but it is still not a direct evidence -> gate -> report foreign-key or join-table lineage.
