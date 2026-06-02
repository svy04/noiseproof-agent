# Retrieval-run-linked Evidence Ledger Endpoint v0

Date: 2026-06-02

Status: implemented as a bounded service endpoint.

## What Changed

NoiseProof now has an explicit handoff from a persisted retrieval run to persisted Evidence Ledger rows:

```text
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
```

The endpoint reads an existing `retrieval_runs` row, uses `metadata_json.candidate_chunk_ids` plus `metadata_json.document_id` to reload referenced `document_chunks`, generates deterministic Evidence Ledger entries, and persists those rows with `retrieval_run_id`.

## Files

- `apps/api/app/routes/retrieval_runs.py`
- `apps/api/app/services/retrieval_run_evidence.py`
- `apps/api/app/db.py`
- `apps/api/app/schemas.py`
- `db/init/001_schema.sql`
- `db/migrations/014_evidence_ledger_retrieval_run_id.sql`
- `apps/api/tests/test_routes.py`

## Claim Boundary

Allowed claim:

```text
NoiseProof can persist Evidence Ledger rows linked to a persisted lexical retrieval run over document_chunks.
```

Forbidden claims:

```text
This is not semantic retrieval.
This is not embeddings.
This is not LLM-based judgment.
This is not final report generation.
This is not Noise Gate generation.
This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not financial advice.
```

## Verification

Local route test:

```text
uv run pytest tests/test_routes.py -q -k retrieval_run_can_generate_persisted_evidence_ledger_from_candidate_chunks
```

Observed:

```text
1 passed, 93 deselected, 1 warning
```

Full API test suite:

```text
uv run pytest -q
```

Observed:

```text
301 passed, 1 warning
```

## Remaining Gap

Runtime Docker DB verification for migration `014_evidence_ledger_retrieval_run_id.sql` and live HTTP calls should be recorded separately. This endpoint artifact does not claim local Docker runtime proof by itself.
