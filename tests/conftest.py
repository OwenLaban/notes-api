import pytest

from app import storage


@pytest.fixture(autouse=True)
def file_sementara(tmp_path, monkeypatch):
    """Setiap test memakai notes.json sendiri di folder sementara.

    Jadi data asli tidak tersentuh dan test tidak saling mempengaruhi.
    """
    monkeypatch.setattr(storage, "FILE", tmp_path / "notes.json")
