# Retrieval-run-linked Report Endpoint

Phase marker: retrieval-run-linked Report endpoint v0.

## What changed

NoiseProof now exposes:

```text
POST /retrieval-runs/{retrieval_run_id}/report
```

The endpoint reads an existing persisted `retrieval_runs` row, requires existing Evidence Ledger rows linked by `retrieval_run_id`, requires an existing Noise Gate record linked through `stage_input_manifest.retrieval_run_id`, runs the existing deterministic report preview formatter, and persists a Report record.

The persisted Report record stores the handoff in `stage_input_manifest`:

```text
retrieval_run_id
input_evidence_ledger_entry_ids
input_noise_gate_record_id
source_endpoint
persistence_boundary
```

## Why this gate exists

The previous gates proved:

```text
retrieval_runs -> evidence_ledger_entries
retrieval_runs + evidence_ledger_entries -> noise_gate_records
```

This gate proves the next bounded handoff:

```text
retrieval_runs
  -> evidence_ledger_entries linked by retrieval_run_id
  -> noise_gate_records linked through stage_input_manifest
  -> report_records with upstream ids in stage_input_manifest
```

The purpose is not free-form report generation. The purpose is to keep the report boundary inspectable and dependent on upstream evidence and gate records.

## Failure boundary

If no Evidence Ledger rows are linked to the retrieval run, the endpoint returns `409`.

If no Noise Gate record is linked to the retrieval run, the endpoint returns `409`.

This prevents report records from being created before the Evidence Ledger and Noise Gate handoffs exist.

## Explicit non-claims

This endpoint does not:

- call an LLM
- create embeddings
- perform semantic retrieval
- create failure cases
- provide buy/sell recommendations
- provide financial advice
- prove hosted deployment
- prove external reviewer feedback
- prove customer validation
- prove Braincrew acceptance
- make NoiseProof product-complete

When the Noise Gate requires revision or blocks output, the persisted Report record remains bounded and does not claim a free-form final answer.

## Verification

Route-level verification is covered by:

```text
test_retrieval_run_can_generate_persisted_report_from_linked_gate_and_ledger
test_retrieval_run_report_requires_linked_noise_gate_first
```

The full local API test suite passed after the endpoint implementation:

```text
305 passed, 1 warning
```

