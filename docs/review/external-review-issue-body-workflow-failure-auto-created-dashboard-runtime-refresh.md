# External Review Issue Body Workflow Failure Auto-created Failure-case Dashboard Runtime Refresh

Phase marker: external review issue body workflow failure auto-created dashboard runtime refresh v0.

This records the owner-authored issue #1 body refresh that routes external reviewers to the workflow failure auto-created failure-case dashboard runtime proof.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Proof documents:

```text
proof_doc: docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md
request_doc: docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md
issue_doc: docs/review/external-review-issue-body-workflow-failure-auto-created-dashboard-runtime-refresh.md
related_proof_doc: docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md
related_request_doc: docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md
```

Observed issue body state after refresh:

```text
updatedAt: 2026-06-05T19:21:14Z
url: https://github.com/svy04/noiseproof-agent/issues/1
starts_with_request: true
first_codepoint: 35
body_length: 7266
comment_count: 1
has_workflow_failure_auto_created_dashboard_runtime_proof: true
has_workflow_failure_auto_created_dashboard_request_refresh: true
has_workflow_failure_auto_created_dashboard_issue_body_record: true
has_dashboard_auto_created_failure_case_id: true
has_dashboard_workflow_parent_link: true
has_dashboard_review_queue_linked_count: true
has_external_feedback_boundary: true
```

Issue body highlights:

```text
POST /workflow-runs/execute-preview -> 500
GET /workflow-runs/{id} -> 200
GET /workflow-runs/{id}/proof-bundle -> 200
GET /failure-cases?workflow_run_id={id} -> 200
GET /ops/dashboard -> 200
failure_case_count_delta -> 1
detail_failure_case_count -> 1
bundle_detail_failure_case_count -> 1
filtered_failure_case_count -> 1
auto_failure_case_id
auto_created_from_workflow_failure_local_v0
local_workflow_stage_failure_event_auto_failure_case_local_v0
dashboard_contains_auto_created_failure_case_id
dashboard_contains_workflow_parent_link
dashboard_contains_review_queue_linked_count
```

Boundary:

```text
owner-authored issue body routing only
not external reviewer feedback
not hosted deployment evidence
not retry behavior
not root-cause automation
not complete workflow failure causality
not production background worker behavior
not distributed tracing
not hosted observability
not customer validation
not Braincrew acceptance
not product-complete
```

Next verification gate:

```text
external feedback current-state workflow failure auto-created dashboard runtime issue verification v0
```

Current-state verification record:

```text
docs/review/external-feedback-current-state-workflow-failure-auto-created-dashboard-runtime-issue-verification.md
```
