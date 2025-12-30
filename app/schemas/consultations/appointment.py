from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator  

class AppointmentIn(BaseModel):
    date: date = Field(...)
    complaint:str = Field(..., min_length=3)
    notes: Optional[str] = None

    @field_validator("date")
    @classmethod
    def validar_data_consulta(cls, value:date) -> date:
        if value > date.today():
            raise ValueError("Data inválida.\nData de consulta não pode ser maior que a data de hoje.")
        return value

class AppointmentOut(BaseModel):
    date: date
    complaint: str
    notes: Optional[str] = None

