# 🩺 Desafio Técnico — API de Consulta (FastAPI)


## Stack Utilizada

- **Python 3.12**
- **pip**

---

## ▶️ Como Rodar o Projeto

### 🔹 Opção 1: Executar Localmente

#### 1️⃣ Criar e ativar o ambiente virtual

```bash
  python -m venv .venv
```

**Windows**
```bash
  .venv\Scripts\Activate
```

**Linux / macOS**
```bash
  source .venv/bin/activate
```

---

#### 2️⃣ Instalar as dependências

```bash
  pip install -r requirements.txt
```

---

#### 3️⃣ Subir a API

```bash
  uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

#### 4️⃣ Acessar

```
  http://127.0.0.1:8000
```

---

### 🔹 Opção 2: Executar com Docker

#### Subir o projeto com Docker Compose

```bash
  docker compose up --build
```

#### 2️⃣ Acessar
```bash
  http://127.0.0.1:8000
```

## 🧪 Testes
#### 1️⃣ Como rodar os Testes
```bash
  pytest -q
```

## 📝Decisões Técnicas e Observações
- Uso do prefix nas rotas
Em vez de definir o caminho diretamente no endpoint, eu utilizei o prefix para sugerir uma organização por domínio e facilitar uma futura escalabilidade da API.

- Schemas - Patient
Adicionei uma validação para a data de nascimento, impedindo que sejam informadas datas no futuro ou iguais à data atual.

- Schemas - Appointment
Adicionei uma validação ao complaint para evitar que ela venha vazia.

