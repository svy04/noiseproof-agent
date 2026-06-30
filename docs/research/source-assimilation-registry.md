# Source Assimilation Registry

Status: active research registry.

Canonical path: `docs/research/source-assimilation-registry.md`.

Phase marker: `source_assimilation_registry_v0`.

This registry turns the source-first doctrine in `docs/MASTER-SPEC.md` into
source cards. A source card does not claim implementation maturity. It records
what NoiseProof borrows, what it rejects, and what it cannot claim.

## Source Card Contract

Each source card uses this shape:

```text
source:
source_type:
pattern_to_borrow:
local_adaptation:
boundary:
rejection_condition:
license_or_rights_note:
```

Future non-trivial gates should add or update source cards before implementing
new behavior.

## Registry Cards

### W3C PROV-DM

source: https://www.w3.org/TR/prov-dm/

source_type: standard

pattern_to_borrow: Model provenance through entities, activities, agents,
derivations, and bundles.

local_adaptation: Treat documents, chunks, retrieval runs, Evidence Ledger
entries, Noise Gate records, reports, workflow runs, and proof packets as
lineage-linked records.

boundary: Provenance records make claims inspectable; they do not make claims
true.

rejection_condition: Reject designs that collapse source, retrieval activity,
claim, and report into one opaque answer object.

license_or_rights_note: Use as a public standard reference; do not copy large
verbatim sections into project docs.

### SLSA Provenance

source: https://slsa.dev/spec/v1.0/provenance

source_type: standard

pattern_to_borrow: Keep subject, build/run type, materials, invocation,
environment, and byproducts explicit.

local_adaptation: Agent and workflow proof packets should expose input
artifacts, workflow version, parameters, output artifacts, trace ids, and
verification status.

boundary: NoiseProof local proof packets are not SLSA certification.

rejection_condition: Reject proof docs that say a run is verified without
recording which subject, command, input, output, and verification result were
observed.

license_or_rights_note: Public specification pattern only.

### OpenTelemetry Specification

source: https://opentelemetry.io/docs/specs/otel/overview/

source_type: standard

pattern_to_borrow: Keep traces, metrics, logs, baggage/context propagation, and
resources conceptually distinct.

local_adaptation: Keep local trace surfaces separate from logs, dashboard
counts, and hosted observability claims.

boundary: Local in-memory spans and trace headers are not distributed tracing or
hosted observability evidence.

rejection_condition: Reject wording that upgrades local trace inspection into
production observability.

license_or_rights_note: Use as an official specification reference.

### RAGAS

source: https://aclanthology.org/2024.eacl-demo.16/

source_type: paper

pattern_to_borrow: Evaluate retrieval-augmented generation through multiple
measurement surfaces instead of one answer-quality score.

local_adaptation: Keep retrieval quality, citation coverage, answer support,
faithfulness, and failure records separate.

boundary: Local NoiseProof fixtures are not public RAGAS benchmark results.

rejection_condition: Reject any claim that a green local report proves general
RAG quality.

license_or_rights_note: Cite the paper; do not reproduce tables or long text.

### ALCE

source: https://aclanthology.org/2023.emnlp-main.398/

source_type: paper

pattern_to_borrow: Treat citation quality as a distinct evaluation target for
attributed long-form generation.

local_adaptation: Claim-bounded reports should expose claim, source id,
evidence span, limitation, and contradiction separately from prose quality.

boundary: Citation presence is not truth.

rejection_condition: Reject report designs that hide evidence spans behind
smooth narrative.

license_or_rights_note: Cite the paper; avoid reproducing benchmark content.

### BEIR and trec_eval

source: https://openreview.net/forum?id=wCu6T5xFjeJ

source: https://github.com/usnistgov/trec_eval

source_type: paper_and_oss

pattern_to_borrow: Shape retrieval evaluation around corpus, queries, qrels,
runs, and explicit metrics.

local_adaptation: Semantic retrieval proof should stay qrels-backed before
stronger quality claims.

boundary: Tiny local qrels are not representative production retrieval quality.

rejection_condition: Reject retrieval claims that lack judged query/document
pairs or disclose no unjudged retrieved count.

license_or_rights_note: Respect upstream project licenses and benchmark terms.

### Model Cards

source: https://arxiv.org/abs/1810.03993

source_type: paper

pattern_to_borrow: Report intended use, factors, metrics, caveats, ethical
considerations, and boundaries.

local_adaptation: Public-facing NoiseProof claims should include implemented,
not implemented, verified, not verified, can claim, cannot claim, and next
evidence gate fields.

boundary: Naming the pattern does not make NoiseProof model-card compliant.

rejection_condition: Reject public copy that presents a capability without a
limitation and verification state.

license_or_rights_note: Cite the paper; avoid long quoted text.

### Datasheets for Datasets

source: https://arxiv.org/abs/1803.09010

source_type: paper

pattern_to_borrow: Document dataset motivation, composition, collection,
preprocessing, recommended use, and maintenance.

local_adaptation: Fixture packs should show source policy, collection method,
hash/download status, omissions, and non-claims.

boundary: Fixture docs are not dataset certification.

rejection_condition: Reject real-world fixture work without license/source
policy and raw-data handling notes.

license_or_rights_note: Cite the paper; keep fixture source terms visible.

### Diataxis

source: https://diataxis.fr/

source_type: documentation_framework

pattern_to_borrow: Separate tutorials, how-to guides, explanation, and
reference.

local_adaptation: Keep `README.md`, `docs/GOAL.md`, `docs/runbook.md`,
`docs/application/portfolio-index.md`, and reviewer proof paths from trying to
serve the same reader job.

boundary: Diataxis is a documentation pattern, not product evidence.

rejection_condition: Reject one-wall documents that mix current proof,
historical ledger, reviewer route, and implementation instructions without
navigation.

license_or_rights_note: Reference the public framework; do not copy site text.

### Docling and Unstructured

source: https://github.com/docling-project/docling

source: https://docs.unstructured.io/open-source/core-functionality/partitioning

source_type: oss_and_official_docs

pattern_to_borrow: Treat parsing, document elements, layout, tables, OCR, and
images as separable capabilities.

local_adaptation: Keep digital PDF text extraction, table candidates, table
adapter output, OCR smoke, layout/image fixtures, and robust extraction claims
separate.

boundary: NoiseProof does not claim Docling or Unstructured integration by
referencing them.

rejection_condition: Reject any parser gate that says "PDF parsing works"
without separating modality, fixture type, table/OCR/layout status, and
failure cases.

license_or_rights_note: Respect upstream licenses before vendoring or direct
integration.

### Source-policy PDF Parse Quality Matrix

source: https://github.com/docling-project/docling

source: https://docs.unstructured.io/open-source/core-functionality/partitioning

source_type: oss_and_official_docs_adaptation

pattern_to_borrow: Treat document parsing as separable elements and stages
rather than one undifferentiated "PDF parsed" claim.

local_adaptation: `source_policy_pdf_parse_quality_matrix_v0` separates
digital-text metadata observations, no-native-text failure candidates, blocked
downloads, visual fidelity, layout ground truth, reading order, image/chart
interpretation, and external validation into different matrix cells.

boundary: A matrix over parse observations does not prove parsing quality.

rejection_condition: Reject parser wording that upgrades PyMuPDF text/block
metadata into robust PDF extraction, rendered visual fidelity, OCR quality, or
image/chart interpretation.

license_or_rights_note: Use public project/docs patterns only; do not copy
project code or long documentation passages.

### Source-policy PDF Quality Gap Review

source: https://arxiv.org/abs/1810.03993

source: https://arxiv.org/abs/1803.09010

source: https://ocr-d.de/en/spec/ocrd_eval.html

source_type: paper_and_spec_adaptation

pattern_to_borrow: Select next evidence by explicit limitations, dataset/source
boundaries, and measurable OCR-quality separation rather than by the most
impressive demo path.

local_adaptation: `source_policy_pdf_quality_gap_review_v0` ranks the six
source-policy PDF quality blockers and selects the NARA no-native-text failure
route because it can preserve a real observed failure before OCR quality work,
without new downloads or OCR calls.

boundary: Selecting a no-native-text failure route does not prove OCR quality,
robust PDF extraction, rendered visual fidelity, layout fidelity, image/chart
interpretation, or external validation.

rejection_condition: Reject next-gate decisions that jump from no-native-text
metadata to OCR quality, or that choose externally blocked routes while a
smaller inspectable failure route remains unpreserved.

license_or_rights_note: Use public paper/spec patterns only; cite sources and
avoid copying benchmark text or evaluation assets.

### Source-policy No-native-text Failure Route

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr

source: https://ocr-d.de/en/spec/ocrd_eval.html

source: https://arxiv.org/abs/1810.03993

source: https://arxiv.org/abs/1803.09010

source_type: official_doc_spec_and_paper_adaptation

pattern_to_borrow: Preserve no-native-text as an explicit failure route before
OCR readiness, OCR execution, or OCR quality claims. Keep dependency readiness,
runtime OCR, quality evaluation, and public claim boundaries as separate gates.

local_adaptation: `source_policy_no_native_text_failure_route_v0` preserves
the selected NARA no-native-text case as a deterministic packet with source
URL, source policy URL, hash, page counts, empty page count, text character
count, warnings, and non-claims. It commits no PDF binary, download cache, raw
text, raw OCR text, page image, screenshot, or table rows.

boundary: A preserved no-native-text failure route does not prove OCR quality,
robust PDF extraction, arbitrary-market PDF parsing reliability, rendered
visual fidelity, layout fidelity, image/chart interpretation, or external
validation.

rejection_condition: Reject any gate that treats the preserved failure route as
OCR evidence, hides the lack of OCR execution, or jumps directly to robust PDF
wording before `source_policy_no_native_text_ocr_readiness_review_v0`.

license_or_rights_note: Cite the official PyMuPDF and OCR-D documentation plus
the model-card/datasheet papers as patterns only; do not copy external PDF
content, benchmark assets, or long documentation passages.

### Source-policy No-native-text OCR Readiness Review

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr

source: https://ocr-d.de/en/spec/ocrd_eval.html

source: https://arxiv.org/abs/1810.03993

source: https://arxiv.org/abs/1803.09010

source_type: official_doc_spec_and_paper_adaptation

pattern_to_borrow: Treat OCR readiness as a separate review surface before
dependency runtime checks, OCR execution, or OCR quality evaluation. Use
Model Cards and Datasheets as patterns for keeping intended-use, source,
dependency, and non-claim boundaries visible.

local_adaptation: `source_policy_no_native_text_ocr_readiness_review_v0`
reviews the preserved NARA no-native-text route and records the readiness
criteria needed before a future dependency check. It commits no source PDF,
raw text, raw OCR text, local paths, tessdata paths, page images, or
screenshots.

boundary: OCR readiness review does not prove OCR dependency availability,
OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF
parsing reliability, rendered visual fidelity, image/chart interpretation, or
external validation.

rejection_condition: Reject any gate that treats readiness as dependency
availability, runs OCR before the dependency check gate, prints local OCR
paths, commits OCR text, or upgrades readiness wording into OCR quality.

license_or_rights_note: Cite official docs and public papers as patterns only;
do not copy external PDF content, benchmark assets, local runtime paths, or
long documentation passages.

### Source-policy No-native-text OCR Dependency Check

source: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html

source: https://tesseract-ocr.github.io/tessdoc/Installation.html

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://ocr-d.de/en/spec/ocrd_eval.html

source_type: official_doc_and_standard_adaptation

pattern_to_borrow: Treat command availability, language data availability, OCR
execution, and OCR quality as separate surfaces. Use command-level probes
without printing local executable or tessdata paths.

local_adaptation: `source_policy_no_native_text_ocr_dependency_check_v0`
records the current missing Tesseract command state for the preserved NARA
no-native-text route. It commits sanitized booleans and counts only; no local
paths, PDFs, raw text, raw OCR text, page images, or screenshots are committed.

boundary: A dependency check does not prove OCR execution, OCR quality, robust
PDF extraction, arbitrary-market PDF parsing reliability, rendered visual
fidelity, image/chart interpretation, or external validation.

rejection_condition: Reject any gate that treats dependency availability as
OCR evidence, prints local paths, commits tessdata paths, or runs OCR before
the dependency state is resolved.

license_or_rights_note: Cite Tesseract, PyMuPDF, and OCR-D docs as public
patterns only; do not copy local runtime paths, traineddata files, source PDF
content, benchmark assets, or long documentation passages.

### Source-policy No-native-text OCR Dependency Resolution

source: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html

source: https://tesseract-ocr.github.io/tessdoc/Installation.html

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://ocr-d.de/en/spec/ocrd_eval.html

source: owner-runtime winget search/list/install output

source_type: official_doc_standard_and_runtime_package_manager_adaptation

pattern_to_borrow: Treat installation, PATH refresh, command version checks,
language-data listing, OCR execution, and OCR quality as separate proof
surfaces.

local_adaptation: `source_policy_no_native_text_ocr_dependency_resolution_v0`
records that the owner runtime can resolve Tesseract and English language data
after installation/configuration and PATH refresh. It commits sanitized
booleans, counts, package id, and version only; no local paths, tessdata paths,
PDFs, raw text, raw OCR text, page images, or screenshots are committed.

boundary: Dependency availability does not prove OCR execution, OCR quality,
robust PDF extraction, arbitrary-market PDF parsing reliability, rendered
visual fidelity, image/chart interpretation, or external validation.

rejection_condition: Reject any gate that treats dependency availability as OCR
execution, commits local executable or tessdata paths, runs OCR before an
explicit execution gate, or upgrades dependency availability into OCR quality.

license_or_rights_note: Cite Tesseract, PyMuPDF, OCR-D, and local package
manager output as public/runtime patterns only; do not copy traineddata files,
installer binaries, source PDF content, benchmark assets, local runtime paths,
or long documentation passages.

### Source-policy No-native-text OCR Execution Plan

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr

source: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html

source: https://ocr-d.de/en/spec/ocrd_eval.html

source_type: official_doc_and_standard_adaptation

pattern_to_borrow: Treat OCR execution as an explicit Tesseract-backed adapter
path with language, dpi, and full-page choices, and keep execution separate
from OCR quality evaluation.

local_adaptation: `source_policy_no_native_text_ocr_execution_plan_v0`
records the planned PyMuPDF/Tesseract owner-runtime OCR smoke for the preserved
NARA no-native-text route. It commits only the execution contract, planned
parameters, stop conditions, output policy, and non-claims.

boundary: An OCR execution plan does not prove OCR execution, OCR quality,
robust PDF extraction, arbitrary-market PDF parsing reliability, rendered
visual fidelity, image/chart interpretation, or external validation.

rejection_condition: Reject any gate that runs OCR inside the plan gate,
commits local paths or raw OCR text, treats execution planning as OCR evidence,
or upgrades a future OCR smoke into OCR quality.

license_or_rights_note: Cite PyMuPDF, Tesseract, and OCR-D docs as public
patterns only; do not copy traineddata files, source PDF content, benchmark
assets, local runtime paths, or long documentation passages.

### Source-policy No-native-text OCR Execution Smoke

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html

source: https://ocr-d.de/en/spec/ocrd_eval.html

source_type: official_doc_standard_and_runtime_evidence_adaptation

pattern_to_borrow: Treat OCR execution as a bounded runtime event with explicit
adapter, language, dpi, source hash, no raw text commits, and a separate later
quality-evaluation gate.

local_adaptation: `source_policy_no_native_text_ocr_execution_smoke_v0`
records one owner-runtime PyMuPDF/Tesseract OCR smoke for the preserved NARA
no-native-text route. It commits sanitized counts, marker-hit booleans, source
hash, and non-claims only.

boundary: An OCR execution smoke does not prove OCR quality, robust PDF
extraction, arbitrary-market PDF parsing reliability, rendered visual fidelity,
image/chart interpretation, or external validation.

rejection_condition: Reject any gate that commits raw OCR text, source PDFs,
local paths, tessdata paths, page images, screenshots, or treats marker hits as
OCR quality evaluation.

license_or_rights_note: Cite PyMuPDF, Tesseract, and OCR-D docs as public
patterns only; do not copy traineddata files, source PDF content, benchmark
assets, local runtime paths, or long documentation passages.

### Source-policy No-native-text OCR Quality Eval Plan

source: https://ocr-d.de/en/spec/ocrd_eval.html

source: https://github.com/jitsi/jiwer

source: https://arxiv.org/abs/1810.03993

source: https://arxiv.org/abs/1803.09010

source_type: standard_oss_and_paper_adaptation

pattern_to_borrow: Treat OCR quality as a reference-backed evaluation surface,
not as a side effect of successful OCR execution, character counts, or marker
hits. Keep metric candidates, reference inputs, normalization rules, source
binding, and non-claims explicit before scoring.

local_adaptation: `source_policy_no_native_text_ocr_quality_eval_plan_v0`
records the reference inputs and metric candidates required before the
preserved NARA no-native-text route can compute OCR quality. It commits no
source PDF, raw OCR text, raw reference text, local paths, tessdata paths, page
images, or screenshots.

boundary: An OCR quality evaluation plan does not prove OCR quality, robust PDF
extraction, arbitrary-market PDF parsing reliability, rendered visual
fidelity, image/chart interpretation, or external validation.

rejection_condition: Reject any gate that treats expected-marker hits or OCR
text counts as quality scores, computes CER/WER without reference data, commits
raw OCR/reference text, or upgrades a plan into an OCR quality claim.

license_or_rights_note: Cite OCR-D, JiWER, and public papers as patterns only;
do not copy benchmark assets, source PDF content, raw text, or long
documentation passages.

### PyMuPDF Table Extraction

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.find_tables

source_type: official_doc

pattern_to_borrow: Use `Page.find_tables()` to locate table structures and
`Table.extract()` to return table rows, while treating that output as adapter
evidence rather than general PDF reliability.

local_adaptation: Keep `pymupdf-find_tables-extract` as a bounded table
adapter. For real-world PDFs, commit only sanitized counts, hashes, table shape
samples, warnings, and non-claims. Do not commit PDF binaries, raw extracted
text, or raw table rows.

boundary: PyMuPDF table extraction output does not prove robust PDF extraction,
OCR, layout fidelity, or arbitrary-market PDF parsing reliability.

rejection_condition: Reject any gate that treats `find_tables()` success on a
few fixtures as a broad robust-PDF claim, or that commits raw table rows from
external source PDFs.

license_or_rights_note: Cite the official PyMuPDF documentation; respect source
publisher reuse policies before using external PDFs as fixtures.

### PyMuPDF OCR

source: https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr

source_type: official_doc

pattern_to_borrow: Treat OCR as an explicit Tesseract-backed path through
`Page.get_textpage_ocr()`, separate from normal digital text extraction.

local_adaptation: Keep owner-runtime OCR observations sanitized. Commit source
URL, source policy URL, hash, page counts, character counts, expected-term hit
metadata, warnings, and non-claims. Do not commit external PDFs, raw OCR text,
local file paths, or tessdata paths.

boundary: One OCR observation through PyMuPDF does not prove robust PDF
extraction, arbitrary-market OCR reliability, layout fidelity, or report truth.

rejection_condition: Reject any OCR gate that silently falls back to OCR, hides
Tesseract/tessdata dependency, commits raw OCR text from external PDFs, or
upgrades one observation into robust parsing wording.

license_or_rights_note: Cite the official PyMuPDF documentation and respect
publisher source policies before using external PDFs as fixtures.

### PyMuPDF Text Blocks and Layout Metadata

source: https://pymupdf.readthedocs.io/en/latest/app1.html

source: https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_text

source_type: official_doc

pattern_to_borrow: Treat text blocks, dictionary blocks, coordinates, and
`sort` behavior as layout metadata surfaces that can be inspected separately
from plain text extraction and table/OCR behavior.

local_adaptation: Keep real-world layout gates limited to sanitized block
counts, page geometry, bbox samples, expected-marker hit booleans, and ordering
sanity checks. Do not commit raw page text, block text, screenshots, rendered
page images, local paths, or source PDFs.

boundary: PyMuPDF block/bbox metadata does not prove arbitrary-market layout
fidelity, natural reading-order correctness, rendered visual fidelity, or
robust PDF extraction.

rejection_condition: Reject any layout gate that treats `get_text("blocks")`,
`get_text("dict")`, or `sort=True` output as a broad visual-fidelity proof.

license_or_rights_note: Cite the official PyMuPDF documentation and respect
source publisher reuse policies before using external PDFs as fixtures.

### Unstructured Coordinates and Layout Metadata

source: https://docs.unstructured.io/open-source/core-functionality/partitioning

source_type: official_doc

pattern_to_borrow: Preserve document element metadata and coordinates as
separate evidence surfaces before downstream retrieval or generation.

local_adaptation: Use the pattern to keep coordinate/layout metadata visible in
NoiseProof proof packets while avoiding claims that coordinates alone prove
visual fidelity or reading order.

boundary: Referencing Unstructured does not mean NoiseProof integrates
Unstructured or has production layout parsing.

rejection_condition: Reject future parser work that collapses document text,
element type, coordinates, and final claim support into one opaque field.

license_or_rights_note: Respect upstream docs and license before integration.

### DocLayNet

source: https://arxiv.org/abs/2206.01062

source_type: paper

pattern_to_borrow: Treat document layout analysis as a labeled,
human-annotated document-understanding task rather than a side effect of text
extraction.

local_adaptation: Use DocLayNet as a reminder that real layout fidelity would
need labeled layout classes or human-reviewable visual evidence. The current
gate records only a tiny metadata sanity observation.

boundary: NoiseProof does not claim DocLayNet evaluation, trained layout models,
or benchmark performance.

rejection_condition: Reject any layout claim that does not disclose the absence
of labeled layout ground truth or rendered visual comparison.

license_or_rights_note: Cite the paper; do not reproduce benchmark content.

### Docling Technical Report

source: https://arxiv.org/abs/2408.09869

source_type: paper

pattern_to_borrow: Treat PDF/document conversion as a multi-stage system with
separate parsing, layout, table, OCR, metadata, and serialization decisions.

local_adaptation: Use Docling as a source pattern for the
`robust_pdf_extraction_generalization_gap_review_v0` capability matrix. The
review keeps current digital text, table, OCR, layout metadata, reading order,
and visual-fidelity claims separate.

boundary: NoiseProof does not claim Docling integration, Docling accuracy, or
production-grade document conversion.

rejection_condition: Reject robust-PDF wording that collapses separate document
conversion capabilities into one successful parser observation.

license_or_rights_note: Cite the paper and check upstream project licensing
before any future integration.

### PubLayNet

source: https://arxiv.org/abs/1908.07836

source_type: paper

pattern_to_borrow: Use large-scale document layout annotations and explicit
layout categories as a reminder that layout fidelity needs labeled or
reviewable ground truth.

local_adaptation: Use PubLayNet with DocLayNet to justify why one block/bbox
metadata sanity observation does not prove arbitrary-market layout fidelity.

boundary: NoiseProof does not claim PubLayNet evaluation, benchmark coverage,
or trained layout model performance.

rejection_condition: Reject any robust layout claim that lacks labeled layout
ground truth, rendered visual comparison, or reviewer-auditable layout checks.

license_or_rights_note: Cite the paper; do not reproduce benchmark artifacts.

### PubTables-1M

source: https://arxiv.org/abs/2110.00061

source_type: paper

pattern_to_borrow: Treat table extraction quality as a structure-recognition
problem with table-level ground truth, not as a raw table-count observation.

local_adaptation: Use PubTables-1M as a source pattern for the
`multi_publisher_modality_stratified_pdf_eval_v0` matrix cell that keeps table
row/cell counts limited until structure quality is evaluated.

boundary: NoiseProof does not claim PubTables-1M evaluation, table benchmark
quality, or table structure correctness.

rejection_condition: Reject any robust table claim that relies only on table
count, row count, or cell count without structure ground truth or reviewer
checks.

license_or_rights_note: Cite the paper; do not reproduce benchmark artifacts.

### TableBank

source: https://arxiv.org/abs/1903.01949

source_type: paper

pattern_to_borrow: Separate table detection and table recognition when
evaluating document table extraction.

local_adaptation: Use TableBank as a reminder that NoiseProof's current
sanitized table metrics are observations, not detection/recognition benchmark
evidence.

boundary: NoiseProof does not claim TableBank evaluation or benchmark
performance.

rejection_condition: Reject any table-extraction claim that does not identify
whether it is measuring detection, recognition, structure, or downstream
source support.

license_or_rights_note: Cite the paper; do not reproduce benchmark artifacts.

### OCR-D Evaluation

source: https://ocr-d.de/en/spec/ocrd_eval.html

source_type: standard

pattern_to_borrow: Treat OCR quality as an evaluable text-recognition surface
with error-rate-like measurements rather than a binary OCR-produced-text flag.

local_adaptation: Use OCR-D evaluation as a source pattern for keeping the NARA
OCR observation limited until future gates add expected-span or CER/WER-style
quality checks.

boundary: NoiseProof does not claim OCR-D compliance, OCR benchmark quality,
or production OCR accuracy.

rejection_condition: Reject any OCR claim that counts OCR text characters or
term hits as robust OCR quality without an explicit quality criterion.

license_or_rights_note: Cite the official OCR-D specification page.

### OCRmyPDF

source: https://ocrmypdf.readthedocs.io/en/latest/introduction.html

source_type: official_doc

pattern_to_borrow: Treat OCR for scanned PDFs as a distinct document-processing
stage that adds searchable text but carries accuracy, structure, and dependency
limits.

local_adaptation: Use OCRmyPDF as a reference pattern for OCR boundaries and
future adapter decisions. Do not claim OCRmyPDF integration in the current
PyMuPDF OCR gate.

boundary: Referencing OCRmyPDF documentation does not mean NoiseProof runs
OCRmyPDF, creates OCRed PDF/A files, or solves poor scan, handwriting, reading
order, or layout-fidelity problems.

rejection_condition: Reject any future OCR work that treats text-layer creation
as evidence of claim truth or layout fidelity.

license_or_rights_note: Reference official documentation only; check OCRmyPDF
license and dependency requirements before integration.

### NARA 9/11 Records and Permissions

source: https://www.archives.gov/research/9-11

source: https://www.archives.gov/global-pages/privacy.html

source_type: official_doc

pattern_to_borrow: Keep collection URL, record URL, source hash, and reuse
boundary visible when using a National Archives PDF as an external fixture.

local_adaptation: Use one NARA 9/11 Commission MFR PDF as a temporary
owner-runtime OCR observation and commit only sanitized metadata. Do not commit
the PDF binary, download cache, local paths, or raw OCR text.

boundary: A NARA source page and general policy URL do not guarantee every
record has the same rights status and do not prove robust PDF extraction.

rejection_condition: Reject any fixture gate that commits raw archival text or
binary source files without a stronger source policy review.

license_or_rights_note: Treat the policy URL as a rights boundary signal, not a
blanket public-domain guarantee for all archival material.

### EIA Content Reuse and Short-Term Energy Outlook

source: https://www.eia.gov/about/copyrights_reuse.php

source: https://www.eia.gov/outlooks/steo/

source_type: official_doc

pattern_to_borrow: Keep official reuse policy, publication page, release date,
download URL, hash, and non-claims visible when adding real-world fixtures.

local_adaptation: Use the EIA Short-Term Energy Outlook PDF as a
source-policy-reviewed cross-publisher real-world PDF observation, while
committing only sanitized metadata, hashes, diagnostics, and no PDF binary or
raw extracted text.

boundary: EIA source policy and one owner-runtime STEO observation do not prove
robust PDF extraction, table extraction, OCR, layout fidelity, or arbitrary
market PDF parsing reliability.

rejection_condition: Reject any EIA fixture gate that commits the external PDF
binary, commits raw extracted text, omits the reuse-policy source URL, or treats
one EIA observation as robust parsing evidence.

license_or_rights_note: EIA describes U.S. government publications on its site
as public domain and asks for acknowledgment; protected third-party materials,
logos, service marks, and photographs remain out of scope.

### BLS Copyright Information and Monthly Labor Review

source: https://www.bls.gov/opub/copyright-information.htm

source: https://www.bls.gov/opub/mlr/about.htm

source_type: official_doc

pattern_to_borrow: Keep BLS public-domain and credit-request boundaries visible
before using BLS reports, MLR articles, tables, charts, or figures as fixture
candidates.

local_adaptation: Use BLS and MLR PDF candidates for reading-order,
multi-column, and figure/image diagnostics in
`targeted_real_world_pdf_fixture_expansion_v0`, while committing only candidate
metadata, policy URLs, acceptance checks, stop conditions, and non-claims.

boundary: BLS/MLR source policy review does not prove robust PDF extraction,
visual fidelity, chart interpretation, table benchmark quality, or permission
to commit screenshots, figure crops, raw extracted text, or third-party
photographs.

rejection_condition: Reject any future BLS fixture gate that omits the source
policy URL, commits raw content from external PDFs, treats public-domain status
as a reason to skip citation/rights review, or upgrades planned candidates into
runtime evidence.

license_or_rights_note: BLS requests source credit and warns that some
photographs or illustrations may be copyrighted; review each fixture before
committing derived visual artifacts.

### Targeted Real-world PDF Fixture Expansion Planning

source: examples/pdf-extraction-quality/targeted-real-world-pdf-fixture-expansion-plan.json

source: docs/evaluation/targeted-real-world-pdf-fixture-expansion-report.md

source_type: runtime_evidence

pattern_to_borrow: Treat fixture expansion as a source-policy and evaluation
design gate before downloads, parsing, OCR, table extraction, layout review, or
visual review.

local_adaptation: Map the six missing cells from
`multi_publisher_modality_stratified_pdf_eval_v0` to candidate fixture routes,
source-policy URLs, acceptance checks, and stop conditions. The next gate may
download/hash selected candidates only after owner approval and must still avoid
committing external binaries, raw extracted text, raw OCR text, raw table rows,
page images, or screenshots.

boundary: The targeted fixture expansion plan is not runtime evidence, robust
PDF extraction evidence, arbitrary-market PDF parsing evidence, OCR quality
evidence, table extraction benchmark evidence, layout fidelity evidence,
external reviewer feedback, hosted deployment evidence, or product-complete.

rejection_condition: Reject any future gate that treats candidate coverage as
observed extraction coverage, downloads external PDFs without source-policy
metadata, or closes external reviewer validation with owner-authored text.

license_or_rights_note: Candidate URLs and source-policy URLs are metadata
only. Do not copy protected source text, screenshots, page images, or binary
PDFs into the repository without a stronger rights review.

### Source-policy PDF Download and Hash

source: examples/pdf-extraction-quality/source-policy-download-hash-observations.json

source: docs/evaluation/source-policy-download-hash-report.md

source_type: runtime_evidence

pattern_to_borrow: Convert source-policy-reviewed candidate routes into
temporary owner-runtime download/hash metadata before parser observations.

local_adaptation: Record HTTP status, content type, byte size, SHA-256 hash,
PDF magic-header result, blocked BLS HTTP 403 candidates, and external review
routes while committing no external PDF binaries, caches, raw text, screenshots,
or page images.

boundary: Source-policy download/hash metadata is not robust PDF extraction
evidence, arbitrary-market PDF parsing evidence, OCR quality evidence, table
extraction benchmark evidence, layout fidelity evidence, external reviewer
feedback, hosted deployment evidence, or product-complete.

rejection_condition: Reject any future parse gate that treats download/hash
metadata as extraction quality, commits external binaries or raw derived text,
or skips blocked-candidate reporting.

license_or_rights_note: The committed artifact is sanitized metadata only.
Temporary downloaded PDFs remain owner-runtime byproducts and must not be
committed without a separate rights review.

### Source-policy PDF Parse Observation

source: examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json

source: docs/evaluation/source-policy-pdf-parse-observation-report.md

source_type: runtime_evidence

pattern_to_borrow: Use PyMuPDF text/block metadata as an explicit parser
observation surface after source-policy download/hash, while preserving blocked
and external routes.

local_adaptation: Record page counts, extracted page counts, empty page counts,
native text character counts, text block counts, image block counts, and
no-native-text failure candidacy for selected candidates without committing raw
text or binaries.

boundary: Source-policy PDF parse observation metadata is not robust PDF
extraction evidence, arbitrary-market PDF parsing evidence, OCR quality
evidence, table extraction benchmark evidence, layout fidelity evidence,
rendered visual fidelity evidence, image/chart interpretation evidence,
external reviewer feedback, hosted deployment evidence, or product-complete.

rejection_condition: Reject any future gate that treats PyMuPDF metadata counts
as parser quality, commits raw extracted text, skips the no-native-text failure
candidate, or claims OCR/table/layout/visual behavior from this observation.

license_or_rights_note: The committed artifact is sanitized metadata only.
External PDFs, raw text, screenshots, page images, and derived visual material
must remain out of the repository without a separate rights review.

### Patent: US20260105079A1

source: https://patents.google.com/patent/US20260105079A1/en

source_type: patent

pattern_to_borrow: Preserve transparent linkage from retrieved semantic units
back to original text and source context.

local_adaptation: Future knowledge-graph, relation, or claim-expansion gates
must keep source-span provenance visible before generating reports.

boundary: Patent documents are inspiration and risk signals, not
implementation permission.

rejection_condition: Reject direct copying of protected claims, diagrams, or
specific implementation mechanics.

license_or_rights_note: Legal review required before implementing any
patent-claim-like design.

### Patent: US10628389B2

source: https://patents.google.com/patent/US10628389B2/en

source_type: patent

pattern_to_borrow: Add provenance verification around systems that were not
built with native provenance.

local_adaptation: Prefer lightweight proof packets, hashes, logs, and route
screens around existing local runs before invasive rewrites.

boundary: NoiseProof does not claim blockchain proof, cryptographic
non-repudiation, or patent implementation.

rejection_condition: Reject designs that introduce cryptographic ceremony
without improving inspectability for current reviewer needs.

license_or_rights_note: Legal review required before implementing any
patent-claim-like design.

## Use Rule

Before a future gate changes architecture, evaluation, parser behavior,
retrieval behavior, report behavior, observability, or public claims, add or
update source cards here.

If no source card supports a proposed direction, the gate must either:

```text
1. add a source card from a primary/original source, or
2. record why no existing source pattern is suitable, or
3. stop and report the missing source basis.
```
