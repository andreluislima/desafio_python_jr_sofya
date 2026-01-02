from fastapi import APIRouter, status

from app.schemas.consultations import ConsultationIn, ConsultationOut
from app.services.consultation_service import processar_consulta

router = APIRouter()

@router.post("", response_model=ConsultationOut, status_code=status.HTTP_201_CREATED)
async def criar_consulta(entrada_consulta:ConsultationIn):
    return processar_consulta(entrada_consulta)

