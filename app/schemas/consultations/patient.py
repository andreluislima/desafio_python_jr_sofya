from datetime import date

from pydantic import BaseModel, Field, field_validator

class PatientIn(BaseModel):
    name: str = Field(..., min_length=3)
    birth_date:date = Field(...)
    gender:str = Field(...)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value:str) -> str:

        value = value.strip()
        if not value:
            raise ValueError("Nome do paciente é obrigatório")
        return value
    
    @field_validator("birth_date")
    @classmethod
    def validate_birth_date(cls, value:date) -> date:

        if value >= date.today():
            raise ValueError("Data de nascimento inválida.\nA data de nascimento não pode ser maior ou igual a data de hoje")
        return value

class PatientOut(BaseModel):
    name:str
    age:int
    gender:str
