
from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Sistema de Controle Financeiro API",
    version="0.1.0",
    description="API para controle financeiro pessoal.",
)

app.include_router(health_router)
