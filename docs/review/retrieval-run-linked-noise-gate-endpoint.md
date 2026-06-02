# Retrieval-run-linked Noise Gate Endpoint

Phase marker: retrieval-run-linked Noise Gate endpoint v0.

## What changed

NoiseProof now exposes:

```text
POST /retrieval-runs/{retrieval_run_id}/noise-gate
```

The endpoint reads an existing persisted `retrieval_runs` row, requires existing Evidence Ledger rows linked by `retrieval_run_id`, runs the existing deterministic Noise Gate, and persists a Noise Gate record.

The persisted Noise Gate record stores the handoff in `stage_input_manifest`:

```text
retrieval_run_id
input_evidence_ledger_entry_ids
source_endpoint
persistence_boundary
```

## Why this gate exists

The previous gate proved that a persisted retrieval run can create persisted Evidence Ledger rows.

This gate proves the next bounded handoff:

```text
retrieval_runs
  -> evidence_ledger_entries linked by retrieval_run_id
  -> noise_gate_records with stage_input_manifest input ids
```

The purpose is not to make the Noise Gate smarter. The purpose is to make the retrieval-to-evidence-to-gate sequence inspectable without jumping to report generation.

## Failure boundary

If no Evidence Ledger rows are linked to the retrieval run, the endpoint returns:

```text
409
```

This prevents an empty or ungrounded Noise Gate record from being created before the Evidence Ledger handoff exists.

## Explicit non-claims

This endpoint does not:

- call an LLM
- create embeddings
- perform semantic retrieval
- generate a report
- create failure cases
- provide buy/sell recommendations
- provide financial advice
- prove hosted deployment
- prove external reviewer feedback
- prove customer validation
- prove Braincrew acceptance
- make NoiseProof product-complete

## Verification

Route-level verification is covered by:

```text
test_retrieval_run_can_generate_persisted_noise_gate_from_linked_ledger_entries
test_retrieval_run_noise_gate_requires_linked_ledger_entries_first
```

The full local API test suite passed after the endpoint implementation:

```text
303 passed, 1 warning
```

