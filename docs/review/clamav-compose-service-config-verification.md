# ClamAV Compose Service Config Verification

Status: implemented.

Phase marker: ClamAV compose service config verification v0.

## Purpose

This gate records config-only evidence for the optional ClamAV Compose service.

It verifies that Docker Compose can render the scanner-profile service shape. It does not start clamd.

## Command

```text
docker compose --profile scanner config -> exit 0
```

## Observed Rendered Shape

```text
service: clamav
image: clamav/clamav:stable
profiles: scanner
expose: 3310
healthcheck: clamdscan --ping=1 || exit 1
volume: noiseproof_clamav_db -> /var/lib/clamav
network: noiseproof-agent_default
clamav ports published to host: false
```

Observed boundary flags:

```text
real_clamav_runtime_verified: false
api_endpoint_verified_with_real_clamav: false
malware_scanning_evidence: false
hosted_deployment_evidence: false
```

The database service still publishes its configured PostgreSQL port. This verification only asserts that the `clamav` service does not publish clamd to the host.

## Boundary

This is config-only verification.

This is not clamd runtime verification.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV compose service runtime smoke v0
```
