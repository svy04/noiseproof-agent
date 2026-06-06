# Uploaded PDF Table Adapter Noise Gate Provenance

Status: implemented.

Phase marker: uploaded PDF table adapter Noise Gate provenance v0.

## Purpose

Prove that bounded uploaded-PDF table-adapter metadata preserved in persisted
Evidence Ledger entry metadata can survive one more deterministic handoff into a
retrieval-run-linked Noise Gate record's `stage_input_manifest`.

The previous uploaded-PDF table-adapter proof reached persisted Evidence Ledger
rows. This gate checks that the Noise Gate handoff does not drop that source
provenance before a future report step.

## Implemented

```text
apps/api/app/services/retrieval_run_source_provenance.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
docs/review/uploaded-pdf-table-adapter-noise-gate-provenance.md
```

Route surfaces covered by regression:

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
GET /noise-gates
```

Regression test:

```text
test_uploaded_pdf_table_adapter_metadata_flows_into_noise_gate_provenance
```

## Observed Markers

The route-level regression checks that the Noise Gate `stage_input_manifest`
preserves:

```text
default_pdf_parser_table_adapter_metadata
table_adapter
table_adapter_boundary
table_adapter_extraction_performed
table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]
table_extraction_performed remains false
source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
source_pdf_table_adapter_provenance_boundary -> noise_gate_stage_input_manifest_from_evidence_ledger_entry_metadata
handoff_performs_pdf_table_extraction -> false
```

The Noise Gate warning surface also records:

```text
Uploaded PDF table-adapter metadata was preserved into Noise Gate stage_input_manifest as provenance only.
Noise Gate handoff does not perform PDF table extraction and is not robust PDF extraction evidence.
```

## Boundary

This is deterministic route-level regression evidence for one synthetic uploaded
PDF table fixture and an in-memory repository test path.

It is not local Docker runtime evidence.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not robust PDF extraction evidence.
It is not table extraction evidence for arbitrary market PDFs.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not Evidence Ledger quality evidence.
It is not Noise Gate quality evidence.
It is not final truth adjudication.
It is not final report generation.
It is not production readiness.
It is not product-complete.

## Next Gate

Next gate: local runtime smoke for this uploaded-PDF table-adapter Noise Gate
provenance path, remote verification after push, external reviewer feedback v0
if qualifying outside feedback exists, or another source-first product gate
selected from the current repository state.
