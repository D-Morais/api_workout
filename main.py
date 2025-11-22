from fastapi import FastAPI
from app.routers.atleta_router import router as atleta_router
from app.routers.categoria_router import router as categoria_router
from app.routers.centro_treinamento_router import router as centro_router


app = FastAPI(title="WorkoutAPI", version="1.0")
app.include_router(atleta_router)
app.include_router(categoria_router)
app.include_router(centro_router)
