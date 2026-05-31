# External Feedback Qualification Preview

Status: external feedback screening helper.

Phase marker: external feedback qualification preview v0.

Label: External feedback qualification preview.

This artifact documents the small local helper that screens public issue comments before any comment is accepted into the proof path.

## Purpose

The next evidence gate remains:

```text
external reviewer feedback v0
```

The helper exists to keep the gate honest. It can separate empty, self-authored, generic, or artifact-free comments from comments that may deserve manual review.

Implementation:

```text
packages/review/external_feedback.py
```

Tests:

```text
apps/api/tests/test_external_feedback.py
```

## What It Screens

The helper accepts issue comment dictionaries, such as comments returned by:

```bash
gh issue view 1 --repo svy04/noiseproof-agent --json comments
```

It returns:

```text
pending
candidate_found_manual_review_required
```

It also returns per-comment reasons such as:

```text
self_authored_comment
missing_inspected_artifact
missing_actionable_critique_or_boundary
```

## Candidate Boundary

`candidate_found_manual_review_required` does not close the gate.

It means only that a comment is not obviously disqualified by the local screen. A human still has to compare it with `docs/review/external-feedback-intake-criteria.md` before it can be recorded as external reviewer feedback.

## Current State

Issue #1 currently has no accepted external reviewer feedback in the proof path.

The screening helper can confirm an empty-comment state as `pending`, but it cannot create external feedback.

## Allowed Claim

NoiseProof Agent has a local screening helper for external feedback comments.

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
