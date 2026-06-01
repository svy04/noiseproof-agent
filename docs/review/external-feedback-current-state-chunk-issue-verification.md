# External Feedback Current-state Chunk Issue Verification

Status: current-state external feedback screen verification artifact.

Phase marker: external feedback current-state chunk issue verification v0.

Label: External feedback current-state chunk issue verification.

This artifact records the current state of the public external review issue after the uploaded-file chunk persistence issue-body refresh. It verifies that the issue body points reviewers to the latest chunk persistence proof while the only public issue comment still does not qualify as external reviewer feedback.

## Verified Surface

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Issue state:

```text
OPEN
```

Observed comment count:

```text
comment_count: 1
candidate_count: 0
draft_count: 0
```

Issue body markers:

```text
uploaded-file chunk persistence proof -> present
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md -> present
not automatic persistence from upload preview -> present
```

## Verification Commands

The live issue payload was captured with:

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json title,state,url,body,comments
```

Then the existing local screeners were run against that payload:

```powershell
python -m packages.review.external_feedback_cli --input <issue.json> --repository-owner svy04
python -m packages.review.external_feedback_acceptance_cli --input <screen.json>
```

The first attempt wrote the temporary JSON with PowerShell redirection, which produced UTF-16 text and failed the UTF-8 CLI input boundary. The payload was recaptured as UTF-8 without BOM and re-run. This was a shell-capture issue, not a product-code change.

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

## What This Proves

The current public issue still has no qualifying outside reviewer feedback.

The only public comment remains owner-authored and is classified as:

```text
non_qualifying
self_authored_comment
```

The issue body does point reviewers to the uploaded-file chunk persistence proof, but that request surface does not close external reviewer feedback v0.

## Allowed Claim

NoiseProof Agent's current external-feedback screen sees the public issue comment and keeps the gate pending because the only comment is owner-authored.

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
