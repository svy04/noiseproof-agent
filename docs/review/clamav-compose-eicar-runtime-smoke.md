# ClamAV Compose EICAR Runtime Smoke

Status: implemented.

Phase marker: ClamAV compose EICAR runtime smoke v0.

## Purpose

This gate verifies that the Compose-managed ClamAV service detects the standard EICAR anti-malware test signature.

The EICAR payload was created only inside the running `clamav` container and deleted after scanning.

It does not connect the API endpoint to ClamAV.

## Source Anchor

- EICAR anti-malware test file: https://www.eicar.org/download-anti-malware-testfile/

## Command Shape

```text
docker compose --profile scanner exec -T -e EICAR_B64=<redacted> clamav sh -lc '<write /tmp/noiseproof-eicar.com inside container; clamdscan --stream; delete temp file>'
```

The base64 payload is intentionally not stored in the repository.

## Observed Output

```text
/tmp/noiseproof-eicar.com: Eicar-Test-Signature FOUND

----------- SCAN SUMMARY -----------
Infected files: 1
Time: 0.004 sec (0 m 0 s)
Start Date: 2026:06:03 04:42:56
End Date:   2026:06:03 04:42:56
clamdscan_return_code=1
```

Additional checks:

```text
temporary_scan_file_deleted: true
host_eicar_file_written: false
repo_eicar_payload_string_present: false
ClamAV version: ClamAV 1.5.2/28017/Sun May 31 06:27:13 2026
```

Observed boundary flags:

```text
eicar_detected: true
clamdscan_return_code: 1
real_clamav_runtime_verified: true
api_endpoint_verified_with_real_clamav: false
production_malware_scanning_evidence: false
```

## Boundary

This is local Docker Compose EICAR detection evidence only.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV service scanner adapter review v0
```
