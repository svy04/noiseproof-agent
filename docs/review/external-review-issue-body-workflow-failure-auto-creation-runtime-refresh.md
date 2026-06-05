# External Review Issue Body Workflow Failure Auto-creation Runtime Refresh

Phase marker: external review issue body workflow failure auto-creation runtime refresh v0.

This records the owner-authored issue #1 body refresh that routes external reviewers to the workflow failure auto-created failure-case runtime proof.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Proof documents:

```text
proof_doc: docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md
request_doc: docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md
issue_doc: docs/review/external-review-issue-body-workflow-failure-auto-creation-runtime-refresh.md
current_state_doc: docs/review/external-feedback-current-state-workflow-failure-auto-creation-runtime-issue-verification.md
```

Observed issue body state after refresh:

```json
{
  "updatedAt": "2026-06-05T18:44:28Z",
  "url": "https://github.com/svy04/noiseproof-agent/issues/1",
  "starts_with_request": true,
  "first_codepoint": 35,
  "body_length": 6598,
  "comment_count": 1,
  "has_workflow_failure_auto_creation_runtime_proof": true,
  "has_workflow_failure_auto_creation_request_refresh": true,
  "has_workflow_failure_auto_creation_issue_body_refresh": true,
  "has_failure_case_count_delta": true,
  "has_auto_failure_case_id": true,
  "has_auto_created_boundary": true,
  "has_external_feedback_boundary": true
}
```

Issue body highlights:

```text
POST /workflow-runs/execute-preview -> 500
GET /workflow-runs/{id} -> 200
GET /workflow-runs/{id}/proof-bundle -> 200
GET /failure-cases?workflow_run_id={id} -> 200
failure_case_count_delta -> 1
detail_failure_case_count -> 1
bundle_detail_failure_case_count -> 1
filtered_failure_case_count -> 1
auto_failure_case_id
auto_created_from_workflow_failure_local_v0
local_workflow_stage_failure_event_auto_failure_case_local_v0
```

Boundary:

```text
owner-authored issue body routing only
not external reviewer feedback
not hosted deployment evidence
not retry behavior
not root-cause automation
not complete workflow failure causality
not distributed tracing
not hosted observability
not customer validation
not Braincrew acceptance
not product-complete
```

Next verification gate:

```text
external feedback current-state workflow failure auto-creation runtime issue verification v0
```
