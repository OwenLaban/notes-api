from app import storage


# --- CONTOH: file belum ada -> list kosong ---
def test_muat_file_belum_ada():
    assert storage.muat() == []


# --- CONTOH: simpan lalu muat lagi ---
def test_simpan_dan_muat():
    data = [{"id": 1, "judul": "Catatan A", "isi": ""}]
    storage.simpan(data)
    assert storage.muat() == data
    assert storage.FILE.exists()


# --- CONTOH: id berikutnya selalu id terbesar + 1 ---
def test_id_baru():
    assert storage.id_baru([]) == 1
    assert storage.id_baru([{"id": 1}]) == 2
    assert storage.id_baru([{"id": 1}, {"id": 7}]) == 8
