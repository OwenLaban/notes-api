from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_get_notes_kosong():
    r = client.get("/notes")
    assert r.status_code == 200
    assert r.json() == []


def test_post_notes():
    r = client.post("/notes", json={"judul": "Catatan pertama"})
    assert r.status_code == 201
    hasil = r.json()
    assert hasil["id"] == 1
    assert hasil["judul"] == "Catatan pertama"
    assert hasil["isi"] == ""

    r = client.get("/notes")
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_get_notes_by_id():
    r = client.post("/notes", json={"judul": "Catatan pertama"})
    assert r.status_code == 201
    id_catatan = r.json()["id"]

    r = client.get(f"/notes/{id_catatan}")
    assert r.status_code == 200
    assert r.json()["judul"] == "Catatan pertama"

    r = client.get("/notes/999")
    assert r.status_code == 404


def test_put_notes():
    r = client.post("/notes", json={"judul": "Catatan pertama"})
    assert r.status_code == 201
    id_catatan = r.json()["id"]

    r = client.put(
        f"/notes/{id_catatan}",
        json={"judul": "Judul baru", "isi": "Isi baru"},
    )
    assert r.status_code == 200
    assert r.json()["judul"] == "Judul baru"
    assert r.json()["isi"] == "Isi baru"

    r = client.get(f"/notes/{id_catatan}")
    assert r.status_code == 200
    assert r.json()["judul"] == "Judul baru"
    assert r.json()["isi"] == "Isi baru"

    r = client.put("/notes/999", json={"judul": "Tidak ada", "isi": ""})
    assert r.status_code == 404


def test_delete_notes():
    r = client.post("/notes", json={"judul": "Catatan pertama"})
    assert r.status_code == 201
    id_catatan = r.json()["id"]

    r = client.delete(f"/notes/{id_catatan}")
    assert r.status_code == 204

    r = client.get(f"/notes/{id_catatan}")
    assert r.status_code == 404

    r = client.delete(f"/notes/{id_catatan}")
    assert r.status_code == 404


def test_validasi_pydantic():
    r = client.post("/notes", json={"judul": ""})
    assert r.status_code == 422

    r = client.post("/notes", json={"isi": "tanpa judul"})
    assert r.status_code == 422
