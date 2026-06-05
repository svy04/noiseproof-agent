# External Feedback Current-state Ops Dashboard Anchor Browser Smoke Issue Verification

Status: implemented.

Phase marker: external feedback current-state ops dashboard anchor browser smoke issue verification v0.

## Purpose

Record the current public issue #1 state after the ops dashboard anchor browser smoke issue-body refresh.

This gate verifies that the latest browser proof links are visible in the request surface and that external reviewer feedback still remains pending because the only issue comment is owner-authored.

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Related artifacts:

```text
docs/review/ops-dashboard-anchor-browser-smoke.md
docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md
docs/review/external-review-issue-body-ops-dashboard-anchor-browser-smoke-refresh.md
```

## Observed Issue Body State

Captured from `gh issue view 1 --repo svy04/noiseproof-agent --json body,comments,author,title,state,url`.

```json
{
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_ops_dashboard_anchor_browser_proof": true,
  "has_ops_dashboard_anchor_browser_request_refresh": true,
  "has_ops_dashboard_anchor_browser_issue_body_refresh": true,
  "has_browser_anchor_count": true,
  "has_browser_get_anchor_count": true,
  "has_browser_post_anchor_count_zero": true,
  "has_post_only_draft_preview_anchor_count_zero": true,
  "has_post_only_draft_preview_cue_visible": true,
  "comment_count": 1,
  "screened_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0,
  "does_not_close_gate": true
}
```

## Screening Result

The external feedback screen saw one comment and rejected it as non-qualifying because it is owner-authored.

```text
classification: non_qualifying
reason: self_authored_comment
external reviewer feedback remains pending
does_not_close_gate: true
```

Acceptance draft output:

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

## Commands

From the repository root:

```powershell
$issuePath = Join-Path $env:TEMP 'noiseproof-issue-1-phase529.json'
$screenPath = Join-Path $env:TEMP 'noiseproof-issue-1-phase529-screen.json'
$draftPath = Join-Path $env:TEMP 'noiseproof-issue-1-phase529-drafts.json'
gh issue view 1 --repo svy04/noiseproof-agent --json body,comments,author,title,state,url | Set-Content -LiteralPath $issuePath -Encoding utf8
$env:PYTHONPATH='.'
uv run --project apps/api python -m packages.review.external_feedback_cli --input $issuePath --repository-owner svy04 | Set-Content -LiteralPath $screenPath -Encoding utf8
uv run --project apps/api python -m packages.review.external_feedback_acceptance_cli --input $screenPath | Set-Content -LiteralPath $draftPath -Encoding utf8
```

## Boundary

This is current-state issue verification only.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not design quality evidence.

It is not product-complete.

It does not prove the dashboard is useful to an outside reviewer.

Self-authored issue edits or comments do not close the `external reviewer feedback v0` gate.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
