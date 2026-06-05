# Persisted Document Failure Candidate Manual Handoff Smoke

Status: route-level smoke evidence.

Phase marker: persisted document failure candidate manual handoff smoke v0.

## Scope

This smoke verifies that a persisted document `profile_json.failure_case_candidate` can become a preview-only draft, then be manually confirmed and submitted through the existing `POST /failure-cases` persistence endpoint.

It does not add a new confirm endpoint.

It does not add automatic persistence.

It does not infer root cause automatically.

## Test Path

The route test is:

```text
tests/test_routes.py::test_persisted_document_failure_candidate_can_be_manually_handed_to_failure_case_persistence
```

## Verification Command

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k "persisted_document_failure_candidate_can_be_manually_handed"
```

Observed output:

```text
1 passed, 171 deselected in 1.64s
```

## Smoke Path

```text
POST /documents/upload-chunks
  -> persisted document row with profile_json.failure_case_candidate
POST /documents/{document_id}/failure-case-draft-preview
  -> preview_only_not_persisted
  -> human_confirmation_required: true
  -> draft.fix_status: draft
human changes draft.fix_status from draft to open
POST /failure-cases -> 201
GET /failure-cases -> 200
```

## Observed Behavior

The fixture proves:

- uploaded blank PDF produces `source_type: pdf`
- uploaded blank PDF produces `chunk_handoff_no_chunks`
- draft preview returns `preview_only_not_persisted`
- draft preview returns `human_confirmation_required: true`
- draft failure type is `pdf_no_extractable_text`
- manual handoff changes `draft.fix_status` from `draft` to `open`
- `POST /failure-cases -> 201`
- persisted failure case has `failure_type: pdf_no_extractable_text`
- persisted failure case has `fix_status: open`
- persisted failure case keeps `agent_run_id: null`
- persisted failure case keeps `workflow_run_id: null`
- `GET /failure-cases -> 200`
- `GET /failure-cases` returns the manually persisted row

## Human Confirmation Boundary

The smoke intentionally changes `draft.fix_status` to `open` before persistence.

That edit is the human confirmation boundary. The system prepares a draft from persisted document metadata; it does not decide that the draft is durable failure evidence without review.

## Allowed Claim

```text
A persisted document failure candidate can be manually handed to the existing failure-case persistence endpoint after human confirmation.
```

## Boundary

This is route-level smoke evidence only.

This is not Docker runtime evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not automatic failure-case creation.

This is not automatic root-cause analysis.

This is not a confirm endpoint.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

If runtime evidence is needed, run a local Docker/FastAPI smoke for this same manual handoff. Otherwise continue to the next source-first product gate from `docs/GOAL.md`.
