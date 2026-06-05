# External Feedback Current-state Workflow Proof Bundle Failure-case Links Runtime Issue Verification

Status: implemented.

Phase marker: external feedback current-state workflow proof bundle failure-case links runtime issue verification v0.

## Purpose

Record the current issue #1 state after the workflow proof bundle failure-case links runtime issue body refresh, and keep the external reviewer feedback gate pending because the only comment is still self-authored.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Related proof:

```text
docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md
```

Related request refresh:

```text
docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md
```

Related issue-body refresh:

```text
docs/review/external-review-issue-body-workflow-proof-bundle-failure-case-links-runtime-refresh.md
```

## Observed Issue State

Observed through `gh issue view 1 --repo svy04/noiseproof-agent --json number,title,state,body,comments,updatedAt,url,labels`.

```json
{
  "updatedAt": "2026-06-05T05:32:58Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_workflow_proof_bundle_failure_case_links_runtime_proof": true,
  "has_workflow_proof_bundle_failure_case_links_request_refresh": true,
  "has_workflow_proof_bundle_failure_case_links_issue_body_refresh": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "screened_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0,
  "status": "pending"
}
```

The issue body still highlights:

```text
GET /workflow-runs/{id}
GET /workflow-runs/{id}/proof-bundle
GET /failure-cases?workflow_run_id={id}
detail_failure_case_count: 1
bundle_failure_case_count: 1
filtered_failure_case_count: 1
unrelated_filtered_out: true
proof_surface_has_failure_case_filter: true
```

## Comment Screening

Screened with:

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json number,title,state,body,comments,updatedAt,url,labels
uv run python -m packages.review.external_feedback_cli --input <captured-issue-json> --repository-owner svy04
uv run python -m packages.review.external_feedback_acceptance_cli --input <screening-json>
```

Current screen result:

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
      "source_url": "https://github.com/svy04/noiseproof-agent/issues/1#issuecomment-4588931954",
      "artifacts": [
        "README.md",
        "docs/review/external-feedback-intake-criteria.md",
        "docs/review/external-reader-proof-path.md"
      ],
      "classification": "non_qualifying",
      "reasons": [
        "self_authored_comment"
      ]
    }
  ]
}
```

Current acceptance draft result:

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

Current comment classification:

```text
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
```

The single issue comment is owner-authored and remains request/status context only.

## Boundary

This is current-state verification of a public request issue.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not automatic failure detection.

It is not background automation.

It is not complete workflow failure causality.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

The external reviewer feedback v0 gate remains pending.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
