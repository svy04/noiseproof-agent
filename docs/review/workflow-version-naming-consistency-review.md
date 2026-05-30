# Workflow version naming consistency review

Status: review-only gate

## Question

After Phase 40 renamed the runtime workflow marker to `phase40-lineage-warning-code-dashboard`, are the project surfaces consistent enough to continue, or is there a bounded follow-up before adding new workflow behavior?

## Observed surfaces

Runtime-facing surfaces use the current marker:

- `apps/api/app/settings.py` defaults to `phase40-lineage-warning-code-dashboard`
- `apps/api/app/schemas.py` defaults `AgentRunCreate` and `WorkflowRunCreate` to `phase40-lineage-warning-code-dashboard`
- `apps/api/tests/test_routes.py` expects `phase40-lineage-warning-code-dashboard`
- `README.md` and `docs/runbook.md` examples show `phase40-lineage-warning-code-dashboard`

Schema defaults still carry older markers:

- `db/init/001_schema.sql` defaults `agent_runs.workflow_version` and `workflow_runs.workflow_version` to `phase36-structured-warning-taxonomy`
- `db/migrations/007_workflow_runs.sql` defaults `workflow_runs.workflow_version` to `phase24-workflow-run-schema`

## Decision

Do not change schema defaults in this review gate.

The current runtime path is inspectable, but stale schema defaults create a real drift risk for direct SQL inserts, future fixture setup, or any path that omits `workflow_version` from inserts.

Treat this as stale schema defaults, not as evidence that workflow semantics changed.

## Boundary

This review adds no runtime behavior, migrations, columns, join tables, trace schema changes, dashboard rendering changes, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

It also does not claim that all historical references to older phase names are wrong. Some older references are valid historical context in review notes and phase history. The problem is limited to executable schema defaults.

## Next direction

schema default workflow version update v0

That follow-up should update executable schema defaults so newly initialized databases no longer default to older workflow-version markers. It should not rewrite historical review documents or old phase history unless those documents are pretending to describe current runtime behavior.
