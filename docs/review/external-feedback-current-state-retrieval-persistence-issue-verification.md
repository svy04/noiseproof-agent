# External Feedback Current-state Retrieval Persistence Issue Verification

Status: current-state external feedback screen verification artifact.

Phase marker: external feedback current-state retrieval persistence issue verification v0.

Label: External feedback current-state retrieval persistence issue verification.

This artifact records the current state of the public external review issue after the uploaded-file retrieval persistence issue-body refresh. It verifies that the issue body points reviewers to the latest uploaded-file retrieval persistence proof while the public issue comments still do not qualify as external reviewer feedback.

## Verified Surface

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Issue state:

```text
OPEN
```

Observed issue body metadata:

```text
updatedAt: 2026-06-02T04:14:29Z
first_codepoint: 35
startsWith: ## Request
```

Observed comment and draft counts:

```text
comment_count: 1
candidate_count: 0
draft_count: 0
```

Issue body markers:

```text
uploaded-file retrieval persistence proof -> present
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md -> present
POST /documents/{document_id}/retrieval-runs -> present
metadata_json.candidate_chunk_ids -> present
metadata_source_table = document_chunks -> present
no Evidence Ledger generation -> present
not hosted deployment evidence -> present
not external reviewer feedback -> present
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

An initial app-venv execution attempt could not import the root `packages` module, and a second attempt passed an unsupported `--output` flag. The successful command used repo-root `PYTHONPATH=.` and stdout capture. These were shell invocation issues, not product-code changes.

## Screening Result

```json
{
  "issue_state": "OPEN",
  "issue_updatedAt": "2026-06-02T04:14:29Z",
  "first_codepoint": 35,
  "has_retrieval_persistence": true,
  "has_endpoint": true,
  "has_candidate_ids": true,
  "has_source_table": true,
  "comment_count": 1,
  "screen_status": "pending",
  "candidate_count": 0,
  "draft_status": "pending",
  "draft_count": 0,
  "reason": "self_authored_comment",
  "draft_warning": "No candidate comments were available for acceptance drafting."
}
```

## What This Proves

The current public issue body points reviewers to the uploaded-file retrieval persistence proof and preserves the proof boundary around `POST /documents/{document_id}/retrieval-runs`.

The current public issue still has no qualifying outside reviewer feedback.

The only public comment remains owner-authored and is screened as:

```text
self_authored_comment
non_qualifying
```

The acceptance draft remains pending because:

```text
No candidate comments were available for acceptance drafting.
```

## Allowed Claim

NoiseProof Agent's current external-feedback screen sees the public issue body pointing to the uploaded-file retrieval persistence proof, but keeps the external reviewer feedback gate pending because the only comment is owner-authored.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that an outside reviewer has inspected the repository.

This does not accept any issue comment into the proof path.

This does not close external reviewer feedback v0.

The next evidence gate remains open until an outside reviewer leaves substantive, evidence-referenced feedback.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
