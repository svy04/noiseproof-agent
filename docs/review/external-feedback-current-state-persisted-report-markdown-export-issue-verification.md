# External Feedback Current-state Persisted Report Markdown Export Issue Verification

Status: live external review issue current-state screen only.

Phase marker: external feedback current-state persisted Report markdown export issue verification v0.

## Purpose

This gate verifies the current public issue #1 state after the owner-authored persisted Report markdown export issue-body refresh.

It checks whether the issue body still exposes the persisted Report markdown export proof links and whether any public comment currently qualifies as external reviewer feedback v0.

It does not accept feedback.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed current state:

```json
{
  "updatedAt": "2026-06-05T15:26:34Z",
  "has_persisted_report_markdown_export_proof": true,
  "has_persisted_report_markdown_export_request_refresh": true,
  "has_persisted_report_markdown_export_issue_body_record": true,
  "has_markdown_route": true,
  "has_remote_ci_run": true,
  "has_external_feedback_screen_run": true,
  "has_external_feedback_boundary": true,
  "starts_with_request": true,
  "first_codepoint": 35,
  "comment_count": 1,
  "screened_comment_count": 1,
  "owner_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0,
  "classification": "non_qualifying",
  "reason": "self_authored_comment",
  "status": "pending"
}
```

Text markers:

```text
updatedAt: 2026-06-05T15:26:34Z
has_persisted_report_markdown_export_proof: true
has_persisted_report_markdown_export_request_refresh: true
has_persisted_report_markdown_export_issue_body_record: true
has_markdown_route: true
has_remote_ci_run: true
has_external_feedback_screen_run: true
has_external_feedback_boundary: true
starts_with_request: true
first_codepoint: 35
comment_count: 1
screened_comment_count: 1
owner_comment_count: 1
candidate_count: 0
draft_count: 0
classification: non_qualifying
reason: self_authored_comment
status: pending
does_not_close_gate: true
```

## Linked Proof Still Visible

persisted Report markdown export proof:

```text
docs/review/persisted-report-markdown-export.md
GET /reports/{report_record_id}/markdown
```

Persisted Report markdown export remote verification:

```text
docs/review/persisted-report-markdown-export-remote-verification.md
CI run 27022884406 -> api-smoke -> success
External Feedback Screen run 27022884394 -> screen -> success
```

External reviewer request refresh:

```text
docs/review/external-reviewer-persisted-report-markdown-export-request-refresh.md
```

External review issue-body refresh record:

```text
docs/review/external-review-issue-body-persisted-report-markdown-export-refresh.md
```

The issue body currently includes:

```text
persisted Report markdown export proof
GET /reports/{report_record_id}/markdown
docs/review/persisted-report-markdown-export.md
docs/review/persisted-report-markdown-export-remote-verification.md
27022884406
27022884394
not external reviewer feedback
not hosted deployment evidence
not free-form report generation
not a new report-generation path
not an LLM call
not retrieval
not Evidence Ledger creation
not Noise Gate behavior
not Report record creation
not financial advice
```

## Comment Screen

Screened with:

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json number,title,state,body,comments,updatedAt,url,labels
uv run --project apps/api python -m packages.review.external_feedback_cli --input <captured-issue-json> --repository-owner svy04
uv run --project apps/api python -m packages.review.external_feedback_acceptance_cli --input <screening-json>
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

The only current issue comment is owner-authored by `svy04`.

Screening result:

```text
self_authored_comment
classification: non_qualifying
candidate_count: 0
draft_count: 0
status: pending
```

This preserves the external reviewer feedback v0 gate as pending.

```text
external reviewer feedback v0 gate remains pending
```

## Boundary

This is a live issue screen after an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not free-form report generation.

This is not a new report-generation path.

This is not an LLM call.

This is not retrieval.

This is not Evidence Ledger creation.

This is not Critic / Noise Gate behavior.

This is not Noise Gate behavior.

This is not Report record creation.

This is not final report generation.

This is not financial advice.

This is not production readiness, embedding generation, LLM output, or product-complete.

Explicit boundary marker:

```text
not product-complete
```
