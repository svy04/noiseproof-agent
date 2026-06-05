# Workflow Stage Event Log

Status: workflow stage event log v0.

This is a local deterministic workflow observability gate. It records one local event row for each deterministic `POST /workflow-runs/execute-preview` stage so reviewers can inspect the input/output summary and timing boundary of the current preview workflow.

Implemented:

```text
workflow_stage_events
db/migrations/024_workflow_stage_events.sql
db/init/001_schema.sql
repository create/list methods
WorkflowStageEventCreate
WorkflowStageEventOut
WorkflowRunDetailOut.stage_events
WorkflowRunDetailSummaryOut.workflow_stage_event_count
GET /workflow-runs/{id}
GET /workflow-runs/{id}/proof-bundle
```

Recorded stages:

```text
1 retrieval
2 evidence_ledger
3 noise_gate
4 report
```

Each event records:

```text
workflow_run_id
workflow_trace_id
stage_name
stage_order
stage_status
started_at
ended_at
latency_ms
input_summary_json
output_summary_json
event_boundary
```

Boundary:

```text
local_workflow_stage_event_log_not_distributed_tracing
```

This is not distributed tracing, not OpenTelemetry, not hosted observability, not an external telemetry export, not autonomous workflow execution, not LLM execution, and not product-complete.

Runtime smoke:

```text
docs/review/workflow-stage-event-log-runtime-smoke.md
```

What this helps a reviewer inspect:

- whether the deterministic workflow preview ran the expected stages in order
- whether each stage produced a bounded output summary
- whether `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle` expose the same stage event count
- whether the current workflow has local stage-level observability without claiming production tracing

What remains unproven:

- distributed tracing across services
- hosted observability
- durable span export
- production monitoring
- autonomous multi-agent execution
- semantic retrieval quality
- actual LLM-based report generation
