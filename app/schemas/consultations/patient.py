from datetime import date

from pydantic import BaseModel, Field, field_validator

class PatientIn(BaseModel):
    name: str = Field(...)
    birth_date:date = Field(...)
    gender:str = Field(...)

    @field_validator("name")
    @classmethod
    def validar_nome(cls, value:str) -> str:
        value = value.strip()

        if len(value) < 3:
            raise ValueError("Nome do paciente é obrigatório e deve ter no mínimo 3 caracteres")
        return value
    
    @field_validator("birth_date")
    @classmethod
    def validar_data_nascimento(cls, value:date) -> date:

        if value >= date.today():
            raise ValueError("Data de nascimento inválida.A data de nascimento não pode ser maior ou igual a data de hoje")
        return value

class PatientOut(BaseModel):
    name:str
    age:int
    gender:str
