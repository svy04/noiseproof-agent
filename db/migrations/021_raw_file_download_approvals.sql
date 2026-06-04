CREATE TABLE IF NOT EXISTS raw_file_download_approvals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  raw_file_id UUID NOT NULL REFERENCES uploaded_raw_files(id) ON DELETE CASCADE,
  latest_scan_result_id UUID NOT NULL REFERENCES raw_file_scan_results(id) ON DELETE CASCADE,
  approval_status TEXT NOT NULL DEFAULT 'approved' CHECK (
    approval_status IN ('approved', 'revoked', 'expired')
  ),
  approval_reason TEXT,
  approved_by_label TEXT NOT NULL CHECK (length(trim(approved_by_label)) > 0),
  expires_at TIMESTAMPTZ NOT NULL,
  revoked_at TIMESTAMPTZ,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  approval_boundary TEXT NOT NULL DEFAULT 'local_v0_manual_operator_approval_not_production_auth',
  identity_boundary TEXT NOT NULL DEFAULT 'operator_label_not_authenticated_identity',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CHECK (expires_at > created_at),
  CHECK (revoked_at IS NULL OR revoked_at >= created_at)
);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_approvals_raw_file_id
  ON raw_file_download_approvals(raw_file_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_approvals_latest_scan_result_id
  ON raw_file_download_approvals(latest_scan_result_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_approvals_status
  ON raw_file_download_approvals(approval_status);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_approvals_expires_at
  ON raw_file_download_approvals(expires_at);
