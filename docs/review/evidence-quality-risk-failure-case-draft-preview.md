# Evidence Quality Risk Failure-case Draft Preview

Status: implemented.

Phase marker: evidence quality risk failure-case draft preview v0.

NoiseProof now exposes a preview-only handoff from a persisted Evidence Ledger quality-risk row to a manual failure-case draft.

## Route

```text
POST /evidence-ledgers/{entry_id}/failure-case-draft-preview
```

## What It Does

The route reads an existing persisted Evidence Ledger row and returns a `FailureCaseDraftPreviewOut` payload when the row has one or more quality-risk markers:

```text
weakly_supported
low_confidence
missing_source_date
```

The response uses the existing manual draft shape:

```text
persistence_boundary -> preview_only_not_persisted
human_confirmation_required -> true
draft.failure_type -> evidence_quality_risk
source_summary.stage -> persisted_evidence_ledger_quality_risk
```

Clean rows that do not match the quality-risk criteria return:

```text
409 evidence ledger entry has no quality risk
```

Missing rows return:

```text
404 evidence ledger entry not found
```

## Why This Exists

The previous ops surface made weak Evidence Ledger rows visible in `GET /ops/summary` and `GET /ops/dashboard`.

This gate makes those rows actionable without pretending the system has diagnosed root cause or created a durable failure record.

## Boundary

This is a preview-only manual handoff.

It is not automatic failure-case creation.
It does not persist a `failure_cases` row.
It does not mutate the Evidence Ledger row.
It is not final truth adjudication.
It is not retrieval quality evidence.
It is not Evidence Ledger quality evidence.
It is not a Critic / Noise Gate decision.
It is not an LLM call.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Verification

Focused route tests cover:

```text
weak row -> 200 draft preview
clean row -> 409 no quality risk
missing row -> 404 not found
failure case count unchanged after preview
```

Local verification command:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "evidence_quality_risk_row_can_preview or evidence_quality_clean_row or evidence_quality_failure_case_draft_preview_missing"
```

## Next Gate

Next gate: local Docker runtime smoke for this preview route if fresh DB evidence is needed, application route refresh if this proof should become the latest reader path, or another source-first product gate selected from the current repository state.
