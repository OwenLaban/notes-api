from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- CONTOH: endpoint health ---
def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


# --- SOAL 1: GET /notes saat kosong ---
# TODO:
#   r = client.get("/notes")
#   assert r.status_code == 200
#   assert r.json() == []


# --- SOAL 2: POST /notes ---
# TODO:
#   r = client.post("/notes", json={"judul": "Catatan pertama"})
#   assert r.status_code == 201
#   hasil = r.json()
#   assert hasil["id"] == 1
#   assert hasil["judul"] == "Catatan pertama"
#   assert hasil["isi"] == ""
#   lalu GET /notes -> panjangnya 1 (data benar-benar tersimpan)


# --- SOAL 3: GET by id + 404 ---
# TODO:
#   buat catatan lewat POST, ambil id-nya
#   GET /notes/{id} -> 200 dan judul sama
#   GET /notes/999 -> 404


# --- SOAL 4: PUT /notes/{id} ---
# TODO:
#   buat catatan, lalu PUT dengan judul/isi baru
#   assert 200, data berubah
#   GET lagi -> data terbaru (persist)
#   PUT /notes/999 -> 404


# --- SOAL 5: DELETE /notes/{id} ---
# TODO:
#   buat catatan, DELETE -> 204
#   GET catatan yang sama -> 404
#   DELETE lagi -> 404


# --- BONUS: validasi Pydantic ---
# TODO:
#   POST {"judul": ""} -> 422 (judul tidak boleh kosong)
#   POST {"isi": "tanpa judul"} -> 422 (judul wajib)
