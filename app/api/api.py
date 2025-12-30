from fastapi import APIRouter
from app.api.endpoints.consultation import router as consulta_rotas

api_router = APIRouter()

api_router.include_router(
    consulta_rotas,
    prefix="/consultations",
    tags=["Consultations"]
)