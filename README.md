# 📝 Notes API

REST API untuk mencatat hal-hal kecil — dibuat dengan FastAPI dan dilengkapi test otomatis.

## Masalah

Catatan cepat sering tersebar di banyak tempat: chat, notepad, potongan kertas. API ini
menyediakan satu sumber data sederhana yang bisa dipakai aplikasi apa pun (CLI, web,
mobile) lewat HTTP + JSON.

## Fitur

- CRUD catatan: lihat semua, lihat detail, tambah, ubah, hapus
- Validasi input dengan Pydantic (judul wajib, maksimal 100 karakter)
- Data tersimpan di `notes.json` — tidak hilang saat server restart
- Dokumentasi otomatis di `/docs` (Swagger UI)
- Test otomatis dengan pytest

## Endpoint

| Method | Path | Fungsi | Sukses |
|---|---|---|---|
| GET | `/health` | cek status server | 200 |
| GET | `/notes` | semua catatan | 200 |
| GET | `/notes/{id}` | detail catatan | 200 |
| POST | `/notes` | buat catatan | 201 |
| PUT | `/notes/{id}` | ubah catatan | 200 |
| DELETE | `/notes/{id}` | hapus catatan | 204 |

Kalau id tidak ditemukan → `404`. Kalau body tidak valid → `422`.

## Contoh

```sh
curl -X POST http://127.0.0.1:8000/notes ^
  -H "Content-Type: application/json" ^
  -d "{\"judul\": \"Belajar FastAPI\", \"isi\": \"Pydantic + pytest\"}"
```

Response:

```json
{"id": 1, "judul": "Belajar FastAPI", "isi": "Pydantic + pytest"}
```

## Cara Menjalankan

Butuh Python 3.10+ (dikembangkan dengan Python 3.13.5).

```sh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Buka <http://127.0.0.1:8000/docs> untuk mencoba endpoint langsung dari browser.

## Test

```sh
pytest -v
```

Test memakai file sementara (`tmp_path`), jadi `notes.json` asli tidak tersentuh dan
setiap test mulai dari data kosong.

## Struktur

```text
notes-api/
├── app/
│   ├── main.py        # route HTTP
│   ├── models.py      # validasi Pydantic
│   └── storage.py     # baca/tulis notes.json
├── tests/
│   ├── conftest.py    # fixture file sementara
│   ├── test_notes.py  # test endpoint
│   └── test_storage.py
├── requirements.txt
└── pytest.ini
```

## Cara Kerja

1. Request masuk → FastAPI mencocokkan method + path.
2. Body divalidasi Pydantic; kalau tidak valid → `422` otomatis.
3. Route memanggil `storage.muat()` / `storage.simpan()` untuk membaca/menulis data.
4. ID baru dihitung dengan `max(id) + 1`.
5. Response dikembalikan sebagai JSON.

## Keterbatasan

- Belum ada autentikasi — siapa pun yang bisa mengakses server bisa mengubah data
- Penyimpanan JSON belum aman untuk banyak pengguna bersamaan (tanpa locking)
- Belum ada pagination atau pencarian
- Rencana berikutnya: Docker + volume (Minggu 6)

## Tech Stack

Python · FastAPI · Pydantic · pytest · JSON
