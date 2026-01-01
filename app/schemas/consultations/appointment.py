from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator  

class AppointmentIn(BaseModel):
    date: date  
    complaint:str = Field(...)
    notes: Optional[str] = None

    @field_validator("date")
    @classmethod
    def validar_data_consulta(cls, value:date) -> date:
        if value > date.today():
            raise ValueError("Data inválida. Data de consulta não pode ser maior que a data de hoje.")
        return value

    @field_validator("complaint")
    @classmethod
    def validar_complaint(cls, value:str) -> str:
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Sintoma do paciente é obrigatório e deve ter no mínimo 3 caracteres.")
        return value

class AppointmentOut(BaseModel):
    date: date
    complaint: str
    notes: Optional[str] = None

