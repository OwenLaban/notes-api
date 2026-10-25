from pydantic import BaseModel, Field


class CatatanMasuk(BaseModel):
    """Data dari client saat membuat atau mengubah catatan."""

    judul: str = Field(min_length=1, max_length=100)
    isi: str = Field(default="", max_length=5000)


class Catatan(CatatanMasuk):
    """Catatan lengkap dengan id, seperti yang dikembalikan API."""

    id: int
