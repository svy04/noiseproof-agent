# Single workflow parent review

Status: Phase 23 review-only gate.

This is a review-only gate. It decides whether NoiseProof should introduce a workflow-level parent before implementing direct evidence -> gate -> report cross-links.

## Current State

`agent_runs` currently represents one endpoint invocation.

That boundary is useful and honest:

- `POST /evidence-ledgers` creates one parent `agent_runs` row.
- `POST /noise-gates` creates one parent `agent_runs` row.
- `POST /reports` creates one parent `agent_runs` row.
- each persisted child record stores the parent `agent_run_id` for that endpoint call.

But this is not a single workflow parent. It does not prove that a persisted report used a specific persisted gate record, or that a persisted gate record used specific persisted Evidence Ledger rows.

## Decision

Do not reuse agent_runs as the workflow parent.

Reusing `agent_runs` would collapse two different concepts:

- operation run: one endpoint invocation
- workflow run: one evidence -> gate -> report chain

That would create a false sense of orchestration because the current service can still run each endpoint independently. A report endpoint call can receive evidence-shaped payloads without consuming persisted Evidence Ledger rows or a persisted Noise Gate record.

The next implementation should introduce a separate `workflow_runs` parent if the project wants true cross-stage lineage.

## Proposed Future Shape

A future `workflow_runs` table should own a whole deterministic chain:

```text
workflow_runs
  -> evidence_ledger_entries
  -> noise_gate_records
  -> report_records
```

Minimum planned fields:

```text
id
question
workflow_version
status
created_at
started_at
ended_at
latency_ms
error_message
trace_json
```

Possible status values:

```text
created
running
completed
failed
blocked
needs_revision
```

The existing `agent_runs` table should continue to describe individual endpoint or operation calls. A future workflow can still create one or more agent runs underneath a workflow parent, but the workflow parent should be the chain owner.

## Alternatives Considered

### Reuse `agent_runs`

Rejected.

It is already used as one endpoint invocation metadata. Reusing it for multi-stage chains would make old and new rows ambiguous. Some rows would mean one endpoint call; others would mean evidence -> gate -> report orchestration.

### Use only `workflow_trace_id`

Rejected for workflow ownership.

`workflow_trace_id` is a useful local correlation id, but it is not a durable parent record with lifecycle, status, or child ownership. It cannot tell whether the workflow completed, blocked, or failed as a chain.

### Add direct child cross-links without a workflow parent

Rejected.

This was already rejected in the evidence-to-gate/report cross-links review. It creates a false sense of orchestration because the current endpoint boundaries do not require persisted upstream records.

### Add `workflow_runs`

Accepted as the likely next implementation direction.

This separates the service into two inspectable layers:

- workflow-level provenance: one evidence -> gate -> report chain
- operation-level traces: individual endpoint or stage runs

## Future Acceptance Criteria

`workflow_runs` should be implemented only when:

- the schema has a dedicated `workflow_runs` table
- a workflow run is created before evidence, gate, or report child records are inserted
- evidence, gate, and report records can store `workflow_run_id`
- the service has an endpoint or service function that owns the chain order
- failure in any stage leaves a failed or blocked workflow parent
- tests prove the chain is created by execution order, not inferred by matching text
- the dashboard labels workflow-level provenance separately from `agent_runs`
- documentation states that this is local workflow provenance, not distributed tracing
- runtime smoke verifies the schema and chain against PostgreSQL

## Boundary

This review does not add migrations.
It does not add a `workflow_runs` table.
It does not add `workflow_run_id` columns.
It does not add a workflow execution endpoint.
It does not change `agent_runs`.
It does not change dashboard behavior.
It does not claim orchestration, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

The current honest claim remains:

```text
NoiseProof has operation-level parent runs for persisted evidence, gate, and report endpoints. It does not yet have a single workflow parent for the full evidence -> gate -> report chain.
```
