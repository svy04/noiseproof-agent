CREATE TABLE IF NOT EXISTS raw_file_scan_results (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  raw_file_id UUID NOT NULL REFERENCES uploaded_raw_files(id) ON DELETE CASCADE,
  scanner_name TEXT NOT NULL,
  scanner_version TEXT,
  signature_db_version TEXT,
  scan_started_at TIMESTAMPTZ,
  scan_finished_at TIMESTAMPTZ,
  scan_status TEXT NOT NULL DEFAULT 'pending' CHECK (
    scan_status IN ('pending', 'running', 'completed', 'failed', 'skipped')
  ),
  scan_verdict TEXT NOT NULL DEFAULT 'pending' CHECK (
    scan_verdict IN (
      'pending',
      'clean',
      'suspicious',
      'infected',
      'scan_error',
      'skipped'
    )
  ),
  matched_signature TEXT,
  error_message TEXT,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_raw_file_scan_results_raw_file_id
  ON raw_file_scan_results(raw_file_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_scan_results_scan_status
  ON raw_file_scan_results(scan_status);

CREATE INDEX IF NOT EXISTS idx_raw_file_scan_results_scan_verdict
  ON raw_file_scan_results(scan_verdict);
