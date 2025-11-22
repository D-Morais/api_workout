from pydantic import BaseModel


class AtletaBase(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int


class AtletaCreate(AtletaBase):
    pass


class AtletaOut(AtletaBase):
    pk_id: int

    model_config = {"from_attributes": True}
