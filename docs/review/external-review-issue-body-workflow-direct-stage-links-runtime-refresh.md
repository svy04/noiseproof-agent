# External Review Issue Body Workflow Direct Stage Links Runtime Refresh

Status: live issue body refresh completed.

Phase marker: external review issue body workflow direct stage links runtime refresh v0.

## Purpose

Record the owner-authored issue #1 body update that points reviewers to the workflow direct stage links runtime smoke and its request-refresh record.

This keeps external reviewer feedback v0 pending.

It does not accept feedback.

It does not close the external feedback gate.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Latest Proof

```text
docs/review/workflow-direct-stage-links-runtime-smoke.md
```

## Reviewer Request Refresh

```text
docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md
```

## Issue-body Refresh Record

```text
docs/review/external-review-issue-body-workflow-direct-stage-links-runtime-refresh.md
```

## Observed Issue State

Observed through `gh issue view 1 --repo svy04/noiseproof-agent --json number,title,state,body,comments,updatedAt,url,labels` after editing the issue body.

```json
{
  "updatedAt": "2026-06-05T09:17:26Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_workflow_direct_stage_links_runtime_proof": true,
  "has_workflow_direct_stage_links_request_refresh": true,
  "has_workflow_direct_stage_links_issue_body_refresh": true,
  "has_direct_stage_link_count": true,
  "has_evidence_to_report": true,
  "has_evidence_to_noise_gate": true,
  "has_noise_gate_to_report": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "body_length": 5233
}
```

## Issue Body Highlights

The issue body now asks reviewers to inspect:

```text
Workflow direct stage links runtime smoke
Workflow direct stage links request refresh
Issue-body refresh record
```

It highlights:

```text
POST /workflow-runs/execute-preview
GET /workflow-runs/{id}/lineage
direct_stage_link_count -> 3
evidence_to_report -> present
evidence_to_noise_gate -> present
noise_gate_to_report -> present
workflow_created_records_only_not_standalone_payload_lineage
```

## Boundary

This is an owner-authored live issue body edit only.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not distributed tracing.

It is not hosted observability.

It is not autonomous workflow execution.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

```text
external feedback current-state workflow direct stage links runtime issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
