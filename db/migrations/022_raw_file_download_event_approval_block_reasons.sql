ALTER TABLE raw_file_download_events
  DROP CONSTRAINT IF EXISTS raw_file_download_events_blocked_reason_check;

ALTER TABLE raw_file_download_events
  ADD CONSTRAINT raw_file_download_events_blocked_reason_check
  CHECK (
    blocked_reason IS NULL OR blocked_reason IN (
      'missing_clean_scan',
      'latest_scan_not_clean',
      'quarantine_status_blocked',
      'rate_limited',
      'raw_file_missing',
      'missing_download_approval',
      'revoked_or_expired_download_approval'
    )
  );
