# Source-policy PDF Parse Observation

status: accepted-for-implementation

date: 2026-06-30

target_gate: `source_policy_pdf_parse_observation_v0`

## Current Repo State

The previous gate, `real_world_pdf_fixture_source_policy_download_hash_v0`,
recorded temporary owner-runtime download/hash metadata for selected
source-policy-reviewed PDF candidates. It recorded 3 downloaded/hashable PDFs,
2 blocked BLS HTTP 403 candidates, and 1 external review route. It did not
parse PDFs, run OCR, extract tables, compare rendered pages, or commit any
external PDF binaries, caches, raw text, page images, or screenshots.

The current next PDF evidence gate in `docs/MASTER-SPEC.md` and `docs/GOAL.md`
is `source_policy_pdf_parse_observation_v0`.

## Sources To Absorb

| Source | Pattern Borrowed | Local Adaptation | Boundary |
|---|---|---|---|
| `docs/MASTER-SPEC.md` | Every gate starts from source-first, short-term spec, bounded proof surfaces. | Keep this as an inspectable parser observation gate. | Spec compliance is not product completion. |
| `docs/evaluation/source-policy-download-hash-report.md` | Only source-policy-reviewed, hash-checked candidates move forward. | Parse only the 3 downloaded/hashable candidates and preserve blocked routes. | Download/hash metadata does not become extraction quality. |
| PyMuPDF official text recipes and text appendix | Use text and block extraction as explicit parser surfaces. | Record page count, extracted page count, native text character count, text block count, and image block count. | PyMuPDF metadata observation is not robust PDF extraction. |
| Existing `real_world_pdf_parse_observation` gate | Regenerate a report from sanitized JSON and enforce staleness in CI. | Reuse report-builder, CLI, test, and proof-surface pattern. | Previous BEA-only observations do not prove these source-policy candidates. |

## Non-goals

- No external PDF binaries committed.
- No download cache committed.
- No raw extracted text.
- No text samples.
- No raw OCR text.
- No raw table rows.
- No page images or screenshots.
- No OCR.
- No table extraction.
- No layout-fidelity scoring.
- No rendered visual comparison.
- No image/chart interpretation.
- No LLM calls.
- No retrieval, Evidence Ledger, Critic, final report generation, or dashboard work.
- No robust PDF extraction claim.

## Implementation Scope

Add a deterministic source-policy PDF parse observation packet from a committed
sanitized manifest:

```text
examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json
packages/ingestion/pdf_quality/source_policy_pdf_parse_observation.py
apps/api/app/services/source_policy_pdf_parse_observation_command.py
apps/api/tests/test_source_policy_pdf_parse_observation.py
docs/evaluation/source-policy-pdf-parse-observation-report.md
docs/review/source-policy-pdf-parse-observation.md
```

Update proof surfaces:

```text
README.md
docs/MASTER-SPEC.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
docs/review/external-reader-proof-path.md
docs/review/proof-gap-action-surface.md
docs/research/source-assimilation-registry.md
apps/api/app/services/proof_gap_registry.py
.github/workflows/ci.yml
```

## Data Contract

The manifest must include:

```text
phase_marker
previous_gate
claim_boundary
source_download_hash_manifest
observed_at_utc
parse_observation_status
owner_approved
parser
parser_version
observed_fixtures
blocked_fixtures
external_routes
runtime/download/parser/OCR/table/LLM booleans
binary/raw/page-image/screenshot booleans
blocked_reasons
warnings
boundary_notes
recommended_next_gate
```

Observed fixture entries must include:

```text
fixture_id
target_missing_cell
publisher
source_url
policy_source_url
source_sha256
http_status
content_type
byte_size
parser
parse_status
page_count
extracted_page_count
empty_page_count
pages_with_text
pages_with_images
text_char_count
text_block_count
image_block_count
table_extraction_performed
ocr_calls_attempted
raw_text_committed
binary_committed
local_pdf_path
failure_case_candidate
warnings
boundary
```

## Tests

- Loading and summary validation for 3 observed fixtures, 2 blocked candidates,
  and 1 external route.
- No binary/raw/page-image/screenshot commitment.
- Native text metadata for EIA and BEA remains observable.
- NARA no-native-text observation is represented as a failure-case candidate.
- Generated report is byte-for-byte current.
- CLI `--check` accepts the report.
- README, GOAL, MASTER-SPEC, runbook, portfolio, external-reader path,
  proof-gap registry, and CI all reference the gate and next gate.

## Stop Conditions

Stop and report if:

- downloaded bytes do not match the previous SHA-256 hashes
- a parser result requires committing raw text to prove the observation
- a source blocks runtime access unexpectedly
- PyMuPDF cannot open a candidate and the failure cannot be represented without raw content
- any implementation drifts into OCR, table extraction, visual comparison, retrieval, or robust-PDF wording

## Claim Boundaries

This gate may claim:

```text
source-policy-reviewed downloaded PDFs were observed with PyMuPDF text/block metadata
```

This gate must not claim:

```text
robust PDF extraction
arbitrary-market PDF parsing reliability
OCR quality
table extraction benchmark quality
layout fidelity
rendered visual fidelity
image/chart interpretation
external reviewer feedback
hosted deployment
product completion
```

## Next Gate If Passed

```text
source_policy_pdf_parse_quality_matrix_v0
```
