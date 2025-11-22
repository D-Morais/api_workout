from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.categoria_model import Categoria
from app.models.centro_treinamento_model import CentroTreinamento


class Atleta(Base):
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)

    categoria: Mapped["Categoria"] = relationship(back_populates="atletas", lazy="selectin")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))

    centro_treinamento: Mapped["CentroTreinamento"] = relationship(back_populates="atletas", lazy="selectin")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_treinamento.pk_id"))
