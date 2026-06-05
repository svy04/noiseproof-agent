# Uploaded PDF No-text Failure Candidate Handoff

Status: local route behavior and metadata handoff.

Phase marker: uploaded PDF no-text failure candidate handoff v0.

## Purpose

This gate preserves a PDF failure signal when uploaded PDF bytes can be opened by PyMuPDF but produce no embedded digital text.

The goal is not robust PDF extraction. The goal is to avoid silently losing the failure candidate before chunk persistence.

## Implemented Behavior

Route:

```text
POST /documents/upload-chunks
```

Observed no-text PDF handoff behavior in unit coverage:

```text
parser -> pdf-pymupdf
document.status -> chunk_handoff_no_chunks
chunk_count -> 0
chunks -> []
failure_case_candidate.failure_type -> pdf_no_extractable_text
page_text_char_counts -> [0]
empty_page_count -> 1
extracted_page_count -> 0
robust_pdf_extraction -> false
```

The persisted document `profile_json` now keeps:

```text
failure_case_candidate
robust_pdf_extraction -> false
page_text_char_counts -> [0]
empty_page_count -> 1
extracted_page_count -> 0
```

## Why This Matters

A blank, scanned, image-only, encrypted, or otherwise no-digital-text PDF should not look like a successful chunk handoff.

The system should preserve the reason it cannot produce chunks so a reviewer can see that the missing chunks are a failure boundary, not a silent success.

## Boundary

This is local route behavior.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Verification

Focused test:

```text
uv run pytest tests/test_routes.py -q -k "no_text_pdf_failure_candidate"
```

Expected result:

```text
1 passed
```

## Next Gate

```text
local runtime smoke for uploaded PDF no-text failure candidate handoff if Docker/FastAPI proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
