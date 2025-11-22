from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_session
from app.models.categoria_model import Categoria
from app.schemas.categoria_schema import CategoriaCreate, CategoriaOut

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def criar_categoria(data: CategoriaCreate, session: AsyncSession = Depends(get_session)):
    categoria = Categoria(**data.model_dump())
    session.add(categoria)
    await session.commit()
    await session.refresh(categoria)
    return categoria


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CategoriaOut])
async def listar_categorias(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Categoria))
    return result.scalars().all()
