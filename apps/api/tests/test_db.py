from datetime import UTC, datetime
from uuid import UUID

from app import schemas
from app.db import PostgresRepository
from app.settings import Settings


class FakeCursor:
    def __init__(self, *, row=None, rows=None):
        self._row = row
        self._rows = rows or []

    def fetchone(self):
        return self._row

    def fetchall(self):
        return self._rows


class FakeConnection:
    def __init__(self, *, row=None, rows=None):
        self.calls = []
        self.committed = False
        self._row = row
        self._rows = rows or []

    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        return False

    def execute(self, sql, params=None):
        self.calls.append((sql, params))
        return FakeCursor(row=self._row, rows=self._rows)

    def commit(self):
        self.committed = True


def test_create_uploaded_file_intake_manifest_inserts_manifest_metadata_only():
    created_at = datetime(2026, 6, 1, tzinfo=UTC)
    manifest_id = UUID("11111111-1111-1111-1111-111111111111")
    row = {
        "id": manifest_id,
        "content_sha256": "abc123",
        "filename": "sample.md",
        "source_type": "markdown",
        "content_type": "text/markdown",
        "size_bytes": 24,
        "parser": "markdown",
        "profile_json": {"extraction_quality": "high"},
        "storage_decision": "do_not_persist_raw_upload_yet",
        "replayable": False,
        "persistence_boundary": "manifest_only_no_raw_file_storage",
        "warnings_json": [],
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    payload = schemas.UploadedFileIntakeManifestCreate(
        content_sha256="abc123",
        filename="sample.md",
        source_type="markdown",
        content_type="text/markdown",
        size_bytes=24,
        parser="markdown",
        profile_json={"extraction_quality": "high"},
    )

    created = repository.create_uploaded_file_intake_manifest(payload)

    sql, params = connection.calls[0]
    assert "INSERT INTO uploaded_file_intake_manifests" in sql
    assert "BYTEA" not in sql
    assert params[:6] == (
        "abc123",
        "sample.md",
        "markdown",
        "text/markdown",
        24,
        "markdown",
    )
    assert getattr(params[6], "obj", params[6]) == payload.profile_json
    assert created["id"] == manifest_id
    assert created["content_sha256"] == "abc123"
    assert connection.committed is True


def test_list_uploaded_file_intake_manifests_reads_recent_manifest_metadata():
    rows = [
        {"content_sha256": "new"},
        {"content_sha256": "old"},
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    listed = repository.list_uploaded_file_intake_manifests(limit=2)

    sql, params = connection.calls[0]
    assert "SELECT * FROM uploaded_file_intake_manifests" in sql
    assert "ORDER BY created_at DESC, id DESC" in sql
    assert "LIMIT %s" in sql
    assert params == (2,)
    assert listed == rows
