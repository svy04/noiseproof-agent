# Application-ready Persisted Document Failure Candidate Manual Handoff Refresh

Status: application-facing evidence refresh only.

Phase marker: application-ready persisted document failure candidate manual handoff refresh v0.

## Purpose

Refresh `docs/review/application-ready-review.md` so the latest persisted document failure candidate manual handoff runtime proof is visible from the application-ready checklist.

The older application-ready review already covered generic failure-case draft manual handoff and workflow-parent failure-case persistence. It did not yet name the newer document-derived failure candidate path that starts from a persisted document `profile_json.failure_case_candidate`.

## Linked Proof

```text
docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md
docs/review/external-feedback-current-state-persisted-document-failure-candidate-manual-handoff-runtime-issue-verification.md
```

Observed proof markers:

```text
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
POST /failure-cases -> 201
GET /failure-cases -> 200
preview_only_not_persisted
human_confirmation_required -> true
human changes draft.fix_status from draft to open
failure_case_count_delta=1
```

## What Changed

`docs/review/application-ready-review.md` now includes a checklist row for:

```text
persisted document failure candidate manual handoff runtime works
```

The best external claim now mentions:

```text
document-derived failure-case draft/manual handoff
```

## Boundary

This is application-facing documentation only.

This is not runtime behavior.

This is not a new endpoint.

This is not automatic failure-case creation.

This is not a confirm endpoint.

This is not automatic root-cause analysis.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
