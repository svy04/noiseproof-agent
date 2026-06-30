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
