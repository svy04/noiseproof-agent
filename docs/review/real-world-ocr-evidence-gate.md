# Real-world OCR Evidence Gate

Phase `real_world_ocr_evidence_gate_v0` records one sanitized OCR observation
from a temporary owner-runtime NARA PDF download.

## What Changed

Added:

- `examples/pdf-extraction-quality/real-world-ocr-evidence.json`
- `packages/ingestion/pdf_quality/real_world_ocr_evidence.py`
- `apps/api/app/services/real_world_ocr_evidence_gate_command.py`
- `docs/evaluation/real-world-ocr-evidence-gate-report.md`
- `apps/api/tests/test_real_world_ocr_evidence_gate.py`

Updated:

- `docs/research/source-assimilation-registry.md`
- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`

## Gate Result

```text
ocr_gate_status -> passed
observed_fixture_count -> 1
ocr_observed_fixture_count -> 1
publisher -> National Archives and Records Administration
fixture_id -> nara_911_mfr_00282
total_page_count -> 4
total_ocr_pages_attempted -> 2
total_native_text_char_count -> 0
total_ocr_text_char_count -> 3992
ocr_page_coverage_ratio -> 0.50
expected_terms_found_count -> 4
has_real_world_ocr_evidence -> true
can_claim_real_world_ocr_evidence -> true
can_claim_robust_pdf_extraction -> false
```

## Evidence Shape

The committed evidence is sanitized metadata only:

```text
source URL
collection/source policy URLs
HTTP metadata
SHA-256
byte size
page count
OCR pages attempted
native text character count
OCR text character count
expected term hit booleans
warnings
```

The repo does not commit:

```text
external PDF binaries
download caches
local PDF paths
tessdata paths
raw extracted text
raw OCR text
```

## Remaining Blocker

The OCR blocker is reduced for one NARA fixture, but robust PDF extraction
remains blocked because layout fidelity is still missing.

Remaining blocked reason:

```text
layout_fidelity_evidence_missing
```

## Boundary

This is real-world OCR evidence over one sanitized owner-runtime observation.

Boundaries:

- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not arbitrary-market PDF OCR evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

## Verification

RED test before implementation:

```text
uv run pytest tests/test_real_world_ocr_evidence_gate.py -q
ModuleNotFoundError: No module named 'packages.ingestion.pdf_quality.real_world_ocr_evidence'
```

Focused verification after implementation:

```text
uv run pytest tests/test_real_world_ocr_evidence_gate.py -q
```

Report staleness verification:

```text
uv run python -m app.services.real_world_ocr_evidence_gate_command --evidence ..\..\examples\pdf-extraction-quality\real-world-ocr-evidence.json --output ..\..\docs\evaluation\real-world-ocr-evidence-gate-report.md --check
```

## Next Gate

```text
real_world_layout_fidelity_evidence_gate_v0
```

Do not use this gate to claim robust PDF extraction.
