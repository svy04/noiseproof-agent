# Uploaded Raw File Dockerized ClamAV EICAR Runtime Smoke

Status: verified locally.

Phase marker: dockerized ClamAV EICAR runtime smoke v0.

## Purpose

This gate verifies a real Dockerized ClamAV runtime against the EICAR anti-malware test file.

It follows `docs/review/uploaded-raw-file-clamav-runtime-verification-review.md` with one evidence-backed adjustment: the EICAR file is created only inside the container instead of on the Windows host. This avoids host antivirus interference and avoids writing the test file into the workspace.

It does not wire ClamAV into the API endpoint.

It does not prove production malware scanning quality.

## Runtime Summary

```json
{
  "phase_marker": "dockerized ClamAV EICAR runtime smoke v0",
  "docker_available": true,
  "clamav_image": "clamav/clamav:stable",
  "clamav_image_id": "sha256:d4000290254603e7ee45d4904425c7d98c015af727f402756198fe41a31e7777",
  "clamav_repo_digest": "clamav/clamav@sha256:d4000290254603e7ee45d4904425c7d98c015af727f402756198fe41a31e7777",
  "clamscan_version": "ClamAV 1.5.2/28017/Sun May 31 06:27:13 2026",
  "signature_database_observed": true,
  "test_file_type": "eicar",
  "test_file_committed_to_repo": false,
  "clamscan_return_code": 1,
  "eicar_detected": true,
  "temporary_scan_file_deleted": true,
  "host_eicar_file_written": false,
  "real_clamav_runtime_verified": true,
  "malware_scanning_evidence": false,
  "api_endpoint_verified_with_real_clamav": false,
  "clamscan_output": "/tmp/eicar.com: Eicar-Test-Signature FOUND"
}
```

## Command Shape

The smoke:

```text
pulled or used clamav/clamav:stable
recorded image id and repo digest
encoded the EICAR string as an environment variable
wrote /tmp/eicar.com inside the container
ran clamscan --no-summary /tmp/eicar.com
removed /tmp/eicar.com inside the container
treated clamscan return code 1 plus FOUND output as expected EICAR detection
```

## Confirmed

```text
Docker is available
the ClamAV container runs clamscan
the ClamAV signature database version is visible in clamscan --version
EICAR was detected as Eicar-Test-Signature
the temporary container test file was removed
the EICAR file was not committed to the repo
the EICAR file was not written to the Windows host workspace
```

## Not Confirmed

```text
API endpoint behavior with NOISEPROOF_SCANNER=clamav
host-installed clamscan availability
Docker-backed scanner adapter behavior
clamd daemon behavior
production malware scanning quality
arbitrary uploaded file safety
hosted deployment behavior
external reviewer feedback
```

## Boundary

This is local Dockerized ClamAV runtime evidence for the EICAR test file only.

This is real ClamAV runtime verification.

This is not malware scanning evidence for production uploads.

This is not production malware scanning evidence.

This is not API endpoint verification with real ClamAV.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV API integration boundary review v0
```
