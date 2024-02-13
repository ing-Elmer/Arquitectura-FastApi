# Importaciones
import os

from fastapi import FastAPI
from Api.Routes.router import router
from Config.config  import ConexionBD
# Configurar la aplicación
app = FastAPI(
  title="Introducción a FastAPI",
  description="Esta es una breve introducción a FastAPI, un framework para construir APIs con Python.",
  version="1.0.0",
)

# Base de datos
#ConexionBD().verificar_conexion()
ConexionBD().create_tables()
#ConexionBD().drop_tables()
# Orígenes permitidos
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/user", tags=["User"])
