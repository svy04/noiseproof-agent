CREATE TABLE IF NOT EXISTS raw_file_download_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  raw_file_id UUID NOT NULL REFERENCES uploaded_raw_files(id) ON DELETE CASCADE,
  latest_scan_result_id UUID REFERENCES raw_file_scan_results(id) ON DELETE SET NULL,
  download_result TEXT NOT NULL CHECK (
    download_result IN ('allowed', 'blocked')
  ),
  blocked_reason TEXT CHECK (
    blocked_reason IS NULL OR blocked_reason IN (
      'missing_clean_scan',
      'latest_scan_not_clean',
      'quarantine_status_blocked',
      'rate_limited',
      'raw_file_missing'
    )
  ),
  http_status_code INTEGER NOT NULL CHECK (
    http_status_code >= 100 AND http_status_code <= 599
  ),
  authorization_boundary TEXT NOT NULL DEFAULT 'local_v0_no_auth_not_production',
  rate_limit_boundary TEXT NOT NULL DEFAULT 'local_v0_in_memory_fixed_window_not_production',
  filename_boundary TEXT NOT NULL DEFAULT 'local_v0_content_disposition_filename_safety_not_production',
  client_host_boundary TEXT NOT NULL DEFAULT 'local_request_client_host_not_identity',
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_events_raw_file_id
  ON raw_file_download_events(raw_file_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_events_latest_scan_result_id
  ON raw_file_download_events(latest_scan_result_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_events_download_result
  ON raw_file_download_events(download_result);
