# Agent-run Linkage Review

Status: Phase 18.5 review gate, updated after Phase 20 child-record linkage implementation.

This began as a review artifact before runtime implementation. It records the decision path for direct `agent_run_id` foreign-key linkage.

## Current State

Persisted records currently share a `workflow_trace_id` with the matching `agent_runs.trace_json` entry and store the parent `agent_run_id`.

This is inspectable through:

- `GET /traces/{workflow_trace_id}`
- `GET /evidence-ledgers?workflow_trace_id=...`
- `GET /noise-gates?workflow_trace_id=...`
- `GET /reports?workflow_trace_id=...`
- `GET /ops/dashboard`

Before Phase 19, `run_with_trace()` created the persisted business record inside the operation, then created the `agent_runs` trace after the operation returned. That order made the current `workflow_trace_id` link valid, but it meant a non-null `agent_run_id` was not available when the persisted record was inserted.

Phase 19 changed the parent run lifecycle: `run_with_trace()` now creates the `agent_runs` row before operation execution and updates the same row after completion or failure.

Phase 20 added direct child-record `agent_run_id` linkage for persisted Evidence Ledger, Noise Gate, and Report records.

## Decision

Original Phase 18.5 decision: Do not add the foreign key in this review gate.

Adding nullable `agent_run_id` columns now would create a false sense of provenance because most new records would still be linked by `workflow_trace_id`, not by a database-enforced parent row.

Before implementing direct foreign-key linkage, the runtime should create the agent run first, pass its id into the operation, then update the trace status and latency after the operation finishes. Phase 19 implemented that prerequisite. Phase 20 added child-record `agent_run_id` fields and tests.

## Alternatives Considered

### Add nullable `agent_run_id` columns before parent lifecycle

Rejected for the Phase 18.5 gate.

This would make the schema look more mature than the runtime is. If the columns are nullable and mostly empty, reviewers may think records are formally linked when the actual linkage still depends on `workflow_trace_id`.

### Keep only `workflow_trace_id`

Accepted during Phase 18.5 and superseded by Phase 20.

The current link is explicit, test-covered, and visible in the dashboard. It is not full provenance, but it is honest and inspectable.

### Create agent runs first, then persist child records

Partially implemented by Phase 19.

This makes `agent_run_id` meaningful because every persisted Evidence Ledger, Noise Gate, and Report record can point to the exact parent run. The parent lifecycle and child-record migration now exist.

### Add a separate workflow run table

Deferred.

It may become useful if a single workflow contains retrieval, evidence, gate, and report stages under one parent execution. That is larger than the current deterministic preview boundary.

## Future Acceptance Criteria

The child-record `agent_run_id` linkage phase should be accepted only when:

- `agent_runs` rows are created before persisted Evidence Ledger, Noise Gate, and Report records are inserted. Phase 19 satisfies this parent lifecycle prerequisite.
- persisted records can store a non-null `agent_run_id` that points to the parent run. Phase 20 satisfies this.
- the same records still expose `workflow_trace_id` for human-readable trace grouping.
- failed operations still leave a failed agent run.
- tests prove child records can be joined through `agent_run_id`. Phase 20 adds this.
- runtime smoke proves the linkage against PostgreSQL, not only the in-memory repository. Phase 20 should be verified with this before external claims.

## Boundary

This review itself did not implement a migration.
Phase 20 later added `db/migrations/006_child_agent_run_ids.sql`.
It does not add new API endpoints.
It does not change dashboard behavior.
It does not claim full distributed tracing or hosted observability.

The current honest claim remains:

```text
Persisted evidence, gate, and report records are correlated with agent-run trace metadata through workflow_trace_id.
Direct agent_run_id foreign-key linkage is implemented for persisted evidence, gate, and report records, but it remains local service provenance rather than distributed tracing.
```
