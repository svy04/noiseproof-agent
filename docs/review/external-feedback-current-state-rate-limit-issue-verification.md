# External Feedback Current-state Rate-limit Issue Verification

Status: live external review issue current-state screen only.

Phase marker: external feedback current-state rate-limit issue verification v0.

## Purpose

This gate verifies the current public issue #1 state after the owner-authored rate-limit issue-body refresh.

It checks whether the issue body exposes the guarded raw file download rate-limit runtime proof links and whether any public comment currently qualifies as external reviewer feedback v0.

It does not judge whether the local v0 rate limit is production-ready.

It does not accept feedback.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed current state:

```json
{
  "updatedAt": "2026-06-04T11:00:35Z",
  "state": "OPEN",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_rate_limit_proof": true,
  "has_rate_limit_request_refresh": true,
  "comment_count": 1,
  "screened_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0
}
```

Text markers:

```text
updatedAt: 2026-06-04T11:00:35Z
starts_with_request: true
first_codepoint: 35
has_rate_limit_proof: true
has_rate_limit_request_refresh: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
does_not_close_gate: true
```

## Verification Commands

The live issue payload was captured with:

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json title,state,url,body,comments,updatedAt,labels
```

The JSON payload was written as UTF-8 without BOM, then the existing local screeners were run against that payload:

```powershell
$env:PYTHONPATH='.'
python -m packages.review.external_feedback_cli --input <issue.json> --repository-owner svy04
python -m packages.review.external_feedback_acceptance_cli --input <screen.json>
```

An initial capture attempt used PowerShell `Tee-Object`, which wrote UTF-16 output and caused the acceptance CLI to fail while reading the screen JSON. The successful command wrote stdout to UTF-8 without BOM using `System.Text.UTF8Encoding($false)`. This was a shell capture issue, not product-code behavior.

## Comment Screen

The only current issue comment is owner-authored.

Screening result:

```text
status: pending
classification: non_qualifying
reason: self_authored_comment
candidate_count: 0
next_gate: external reviewer feedback v0
does_not_close_gate: true
```

Acceptance draft result:

```text
status: pending
draft_count: 0
warning: No candidate comments were available for acceptance drafting.
does_not_close_gate: true
```

This preserves the external reviewer feedback v0 gate as pending.

## Boundary

This is a live issue screen after an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not distributed rate limiting.

This is not production authorization.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external reviewer feedback v0
```
