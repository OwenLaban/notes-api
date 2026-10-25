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
- Siap dijalankan dalam container Docker (image tanpa dependensi test)

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

```powershell
$body = '{"judul": "Belajar FastAPI", "isi": "Pydantic + pytest"}'
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/notes `
  -ContentType "application/json" -Body $body
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
pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Buka <http://127.0.0.1:8000/docs> untuk mencoba endpoint langsung dari browser.

`requirements.txt` hanya berisi dependensi runtime (dipakai Docker), sedangkan
`requirements-dev.txt` menambahkan pytest + httpx2 untuk development.

## Menjalankan dengan Docker

Build image:

```sh
docker build -t notes-api:1.0 .
```

Jalankan container dengan volume supaya data tetap ada:

```sh
docker run -d --name notes-api -p 8000:8000 -v notes-data:/app/data -e NOTES_FILE=/app/data/notes.json notes-api:1.0
```

Buka <http://127.0.0.1:8000/docs>. Kalau port 8000 sudah dipakai, ganti sisi kiri
menjadi `-p 8001:8000` lalu akses port 8001.

Atau pakai Docker Compose:

```sh
docker compose up -d --build
docker compose down
```

Kalau port 8000 dipakai proyek lain, set port lewat environment variable:

```powershell
$env:NOTES_API_PORT = "8001"
docker compose up -d --build
```

Data disimpan di named volume `notes-data`, jadi tidak hilang saat container
dihapus. Untuk menghapus data juga:

```sh
docker compose down -v
```

## Test

```sh
pip install -r requirements-dev.txt
pytest -v
```

Test memakai file sementara (`tmp_path`), jadi `notes.json` asli tidak tersentuh dan
setiap test mulai dari data kosong. Test dijalankan di host — image Docker sengaja
tidak membawa pytest.

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
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt       # runtime (Docker)
├── requirements-dev.txt   # + pytest & httpx2
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
- Image Docker belum memakai non-root user (hardening berikutnya)
- Belum ada CI/CD

## Tech Stack

Python · FastAPI · Pydantic · pytest · JSON · Docker
