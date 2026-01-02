from pydantic import BaseModel, Field

from typing import List

from .patient import PatientIn, PatientOut
from .appointment import AppointmentIn, AppointmentOut
from .medication import MedicationIn


class ConsultationIn(BaseModel):
    patient: PatientIn
    appointment: AppointmentIn
    medications: List[MedicationIn] = Field(default_factory=list)

class ConsultationOut(BaseModel):
    patient_summary: PatientOut
    appointment_summary: AppointmentOut
    medications: List[str]
    text_summary: str