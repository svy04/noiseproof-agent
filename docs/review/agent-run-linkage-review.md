# Agent-run Linkage Review

Status: Phase 18.5 review gate.

This is a review artifact, not a runtime implementation. It decides whether the current persisted Evidence Ledger, Noise Gate, and Report records are ready for direct `agent_run_id` foreign-key linkage.

## Current State

Persisted records currently share a `workflow_trace_id` with the matching `agent_runs.trace_json` entry.

This is inspectable through:

- `GET /traces/{workflow_trace_id}`
- `GET /evidence-ledgers?workflow_trace_id=...`
- `GET /noise-gates?workflow_trace_id=...`
- `GET /reports?workflow_trace_id=...`
- `GET /ops/dashboard`

The current `run_with_trace()` lifecycle creates the persisted business record inside the operation, then creates the `agent_runs` trace after the operation returns. That order makes the current `workflow_trace_id` link valid, but it means a non-null `agent_run_id` is not available when the persisted record is inserted.

## Decision

Do not add the foreign key in this review gate.

Adding nullable `agent_run_id` columns now would create a false sense of provenance because most new records would still be linked by `workflow_trace_id`, not by a database-enforced parent row.

Before implementing direct foreign-key linkage, the runtime should create the agent run first, pass its id into the operation, then update the trace status and latency after the operation finishes.

## Alternatives Considered

### Add nullable `agent_run_id` columns now

Rejected for this gate.

This would make the schema look more mature than the runtime is. If the columns are nullable and mostly empty, reviewers may think records are formally linked when the actual linkage still depends on `workflow_trace_id`.

### Keep only `workflow_trace_id`

Accepted for now.

The current link is explicit, test-covered, and visible in the dashboard. It is not full provenance, but it is honest and inspectable.

### Create agent runs first, then persist child records

Preferred future implementation.

This would make `agent_run_id` meaningful because every persisted Evidence Ledger, Noise Gate, and Report record could point to the exact parent run. It requires a lifecycle change, not just a migration.

### Add a separate workflow run table

Deferred.

It may become useful if a single workflow contains retrieval, evidence, gate, and report stages under one parent execution. That is larger than the current deterministic preview boundary.

## Future Acceptance Criteria

A future `agent_run_id` linkage phase should be accepted only when:

- `agent_runs` rows are created before persisted Evidence Ledger, Noise Gate, and Report records are inserted.
- persisted records can store a non-null `agent_run_id` that points to the parent run.
- the same records still expose `workflow_trace_id` for human-readable trace grouping.
- failed operations still leave a failed agent run.
- tests prove child records can be joined through `agent_run_id`.
- runtime smoke proves the linkage against PostgreSQL, not only the in-memory repository.

## Boundary

This review does not implement a migration.
It does not add new API endpoints.
It does not change dashboard behavior.
It does not claim full distributed tracing or hosted observability.

The current honest claim remains:

```text
Persisted evidence, gate, and report records are correlated with agent-run trace metadata through workflow_trace_id.
Direct agent_run_id foreign-key linkage is reviewed but not implemented.
```
