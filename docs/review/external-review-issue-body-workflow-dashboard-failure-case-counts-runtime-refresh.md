# External Review Issue Body Workflow Dashboard Failure-case Counts Runtime Refresh

Status: live issue body refresh completed.

Phase marker: external review issue body workflow dashboard failure-case counts runtime refresh v0.

## Purpose

Record the owner-authored issue #1 body update that points reviewers to the workflow dashboard failure-case counts runtime smoke and its request-refresh record.

This keeps external reviewer feedback v0 pending.

It does not accept feedback.

It does not close the external feedback gate.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Latest Proof

```text
docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md
```

## Reviewer Request Refresh

```text
docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md
```

## Issue-body Refresh Record

```text
docs/review/external-review-issue-body-workflow-dashboard-failure-case-counts-runtime-refresh.md
```

## Observed Issue State

Observed through `gh issue view 1 --repo svy04/noiseproof-agent --json number,title,body,comments,updatedAt` after editing the issue body.

```json
{
  "updatedAt": "2026-06-05T06:25:07Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_workflow_dashboard_failure_case_counts_runtime_proof": true,
  "has_workflow_dashboard_failure_case_counts_request_refresh": true,
  "has_workflow_dashboard_failure_case_counts_issue_body_refresh": true,
  "has_dashboard_contains_linked_failure_cases_header": true,
  "has_dashboard_contains_linked_failure_case_filter": true,
  "has_dashboard_omits_unlinked_failure_case_filter": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "body_length": 12392
}
```

## Issue Body Highlights

The issue body now asks reviewers to inspect:

```text
Workflow dashboard failure-case counts runtime smoke
Workflow dashboard failure-case counts request refresh
Issue-body refresh record
```

It highlights:

```text
GET /ops/dashboard
dashboard_contains_linked_failure_cases_header -> true
dashboard_contains_linked_failure_case_filter -> true
dashboard_omits_unlinked_failure_case_filter -> true
```

## Boundary

This is an owner-authored live issue body edit only.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not automatic failure detection.

It is not background automation.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not LLM-backed repair.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

```text
external feedback current-state workflow dashboard failure-case counts runtime issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
