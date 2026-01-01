from pydantic import BaseModel, Field

class MedicationIn(BaseModel):
    name:str = Field(...)
    dosage:str = Field(...)
    frequency:str = Field(...)


class MedicationOut(BaseModel):
    name:str
    dosage:str
    frequency:str
