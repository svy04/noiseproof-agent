# WorkflowRun child-link review

Status: reviewed, not implemented.

This is a review-only gate.

## Question

Should persisted Evidence Ledger, Noise Gate, Report, RetrievalRun, or AgentRun records get nullable `workflow_run_id` columns now that `workflow_runs` can be created, listed, and viewed in the dashboard?

## Decision

Do not add child workflow_run_id columns in this review gate.

Keep the current local provenance model:

- `agent_run_id` links persisted Evidence Ledger, Noise Gate, and Report records to the operation that created them.
- `workflow_trace_id` correlates deterministic preview and persistence records across endpoints.
- `workflow_runs` is currently metadata-only. It can be created, listed, and viewed in the dashboard, but it does not execute an evidence -> gate -> report workflow.

## Why

Adding nullable `workflow_run_id` columns now would make the schema look more complete than the runtime.

The system does not yet have a single endpoint or service that:

1. creates a workflow run,
2. executes retrieval,
3. creates Evidence Ledger records,
4. runs a Noise Gate,
5. creates a Report Preview record,
6. attaches every child record to the same parent workflow run,
7. records failures against that workflow run.

Without that owner, child `workflow_run_id` columns would create a false sense of workflow causality.

## What stays true

- `workflow_runs` exists as metadata storage.
- `GET /ops/dashboard` can show workflow-run metadata.
- `agent_run_id` remains operation-level provenance.
- `workflow_trace_id` remains local correlation.
- Direct evidence -> gate -> report links remain deferred.

## What remains unproven

- A workflow run can own a full evidence -> gate -> report sequence.
- Failures inside a multi-step workflow can be attached to the workflow parent.
- Child records can be safely migrated from trace-level correlation to workflow-level causality.
- Dashboard links can show a complete workflow tree rather than parallel metadata tables.

## Acceptance criteria for adding child links later

Before adding `workflow_run_id` columns to child records, the project should have:

- a minimal workflow execution endpoint or service boundary,
- one deterministic workflow path that creates a parent `workflow_runs` row first,
- child creation calls that receive the parent workflow id explicitly,
- failure handling that updates the parent workflow status,
- tests proving all created child records share the same workflow parent,
- dashboard copy that distinguishes workflow causality from local trace correlation.

## Next gate

Implement either:

1. a review-only workflow execution boundary, or
2. a minimal workflow execution service that owns the deterministic retrieval -> evidence -> gate -> report path.

Do not add child links before that boundary exists.

## Follow-up status after Phase 28

Phase 28 implemented a minimal deterministic workflow execution preview at `POST /workflow-runs/execute-preview`.

That endpoint now creates a parent `workflow_runs` row and runs retrieval -> evidence -> gate -> report preview steps. Child records are still correlated by `workflow_trace_id`; they are not attached to `workflow_run_id` columns.

The next gate should review whether this deterministic execution preview provides enough runtime evidence to justify nullable child `workflow_run_id` schema changes.

## Follow-up status after Phase 29

Phase 29 added nullable `workflow_run_id` fields to retrieval, Evidence Ledger, Noise Gate, and Report records. The deterministic workflow execution preview now attaches those child records to the parent workflow run.

This remains local workflow provenance. It is not distributed tracing, autonomous workflow execution, or direct evidence -> gate -> report foreign-key lineage.

## Follow-up status after Phase 30

Phase 30 added `GET /workflow-runs/{id}` so the parent workflow run can be inspected with its linked retrieval, Evidence Ledger, Noise Gate, and Report child records.

This improves workflow-level inspectability, but it still does not create direct evidence -> gate -> report foreign-key lineage. A separate review should decide whether cross-stage links are justified now that the deterministic parent and child inspection surface exist.
