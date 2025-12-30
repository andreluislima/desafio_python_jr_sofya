import pytest

from datetime import date, timedelta
from pydantic import ValidationError

from app.schemas.consultations import (
    ConsultationIn,
    PatientIn,
    AppointmentIn,
    MedicationIn
)

def test_validar_entrada_consulta():
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

def test_validar_data_nascimento():
    amanha = date.today() + timedelta(days=1)

    entrada_consulta = {
        "name": "Carlos Lins",
        "birth_date":str(amanha),
        "gender":"M"
    }

    with pytest.raises(ValidationError) as ex:
        PatientIn.model_validate(entrada_consulta)

def test_validar_data_consulta():

    amanha = date.today() + timedelta(days=1)

    entrada_consulta = {
        "date":str(amanha),
        "complaint":"Febre",
        "notes":"Paciente se queixa de febres frequentes"
    }
    ...