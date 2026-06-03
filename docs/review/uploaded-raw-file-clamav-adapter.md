# Uploaded Raw File ClamAV Adapter

Status: implemented.

Phase marker: uploaded raw file ClamAV adapter v0.

## Purpose

This gate adds a conservative `ClamAvScannerAdapter` implementation on top of the generic scanner adapter boundary.

It does not install ClamAV.

It does not verify a real local ClamAV runtime.

It does not add an API endpoint.

It does not open a download endpoint.

## Added Code

```text
packages/ingestion/scanning/clamav.py
packages/ingestion/scanning/__init__.py
packages/ingestion/__init__.py
apps/api/tests/test_raw_file_scanning.py
```

Exported adapter:

```text
ClamAvScannerAdapter
```

The adapter uses dependency injection for binary discovery and process execution:

```text
which
runner
```

This keeps tests deterministic and avoids requiring ClamAV on every development or CI machine.

## Behavior

The implementation uses:

```text
shutil.which
subprocess.run
clamscan
--no-summary
```

The adapter never adds:

```text
no --remove
no --move
no daemon TCP sockets
```

Covered mappings:

```text
missing clamscan -> failed / scan_error
missing temporary_scan_path -> failed / scan_error
timeout -> failed / scan_error
unknown return code -> failed / scan_error
clean output -> completed / clean
FOUND output -> completed / infected
```

`temporary_scan_path` is used only as internal process input.

It is not persisted into result metadata.

The public metadata keeps only:

```text
temporary_scan_path_present
clamav_command = ["clamscan.exe", "--no-summary", "<temporary_scan_path>"]
```

## Tests

Focused test:

```bash
uv run pytest -q tests/test_raw_file_scanning.py -k "clamav_adapter"
```

Observed:

```text
5 passed, 2 deselected
```

The tests cover:

```text
missing binary
missing temporary path
clean output
FOUND output signature parsing
timeout
unknown return code
```

## Boundary

This is not ClamAV installation.

This is not runtime ClamAV verification.

This is not malware scanning evidence.

This is not scanner endpoint behavior.

This is not file signature validation.

This is not a download endpoint.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

It is not Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
uploaded raw file ClamAV adapter runtime smoke v0
```

That gate should verify adapter behavior through a small script or smoke command without claiming real malware scanning unless a real ClamAV binary and signature database are present and recorded.
