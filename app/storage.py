import json
import os
from pathlib import Path

# Lokasi file data. Bisa dioverride lewat environment variable NOTES_FILE
# (berguna nanti saat jalan di Docker / test).
FILE_DEFAULT = Path(__file__).parent.parent / "notes.json"
FILE = Path(os.getenv("NOTES_FILE", FILE_DEFAULT))


def muat() -> list[dict]:
    """Baca semua catatan dari file. Kalau file belum ada -> list kosong."""
    if not FILE.exists():
        return []
    with open(FILE, encoding="utf-8") as f:
        return json.load(f)


def simpan(daftar: list[dict]) -> None:
    """Tulis seluruh daftar ke file (overwrite)."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(daftar, f, indent=2, ensure_ascii=False)


def id_baru(daftar: list[dict]) -> int:
    """ID berikutnya = id terbesar + 1."""
    return max((item["id"] for item in daftar), default=0) + 1
