from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_session
from app.models.atleta_model import Atleta
from app.schemas.atleta_schema import AtletaCreate, AtletaOut

router = APIRouter(prefix="/atletas", tags=["Atletas"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def criar_atleta(
        data: AtletaCreate,
        session: AsyncSession = Depends(get_session)
):
    atleta = Atleta(**data.model_dump())
    session.add(atleta)
    await session.commit()
    await session.refresh(atleta)
    return atleta


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AtletaOut])
async def listar_atletas(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Atleta))
    return result.scalars().all()
