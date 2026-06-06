# External-reader Proof Path Uploaded PDF Table Adapter Evidence Ledger Provenance Runtime Route Refresh

Status: implemented.

Phase marker: external-reader proof path uploaded PDF table adapter Evidence Ledger provenance runtime route refresh v0.

## Purpose

Route first-pass external readers to the latest uploaded-PDF table-adapter
Evidence Ledger provenance runtime proof.

Before this refresh, the first uploaded-PDF table-adapter route stopped at
retrieval-run candidate metadata. The new first route points to the same
metadata surviving one more handoff into persisted Evidence Ledger row metadata.

## Updated Surfaces

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
```

## Routed Proof Chain

```text
docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance.md
docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance-runtime-smoke-remote-verification.md
```

API route markers:

```text
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}
```

Evidence markers:

```text
default_pdf_parser_table_adapter_metadata
table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]
table_extraction_performed remains false
source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
CI run `27076548950`
External Feedback Screen run `27076548930`
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
It is not final truth adjudication.
It is not product-complete.

## Next Gate

Next gate: remote verification after push, live issue body route refresh if this
should become the public issue's latest proof, external reviewer feedback v0 if
qualifying outside feedback exists, or another source-first product gate selected
from the current repository state.
