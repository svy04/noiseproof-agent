# Source-policy No-native-text OCR Execution Plan

Phase marker: source_policy_no_native_text_ocr_execution_plan_v0.

This report records a bounded OCR execution plan for the preserved NARA no-native-text route.

It plans a future PyMuPDF/Tesseract OCR smoke only.

It does not run OCR.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

## Gate Result

plan_status -> planned_execution_contract
previous_gate -> source_policy_no_native_text_ocr_dependency_resolution_v0
execution_adapter -> pymupdf_page_get_textpage_ocr
execution_mode -> owner_runtime_opt_in_smoke
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
failure_type -> no_native_text_observed
target_page_count -> 4
target_empty_page_count -> 4
target_text_char_count -> 0
dependency_available -> true
path_refresh_required -> true
opt_in_required -> true
planned_ocr_language -> eng
planned_dpi -> 300
planned_full_page_ocr -> true
planned_pages -> 1, 2, 3, 4
planned_output_policy -> sanitized_counts_and_expected_marker_hits_only
ocr_execution_performed -> false
ocr_quality_eval_performed -> false
pdf_downloads_performed -> false
parser_calls_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
download_cache_committed -> false
raw_text_committed -> false
raw_ocr_text_committed -> false
page_images_committed -> false
screenshots_committed -> false
can_claim_ocr_execution_plan -> true
can_claim_ocr_execution -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Sources

| Label | Type | URL | Pattern |
|---|---|---|---|
| PyMuPDF OCR recipes | official_doc | https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html | Keep OCR explicit, Tesseract-backed, and separate from normal text extraction. |
| PyMuPDF Page.get_textpage_ocr | official_doc | https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr | Plan the owner-runtime smoke around the explicit OCR adapter and its language, dpi, and full-page options. |
| Tesseract command line usage | official_doc | https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html | Treat command and language availability as prerequisites, not OCR execution or quality. |
| OCR-D evaluation | standard | https://ocr-d.de/en/spec/ocrd_eval.html | Keep OCR execution separate from recognition quality evaluation. |

## Planned Execution Steps

- Refresh owner-runtime PATH before resolving the tesseract command.
- Require explicit opt-in before any OCR call.
- Use the preserved no-native-text route only.
- Run PyMuPDF get_textpage_ocr with English language, 300 dpi, and full-page OCR in the next gate.
- Record only sanitized counts, expected-marker hit booleans, warnings, and non-claims.

## Stop Conditions

- Stop if the source PDF is unavailable in the owner-runtime cache.
- Stop if the tesseract command or English language data is unavailable.
- Stop if OCR would require committing raw OCR text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if OCR output is requested to be treated as quality evidence without a separate quality gate.

## Minimum Next Evidence

- A bounded owner-runtime OCR smoke packet that records attempted page count and sanitized OCR text counts.
- A report that keeps raw OCR text and source PDF binaries out of the repository.
- A next gate for OCR quality evaluation only after execution evidence exists.

## Warnings

- This is an execution plan only and does not run OCR.
- Dependency availability does not prove OCR execution.
- OCR execution will not prove OCR quality without a separate evaluation criterion.

## Next Gate

- source_policy_no_native_text_ocr_execution_smoke_v0

## Boundary Notes

- source-policy no-native-text OCR execution plan only
- not OCR execution evidence
- not OCR quality evidence
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not table extraction benchmark evidence
- not layout fidelity evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic OCR execution-plan packet over the current source-policy no-native-text route.

It does not download PDFs, parse PDFs, run OCR, evaluate OCR output, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or build a dashboard.

It does not commit local executable paths, tessdata paths, external PDF binaries, download caches, raw text, raw OCR text, page images, or screenshots.

It does not prove OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
