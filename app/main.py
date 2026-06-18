from fastapi import FastAPI
from app.config.database import supabase
from app.routers import categorias
from app.routers import subcategorias
from app.routers import productos

app = FastAPI(
    title="API Sistema de Liquidacion",
    description="Gestion de categorias, subcategorias y productos",
    version="1.0.0"
)

# Routers
app.include_router(categorias.router)
app.include_router(subcategorias.router)
app.include_router(productos.router)

@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


@app.get("/test-supabase")
def test_supabase():

    respuesta = supabase.table("categorias").select("*").execute()

    return {
        "estado": "conectado",
        "datos": respuesta.data
    }