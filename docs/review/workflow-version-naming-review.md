# Workflow Version Naming Review

Status: Accepted

Workflow version naming review is a bounded review-only gate.

## Context

The API currently reports `workflow_version` as:

```text
phase36-structured-warning-taxonomy
```

That value appears in health checks, ops summary responses, workflow-run defaults, agent-run traces, and docs examples.

After Phase 36, several later gates were documentation or dashboard-only phases:

- warning-code documentation review
- warning-code runbook example
- warning-code dashboard review
- warning-code dashboard surfacing
- warning-code dashboard smoke example

Those phases improved inspectability around warning codes, but they did not change the deterministic workflow execution semantics, lineage read-model semantics, or warning-code taxonomy itself.

## Decision

Do not rename workflow_version in this review gate.

Keep `phase36-structured-warning-taxonomy` until a dedicated update gate changes the runtime identifier and all affected examples together.

The name is currently stale relative to the latest dashboard docs, but it remains accurate for the lineage warning taxonomy behavior that the deterministic workflow uses.

## Why Not Rename Now

Changing `workflow_version` touches more than display copy:

- `GET /health`
- `GET /ops/summary`
- default `WorkflowRun` rows
- auto-created `agent_runs.trace_json`
- runbook expected response examples
- route tests that assert stable workflow-version values

Doing that inside a review gate would make the review look like a runtime behavior change.

## Explicit Non-changes

This gate adds:

- no runtime behavior
- no `workflow_version` rename
- no migrations
- no columns
- no join tables
- no trace schema changes
- no dashboard rendering changes
- no LLM calls
- no embeddings
- no semantic retrieval
- no autonomous workflow execution
- no free-form final answer generation

## Next Gate

Recommended next gate:

```text
workflow version naming update v0
```

Acceptance for that gate should require:

- a new runtime version string chosen once
- `app.settings.Settings.workflow_version` updated
- route tests updated through one shared constant
- runbook examples updated
- README/docs updated
- no workflow semantics, storage schema, retrieval, Evidence Ledger, Noise Gate, report, dashboard, LLM, or embedding behavior changes
