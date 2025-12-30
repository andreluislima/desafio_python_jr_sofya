import pytest

from datetime import date, timedelta
from pydantic import ValidationError

from app.schemas.consultations import (
    ConsultationIn,
    PatientIn,
    AppointmentIn,
    MedicationIn
)

def test_validacao_entrada_consulta():
    entrada_consulta = {
        "patient": {
            "name": "André Lima",
            "birth_date": "1995-05-10",
            "gender": "M",
        },
        "appointment": {
            "date": str(date.today()),
            "complaint": "Febre alta",
            "notes": "Paciente relatou piora à noite",
        },
        "medications": [
            {"name": "Dipirona", "dosage": "500mg", "frequency": "8/8h"},
            {"name": "Omeprazol", "dosage": "20mg", "frequency": "1x ao dia"},
        ],
    }

    model = ConsultationIn.model_validate(entrada_consulta)

    assert model.patient.name == "André Lima"
    assert model.appointment.complaint == "Febre alta"
    assert len(model.medications) == 2