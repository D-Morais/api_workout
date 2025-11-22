from fastapi import FastAPI
from app.routers import atleta_router

app = FastAPI(title="WorkoutAPI", version="1.0")
app.include_router(atleta_router.router)
