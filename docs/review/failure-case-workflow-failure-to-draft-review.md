# Failure-case workflow failure-to-draft review

## Status

Accepted.

This is a review-only gate.

## Question

NoiseProof now has two separate proof surfaces:

1. a failed workflow parent can be inspected after a deterministic workflow stage raises
2. `POST /failure-cases/draft-preview` can prepare a non-persisting human-confirmed draft payload

The next question is:

```text
Should the system now connect a failed workflow parent to draft-preview input, or jump directly to automatic failure-case creation?
```

## Current evidence

Implemented evidence:

- `tests/test_routes.py::test_workflow_execute_preview_marks_parent_failed_when_stage_errors`
- `workflow_run.status = failed`
- `workflow_run.error_message` records the stage exception
- `workflow_run.trace_json.stage` remains `workflow_execute_preview`
- `workflow_run.trace_json.error_type` records `RuntimeError`
- `POST /failure-cases/draft-preview` accepts `workflow_run_id`, `workflow_status`, `error_message`, and `trace_json`
- draft preview returns `preview_only_not_persisted`
- draft preview requires human confirmation
- draft preview can be manually persisted through `POST /failure-cases`
- fresh migrated Docker DB handoff smoke verifies the manual persistence path

Missing evidence:

- no smoke test takes a real failed workflow parent response and feeds that evidence to `POST /failure-cases/draft-preview`
- no route proves the failed workflow parent fields are sufficient draft-preview input
- no API endpoint automatically creates failure cases from failed workflow parents

## Decision

Do not add automatic failure-case creation in this review gate.

Do not add workflow_run_id to failure_cases in this review gate.

Do not add a confirm endpoint in this review gate.

The next bounded proof should be a workflow failure-to-draft smoke:

```text
POST /workflow-runs/execute-preview
  -> force a deterministic stage failure in the route fixture
  -> inspect failed workflow parent
  -> build draft-preview input from workflow_run.id, workflow_run.status, workflow_run.error_message, and workflow_run.trace_json
  -> POST /failure-cases/draft-preview
  -> verify the draft references the workflow failure evidence
  -> verify failure_cases remain unchanged
```

This proves the handoff from workflow failure evidence to draft preparation without adding persistence automation.

## Alternatives considered

### Automatically create a failure case when a workflow fails

Rejected.

The project still cannot prove that every failed workflow parent should become a durable failure-case record. Some failures may be expected boundary behavior, test fixtures, user input problems, or transient runtime issues.

### Add `workflow_run_id` to `failure_cases`

Rejected.

Adding schema linkage before proving the workflow failure-to-draft handoff would make the data model look more causally complete than the runtime evidence.

### Add a confirm endpoint

Rejected.

The manual handoff through existing `POST /failure-cases` already works. A confirm endpoint should wait until the project proves repeated manual handoff friction or a clearer UI/API requirement.

### Prove failed workflow parent to draft-preview input first

Accepted.

This is the smallest honest next step. It connects two existing surfaces without adding schema, automation, or persistence claims.

## Required next smoke

The next smoke should verify:

- the workflow parent is marked failed
- the workflow parent has an error message
- the workflow parent has trace metadata with stage and error type
- draft-preview accepts the failed workflow parent fields
- draft-preview returns `preview_only_not_persisted`
- draft-preview returns `human_confirmation_required: true`
- failure cases remain unchanged

## Claim boundary

Allowed claim after this review:

```text
NoiseProof has selected a failed-workflow-parent to draft-preview smoke as the next proof step before any automatic failure-case creation.
```

Forbidden claims:

```text
This is not automatic failure detection.
This is not automatic failure-case creation.
This is not automatic failure-case persistence.
This does not add workflow_run_id to failure_cases.
This is not complete workflow failure causality.
This does not prove complete workflow failure causality.
This is not hosted deployment evidence.
```

## Next bounded gate

The next bounded gate should be:

```text
workflow failure-to-draft smoke verification v0
```

That gate should prove a failed workflow parent can feed the existing draft-preview endpoint without creating or persisting a failure case.
