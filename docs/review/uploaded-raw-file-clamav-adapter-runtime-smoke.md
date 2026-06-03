# Uploaded Raw File ClamAV Adapter Runtime Smoke

Status: implemented.

Phase marker: uploaded raw file ClamAV adapter runtime smoke v0.

## Purpose

This smoke exercises the `ClamAvScannerAdapter` through a deterministic command path.

It uses dependency-injected fake binary discovery and fake process runners for adapter behavior.

It does not install ClamAV.

It does not execute a real `clamscan` binary.

It does not verify a ClamAV signature database.

It does not prove malware scanning.

## Added Code

```text
apps/api/app/services/clamav_adapter_smoke_command.py
apps/api/tests/test_clamav_adapter_smoke_command.py
```

Command:

```bash
uv run python -m app.services.clamav_adapter_smoke_command
```

## Observed Local Result

Observed on this workstation:

```text
smoke_status -> passed
real_clamav_runtime_verified -> false
clamav_binary_present -> false
binary_probe_only -> true
```

Covered deterministic scenarios:

```text
missing_binary -> failed / scan_error / missing_clamscan
clean_output -> completed / clean
infected_output -> completed / infected / Eicar-Test-Signature
timeout -> failed / scan_error / timeout
unknown_return_code -> failed / scan_error / unknown_return_code
```

Temporary path safety:

```text
temporary_scan_path_leaked -> false for every scenario
```

## Interpretation

This proves only that the adapter boundary can be exercised through an inspectable command and that the deterministic mappings stay stable.

The command can also report whether a `clamscan` binary is present through `shutil.which`, but it does not execute that binary.

## Boundary

This is not malware scanning evidence.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not endpoint behavior.

This is not download behavior.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

It is not Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
external reviewer ClamAV adapter runtime smoke request refresh v0
```

That gate may point reviewer-facing request surfaces to this proof, but it should not claim real malware scanning, ClamAV installation, signature database verification, endpoint behavior, download behavior, hosted deployment evidence, external reviewer feedback, customer validation, or product completeness.
