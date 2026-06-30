# Source-policy No-native-text OCR Dependency Resolution

Phase marker: source_policy_no_native_text_ocr_dependency_resolution_v0.

This report records a sanitized owner-runtime dependency resolution observation for the preserved NARA no-native-text route.

It records command and English language-data availability only.

It does not commit local executable or tessdata paths.

It does not run OCR.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

## Gate Result

dependency_resolution_status -> resolved_dependency_available
previous_gate -> source_policy_no_native_text_ocr_dependency_check_v0
observation_source -> owner_runtime_path_refresh_after_winget_install_2026_06_30
installation_method -> winget
installation_package_id -> tesseract-ocr.tesseract
installed_package_version -> 5.5.0.20241111
codex_parent_path_inheritance_mismatch -> true
owner_runtime_path_refresh_performed -> true
fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
failure_type -> no_native_text_observed
page_count -> 4
empty_page_count -> 4
text_char_count -> 0
tesseract_command_present -> true
version_check_performed -> true
language_list_check_performed -> true
tesseract_version_reported -> true
tesseract_version -> 5.5.0.20241111
detected_language_count -> 2
eng_language_available -> true
local_path_discovery_performed -> true
local_paths_committed -> false
tesseract_path_committed -> false
tessdata_path_committed -> false
runtime_work_performed -> true
pdf_downloads_performed -> false
parser_calls_performed -> false
ocr_execution_performed -> false
ocr_quality_eval_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
download_cache_committed -> false
raw_text_committed -> false
raw_ocr_text_committed -> false
can_claim_ocr_dependency_available -> true
can_claim_ocr_execution -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Sources

| Label | Type | URL | Pattern |
|---|---|---|---|
| Tesseract command line usage | official_doc | https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html | Use command-level probes such as version and language listing without treating them as OCR execution or quality. |
| Tesseract installation | official_doc | https://tesseract-ocr.github.io/tessdoc/Installation.html | Treat engine installation, PATH configuration, and traineddata/language files as setup concerns. |
| PyMuPDF OCR recipes | official_doc | https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html | Keep PyMuPDF OCR explicit and Tesseract-backed. |
| OCR-D evaluation | standard | https://ocr-d.de/en/spec/ocrd_eval.html | Keep dependency availability separate from recognition quality evaluation. |
| Windows Package Manager | runtime_package_manager | owner-runtime winget search/list/install output | Use winget as local installation evidence without committing installer binaries or local paths. |

## Resolved Evidence

- winget reported tesseract-ocr.tesseract version 5.5.0.20241111 installed
- owner-runtime PATH refresh made the tesseract command resolvable
- tesseract version check completed
- tesseract language list check completed
- English language data was available

## Remaining Blockers

- ocr_execution_not_performed
- ocr_quality_eval_not_performed
- robust_pdf_claim_still_blocked
- codex_parent_process_needs_path_refresh_or_restart_for_default_probe

## Minimum Next Evidence

- Create a bounded OCR execution plan for the preserved no-native-text route.
- Run OCR only in an explicit follow-up gate.
- Keep raw OCR text, source PDFs, executable paths, tessdata paths, page images, and screenshots out of committed artifacts.

## Warnings

- Dependency availability does not prove OCR execution.
- Dependency availability does not prove OCR quality.
- The Codex parent process did not automatically inherit the refreshed user PATH; the owner-runtime probe refreshed PATH in-process.

## Next Gate

- source_policy_no_native_text_ocr_execution_plan_v0

## Boundary Notes

- source-policy no-native-text OCR dependency resolution only
- OCR dependency availability evidence only
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

This is a deterministic dependency-resolution packet over the current owner-runtime OCR dependency state.

It does not download PDFs, parse PDFs, run OCR, evaluate OCR output, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or build a dashboard.

It does not commit local executable paths, tessdata paths, external PDF binaries, download caches, raw text, raw OCR text, page images, or screenshots.

It does not prove OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
