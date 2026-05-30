# Failure-case workflow linkage review

## Status

Accepted.

This is a review-only gate.

## Question

After Phase 56, the system has two separate pieces of evidence:

- a manual failure record can link to a failed `agent_runs` row through `agent_run_id`
- a failed workflow parent can be left behind when a deterministic workflow preview stage raises

The question is whether that is enough to add `workflow_run_id` to `failure_cases`.

## Current evidence

Implemented evidence:

- `docs/review/agent-run-failure-linkage-smoke-verification.md`
- `docs/review/workflow-failure-linkage-smoke-verification.md`
- `failure_cases.agent_run_id` can point to a manually created failed agent run
- `POST /workflow-runs/execute-preview` can mark a workflow parent as failed in a route-level test fixture

This proves two local boundaries. It does not yet prove a direct failure-case-to-workflow relationship.

## Decision

Do not add workflow_run_id to failure_cases yet.

The schema remains unchanged.

## Why

The current `failure_cases` path is a manual failure record path.

The current workflow failure smoke is a route-level test fixture that raises during a downstream workflow stage and marks the workflow parent failed.

There is still no failure-case creation path from a failed workflow parent.

Specifically, the system does not yet decide whether failure cases should be:

- manually recorded by a human after inspecting a workflow
- automatically created when a workflow stage raises
- derived from failed child records
- attached to an `agent_run_id`
- attached to a `workflow_run_id`
- attached to both

Until that creation path exists, adding a nullable `workflow_run_id` column to `failure_cases` would make the schema look more causally complete than the runtime.

## Allowed claim

```text
Failure cases can be manually recorded, and deterministic workflow preview failures can mark a workflow parent failed.
```

## Forbidden claims

```text
Failure cases are automatically created from failed workflows.
Failure cases have workflow_run_id linkage.
Every failed workflow has a failure case.
The system has complete workflow failure causality.
The workflow failure smoke is fresh Docker DB evidence.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case workflow linkage application refresh v0
```

That gate should expose the review boundary in application-facing docs without adding schema, API behavior, automatic detection, or a new failure-case creation path.
