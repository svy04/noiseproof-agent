# OCR Layout Image Fixture Adapter Runtime Pack

Phase 874 adds OCR/layout/image fixture adapter runtime pack v0.

Purpose: turn the Phase 872 synthetic observation pack into an executable
adapter-runtime pack for the four PDF roles that are most likely to be
overclaimed: scanned image PDFs, image-heavy PDFs, multi-column layout PDFs,
and PDFs with no extractable digital text.

This gate adds:

- `packages/ingestion/pdf_quality/ocr_layout_image_pack.py`
- `apps/api/app/services/ocr_layout_image_fixture_adapter_runtime_pack_command.py`
- `apps/api/tests/test_ocr_layout_image_fixture_adapter_runtime_pack.py`
- `docs/evaluation/ocr-layout-image-fixture-adapter-runtime-pack-report.md`

Report markers:

```text
phase_marker -> ocr_layout_image_fixture_adapter_runtime_pack_v0
fixture_count -> 8
adapter_runtime_observed_count -> 4
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
```

Adapter boundary markers:

```text
scanned_image_pdf -> ocr_adapter_not_implemented
image_heavy_pdf -> image_chart_interpretation_not_claimed
multi_column_layout_pdf -> layout_fidelity_not_claimed
no_extractable_text_pdf -> empty_text_failure_boundary_only
```

Reproduce locally:

```powershell
cd apps/api
uv run python -m app.services.ocr_layout_image_fixture_adapter_runtime_pack_command `
  --fixture ../../examples/pdf-extraction-quality `
  --output ../../docs/evaluation/ocr-layout-image-fixture-adapter-runtime-pack-report.md `
  --check
uv run pytest tests/test_ocr_layout_image_fixture_adapter_runtime_pack.py -q
```

CI now checks the report with:

```text
Check OCR layout image fixture adapter runtime pack report staleness
```

Next recommended gate: `committed_ocr_layout_image_binary_fixture_provenance_v0`.

This is a synthetic adapter runtime pack only. It is not robust PDF extraction
evidence, not OCR evidence, not image/chart interpretation evidence, not layout
fidelity evidence, not hosted deployment evidence, not external reviewer
feedback, and not product-complete.

Boundary phrases: not robust PDF extraction evidence; not layout fidelity evidence.
