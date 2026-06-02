# Retrieval-run-linked Proof Surface Regression Coverage

Status: documentation regression coverage.

Phase marker: retrieval-run-linked proof surface regression coverage v0.

This artifact exists to keep the Phase 202-207 endpoint docs and runtime smoke docs discoverable as one proof chain.

## Endpoint Docs

endpoint docs:

```text
docs/review/retrieval-run-linked-evidence-ledger-endpoint.md
docs/review/retrieval-run-linked-noise-gate-endpoint.md
docs/review/retrieval-run-linked-report-endpoint.md
```

Endpoint markers:

```text
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
POST /retrieval-runs/{retrieval_run_id}/report
```

## Runtime Smoke Docs

runtime smoke docs:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

Runtime boundary markers:

```text
pre_gate_status: 409
pre_report_status: 409
input_noise_gate_record_id
```

## Allowed Claim

NoiseProof has a documented retrieval-run-linked proof chain from persisted lexical retrieval runs to Evidence Ledger rows, then Noise Gate records, then Report records.

## Boundary

This is documentation regression coverage only.

This is not new runtime behavior.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not semantic retrieval.

This is not embeddings.

This is not LLM judgment.

This is not financial advice.

This is not automatic failure-case creation.

This is not product-complete.
