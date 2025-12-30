from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(
    title = "API de consultas médicas",
    description = "API para cadastro e validação de consultas médicas",
    version= "1.0.0"
)

app.include_router(api_router)

#Endpoint -> /consultations/


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000,
        log_level='info',
        reload=True
    )
