# Multi-fixture PDF Extraction Quality Eval

Phase 870 adds multi-fixture PDF extraction quality eval v0.

Purpose: make the full PDF extraction quality fixture matrix visible before any
robust PDF extraction claim can pass.

This gate uses the existing fixture manifest and caller-provided observation
file to generate:

- `docs/evaluation/multi-fixture-pdf-extraction-quality-report.md`
- `packages/ingestion/pdf_quality/multi_fixture.py`
- `app.services.multi_fixture_pdf_extraction_quality_command`

The committed matrix keeps every fixture role visible:

```text
phase_marker -> multi_fixture_pdf_extraction_quality_eval_v0
fixture_count -> 8
observed_fixture_count -> 4
gap_fixture_count -> 4
quality_gate_status -> blocked
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
```

Observed fixture states:

```text
born_digital_text -> observed_passed
table_heavy_report -> observed_with_gaps
deterministic_table_adapter_pdf -> adapter_contract_observed
encrypted_pdf -> expected_failure_observed
```

Missing runtime observations remain explicit:

```text
scanned_image_pdf -> missing_runtime_observation
image_heavy_pdf -> missing_runtime_observation
multi_column_layout_pdf -> missing_runtime_observation
no_extractable_text_pdf -> missing_runtime_observation
```

Boundary notes surfaced by the report:

```text
not robust PDF extraction evidence
not OCR evidence
not table extraction evidence for arbitrary market PDFs
not layout fidelity evidence
not hosted deployment evidence
not product-complete
```

Reproduce locally:

```powershell
cd apps/api
uv run python -m app.services.multi_fixture_pdf_extraction_quality_command `
  --fixture ../../examples/pdf-extraction-quality `
  --observations ../../examples/pdf-extraction-quality/observations.json `
  --output ../../docs/evaluation/multi-fixture-pdf-extraction-quality-report.md `
  --check
uv run pytest tests/test_multi_fixture_pdf_extraction_quality.py -q
```

CI now checks the report with:

```text
Check multi-fixture PDF extraction quality report staleness
```

Next recommended gate: `missing_pdf_runtime_observation_pack_v0`.

This is a multi-fixture matrix and gap surface only. It is not robust PDF
extraction implementation, not OCR implementation, not layout fidelity
evidence, not table extraction evidence for arbitrary market PDFs, not hosted
deployment evidence, not external reviewer feedback, and not product-complete.
