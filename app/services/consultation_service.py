from datetime import date
from typing import List

from app.schemas.consultations import ConsultationIn, ConsultationOut

def calcular_idade(data_nascimento: date, data_atual:date) -> int:
    idade = data_atual.year - data_nascimento.year

    mes_atual = data_atual.month
    dia_atual = data_atual.day

    mes_nascimento = data_nascimento.month
    dia_nascimento = data_nascimento.day

    if mes_atual > mes_nascimento:
        return idade
    
    if mes_atual == mes_nascimento:
        if dia_atual >= dia_nascimento:
            return idade
    
    return idade -1

def padronizar_genero(linha: str) -> str:
    valor = (linha or "").strip().lower()

    genero_feminino = {"f", "famale", "woman", "feminino", "mulher"}
    genero_masculino = {"m", "male", "man", "masculino", "masc", "homem"}

    if valor in genero_feminino:
        return "female"
    elif valor in genero_masculino:
        return "male"
    else:
        return "other"

def processar_consulta(entrada_consulta: ConsultationIn) -> ConsultationOut:
    idade = calcular_idade(
                entrada_consulta.patient.birth_date, 
                entrada_consulta.appointment.date
            )

    genero_format = padronizar_genero(entrada_consulta.patient.gender)
    
    medicamentos: List[str] = []
    for m in entrada_consulta.medications:
        medicamentos.append(m.name)
        medicamentos.append(m.dosage)
        medicamentos.append(m.frequency)

    entrada_genero = entrada_consulta.patient.gender

    if entrada_genero == "F":
        genero_pt_br = "feminino"
    elif entrada_genero == "M":
        genero_pt_br = "masculino"
    else:
        genero_pt_br = "outro"
    
    resumo_prontuario = (
        f"Paciente {entrada_consulta.patient.name}, {idade} anos, sexo {genero_pt_br}. Queixa principal: {entrada_consulta.appointment.complaint}"
    )
    
    return ConsultationOut(
         patient = {
            "name": entrada_consulta.patient.name,
            "age":idade,
            "gender":genero_pt_br
         },
         appointment = {
            "date":entrada_consulta.appointment.date,
            "complaint":entrada_consulta.appointment.complaint,
            "notes":entrada_consulta.appointment.notes
         },
         medications = medicamentos,
         text_sumary = resumo_prontuario
    )
