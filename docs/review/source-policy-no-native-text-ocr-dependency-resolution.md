# Source-policy No-native-text OCR Dependency Resolution

Phase marker: `source_policy_no_native_text_ocr_dependency_resolution_v0`.

This review records the dependency-resolution gate after the previous
dependency check found the Tesseract command missing.

## What Changed

- `winget` was used as the owner-runtime installer/package manager surface.
- `tesseract-ocr.tesseract` is recorded as installed at version `5.5.0.20241111`.
- The owner-runtime probe refreshed machine/user PATH in-process because the
  Codex parent process did not inherit the updated user PATH automatically.
- The sanitized probe observed command availability, version check completion,
  language-list check completion, and English language data availability.

## Evidence

- Packet: `examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-resolution.json`
- Report: `docs/evaluation/source-policy-no-native-text-ocr-dependency-resolution-report.md`
- Command: `app.services.source_policy_no_native_text_ocr_dependency_resolution_command`
- Previous gate: `source_policy_no_native_text_ocr_dependency_check_v0`
- Next gate: `source_policy_no_native_text_ocr_execution_plan_v0`

## Can Claim

- The source-policy no-native-text OCR dependency is available in the owner
  runtime after installation/configuration and sanitized PATH refresh.

## Cannot Claim

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

This gate records dependency availability only. It does not download PDFs,
parse PDFs, run OCR, evaluate OCR output, extract tables, compare rendered
pages, interpret images or charts, call LLMs, chunk, retrieve, generate
Evidence Ledger entries, run Noise Gate, or build a dashboard.

No local executable paths, tessdata paths, external PDF binaries, download
caches, raw text, raw OCR text, page images, screenshots, or table rows are
committed in the packet, report, or review artifact.
