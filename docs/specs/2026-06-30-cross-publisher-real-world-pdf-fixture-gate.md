# Cross-publisher Real-world PDF Fixture Gate Spec

title: Cross-publisher real-world PDF fixture gate

status: implemented

date: 2026-06-30

target_gate: `cross_publisher_real_world_pdf_fixture_gate_v0`

## current_repo_state

The accepted robust-PDF quality gate is
`robust_pdf_extraction_next_real_world_quality_gate_v0`.

It blocks robust PDF extraction because the current real-world PDF observation
matrix has one publisher family only and no table extraction, OCR, or layout
fidelity evidence.

Existing local input:

- `examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json`
- `docs/evaluation/robust-pdf-real-world-quality-gate-report.md`

The existing matrix has three BEA digital-text observations. It is not
cross-publisher evidence.

## sources_to_absorb

Use existing source cards:

- Datasheets for Datasets: expose source policy, collection method, omissions,
  and non-claims for fixture data.
- Docling and Unstructured: keep digital text, tables, OCR, layout, and image
  interpretation separated.
- SLSA Provenance: keep input, command, generated report, and verification
  explicit.
- Model Cards: expose status, caveats, and non-claims beside the capability.

Add a source card for EIA content reuse and the Short-Term Energy Outlook page.
The local adaptation is source-policy-reviewed, metadata-only commitment of a
temporary owner-runtime EIA PDF download/hash/parse observation. No EIA PDF
binary, download cache, or raw extracted text is committed.

## non_goals

- Do not commit external PDF binaries.
- Do not commit raw extracted text or download caches.
- Do not implement OCR.
- Do not implement table extraction.
- Do not claim layout fidelity.
- Do not claim robust PDF extraction.
- Do not claim arbitrary-market PDF parsing reliability.
- Do not expand into retrieval, Evidence Ledger, Critic, reports, or dashboard.

## implementation_scope

Create:

- `examples/pdf-extraction-quality/cross-publisher-real-world-pdf-observation.json`
- `packages/ingestion/pdf_quality/cross_publisher_real_world_fixture.py`
- `apps/api/app/services/cross_publisher_real_world_pdf_fixture_gate_command.py`
- `docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md`
- `docs/review/cross-publisher-real-world-pdf-fixture-gate.md`
- `apps/api/tests/test_cross_publisher_real_world_pdf_fixture_gate.py`

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

## data_or_api_contract

No API endpoint or database schema changes.

The gate consumes:

```text
base_matrix -> examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json
cross_publisher_observation -> examples/pdf-extraction-quality/cross-publisher-real-world-pdf-observation.json
```

It produces:

```text
phase_marker
base_matrix_phase
cross_publisher_gate_status
base_observed_fixture_count
added_observed_fixture_count
combined_observed_fixture_count
distinct_publisher_count
publishers
has_cross_publisher_coverage
has_table_extraction_evidence
has_ocr_evidence
has_layout_fidelity_evidence
can_claim_cross_publisher_real_world_pdf_fixture_coverage
can_claim_robust_pdf_extraction
blocked_reasons
passed_checks
next_gate
```

Expected result:

```text
cross_publisher_gate_status -> passed
distinct_publisher_count -> 2
has_cross_publisher_coverage -> true
can_claim_cross_publisher_real_world_pdf_fixture_coverage -> true
can_claim_robust_pdf_extraction -> false
next_gate -> real_world_table_extraction_evidence_gate_v0
```

## tests

Write RED tests first:

```text
uv run pytest tests/test_cross_publisher_real_world_pdf_fixture_gate.py -q
```

Expected before implementation:

```text
FAIL because the package module, command, report, and review artifact do not exist.
```

## docs_to_update

Update proof surfaces so reviewers see cross-publisher fixture coverage as a
real improvement but not a robust-PDF claim.

## stop_conditions

Stop if:

- EIA source policy or STEO source availability cannot be verified from official
  EIA pages;
- the local owner-runtime observation cannot be reproduced without committing an
  external PDF binary;
- the gate starts claiming robust PDF extraction, OCR, table extraction, layout
  fidelity, or arbitrary-market PDF reliability.

If stopped, report:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

## claim_boundaries

This gate can claim cross-publisher fixture coverage across BEA and EIA
sanitized owner-runtime observations.

It cannot claim robust PDF extraction, arbitrary-market PDF parsing reliability,
OCR evidence, table extraction evidence, layout fidelity evidence, hosted
deployment evidence, external reviewer feedback, customer validation, Braincrew
acceptance, or product-complete.

## next_gate_if_passed

```text
real_world_table_extraction_evidence_gate_v0
```
