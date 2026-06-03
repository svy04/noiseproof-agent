# External Feedback Current-state Raw File Storage Issue Verification

Status: current-state screen only.

Phase marker: external feedback current-state raw file storage issue verification v0.

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

This records the current state of the public external review issue after the owner-authored raw file storage issue-body refresh.

## Observed Issue State

```text
state: OPEN
updatedAt: 2026-06-02T23:57:53Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
```

The existing public comment is owner-authored. It is useful request/status context, but it is not external reviewer feedback.

## Latest Proof Now Linked

uploaded raw file storage proof:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
POST /documents/upload-raw-files
GET /documents/upload-raw-files
raw_upload_quarantine_db_bytea_no_download_endpoint
not malware scanning
not a download endpoint
```

The issue body also points to the request refresh:

```text
docs/review/external-reviewer-raw-file-storage-request-refresh.md
```

## Verification Commands

The live issue payload was captured with:

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json title,state,url,body,comments,updatedAt
```

The JSON payload was written as UTF-8 without BOM, then the existing local screeners were run against that payload:

```powershell
$env:PYTHONPATH='.'
python -m packages.review.external_feedback_cli --input <issue.json> --repository-owner svy04
python -m packages.review.external_feedback_acceptance_cli --input <screen.json>
```

PowerShell redirection and `Tee-Object` produced UTF-16 files during initial attempts. The successful command wrote the issue and screen JSON with `System.Text.UTF8Encoding($false)`. These were shell encoding issues, not product-code changes.

## Screening Result

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

## Acceptance Draft Result

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

## Boundary

This is a current-state screen only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not malware scanning.

This is not a download endpoint.

This is not customer validation.

This is not Braincrew acceptance.

This does not close external reviewer feedback v0.

Self-authored comments, issue edits, bot summaries, CI checks, and generic praise do not close the gate.
