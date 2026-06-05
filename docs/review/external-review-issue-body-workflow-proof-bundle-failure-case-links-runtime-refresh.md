# External Review Issue Body Workflow Proof Bundle Failure-case Links Runtime Refresh

Status: live issue body refresh completed.

Phase marker: external review issue body workflow proof bundle failure-case links runtime refresh v0.

## Purpose

Record the owner-authored issue #1 body update that points reviewers to the workflow proof bundle failure-case links runtime smoke and its request-refresh record.

This keeps external reviewer feedback v0 pending.

It does not accept feedback.

It does not close the external feedback gate.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Latest Proof

```text
docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md
```

## Reviewer Request Refresh

```text
docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md
```

## Issue-body Refresh Record

```text
docs/review/external-review-issue-body-workflow-proof-bundle-failure-case-links-runtime-refresh.md
```

## Observed Issue State

Observed through `gh issue view 1 --repo svy04/noiseproof-agent --json number,title,state,body,comments,updatedAt,url` after editing the issue body.

```json
{
  "updatedAt": "2026-06-05T05:32:58Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_workflow_proof_bundle_failure_case_links_runtime_proof": true,
  "has_workflow_proof_bundle_failure_case_links_request_refresh": true,
  "has_workflow_proof_bundle_failure_case_links_issue_body_refresh": true,
  "has_detail_failure_case_count": true,
  "has_bundle_failure_case_count": true,
  "has_filtered_failure_case_count": true,
  "has_unrelated_filtered_out": true,
  "has_proof_surface_has_failure_case_filter": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "body_length": 11110
}
```

## Issue Body Highlights

The issue body now asks reviewers to inspect:

```text
Workflow proof bundle failure-case links runtime smoke
Workflow proof bundle failure-case links request refresh
Issue-body refresh record
```

It highlights:

```text
GET /workflow-runs/{id}
GET /workflow-runs/{id}/proof-bundle
GET /failure-cases?workflow_run_id={id}
detail_failure_case_count -> 1
bundle_failure_case_count -> 1
filtered_failure_case_count -> 1
unrelated_filtered_out -> true
proof_surface_has_failure_case_filter -> true
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
external feedback current-state workflow proof bundle failure-case links runtime issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
