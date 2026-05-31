# External Feedback Screening Workflow

Status: GitHub Actions issue-comment screening workflow.

Phase marker: external feedback screening workflow v0.

Phase marker: external feedback acceptance draft workflow v0.

Label: External feedback screening workflow.

This artifact documents the GitHub Actions workflow that runs the local screening CLI against the public issue comment stream.

## Purpose

The next evidence gate remains:

```text
external reviewer feedback v0
```

The workflow exists to make incoming issue comments inspectable without manually remembering the command.

Workflow:

```text
.github/workflows/external-feedback-screen.yml
```

CLI:

```text
python -m packages.review.external_feedback_cli
```

## Triggers

The workflow can run from:

```text
workflow_dispatch
issue_comment created/edited
push to main or codex/**
```

It reads issue comments with:

```text
gh issue view 1 --repo "${{ github.repository }}" --json comments
```

It uploads:

```text
external-feedback-screen.json
external-feedback-acceptance-draft.json
```

The second artifact is produced by:

```text
python -m packages.review.external_feedback_acceptance_cli
```

It converts candidate screening results into `manual_acceptance_required` drafts only. It does not close the gate.

Remote verification:

```text
docs/review/external-feedback-screening-workflow-verification.md
```

## Boundary

This workflow does not close the gate and is not external reviewer feedback.

If the artifact says `candidate_found_manual_review_required`, a human still has to compare the comment with `docs/review/external-feedback-intake-criteria.md` before writing a separate accepted-feedback proof artifact.

If the acceptance draft artifact says `manual_acceptance_required`, a human still has to fill `docs/review/external-feedback-acceptance-template.md` before any feedback can be accepted into the proof path.

## Allowed Claim

NoiseProof Agent has a GitHub Actions workflow that can screen public issue comments and upload the screening result.

NoiseProof Agent has a GitHub Actions workflow that can upload an acceptance-draft artifact for future candidate comments.

## Forbidden Claim

Do not claim that this is external reviewer feedback.

Do not claim that this is customer validation.

Do not claim that this is Braincrew acceptance.

Do not claim that this is hosted deployment evidence for the product.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
