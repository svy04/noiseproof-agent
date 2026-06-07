# External-reader Proof Path Uploaded PDF Table Adapter Noise Gate Provenance Runtime Route Refresh

Status: implemented.

Phase marker: external-reader proof path uploaded PDF table adapter Noise Gate provenance runtime route refresh v0.

## Purpose

Route first-pass external readers to the latest uploaded-PDF table-adapter Noise
Gate provenance runtime proof.

Before this refresh, the first uploaded-PDF table-adapter route stopped at
Evidence Ledger row metadata. The new first route points to the same bounded
metadata surviving one more handoff into the retrieval-run-linked Noise Gate
`stage_input_manifest`.

## Updated Surfaces

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
```

## Routed Proof Chain

```text
docs/review/uploaded-pdf-table-adapter-noise-gate-provenance.md
docs/review/uploaded-pdf-table-adapter-noise-gate-provenance-remote-verification.md
docs/review/uploaded-pdf-table-adapter-noise-gate-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-adapter-noise-gate-provenance-runtime-smoke-remote-verification.md
```

API route markers:

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
GET /noise-gates
```

Evidence markers:

```text
default_pdf_parser_table_adapter_metadata
table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]
table_extraction_performed -> False
source_pdf_table_adapter_provenance_boundary -> noise_gate_stage_input_manifest_from_evidence_ledger_entry_metadata
handoff_performs_pdf_table_extraction -> False
CI run `27077666558`
External Feedback Screen run `27077666546`
```

## Boundary

This is reviewer route hygiene only.

It is not new runtime evidence.
It is not a live issue body edit.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not robust PDF extraction evidence.
It is not table extraction evidence for arbitrary market PDFs.
It is not Evidence Ledger quality evidence.
It is not Noise Gate quality evidence.
It is not final truth adjudication.
It is not final report generation.
It is not product-complete.

## Next Gate

Next gate: remote verification after push, live issue body route refresh if this
should become the public issue's latest proof, external reviewer feedback v0 if
qualifying outside feedback exists, or another source-first product gate selected
from the current repository state.
