# Evidence Quality Risk Ops Surface

Phase marker: evidence quality risk ops surface v0

## Scope

`GET /ops/summary` now surfaces persisted Evidence Ledger quality-risk counts:

- `weakly_supported_evidence_count`
- `low_confidence_evidence_count`
- `missing_source_date_evidence_count`
- `evidence_quality_risk_count`

`GET /ops/dashboard` renders the same signal as:

- `Weak Evidence`
- `Low Confidence Evidence`
- `Missing Source Dates`
- `Evidence Quality Risk Rows`

The dashboard also links to `GET /evidence-ledgers?status=weakly_supported`.

## Boundary

This is operations metadata from persisted Evidence Ledger rows.

It is not final truth adjudication. It does not judge final truth, improve retrieval quality, create new Evidence Ledger rows, call an LLM, call an embedding provider, or generate a final report. The risk count is a row-level count of evidence entries with weak support, low confidence, or missing source-date metadata; it is not a score and not a benchmark.

## Verification

Focused route test:

```bash
cd apps/api
uv run pytest tests/test_routes.py -q -k evidence_quality_risks
```

Observed local result:

```text
1 passed, 192 deselected
```

## Next Gate

Continue with the next source-first product gate that improves inspectability without claiming production quality. External reviewer feedback remains pending, hosted deployment evidence remains unproven, and semantic retrieval quality / live embedding generation remain unproven.
