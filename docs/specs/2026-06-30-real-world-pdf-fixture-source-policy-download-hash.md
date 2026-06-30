# Real-world PDF Fixture Source-policy Download Hash

status: accepted-for-implementation

date: 2026-06-30

target_gate: `real_world_pdf_fixture_source_policy_download_hash_v0`

## Current Repo State

The previous gate, `targeted_real_world_pdf_fixture_expansion_v0`, mapped the
six missing PDF matrix cells to source-policy-reviewed candidate routes. It did
not download, hash, parse, OCR, table-extract, or visually inspect any PDF.

This gate performs the smallest safe runtime step after that plan: temporary
owner-runtime downloads for selected PDF candidates, SHA-256 hashes, byte-size
metadata, HTTP status, PDF magic-header checks, and non-commitment boundaries.

## Sources To Absorb

| Source | Pattern Borrowed | Local Adaptation | Boundary |
|---|---|---|---|
| Targeted fixture expansion plan | Only source-policy-reviewed candidates move to download/hash. | Use the 5 PDF candidates from the plan and keep the GitHub issue as an external route. | Planned coverage is not runtime parsing evidence. |
| BLS copyright information and MLR page | Source-policy review can still be blocked by runtime access. | Record BLS HTTP 403 as blocked candidates, not failures hidden from the proof chain. | HTTP 403 is not a parsing result. |
| EIA reuse policy | Download/hash a stable STEO PDF only as metadata. | Keep URL, policy URL, byte size, hash, and PDF magic flag. | Not visual fidelity evidence. |
| BEA FAQ 147 | Download/hash the existing BEA working paper candidate. | Keep metadata only for future layout-label candidate work. | Not layout benchmark evidence. |
| NARA policy boundary | Archive records need explicit caution even if retrievable. | Record NARA hash and content-type warning without raw OCR text or binary. | Not OCR quality evidence. |

## Implementation Target

Add a deterministic download/hash report from a committed sanitized manifest:

```text
examples/pdf-extraction-quality/source-policy-download-hash-observations.json
packages/ingestion/pdf_quality/source_policy_download_hash.py
apps/api/app/services/source_policy_download_hash_command.py
apps/api/tests/test_source_policy_download_hash.py
docs/evaluation/source-policy-download-hash-report.md
docs/review/source-policy-download-hash.md
```

Required proof-surface updates:

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
source_plan
observed_at_utc
download_hash_status
owner_approved
downloaded_fixtures
blocked_fixtures
external_routes
runtime/download/parser/OCR/table/LLM booleans
binary/raw/page-image/screenshot booleans
blocked_reasons
warnings
boundary_notes
recommended_next_gate
```

Downloaded fixture entries must include:

```text
fixture_id
target_missing_cell
publisher
source_url
policy_source_url
download_status
http_status
content_type
byte_size
sha256
pdf_magic_header
binary_committed
local_pdf_path
raw_text_committed
boundary
```

## Non-goals

- No external PDF binaries committed.
- No download cache committed.
- No raw extracted text.
- No raw OCR text.
- No raw table rows.
- No page images or screenshots.
- No parser runtime call.
- No OCR runtime call.
- No table extraction runtime call.
- No LLM calls.
- No retrieval, Evidence Ledger, Critic, final report generation, or dashboard work.
- No robust PDF extraction claim.

## Acceptance

- The manifest records 3 downloaded/hashable PDFs.
- The manifest records 2 blocked BLS HTTP 403 candidates.
- The manifest records 1 external-review route with no download.
- `can_claim_download_hash_metadata -> true`.
- `can_claim_robust_pdf_extraction -> false`.
- No external PDF binary, raw content, screenshots, or page images are committed.
- The next gate is `source_policy_pdf_parse_observation_v0`.
- CI checks that the generated report is not stale.
