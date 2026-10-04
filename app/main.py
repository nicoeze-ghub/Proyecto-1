from fastapi import FastAPI

app = FastAPI(
    title = "Mi API de tareas",
    description = "API REST para gestionar tareas",
    version = "0.1.0"   
)

# VALIDACION DE FUNCIONAMIENTO
@app.get("/")
def read_root():
    return {"mensaje" : "Funcionando correctamente"}