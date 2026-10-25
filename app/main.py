from fastapi import FastAPI, HTTPException

from app import storage
from app.models import Catatan, CatatanMasuk

app = FastAPI(title="Notes API", version="1.0.0")


@app.get("/health")
def health():
    """Cek status server."""
    return {"status": "ok"}


@app.get("/notes", response_model=list[Catatan])
def daftar_catatan():
    """Kembalikan semua catatan."""
    return storage.muat()


@app.get("/notes/{id}", response_model=Catatan)
def detail_catatan(id: int):
    """Kembalikan satu catatan berdasarkan id."""
    daftar = storage.muat()
    for cat in daftar:
        if cat["id"] == id:
            return cat
    raise HTTPException(status_code=404, detail="Catatan tidak ditemukan")


@app.post("/notes", response_model=Catatan, status_code=201)
def buat_catatan(data: CatatanMasuk):
    """Buat catatan baru."""
    daftar = storage.muat()
    baru = {"id": storage.id_baru(daftar), "judul": data.judul, "isi": data.isi}
    daftar.append(baru)
    storage.simpan(daftar)
    return baru


@app.put("/notes/{id}", response_model=Catatan)
def ubah_catatan(id: int, data: CatatanMasuk):
    """Ubah catatan yang sudah ada."""
    daftar = storage.muat()
    for i, cat in enumerate(daftar):
        if cat["id"] == id:
            daftar[i] = {"id": id, "judul": data.judul, "isi": data.isi}
            storage.simpan(daftar)
            return daftar[i]
    raise HTTPException(status_code=404, detail="Catatan tidak ditemukan")


@app.delete("/notes/{id}", status_code=204)
def hapus_catatan(id: int):
    """Hapus catatan berdasarkan id."""
    daftar = storage.muat()
    for i, cat in enumerate(daftar):
        if cat["id"] == id:
            daftar.pop(i)
            storage.simpan(daftar)
            return None
    raise HTTPException(status_code=404, detail="Catatan tidak ditemukan")
