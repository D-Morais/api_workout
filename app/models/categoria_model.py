from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.atleta_model import Atleta


class Categoria(Base):
    __tablename__ = "categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    atletas: Mapped["Atleta"] = relationship(back_populates="categoria")
