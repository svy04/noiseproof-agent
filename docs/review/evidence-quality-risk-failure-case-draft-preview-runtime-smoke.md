# Evidence Quality Risk Failure-case Draft Preview Runtime Smoke

Status: verified.

Phase marker: evidence quality risk failure-case draft preview runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence for the preview-only Evidence Ledger quality-risk to failure-case draft handoff.

## Environment

```text
Compose project: noiseproof-phase694
POSTGRES_PORT: 55451
FastAPI URL: http://127.0.0.1:8110
Applied migrations: 23
Pending migrations: 0
docker compose -p noiseproof-phase694 down -v -> completed
```

## HTTP Path

```text
GET /health -> 200
POST /evidence-ledgers -> 201
POST /evidence-ledgers/{weak_entry_id}/failure-case-draft-preview -> 200
GET /failure-cases -> 200
POST /evidence-ledgers/{clean_entry_id}/failure-case-draft-preview -> 409
POST /evidence-ledgers/{missing_entry_id}/failure-case-draft-preview -> 404
```

## Observed Result

```text
health_status -> 200
weak_ledger_status -> 201
weak_entry_status -> weakly_supported
weak_entry_confidence -> low
weak_entry_source_date -> null
preview_status -> 200
preview_persistence_boundary -> preview_only_not_persisted
preview_failure_type -> evidence_quality_risk
preview_risk_reasons -> weakly_supported, low_confidence, missing_source_date
failure_case_count_delta -> 0
clean_preview_status -> 409
clean_preview_detail -> evidence ledger entry has no quality risk
missing_preview_status -> 404
missing_preview_detail -> evidence ledger entry not found
```

## Boundary

This is local runtime evidence only.

It is not hosted deployment evidence.
It is not automatic failure-case creation.
It does not persist a `failure_cases` row during preview.
It is not final truth adjudication.
It is not retrieval quality evidence.
It is not Evidence Ledger quality evidence.
It is not a Critic / Noise Gate decision.
It is not an LLM call.
It is not external reviewer feedback.
It is not product-complete.

## Cleanup

The FastAPI process was stopped, and Docker resources were removed with:

```text
docker compose -p noiseproof-phase694 down -v -> completed
```

## Next Gate

Next gate: remote verification after push, route refresh if this proof should become reviewer-facing, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
