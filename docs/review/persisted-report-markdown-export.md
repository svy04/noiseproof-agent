# Persisted Report Markdown Export

Phase marker: persisted report markdown export v0.

## Purpose

Make a persisted claim-bounded Report record easier for a reviewer to inspect as a deterministic Markdown artifact.

This gate does not make NoiseProof a free-form report writer. It only renders an existing persisted report record.

## Implemented Artifacts

- `GET /reports/{report_record_id}/markdown`
- `apps/api/app/services/report_markdown.py`
- `Repository.get_report_record`
- `test_report_record_markdown_export_renders_stored_claim_boundaries`
- `test_report_record_markdown_export_returns_404_for_unknown_report`

## Behavior

The endpoint reads one existing `report_records` row and returns `text/markdown`.

The Markdown includes:

- report record id
- workflow trace id
- status
- gate decision
- question
- deterministic export boundary
- claim text
- source ids
- confidence
- evidence spans
- limitations
- contradictions
- next data needed
- stage input manifest
- warnings

If the report id is unknown, the endpoint returns `404` with `Report record not found`.

## Verification

RED:

```text
uv run pytest tests/test_routes.py -q -k "report_record_markdown_export"
```

Observed before implementation:

```text
2 failed, 172 deselected
```

Expected failure reason:

```text
GET /reports/{report_record_id}/markdown did not exist yet and returned 404 Not Found.
```

GREEN:

```text
uv run pytest tests/test_routes.py -q -k "report_record_markdown_export"
```

Observed after implementation:

```text
2 passed, 172 deselected
```

## Boundary

This is a deterministic read/export surface only.

It does not:

- generate new report claims
- call an LLM
- run retrieval
- create Evidence Ledger rows
- create Noise Gate records
- create Report records
- create failure cases
- provide financial advice
- prove hosted deployment
- prove external reviewer feedback
- make the project product-complete

Free-form reports remain unimplemented.

## Next Recommended Evidence Gate

After push, record remote CI verification for this product gate, or continue to the next source-first product gate selected from `docs/GOAL.md`.
