# External Feedback Current-state Issue Body BOM Removal Issue Verification

Status: live external review issue current-state screen only.

Phase marker: external feedback current-state issue body BOM removal issue verification v0.

## Purpose

This gate verifies the current public issue #1 state after the owner-authored issue body BOM removal refresh.

It checks that the public issue body now starts with the visible markdown heading, keeps the persisted Report markdown export proof routing, and still has no qualifying external reviewer feedback.

It does not accept feedback.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed current state:

```json
{
  "updatedAt": "2026-06-05T15:48:38Z",
  "first_codepoint": 35,
  "has_leading_bom": false,
  "starts_with_request": true,
  "has_persisted_report_markdown_export_proof": true,
  "has_markdown_route": true,
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
updatedAt: 2026-06-05T15:48:38Z
first_codepoint: 35
has_leading_bom: false
starts_with_request: true
has_persisted_report_markdown_export_proof: true
has_markdown_route: true
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

## Related Repair Artifact

```text
docs/review/external-review-issue-body-bom-removal-refresh.md
```

The live issue body still includes:

```text
persisted Report markdown export proof
GET /reports/{report_record_id}/markdown
docs/review/persisted-report-markdown-export.md
docs/review/persisted-report-markdown-export-remote-verification.md
docs/review/external-reviewer-persisted-report-markdown-export-request-refresh.md
docs/review/external-review-issue-body-persisted-report-markdown-export-refresh.md
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

This is a live issue screen after an owner-authored issue body readability repair.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not free-form report generation.

This is not a new report-generation path.

This is not an LLM call.

This is not retrieval.

This is not Evidence Ledger creation.

This is not Noise Gate behavior.

This is not Report record creation.

This is not financial advice.

This is not product-complete.
