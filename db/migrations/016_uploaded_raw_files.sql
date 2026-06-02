CREATE TABLE IF NOT EXISTS uploaded_raw_files (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_sha256 TEXT NOT NULL,
  storage_key TEXT NOT NULL UNIQUE,
  filename TEXT,
  source_type TEXT NOT NULL,
  content_type TEXT,
  size_bytes INTEGER NOT NULL DEFAULT 0 CHECK (size_bytes >= 0),
  storage_backend TEXT NOT NULL DEFAULT 'postgres_bytea',
  quarantine_status TEXT NOT NULL DEFAULT 'stored_quarantined' CHECK (
    quarantine_status IN ('stored_quarantined', 'rejected')
  ),
  persistence_boundary TEXT NOT NULL DEFAULT 'raw_upload_quarantine_db_bytea_no_download_endpoint',
  raw_bytes BYTEA NOT NULL,
  warnings_json JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_uploaded_raw_files_content_sha256
  ON uploaded_raw_files(content_sha256);
