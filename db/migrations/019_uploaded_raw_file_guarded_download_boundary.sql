ALTER TABLE uploaded_raw_files
  ALTER COLUMN persistence_boundary
  SET DEFAULT 'raw_upload_quarantine_db_bytea_guarded_download_endpoint';
