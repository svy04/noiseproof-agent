# Uploaded Raw File ClamAV Adapter Review

Status: review-only source-first adapter decision.

Phase marker: uploaded raw file ClamAV adapter review v0.

## Purpose

NoiseProof now has generic scanner adapter types and failure mapping.

This review decides the smallest ClamAV-specific adapter boundary before writing any ClamAV execution code.

It does not add scanner execution.

It does not install ClamAV.

It does not claim malware scanning.

## Source-first Inputs

Primary references:

- ClamAV Scanning: `https://docs.clamav.net/manual/Usage/Scanning.html`
- Python subprocess: `https://docs.python.org/3/library/subprocess.html`
- OWASP File Upload Cheat Sheet: `https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html`

Relevant observations:

- ClamAV Scanning documents both direct `clamscan` usage and daemon-backed `clamdscan` usage.
- Daemon-backed scanning adds socket and service-operation decisions, so use `clamdscan later`.
- Python subprocess supports timeout and return-code inspection, so timeout and unknown return codes must become scan errors.
- OWASP file upload guidance treats upload safety as defense in depth, not just antivirus.
- ClamAV output and return codes must never become a silent clean verdict when the scanner is missing, times out, or returns an unknown shape.

## Decision

For the first ClamAV-specific implementation:

```text
ClamAvScannerAdapter
clamscan first
clamdscan later
```

The adapter should use the existing generic scanner boundary:

```text
ScanAdapterRequest
ScanAdapterResult
ScannerAdapter
build_scan_error_result
```

Selected process boundary:

```text
shutil.which("clamscan")
subprocess.run([...], capture_output=True, text=True, timeout=request.scanner_timeout_seconds)
temporary_scan_path required
```

Required conservative mappings:

```text
missing clamscan -> failed / scan_error
timeout -> failed / scan_error
unknown return code -> failed / scan_error
unparseable output -> failed / scan_error
matched malware signature -> completed / infected
no match -> completed / clean
```

## Explicit Safety Rules

```text
do not use --remove
do not use --move
do not open daemon TCP sockets
do not trust original_filename
do not return temporary_scan_path
do not add a download endpoint
```

ClamAV scan output may later include matched signatures, but only as scan evidence.

It is not permission to serve the raw file back to users.

## Why Not clamdscan Yet

`clamdscan` may be useful later, but it requires additional operational decisions:

```text
daemon install and startup
socket path or TCP endpoint
container networking
signature database freshness
health checks
service permissions
timeout behavior across client and daemon
```

So the first implementation should stay with `clamscan first` and reserve `clamdscan later`.

## Next Product Gate

```text
next product gate: uploaded raw file ClamAV adapter v0
```

That gate may add a `ClamAvScannerAdapter` class with tests around missing binary, timeout, clean output, infected output, and unknown return code.

It should not add a download endpoint, file signature validation, daemon sockets, automatic removal, hosted deployment evidence, or external reviewer feedback.

## Boundary

This is review-only.

This is not malware scanning.

This is not scanner execution.

This is not ClamAV integration.

This is not file signature validation.

This is not a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

It is not Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.
