from fastapi import FastAPI
from app.config.database import supabase

from app.routers.categorias import router as categorias_router
from app.routers.subcategorias import router as subcategorias_router
from app.routers.productos import router as productos_router

app = FastAPI(
    title="API Sistema de Liquidacion",
    description="""
API REST desarrollada con FastAPI y Supabase para la gestión de categorias,
subcategorias y productos.

Funcionalidades:

- Registrar categorias
- Registrar subcategorias
- Registrar productos
- Consultar informacion
- Actualizar registros
- Eliminar registros

Arquitectura:

Usuario → Frontend → API REST → Supabase PostgreSQL
""",
    version="1.0.0"
)

# Registrar routers
app.include_router(categorias_router)
app.include_router(subcategorias_router)
app.include_router(productos_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


@app.get("/test-supabase")
def test_supabase():

    respuesta = supabase.table(
        "categorias"
    ).select("*").execute()

    return {
        "estado": "conectado",
        "datos": respuesta.data
    }