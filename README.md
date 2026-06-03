# NoiseProof Agent

A noise-resilient data agent for messy market intelligence.

This project ingests messy documents and market data, evaluates chunking and retrieval strategies, detects contradictory evidence, and generates claim-bounded reports with citations. It is not a trading bot and does not provide buy/sell recommendations.

## External Reviewer Fast Path

Start with `docs/review/external-reader-proof-path.md`.

That file is the 5-minute repository-native path for reviewing what this project currently proves. It points to the README, portfolio index, failure-case workflow parent proof index, application-ready review, and Braincrew role map.

Boundary: this fast path is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## What This Is

NoiseProof Agent is a planned RAG/agent service for market intelligence work where the input data is inconsistent, noisy, and difficult to trust.

Current implemented capability groups:

- service skeleton, metadata persistence, PostgreSQL schema, migration runner, and CI
- document profiling, parser boundaries, chunk strategy comparison, and lexical retrieval
- collection planning, Evidence Ledger, Noise Gate, and claim-bounded report previews
- persisted evidence/gate/report records, trace lookup, filters, workflow parents, and derived lineage
- operations dashboard, failure-case persistence, manual workflow parent provenance, and proof-path documentation

Detailed phase history lives in `docs/GOAL.md`, `docs/application/portfolio-index.md`, and the phase-specific `docs/review/*` artifacts. This README now keeps the first-pass narrative focused on what the project currently demonstrates and what it still does not claim.
The product thesis:

> A good data agent does not start by answering well. It starts by preventing unsupported answers from passing.

## What This Is Not

NoiseProof Agent is not a trading bot.

This repository will not build:

- buy/sell signals
- automatic order execution
- return prediction
- stock recommendations
- financial advice
- real-time trading infrastructure
- reinforcement-learning trading logic
- a large-scale data lake
- a multi-tenant SaaS v1
- polished UI before evidence, logging, and evaluation work

Correct questions for this system:

- What happened?
- What evidence supports it?
- Which sources conflict?
- Which claims are weak?
- What data is missing?
- Why should this conclusion not be trusted yet?

Incorrect questions for this system:

- Should I buy?
- Should I sell?
- What is the target price?
- How much return will this make?

## Why This Exists

Market intelligence work often starts with mixed inputs: PDFs, CSVs, news pages, internal notes, reports, and stale or conflicting sources. LLMs can turn that mess into a confident answer too quickly.

NoiseProof Agent is designed to make unsupported answers harder to pass. The main artifact is not a fluent answer. The main artifact is an inspectable trail: source profiles, retrieval runs, evidence spans, contradictions, blocked claims, limitations, run logs, and failure cases.

## Target User Problem

The target user is a market researcher, analyst, founder, or operator who needs to read messy market material without accidentally treating weak evidence as a strong conclusion.

They need a system that can:

- ingest mixed document formats
- profile source quality
- compare chunk strategies
- retrieve source-linked evidence
- record which claims are supported, weak, contradicted, unsupported, or blocked
- show why a final report should or should not be trusted

## Planned Architecture

```text
Source Upload / URL Input
  -> Document Profiler
  -> Parser Selector
  -> Chunk Strategy Experiment
  -> Collection Plan Preview
  -> Indexing
  -> Retrieval
  -> Evidence Ledger
  -> Analysis Draft
  -> Critic / Noise Gate
  -> Claim-bounded Report
  -> Run Log / Failure Case
```

Implementation status:

Current status groups:

- documentation: product brief, architecture, ADRs, runbook, application package, and review artifacts
- service skeleton: FastAPI health, ops summary/dashboard, metadata routes, PostgreSQL schema, document chunk repository, migration runner, and CI
- ingestion/RAG boundaries: document profiling, parser adapters, chunk strategy comparison, lexical retrieval, semantic retrieval preview/persistence, and collection planning
- evidence/report boundaries: Evidence Ledger, Noise Gate, claim-bounded report previews, trace lookup, filters, workflow parents, lineage, and warning codes
- proof surfaces: DB/failure smoke artifacts, reviewer path/request/brief/link-map/root-guide, live issue/request-surface checks, feedback screening artifacts, and Braincrew application mapping

Detailed implementation history remains in the lower detailed Implementation Status section, `docs/GOAL.md`, and phase-specific `docs/review/*` artifacts.

Still planned or explicitly unclaimed near the top:

- web app and polished dashboard UI
- raw upload quarantine storage is implemented; robust PDF extraction is still unclaimed
- automatic upload-preview-to-chunk persistence wiring, embedding generation, vector search quality evidence, and LLM calls
- hosted deployment evidence
- automatic failure-case creation from workflow failures
- complete workflow failure causality
- free-form final report generation

## Implementation Status

Major implementation milestones:
- README proof-marker archive review v0: implemented
- README proof-marker archive extraction v0: implemented
- README proof-marker archive application refresh v0: implemented
- README proof-marker archive external path review v0: implemented
- README proof-marker archive external path refresh v0: implemented
- Application current-claim compression review v0: implemented
- Application current-claim compression v0: implemented
- Braincrew role-map runtime proof compression review v0: implemented
- Braincrew role-map runtime proof compression v0: implemented
- Application proof surface final scan review v0: implemented
- Application-ready summary compression v0: implemented
- External-reader final proof-path dry-read review v0: implemented
- External-reader proof path next-gate refresh v0: implemented
- Application package final consistency review v0: implemented
- Portfolio site handoff review v0: implemented
- Portfolio site proof artifact route verification v0: implemented
- Demo transcript capture v0: implemented
- Local browser screenshot walkthrough v0: implemented
- External review request packet v0: implemented
- External feedback intake criteria v0: implemented
- External reviewer brief v0: implemented
- External reviewer live proof route refresh v0: implemented
- External reviewer link map v0: implemented
- External review root guide v0: implemented
- External review issue body encoding verification v0: implemented
- External review issue body root-guide verification v0: implemented
- External review issue body link-map verification v0: implemented
- External review issue template link-map refresh v0: implemented
- External review issue label verification v0: implemented
- External review owner request comment verification v0: implemented
- External reviewer outreach packet v0: implemented
- External feedback qualification preview v0: implemented
- External feedback screening CLI v0: implemented
- External feedback screening workflow v0: implemented
- External feedback screening workflow verification v0: implemented
- Owner-approved product continuation decision v0: implemented
- File upload preview v0: implemented
- Uploaded file chunk preview v0: implemented
- Uploaded file retrieval preview v0: implemented
- Uploaded file Evidence Ledger preview v0: implemented
- Uploaded file Noise Gate preview v0: implemented
- Uploaded file report preview v0: implemented
- Uploaded file failure-case draft preview v0: implemented
- Uploaded file failure-case manual handoff smoke v0: implemented
- Uploaded file proof path index refresh v0: implemented
- Uploaded file runtime smoke packet v0: implemented
- Persisted uploaded file intake review v0: implemented
- Uploaded file intake manifest preview v0: implemented
- Uploaded file intake manifest runtime smoke v0: implemented
- Uploaded file intake manifest application refresh v0: implemented
- Uploaded file intake manifest persistence schema v0: implemented
- Uploaded file intake manifest persistence repository review v0: implemented
- Uploaded file intake manifest persistence repository v0: implemented
- Uploaded file intake manifest persistence endpoint review v0: implemented
- Uploaded file intake manifest persistence endpoint v0: implemented
- Uploaded file intake manifest persistence runtime smoke v0: implemented
- Uploaded file intake manifest persistence application refresh v0: implemented
- Uploaded file parsed document persistence v0: implemented
- Uploaded file parsed document persistence runtime smoke v0: implemented
- Uploaded file parsed document persistence application refresh v0: implemented
- External reviewer parsed-document persistence request refresh v0: implemented
- External reviewer parsed-document persistence issue-body refresh v0: implemented
- Uploaded file chunk persistence review v0: implemented
- Uploaded file chunk persistence schema v0: implemented
- Uploaded file chunk persistence repository v0: implemented
- Uploaded file chunk persistence runtime smoke v0: implemented
- Uploaded file chunk persistence application refresh v0: implemented
- Uploaded file retrieval persistence application refresh v0: implemented
- Embedding endpoint runtime smoke v0: implemented
- Semantic retrieval persistence endpoint v0: implemented
- Semantic retrieval persistence runtime smoke v0: implemented
- Semantic retrieval persistence application refresh v0: implemented

For exhaustive phase history, use `docs/GOAL.md`.

Not implemented yet:

- robust PDF extraction
- download endpoint for stored raw uploads
- malware scanning for stored raw uploads
- automatic upload-preview-to-chunk persistence wiring
- autonomous workflow execution endpoints
- automatic failure-case persistence from workflow failures
- embedding generation and vector search quality evidence
- full distributed tracing or hosted observability

Uploaded raw file storage v0: implemented. Boundary: quarantined PostgreSQL BYTEA storage with metadata-only responses; no download endpoint, no malware scanning, and no robust PDF extraction.

Uploaded raw file storage runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence only; not hosted deployment evidence, not external reviewer feedback, and not malware scanning.

Uploaded raw file storage application refresh v0: implemented. Boundary: the local runtime proof is now surfaced in application-facing docs; not hosted deployment evidence, not external reviewer feedback, and not product-complete.

External reviewer raw file storage request refresh v0: implemented. Boundary: reviewer request surfaces now point to the uploaded raw file storage proof; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External review issue body raw file storage refresh v0: implemented. Boundary: issue #1 now points to the uploaded raw file storage proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External feedback current-state raw file storage issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

Uploaded raw file storage safety review v0: implemented. Boundary: source-first review keeps raw uploads quarantine-only and selects scan result schema review before any download endpoint; not malware scanning, not a download endpoint, and not hosted deployment evidence.

Uploaded raw file scan result schema review v0: implemented. Boundary: review-only decision to use future `raw_file_scan_results` linked to `uploaded_raw_files(id)` before any scanner or download endpoint; not malware scanning, not runtime evidence, and not product-complete.

Uploaded raw file scan result schema v0: implemented. Boundary: schema-only `raw_file_scan_results` table linked to `uploaded_raw_files(id)` for future scan attempts; not malware scanning, not scanner execution, not ClamAV integration, not a download endpoint, and not runtime evidence.

Uploaded raw file scan result repository review v0: implemented. Boundary: review-only selection of `RawFileScanResultCreate`, `create_raw_file_scan_result`, and `list_raw_file_scan_results`; no repository code, endpoint, scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result repository v0: implemented. Boundary: repository-only caller-provided scan result persistence through `RawFileScanResultCreate`, `create_raw_file_scan_result`, and `list_raw_file_scan_results`; no endpoint, scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result endpoint review v0: implemented. Boundary: review-only selection of metadata-only `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`; no endpoint code, scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result endpoint v0: implemented. Boundary: metadata-only caller-provided scan result `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`; no scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result endpoint runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof for metadata-only scan result POST/GET and path/body mismatch 400; not scanner execution, not ClamAV integration, not a download endpoint, and not hosted deployment evidence.

External reviewer scan-result endpoint request refresh v0: implemented. Boundary: reviewer request surfaces now point to the uploaded raw file scan result endpoint proof; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External review issue body scan-result endpoint refresh v0: implemented. Boundary: issue #1 now points to the uploaded raw file scan result endpoint proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External feedback current-state scan-result endpoint issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

Uploaded raw file scanner adapter review v0: implemented. Boundary: review-only selection of `ScannerAdapter`, `ScanAdapterRequest`, and `ScanAdapterResult` before ClamAV or scanner execution; missing scanners and timeouts must map to `scan_error`, not clean.

Uploaded raw file scanner adapter v0: implemented. Boundary: generic scanner adapter types plus unavailable/timeout failure mapping only; not ClamAV integration, not malware scanning, not scanner process execution, and not a download endpoint.

Uploaded raw file ClamAV adapter review v0: implemented. Boundary: review-only selection of `ClamAvScannerAdapter` with `clamscan first`, `clamdscan later`, and conservative subprocess failure mapping; not malware scanning or scanner execution.

Uploaded raw file ClamAV adapter v0: implemented. Boundary: `ClamAvScannerAdapter` maps missing binary, missing temporary path, timeout, unknown return code, clean output, and FOUND output without installing or runtime-verifying ClamAV.

Uploaded raw file ClamAV adapter runtime smoke v0: implemented. Boundary: deterministic command smoke exercises missing/clean/infected/timeout/error mappings through fake runners; not real ClamAV execution, not signature database evidence, not endpoint behavior, and not malware scanning evidence.

External reviewer ClamAV adapter runtime smoke request refresh v0: implemented. Boundary: reviewer request surfaces now point to the deterministic ClamAV adapter smoke proof; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, not signature database evidence, and not malware scanning.

External review issue body ClamAV adapter runtime smoke refresh v0: implemented. Boundary: issue #1 now points to the deterministic ClamAV adapter smoke proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, not signature database evidence, and not malware scanning.

External feedback current-state ClamAV adapter runtime smoke issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, not signature database evidence, and not malware scanning.

Uploaded raw file scan execution review v0: implemented. Boundary: source-first review selects a future explicit `POST /documents/upload-raw-files/{raw_file_id}/scan` endpoint and keeps scan execution separate from caller-provided scan result metadata; review-only, not endpoint code, not real ClamAV execution, and not malware scanning evidence.

Uploaded raw file scan execution endpoint v0: implemented. Boundary: explicit `POST /documents/upload-raw-files/{raw_file_id}/scan` writes stored raw bytes to a service-generated temporary scan file, executes the configured scanner adapter, persists metadata-only scan results, and defaults to `scanner-unavailable` / `scan_error`; not real ClamAV execution, not malware scanning evidence, not hosted evidence, and not a download endpoint.

Uploaded raw file scan execution endpoint runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof for upload, explicit scan execution, and scan-result listing with default `scanner-unavailable` / `scan_error`; not real ClamAV execution, not malware scanning evidence, not hosted evidence, and not external reviewer feedback.

External reviewer scan execution endpoint request refresh v0: implemented. Boundary: reviewer request surfaces now point to the scan execution endpoint runtime smoke proof; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, and not malware scanning.

External review issue body scan execution endpoint refresh v0: implemented. Boundary: issue #1 now points to the scan execution endpoint runtime proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, and not malware scanning.

External feedback current-state scan execution endpoint issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, and not malware scanning.

Uploaded raw file ClamAV runtime verification review v0: implemented. Boundary: review-only selection of a future Dockerized ClamAV + EICAR smoke before changing API defaults or claiming real scanner evidence; not runtime evidence, not malware scanning evidence, and not endpoint verification with real ClamAV.

Dockerized ClamAV EICAR runtime smoke v0: implemented. Boundary: local Dockerized `clamav/clamav:stable` detected container-internal EICAR with `Eicar-Test-Signature`, recording image digest and signature DB version; real ClamAV runtime verified for EICAR only, not production malware scanning evidence, not API endpoint verification with real ClamAV, and not hosted evidence.

ClamAV API integration boundary review v0: implemented. Boundary: review-only decision not to wire Docker CLI execution into the API endpoint and not to change the default scanner yet; selects a future ClamAV service boundary review before endpoint integration.

ClamAV service boundary review v0: implemented. Boundary: review-only decision to design a dedicated ClamAV service/daemon boundary before compose or API code; no clamd exposure, no endpoint integration, no malware scanning evidence.

ClamAV compose service review v0: implemented. Boundary: review-only decision to design a future internal-only `clamav` Docker Compose service before editing compose or API code; no compose code, no clamd runtime verification, no endpoint integration, and no malware scanning evidence.

ClamAV compose service implementation v0: implemented. Boundary: optional internal-only `clamav` Docker Compose service behind the `scanner` profile with no host port publishing and a signature DB volume; not clamd runtime verification, not API endpoint integration, and not malware scanning evidence.

ClamAV compose service config verification v0: implemented. Boundary: `docker compose --profile scanner config` rendered the optional `clamav` service with `profiles: scanner`, `expose: 3310`, no clamd host port publishing, and `clamdscan --ping=1`; not clamd runtime verification, not API endpoint integration, and not malware scanning evidence.

ClamAV compose service runtime smoke v0: implemented. Boundary: local Docker Compose `clamav` service reached healthy state, returned `PONG` to `clamdscan --ping=1`, and exposed no host port bindings; real ClamAV runtime verified for daemon availability only, not API endpoint integration and not malware scanning evidence.

ClamAV compose EICAR runtime smoke v0: implemented. Boundary: local Docker Compose `clamav` service detected container-internal EICAR as `Eicar-Test-Signature`, deleted the temporary file, and kept the payload out of the repo; not API endpoint integration and not production malware scanning evidence.

ClamAV service scanner adapter review v0: implemented. Boundary: review-only decision to add a future `ClamdScannerAdapter` that uses clamd `INSTREAM` over the internal Docker network instead of API temp paths or `clamdscan` subprocesses; no adapter code and no API endpoint integration.

ClamAV service scanner adapter v0: implemented. Boundary: `ClamdScannerAdapter` streams bytes with clamd `INSTREAM` and maps clean, infected, timeout, unavailable, and unexpected responses through unit tests; no API endpoint integration, no default scanner switch, and no real endpoint proof.

ClamAV API service network boundary review v0: implemented. Boundary: review-only decision that host-local FastAPI must not reach ClamAV by publishing unauthenticated clamd TCP; API service integration requires the API runtime to join the same internal Docker network as `clamav`.

ClamAV API compose service review v0: implemented. Boundary: review-only decision to add a future profiled `api` Compose service that joins the same network as `clamav` and uses `CLAMD_HOST=clamav`, while keeping scanner opt-in explicit and clamd host ports unpublished.

ClamAV API compose service implementation v0: implemented. Boundary: added `apps/api/Dockerfile` and a profiled `api` Compose service with `DATABASE_URL` pointing at `db`, `CLAMD_HOST=clamav`, and `NOISEPROOF_SCANNER=unavailable`; not default scanner switch and not endpoint runtime proof.

ClamAV API compose service config verification v0: implemented. Boundary: `docker compose --profile api --profile scanner config` renders the profiled `api` service with `DATABASE_URL` to `db`, `CLAMD_HOST=clamav`, `NOISEPROOF_SCANNER=unavailable`, and no ClamAV host port publishing; not API runtime smoke or endpoint proof.

ClamAV API compose service runtime smoke v0: implemented. Boundary: `docker compose --profile api up -d api` starts the profiled API service and `GET /health` returns `{"status":"ok"}` while `NOISEPROOF_SCANNER=unavailable`; not scan endpoint proof, not endpoint runtime proof with real ClamAV, and not production malware scanning evidence.

ClamAV API endpoint scanner opt-in review v0: implemented. Boundary: review-only decision to add a future explicit `NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter` path for `POST /documents/upload-raw-files/{raw_file_id}/scan`; default remains `NOISEPROOF_SCANNER=unavailable`, not endpoint runtime proof with real ClamAV, and not malware scanning evidence.

ClamAV API endpoint scanner opt-in implementation v0: implemented. Boundary: `get_scanner_adapter()` now supports explicit `NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter(host=CLAMD_HOST, port=CLAMD_PORT)` while preserving `NOISEPROOF_SCANNER=clamav -> ClamAvScannerAdapter` and keeping the default unavailable; not endpoint runtime proof with real ClamAV and not malware scanning evidence.

ClamAV API endpoint scanner opt-in runtime smoke v0: implemented. Boundary: local Docker Compose API ran with `NOISEPROOF_SCANNER=clamd` and `POST /documents/upload-raw-files/{raw_file_id}/scan` returned `scanner_name=clamav-clamd`, `scan_status=completed`, `scan_verdict=clean`, and `clamd_response=stream: OK`; clean-file endpoint proof only, not malware detection proof and not EICAR-through-API proof.

ClamAV API endpoint malicious-detection runtime review v0: implemented. Boundary: review-only safety gate for a future EICAR-through-API smoke; clean-file endpoint proof exists and `malicious_detection_verified: false` remains current. Do not store the EICAR payload in the repository, do not bypass OS security controls, and do not claim production malware scanning evidence.

ClamAV API endpoint malicious-detection runtime blocked v0: implemented. Boundary: EICAR-through-API runtime smoke was not completed because the host command was rejected before endpoint request; `payload_committed_to_repo: false`, `malicious_detection_verified: false`, and this is not malware detection proof.

ClamAV API endpoint malicious-detection test harness review v0: implemented. Boundary: review-only plan for a future opt-in harness using an owner-provided runtime-only test signature via `NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1` and `NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT`; `payload_committed_to_repo: false`, no encoded payload is stored, and this is not malware detection proof.

ClamAV API endpoint malicious-detection test harness v0: implemented. Boundary: `app.services.clamav_api_malicious_detection_harness` adds a disabled-by-default opt-in command that returns `not_configured` without API calls unless `NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1` and `NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT` are provided; fake-client tests cover `verified_infected` and `blocked_by_environment`, but this is not malware detection proof.

ClamAV API endpoint malicious-detection harness default smoke v0: implemented. Boundary: default command execution returned `harness_status=not_configured`, `api_calls_attempted=false`, `malicious_detection_verified=false`, `payload_committed_to_repo=false`, and `raw_payload_logged=false`; this is safe no-op evidence, not malware detection proof.

ClamAV API endpoint malicious-detection stdin input review v0: implemented. Boundary: review-only decision to add a stdin-only owner input path before retrying the owner-provided runtime smoke; `NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT` remains supported, but no test signature is supplied here, `payload_committed_to_repo=false`, `raw_payload_logged=false`, and this is not malware detection proof.

ClamAV API endpoint malicious-detection stdin input harness v0: implemented. Boundary: `--signature-stdin` lets the opt-in harness accept owner-provided runtime input through stdin, reports `input_source=stdin`, keeps `payload_committed_to_repo=false` and `raw_payload_logged=false`, and has fake-client coverage only; this is not malware detection proof.

ClamAV API endpoint malicious-detection stdin default smoke v0: implemented. Boundary: `uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin` with empty stdin returned `harness_status=not_configured`, `input_source=stdin`, `api_calls_attempted=false`, `malicious_detection_verified=false`, `payload_committed_to_repo=false`, and `raw_payload_logged=false`; owner-provided runtime smoke remains pending.

ClamAV API endpoint malicious-detection owner-runtime preflight v0: implemented. Boundary: local Compose preflight shows API up, `GET /health -> 200`, API scanner env `NOISEPROOF_SCANNER=clamd`, `CLAMD_HOST=clamav`, `CLAMD_PORT=3310`, and clamd `PING -> PONG`; owner-provided test signature is absent, no scan endpoint request was made, and this is not malware detection proof.

ClamAV API endpoint malicious-detection owner-input guard v0: implemented. Boundary: `--require-owner-input` returns `exit_code=4`, `required_owner_input_missing=true`, `api_calls_attempted=false`, and `malicious_detection_verified=false` when stdin owner input is absent; owner-provided runtime smoke remains pending and this is not malware detection proof.

ClamAV API endpoint malicious-detection owner runtime smoke packet v0: implemented. Boundary: `--print-owner-runtime-smoke-packet` emits a no-payload packet with `packet_status=ready_for_owner_input`, the stdin command template, success criteria `scanner_name=clamav-clamd`, `scan_status=completed`, `scan_verdict=infected`, `matched_signature=Eicar-Test-Signature`, and no API/scan call; owner-provided runtime smoke remains pending.

ClamAV API endpoint malicious-detection owner runtime smoke validator v0: implemented. Boundary: `--validate-owner-runtime-smoke-report` validates future owner-provided runtime smoke metadata for `verified_infected`, stdin input, no committed/logged payload, and exact `clamav-clamd` infected summary; it does not include a payload, call the API, upload raw bytes, call the scan endpoint, or prove production malware scanning.

ClamAV API endpoint malicious-detection owner runtime smoke validator leak-field hardening v0: implemented. Boundary: the validator now rejects otherwise successful owner runtime smoke JSON reports that include payload-bearing fields such as `test_signature_text` or `encoded_payload`; it reports forbidden field paths only and does not echo values.

ClamAV API endpoint malicious-detection owner runtime smoke report contract v0: implemented. Boundary: `--print-owner-runtime-smoke-report-contract` emits the no-payload accepted/rejected metadata contract for future owner-provided runtime smoke reports; it does not call the API, upload raw bytes, or call the scan endpoint.

ClamAV API endpoint malicious-detection owner runtime smoke report schema v0: implemented. Boundary: `--print-owner-runtime-smoke-report-schema` emits a JSON Schema-shaped accepted report surface using Draft 2020-12 metadata; the Python validator remains authoritative and this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke validator strict-shape alignment v0: implemented. Boundary: the validator now rejects unknown top-level and `scan_result_summary` fields such as `template_status` and `scan_result_summary.extra_note`, aligning runtime validation with the schema's `additionalProperties: false` contract.

ClamAV API endpoint malicious-detection owner runtime smoke cross-shell packet v0: implemented. Boundary: `--print-owner-runtime-smoke-packet` now includes POSIX and PowerShell command templates plus `runtime_report_handling` for writing reports outside the repo and validating metadata only; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke report path guard v0: implemented. Boundary: `--validate-owner-runtime-smoke-report` now rejects report JSON paths that resolve inside the repository with `report_path_boundary.report_path_allowed=false`; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke output path guard v0: implemented. Boundary: actual `--signature-stdin --require-owner-input --output` smoke attempts now reject output paths inside the repository with `harness_status=output_path_rejected` before API calls; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke validator handoff report v0: implemented. Boundary: actual `--signature-stdin --require-owner-input --owner-runtime-smoke-report --output` smoke attempts can write a strict validator-accepted metadata shape outside the repository; the handoff report excludes `phase_marker` and `payload_length_bytes`, does not include a test signature payload, and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke command-template handoff alignment v0: implemented. Boundary: the packet's singular `command_template` now matches the validator handoff report path by including `--owner-runtime-smoke-report --output <runtime-report-path-outside-repo>`; this updates no-payload command metadata only and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke post-run validation command v0: implemented. Boundary: the no-payload packet now includes `post_run_validation_command` for `--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>` so future owner-provided runtime smoke reports have an explicit metadata validator step; this does not run the smoke and is not endpoint malicious-detection runtime proof.

ci node24 actions runtime opt-in v0: implemented. Boundary: `.github/workflows/ci.yml` and `.github/workflows/external-feedback-screen.yml` set `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"` after the remote run warned that Node.js 20 actions are deprecated; this is workflow runtime compatibility only, not product runtime evidence.

ci node24 actions runtime remote verification v0: implemented. Boundary: remote runs `26870586255` (`CI`) and `26870586219` (`External Feedback Screen`) succeeded on head `c3c6908`; the annotation is still present as a forced Node.js 24 runtime warning, so this is compatibility evidence only, not product runtime evidence.


## Planned Agent Workflow

NoiseProof Agent will use five explicit roles before introducing any complex multi-agent abstraction:

1. Ingestion Agent: parse and profile inputs
2. Retrieval Agent: compare chunk strategies and retrieve source-linked evidence
3. Analysis Agent: draft claims from retrieved evidence
4. Critic Agent: block unsupported claims, contradictions, overconfident language, missing limitations, and trading-advice drift
5. Report Agent: generate a claim-bounded report with citations and next data needed

Each planned stage must log its input and output.

Auto Trace behavior records preview endpoint metadata in `agent_runs.trace_json` using the current workflow version. This is not full workflow tracing or distributed observability.

## Evidence Ledger

The Evidence Ledger is the control surface between retrieval and final answer generation. Phase 6 implements a deterministic preview boundary. Phase 12 persists generated ledger entries so operations views can count unsupported and contradicted claims. Phase 202 adds a retrieval-run-linked handoff endpoint that reads a persisted retrieval run's `metadata_json.candidate_chunk_ids`, reloads the referenced `document_chunks`, and stores Evidence Ledger rows with `retrieval_run_id`.

Each ledger entry records:

- claim
- source id
- source type
- source date
- evidence span
- confidence
- limitation
- contradicting source ids
- status

Allowed status values:

```text
supported
weakly_supported
contradicted
unsupported
blocked
```

The system should generate the ledger before generating a final report. Current persistence is v0, and retrieval-run-linked rows can now carry `retrieval_run_id` when created through `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`.

## Noise Gate

The Noise Gate is the reviewer before a final response is allowed through. Phase 7 implements a deterministic preview boundary. Phase 13 persists gate decisions so blocked and revision-needed outputs remain inspectable. Phase 204 adds a retrieval-run-linked handoff endpoint that requires persisted Evidence Ledger rows for the same retrieval run before creating a Noise Gate record.

It checks:

- Does every strong claim have evidence?
- Are there at least two sources for high-confidence claims?
- Is source recency visible?
- Are contradictions surfaced?
- Are quantitative and qualitative signals separated?
- Is the answer drifting into trading advice?
- Are limitations explicit?

The current preview returns `pass`, `needs_revision`, or `blocked`. `POST /noise-gates` stores the decision and checks. It does not generate the final report.

If the gate fails, the system should return:

```text
현재 근거만으로는 결론을 내릴 수 없습니다. 가능한 해석은 다음과 같고, 추가로 확인해야 할 데이터는 다음과 같습니다.
```

## Evaluation

Evaluation is organized around inspectability, not polished demo output.

The Phase 10 evaluation package tracks:

- sample dataset description
- retrieval hit rate
- citation coverage
- missing evidence count
- unsupported claim examples
- contradiction examples
- failure cases and next fixes

See:

- `docs/evaluation/eval-plan.md`
- `docs/evaluation/retrieval-eval-report.md`
- `docs/evaluation/failure-cases.md`

The project does not claim model quality, semantic retrieval quality, or answer quality success.

Semantic retrieval quality report regeneration:

- command: `uv run python -m app.services.semantic_quality_report_command`
- proof: `docs/review/semantic-retrieval-quality-report-regeneration-command.md`
- failure boundary: `docs/review/semantic-retrieval-quality-report-regeneration-failure-boundary.md`
- check mode: `docs/review/semantic-retrieval-quality-report-check-mode.md`
- CI staleness check: `docs/review/semantic-retrieval-quality-report-ci-check.md`

This provides byte-for-byte regeneration and CI staleness detection for the toy semantic retrieval quality report. It is not vector search quality evidence, not a benchmark result, and not a model comparison.

## Failure Cases

Failure cases are first-class artifacts. The planned system will record:

- failed questions
- retrieval misses
- unsupported claims
- contradicted claims
- trading-advice drift
- missing source recency
- parser failures
- root cause and next action

## Local Setup

The current local stack defines a PostgreSQL + pgvector database service and a FastAPI skeleton.

```bash
cp .env.example .env
docker compose up -d db
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Smoke checks:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl http://localhost:8000/ops/dashboard
curl -X POST http://localhost:8000/documents/profile \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"text\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/chunk-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Market\nRevenue grew 12% in 2026.\n\n## Risks\nCosts rose 7%.\",\"max_characters\":80,\"overlap\":10}"
curl -X POST http://localhost:8000/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"heading-aware\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"# Demand\nEnterprise demand grew 12% in 2026.\"}]}"
curl -X POST http://localhost:8000/collection-plans/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Did this company's AI narrative become materially stronger?\"}"
curl -X POST http://localhost:8000/evidence-ledgers/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"retrieval_results\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"chunk_strategy\":\"heading-aware\",\"chunk_index\":0,\"text\":\"Enterprise demand grew 12% in 2026.\",\"score\":0.75,\"matched_terms\":[\"demand\",\"enterprise\",\"growth\"],\"metadata\":{\"source_date\":\"2026-05-28\"}}]}"
curl -X POST http://localhost:8000/evidence-ledgers \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"retrieval_results\":[]}"
curl http://localhost:8000/evidence-ledgers
curl -X POST http://localhost:8000/retrieval-runs/<uuid>/evidence-ledger
curl -X POST http://localhost:8000/retrieval-runs/<uuid>/noise-gate
curl -X POST http://localhost:8000/retrieval-runs/<uuid>/report
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/noise-gates \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"evidence_entries\":[{\"claim\":\"Should I buy this company\",\"source_id\":null,\"source_type\":null,\"source_date\":null,\"evidence_span\":\"\",\"confidence\":\"none\",\"limitation\":\"Question drifts into buy/sell or financial-advice intent.\",\"contradicting_source_ids\":[],\"status\":\"blocked\",\"matched_terms\":[],\"role\":\"user_intent_check\"}],\"draft_claims\":[\"Should I buy this company?\"]}"
curl http://localhost:8000/noise-gates
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/workflow-runs/execute-preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"fixed-window\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"Enterprise segment demand growth was 12 percent in 2026.\"}],\"draft_claims\":[\"Enterprise segment demand growth was supported by current retrieved evidence.\"]}"
curl http://localhost:8000/workflow-runs/<uuid>
curl http://localhost:8000/workflow-runs/<uuid>/lineage
curl http://localhost:8000/agent-runs
```

Reviewer-facing public proof route:

```text
docs/review/external-reviewer-live-proof-route-refresh.md
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

This route helps external reviewers find the latest public proof surface, reviewer brief, and issue #1. It is not external reviewer feedback, not hosted deployment evidence for NoiseProof Agent, and not customer validation.

## Demo Flow

Planned demo flow after implementation:

1. Upload or reference messy PDF, CSV, URL/HTML, and markdown memo inputs.
2. Generate a document profile for each input.
3. Compare fixed-window, heading-aware, and row-aware chunk strategies.
4. Create a Collection Plan Preview for a market-intelligence question.
5. Run retrieval for source-linked candidate chunks.
6. Generate an Evidence Ledger Preview before the answer.
7. Ask the Critic Agent to block unsupported claims and surface contradictions.
8. Generate a claim-bounded report preview with citations and limitations.
9. Show the run log and failure case record.

## What I Would Improve Next

The current next evidence gate remains external reviewer feedback v0.

The project already has a reviewer request packet, intake criteria, reviewer brief, direct link map, root review guide, live issue-body encoding verification, live issue-body root-guide verification, live issue-body link-map verification, issue-template link-map refresh, issue-label verification, owner request comment rejection verification, outreach packet, screening CLI, screening workflow, and remote pending artifact verification. Those artifacts prepare the path, but they do not prove that an outside reviewer inspected the work.

The owner approved continuing implementation while that external-review gate stays pending. That approval is recorded in `docs/review/owner-approved-product-continuation-decision.md`; it is not external reviewer feedback, customer validation, Braincrew acceptance, hosted deployment evidence, or production readiness.

File upload preview v0 through uploaded file retrieval persistence application refresh v0 are now implemented as bounded upload proof steps. The current next evidence gate remains `external reviewer feedback v0`; external reviewer feedback is still pending.

The latest current-state screen after the uploaded-file chunk persistence issue-body refresh is recorded in `docs/review/external-feedback-current-state-chunk-issue-verification.md`. It observes `comment_count: 1`, `candidate_count: 0`, and `draft_count: 0`; the only public comment is owner-authored and does not close `external reviewer feedback v0`.

The explicit upload-to-chunks handoff endpoint is now implemented and recorded in `docs/review/uploaded-file-chunk-persistence-handoff-endpoint.md`: `POST /documents/upload-chunks` creates document metadata plus derived chunk rows while keeping the existing upload chunk preview preview-only. Local runtime evidence and application-facing proof refresh for that endpoint are recorded in `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md` and `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md`.

The document-scoped retrieval persistence endpoint is now implemented and recorded in `docs/review/uploaded-file-retrieval-persistence-endpoint.md`: `POST /documents/{document_id}/retrieval-runs` reads existing `document_chunks`, persists one row in the existing `retrieval_runs` table, and stores `metadata_json.candidate_chunk_ids` without adding embeddings, semantic retrieval, Evidence Ledger generation, or financial advice behavior. Local runtime evidence is recorded in `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`, and the application-facing refresh is recorded in `docs/review/uploaded-file-retrieval-persistence-application-refresh.md`.

The retrieval-run-linked Evidence Ledger endpoint is implemented as `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`: it uses an existing persisted `retrieval_runs` row and its `metadata_json.candidate_chunk_ids` to reload `document_chunks`, generate deterministic Evidence Ledger entries, and persist those rows with `retrieval_run_id`. Local Docker runtime evidence is recorded in `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`. It does not call an LLM, create embeddings, perform semantic retrieval, generate a Noise Gate or report, or provide financial advice.

The retrieval-run-linked Noise Gate endpoint is implemented as `POST /retrieval-runs/{retrieval_run_id}/noise-gate`: it requires existing Evidence Ledger rows linked to that retrieval run, persists a Noise Gate record, and records `stage_input_manifest.input_evidence_ledger_entry_ids`. Local Docker runtime evidence is recorded in `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`. It does not call an LLM, create embeddings, perform semantic retrieval, generate a report, create failure cases, or provide financial advice.

The retrieval-run-linked Report endpoint is implemented as `POST /retrieval-runs/{retrieval_run_id}/report`: it requires existing Evidence Ledger rows and a linked Noise Gate record, persists a Report record, and records `stage_input_manifest.input_evidence_ledger_entry_ids` plus `stage_input_manifest.input_noise_gate_record_id`. Local Docker runtime evidence is recorded in `docs/review/retrieval-run-linked-report-runtime-smoke.md`. It does not call an LLM, create embeddings, perform semantic retrieval, create failure cases, or provide financial advice; when the gate requires revision, the report body remains bounded instead of becoming a free-form answer.

## Braincrew Role Alignment

Primary hiring target:

```text
Braincrew Forward Deployed Engineer
```

Secondary / long-term target:

```text
Braincrew Product Engineer
```

NoiseProof Agent is designed to produce evidence for customer problem definition, RAG/agent workflow design, full-stack service implementation, logging, monitoring, evaluation, deployment readiness, and technical decision documentation.

This repository is the implementation artifact. The portfolio blog is the strategy, explanation, and proof surface.
