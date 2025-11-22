from pydantic import BaseModel


class CentroTreinamentoBase(BaseModel):
    nome: str
    endereco: str
    proprietario: str


class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass


class CentroTreinamentoOut(CentroTreinamentoBase):
    pk_id: int

    model_config = {"from_attributes": True}
