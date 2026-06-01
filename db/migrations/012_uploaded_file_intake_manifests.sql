CREATE TABLE IF NOT EXISTS uploaded_file_intake_manifests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_sha256 TEXT NOT NULL,
  filename TEXT,
  source_type TEXT NOT NULL,
  content_type TEXT,
  size_bytes INTEGER NOT NULL DEFAULT 0 CHECK (size_bytes >= 0),
  parser TEXT,
  profile_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  storage_decision TEXT NOT NULL DEFAULT 'do_not_persist_raw_upload_yet',
  replayable BOOLEAN NOT NULL DEFAULT false,
  persistence_boundary TEXT NOT NULL DEFAULT 'manifest_only_no_raw_file_storage',
  warnings_json JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_uploaded_file_intake_manifests_content_sha256
  ON uploaded_file_intake_manifests(content_sha256);
