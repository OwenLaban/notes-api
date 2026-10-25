from fastapi import FastAPI, HTTPException

from app import storage
from app.models import Catatan, CatatanMasuk

app = FastAPI(title="Notes API", version="1.0.0")


@app.get("/health")
def health():
    """Cek cepat apakah server hidup. Contoh endpoint yang sudah jadi."""
    return {"status": "ok"}


# --- SOAL 1: GET /notes -> semua catatan ---
# TODO: return storage.muat()
# response_model memastikan bentuk response sesuai model Catatan.
@app.get("/notes", response_model=list[Catatan])
def daftar_catatan():
    raise HTTPException(status_code=501, detail="Belum diimplementasikan")


# --- SOAL 2: GET /notes/{id} -> satu catatan ---
# TODO:
#   daftar = storage.muat()
#   cari item yang id-nya cocok
#   kalau tidak ada -> HTTPException(status_code=404, detail="Catatan tidak ditemukan")
@app.get("/notes/{id}", response_model=Catatan)
def detail_catatan(id: int):
    raise HTTPException(status_code=501, detail="Belum diimplementasikan")


# --- SOAL 3: POST /notes -> buat catatan baru ---
# TODO:
#   daftar = storage.muat()
#   baru = {"id": storage.id_baru(daftar), "judul": data.judul, "isi": data.isi}
#   daftar.append(baru)
#   storage.simpan(daftar)
#   return baru
@app.post("/notes", response_model=Catatan, status_code=201)
def buat_catatan(data: CatatanMasuk):
    raise HTTPException(status_code=501, detail="Belum diimplementasikan")


# --- SOAL 4: PUT /notes/{id} -> ubah catatan ---
# TODO:
#   daftar = storage.muat()
#   cari index item dengan id tersebut
#   tidak ada -> 404
#   ganti judul + isi, simpan, return item terbaru
@app.put("/notes/{id}", response_model=Catatan)
def ubah_catatan(id: int, data: CatatanMasuk):
    raise HTTPException(status_code=501, detail="Belum diimplementasikan")


# --- SOAL 5: DELETE /notes/{id} -> hapus catatan ---
# TODO:
#   daftar = storage.muat()
#   cari index item dengan id tersebut
#   tidak ada -> 404
#   hapus, simpan, return None (status 204 = tanpa body)
@app.delete("/notes/{id}", status_code=204)
def hapus_catatan(id: int):
    raise HTTPException(status_code=501, detail="Belum diimplementasikan")
