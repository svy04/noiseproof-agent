# Real-world Table Extraction Evidence Gate Spec

title: Real-world table extraction evidence gate

status: implemented

date: 2026-06-30

target_gate: `real_world_table_extraction_evidence_gate_v0`

## current_repo_state

The accepted previous gate is
`cross_publisher_real_world_pdf_fixture_gate_v0`.

That gate reduced the publisher-family blocker by adding an EIA Short-Term
Energy Outlook owner-runtime observation to the existing BEA matrix, but
robust PDF extraction remained blocked because there was no real-world table
extraction evidence, OCR evidence, or layout fidelity evidence.

## sources_to_absorb

Use existing source cards:

- Docling and Unstructured: keep digital text, table extraction, OCR, layout,
  and image interpretation separate.
- Datasheets for Datasets: expose source policy, source collection method,
  omissions, and non-claims for fixture data.
- SLSA Provenance: keep inputs, commands, generated reports, hashes, and
  byproducts explicit.
- Model Cards: keep capability status and caveats near the claim.
- EIA Content Reuse and Short-Term Energy Outlook: commit only sanitized
  metadata, no EIA PDF binary, no download cache, and no raw extracted text.

Add or update a source card for PyMuPDF `Page.find_tables()` /
`Table.extract()`. The local adaptation is a bounded table adapter observation
over temporary owner-runtime real-world PDF downloads.

## non_goals

- Do not commit external PDF binaries.
- Do not commit raw extracted text.
- Do not commit raw table rows.
- Do not implement OCR.
- Do not claim layout fidelity.
- Do not claim robust PDF extraction.
- Do not claim arbitrary-market PDF parsing reliability.
- Do not expand into retrieval, Evidence Ledger, Critic, reports, or dashboard.

## implementation_scope

Create:

- `examples/pdf-extraction-quality/real-world-table-extraction-evidence.json`
- `packages/ingestion/pdf_quality/real_world_table_extraction_evidence.py`
- `apps/api/app/services/real_world_table_extraction_evidence_gate_command.py`
- `docs/evaluation/real-world-table-extraction-evidence-gate-report.md`
- `docs/review/real-world-table-extraction-evidence-gate.md`
- `apps/api/tests/test_real_world_table_extraction_evidence_gate.py`

Update:

- `docs/research/source-assimilation-registry.md`
- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`

## data_contract

The gate consumes:

```text
table_evidence -> examples/pdf-extraction-quality/real-world-table-extraction-evidence.json
```

The JSON evidence records sanitized metrics only:

```text
fixture_id
publisher
source_url
license_source_url
source_sha256
page_count
table_extraction_engine
table_extraction_performed
table_count
table_rows_extracted
table_cell_count
table_shapes_sample
warnings
```

The JSON evidence must not include:

```text
external PDF binaries
download cache paths
raw extracted text
raw table rows
```

Expected result:

```text
table_extraction_gate_status -> passed
observed_fixture_count -> 3
table_extraction_observed_fixture_count -> 3
distinct_publisher_count -> 2
has_table_extraction_evidence -> true
can_claim_real_world_table_extraction_evidence -> true
can_claim_robust_pdf_extraction -> false
next_gate -> real_world_ocr_evidence_gate_v0
```

## tests

RED test before implementation:

```text
uv run pytest tests/test_real_world_table_extraction_evidence_gate.py -q
```

Expected before implementation:

```text
ModuleNotFoundError: No module named 'packages.ingestion.pdf_quality.real_world_table_extraction_evidence'
```

## stop_conditions

Stop if:

- temporary owner-runtime PDF access fails for both BEA and EIA sources;
- table extraction cannot return rows or shape counts on real-world fixtures;
- the gate requires committing external PDF binaries or raw table rows;
- the gate starts claiming robust PDF extraction, OCR, or layout fidelity.

If stopped, report:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

## claim_boundaries

This gate can claim sanitized real-world table extraction evidence for the
listed BEA/EIA fixtures.

It cannot claim robust PDF extraction, arbitrary-market PDF parsing reliability,
OCR evidence, layout fidelity evidence, hosted deployment evidence, external
reviewer feedback, customer validation, Braincrew acceptance, or
product-complete.

## next_gate_if_passed

```text
real_world_ocr_evidence_gate_v0
```
