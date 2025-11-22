from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_session
from app.models.centro_treinamento_model import CentroTreinamento
from app.schemas.centro_treinamento_schema import (
    CentroTreinamentoCreate, CentroTreinamentoOut
)

router = APIRouter(prefix="/centros", tags=["Centros de Treinamento"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)
async def criar_centro_treinamento(
        data: CentroTreinamentoCreate,
        session: AsyncSession = Depends(get_session)
):
    ct = CentroTreinamento(**data.model_dump())
    session.add(ct)
    await session.commit()
    await session.refresh(ct)
    return ct


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CentroTreinamentoOut])
async def listar_centros(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(CentroTreinamento))
    return result.scalars().all()
