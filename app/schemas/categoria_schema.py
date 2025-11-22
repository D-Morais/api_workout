from pydantic import BaseModel


class CategoriaBase(BaseModel):
    nome: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaOut(CategoriaBase):
    pk_id: int

    modul_config = {"from_attributes": True}
