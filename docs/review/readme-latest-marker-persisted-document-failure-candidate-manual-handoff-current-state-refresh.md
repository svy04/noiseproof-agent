# README Latest-marker Persisted Document Failure Candidate Manual Handoff Current-state Refresh

Status: README first-pass marker refresh only.

Phase marker: readme latest-marker persisted document failure candidate manual handoff current-state refresh v0.

## Purpose

The README first-pass implementation status still pointed to the older PDF page diagnostics downstream issue-body refresh and current-state issue verification.

Those artifacts remain valid historical proof, but they no longer describe the clearest current reviewer-routing state after the persisted document failure candidate manual handoff runtime issue-body refresh and current-state issue verification.

This refresh updates the README top markers only.

## README Markers

```text
Latest reviewer-routing marker: Persisted document failure candidate manual handoff runtime issue-body refresh v0
Latest external-feedback state: pending after persisted document failure candidate manual handoff issue verification; candidate_count=0; self-authored comment only
```

## Linked Current Proof

```text
docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md
docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md
docs/review/external-review-issue-body-persisted-document-failure-candidate-manual-handoff-runtime-refresh.md
docs/review/external-feedback-current-state-persisted-document-failure-candidate-manual-handoff-runtime-issue-verification.md
```

## What Changed

README top marker now points to:

```text
Persisted document failure candidate manual handoff runtime issue-body refresh v0
pending after persisted document failure candidate manual handoff issue verification; candidate_count=0; self-authored comment only
```

The older top marker is no longer the README first-pass current state:

```text
Latest reviewer-routing marker: PDF page diagnostics downstream runtime issue-body refresh v0
```

## Evidence Markers

```text
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
POST /failure-cases -> 201
GET /failure-cases -> 200
preview_only_not_persisted
human_confirmation_required -> true
human changes draft.fix_status from draft to open
failure_case_count_delta -> 1
candidate_count=0
draft_count=0
self_authored_comment
```

## Boundary

This is README current-state alignment only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not automatic failure-case creation.

This is not a confirm endpoint.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not raw file storage.

This is not full parsed text persistence.

This is not semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not live embedding generation proof.

This is not product-complete.

Explicit status:

```text
external-feedback remains pending
```

## Next Gate

```text
remote verification for this README marker refresh after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
