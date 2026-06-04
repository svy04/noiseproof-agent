# Uploaded Raw File Download Approval Schema Runtime Verification

Status: local Docker DB runtime verification.

Phase marker: uploaded raw file download approval schema runtime verification v0.

## Purpose

Verify that migration `021_raw_file_download_approvals.sql` applies to the local Docker PostgreSQL database and creates the expected table, indexes, and constraints.

This verifies schema application only.

It does not change guarded raw file download route behavior.

## Environment

```text
Docker Compose db service
PostgreSQL pgvector image
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

## Migration Runner

Command:

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run python -m app.migration_runner
```

Observed output:

```text
Applied migrations: 19
Pending migrations: 1
applied 021_raw_file_download_approvals.sql
```

Status command:

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run python -m app.migration_runner --status
```

Observed output:

```text
Applied migrations: 20
Pending migrations: 0
```

## Column Introspection

Command:

```powershell
docker compose exec -T db psql -U noiseproof -d noiseproof -c "SELECT column_name, data_type, is_nullable, column_default FROM information_schema.columns WHERE table_name = 'raw_file_download_approvals' ORDER BY ordinal_position;"
```

Observed output:

```text
      column_name      |        data_type         | is_nullable |                        column_default
-----------------------+--------------------------+-------------+---------------------------------------------------------------
 id                    | uuid                     | NO          | gen_random_uuid()
 raw_file_id           | uuid                     | NO          |
 latest_scan_result_id | uuid                     | NO          |
 approval_status       | text                     | NO          | 'approved'::text
 approval_reason       | text                     | YES         |
 approved_by_label     | text                     | NO          |
 expires_at            | timestamp with time zone | NO          |
 revoked_at            | timestamp with time zone | YES         |
 metadata_json         | jsonb                    | NO          | '{}'::jsonb
 approval_boundary     | text                     | NO          | 'local_v0_manual_operator_approval_not_production_auth'::text
 identity_boundary     | text                     | NO          | 'operator_label_not_authenticated_identity'::text
 created_at            | timestamp with time zone | NO          | now()
(12 rows)
```

## Index Introspection

Command:

```powershell
docker compose exec -T db psql -U noiseproof -d noiseproof -c "SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'raw_file_download_approvals' ORDER BY indexname;"
```

Observed index names:

```text
idx_raw_file_download_approvals_expires_at
idx_raw_file_download_approvals_latest_scan_result_id
idx_raw_file_download_approvals_raw_file_id
idx_raw_file_download_approvals_status
raw_file_download_approvals_pkey
(5 rows)
```

## Constraint Introspection

Command:

```powershell
docker compose exec -T db psql -U noiseproof -d noiseproof -c "SELECT conname, contype, pg_get_constraintdef(oid) AS definition FROM pg_constraint WHERE conrelid = 'raw_file_download_approvals'::regclass ORDER BY conname;"
```

Observed constraints:

```text
raw_file_download_approvals_approval_status_check
raw_file_download_approvals_approved_by_label_check
raw_file_download_approvals_check
raw_file_download_approvals_check1
raw_file_download_approvals_latest_scan_result_id_fkey
raw_file_download_approvals_pkey
raw_file_download_approvals_raw_file_id_fkey
(7 rows)
```

Observed foreign key definitions:

```text
FOREIGN KEY (raw_file_id) REFERENCES uploaded_raw_files(id) ON DELETE CASCADE
FOREIGN KEY (latest_scan_result_id) REFERENCES raw_file_scan_results(id) ON DELETE CASCADE
```

## Boundary

This is local Docker DB schema verification only.

This is not endpoint code.

This is not repository code.

This is not route behavior.

This is not production authorization.

This is not user identity.

This is not signed URL support.

This is not RBAC.

This is not ABAC.

This is not ReBAC.

This is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, malware detection proof, endpoint malicious-detection runtime proof, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file download approval repository review v0
```
