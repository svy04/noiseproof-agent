# External Feedback Current-state Workflow Failure Auto-creation Runtime Issue Verification

Phase marker: external feedback current-state workflow failure auto-creation runtime issue verification v0.

This records the current issue #1 screen after the workflow failure auto-creation runtime issue-body refresh. It verifies that the request now points to the latest local v0 workflow failure auto-created failure-case proof while external reviewer feedback remains pending.

Previous routing gate: external review issue body workflow failure auto-creation runtime refresh v0.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Proof documents:

```text
proof_doc: docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md
request_doc: docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md
issue_doc: docs/review/external-review-issue-body-workflow-failure-auto-creation-runtime-refresh.md
```

Observed issue body state:

```json
{
  "updatedAt": "2026-06-05T18:44:28Z",
  "url": "https://github.com/svy04/noiseproof-agent/issues/1",
  "starts_with_request": true,
  "first_codepoint": 35,
  "body_length": 6598,
  "comment_count": 1,
  "screened_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0,
  "status": "pending",
  "has_workflow_failure_auto_creation_runtime_proof": true,
  "has_workflow_failure_auto_creation_request_refresh": true,
  "has_workflow_failure_auto_creation_issue_body_refresh": true,
  "has_failure_case_count_delta": true,
  "has_auto_failure_case_id": true,
  "has_auto_created_boundary": true,
  "has_external_feedback_boundary": true
}
```

Current issue proof markers:

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

Screening commands:

```text
uv run python -m packages.review.external_feedback_cli --input <captured-issue-json> --repository-owner svy04
uv run python -m packages.review.external_feedback_acceptance_cli --input <screening-json>
```

Screening result:

```json
{
  "status": "pending",
  "candidate_count": 0,
  "next_gate": "external reviewer feedback v0",
  "does_not_close_gate": true,
  "warnings": [],
  "screened_comments": [
    {
      "author_login": "svy04",
      "classification": "non_qualifying",
      "reasons": [
        "self_authored_comment"
      ]
    }
  ]
}
```

Acceptance draft result:

```json
{
  "status": "pending",
  "draft_count": 0,
  "next_gate": "external reviewer feedback v0",
  "does_not_close_gate": true,
  "warnings": [
    "No candidate comments were available for acceptance drafting."
  ],
  "drafts": []
}
```

Comment screening:

```text
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
external reviewer feedback v0 gate remains pending
```

Boundary:

```text
current-state issue verification only
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
