# External Feedback Screening CLI

Status: local issue-comment screening CLI.

Phase marker: external feedback screening cli v0.

Label: External feedback screening CLI.

This artifact documents the command-line path for screening GitHub issue comments before any future comment is accepted into the proof path.

## Purpose

The next evidence gate remains:

```text
external reviewer feedback v0
```

The CLI exists so the same local qualification helper can be run against real `gh issue view` output.

## Command

Capture the current public issue comments:

```powershell
$tmp = Join-Path $env:TEMP "noiseproof-issue-1-comments.json"
gh issue view 1 --repo svy04/noiseproof-agent --json comments | Set-Content -Path $tmp -Encoding utf8
```

Screen them:

```powershell
python -m packages.review.external_feedback_cli --input $tmp --repository-owner svy04
```

The CLI accepts JSON payloads shaped like `gh issue view --json comments` and tolerates UTF-8 files with a BOM.

## Current Smoke Result

Current issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Current public comment_count: 0

Current screen result:

```json
{
  "status": "pending",
  "candidate_count": 0,
  "next_gate": "external reviewer feedback v0",
  "does_not_close_gate": true,
  "warnings": [
    "No public issue comments were available to screen."
  ],
  "screened_comments": []
}
```

## Candidate Boundary

This command does not close the gate.

If the result becomes `candidate_found_manual_review_required`, the comment still has to be compared manually with:

```text
docs/review/external-feedback-intake-criteria.md
```

Only then can a separate proof artifact record accepted external reviewer feedback.

## Allowed Claim

NoiseProof Agent can run a local CLI against issue-comment JSON to pre-screen possible external feedback candidates.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that any reviewer has inspected the repository.

This does not automatically accept any comment into the proof path.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
