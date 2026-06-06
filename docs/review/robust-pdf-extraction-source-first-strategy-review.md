# Robust PDF Extraction Source-first Strategy Review

Phase marker: robust PDF extraction source-first strategy review v0.

Status: implemented as a strategy review only.

Purpose: define the smallest source-first path from the current digital-text PDF parser toward a future robust PDF extraction claim without pretending that the current parser already covers OCR, tables, or layout fidelity.

## Current code evidence

The current parser boundary lives in `packages/ingestion/parsers/pdf.py`.

Observed current behavior:

```text
parser: pdf-pymupdf
robust_pdf_extraction: false
digital_pdf_text_extraction: true
table_extraction_performed: false
```

The parser can use PyMuPDF on uploaded PDF bytes for embedded digital text. It records page counts, page-level character counts, empty-page counts, layout block diagnostics, image block counts, and table candidate diagnostics. It also keeps table extraction explicitly false.

Failure boundaries already represented in code:

```text
pdf_encrypted_requires_password
pdf_no_extractable_text
pdf_binary_preview
```

This means NoiseProof currently has a useful PDF intake boundary, not robust PDF extraction. The code should keep saying this until extraction quality is evaluated against a known fixture set.

## Primary sources checked

- PyMuPDF text recipes: https://pymupdf.readthedocs.io/en/latest/recipes-text.html
- PyMuPDF page API and table detection: https://pymupdf.readthedocs.io/en/latest/page.html#Page.find_tables
- pdfplumber project and examples: https://github.com/jsvine/pdfplumber
- OCRmyPDF introduction: https://ocrmypdf.readthedocs.io/en/latest/introduction.html
- OCRmyPDF cookbook: https://ocrmypdf.readthedocs.io/en/latest/cookbook.html

Source-first reading: PyMuPDF is already the right baseline for embedded digital text and page diagnostics. Table handling should be separated from text extraction because table detection is not the same thing as table content extraction. OCR should be opt-in because it adds runtime, dependency, language, and quality risks, and scanned-image PDFs need different evidence than born-digital PDFs.

## adapter ladder

### Stage 1: Digital text adapter

Keep the current PyMuPDF path as the baseline adapter for born-digital PDFs. It should preserve:

- page count
- extracted page count
- empty page count
- page text character counts
- text block count
- image block count
- encrypted/password failure candidate
- no-extractable-text failure candidate

Boundary: this stage must keep `robust_pdf_extraction: false`.

### Stage 2: Table extraction adapter

Add a table adapter only after a test fixture proves what table output should look like. PyMuPDF `find_tables()` can remain table candidate diagnostics. A separate adapter can evaluate whether PyMuPDF table objects or pdfplumber table extraction produces more inspectable rows for table-heavy market reports.

Required metadata before claiming table handling:

```text
table_extraction_performed
table_extraction_engine
table_count
table_page_indexes
table_cell_count
table_warning_count
```

Boundary: table candidate detection is not table extraction.

### Stage 3: OCR adapter

Add OCR only as an explicit opt-in adapter for scanned or image-only PDFs. OCRmyPDF and Tesseract are plausible implementation sources, but they should not run silently in CI or regular preview paths.

Required metadata before claiming OCR handling:

```text
ocr_performed
ocr_engine
ocr_language
ocr_page_count
ocr_runtime_ms
ocr_warnings
```

Boundary: OCR output is extracted text with additional uncertainty, not truth.

### Stage 4: Quality ledger

Before any robust claim, create a small PDF extraction quality ledger. It should include born-digital, table-heavy, scanned, encrypted, image-heavy, and multi-column PDFs. Each fixture should name expected spans, expected warnings, and unsupported cases.

Potential metrics:

- page coverage
- character coverage
- empty-page count
- expected-span recall
- table row coverage
- OCR page coverage
- warning correctness
- failure-case candidate correctness

Only this stage can justify changing any public wording from "digital PDF text extraction" toward "robust PDF extraction".

## Proposed metadata fields

Future adapters should converge on these fields:

```text
pdf_extraction_strategy
ocr_performed
table_extraction_performed
layout_fidelity_claimed
quality_score
quality_warnings
unsupported_reason
```

The default should remain conservative:

```text
layout_fidelity_claimed: false
robust_pdf_extraction: false
```

## Acceptance gate for future implementation

Do not promote `robust_pdf_extraction` from false unless all of the following are true:

- fixture PDFs exist for digital text, tables, scanned pages, encrypted files, and no-text files
- tests cover success, warning, and failure-case candidate paths
- the quality ledger records what passed, what failed, and what remains unsupported
- docs and API responses separate digital text, table extraction, OCR, and layout fidelity
- README and GOAL still describe remaining unclaimed behavior

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not layout fidelity evidence.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: PDF extraction quality fixture packet v0 or a small parser adapter interface review, not a robust extraction claim.
