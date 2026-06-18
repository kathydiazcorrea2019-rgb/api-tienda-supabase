from fastapi import APIRouter
from app.config.database import supabase
from app.schemas.categoria import Categoria

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)

# Obtener todas las categorias
@router.get("/")
def obtener_categorias():

    respuesta = supabase.table(
        "categorias"
    ).select("*").execute()

    return respuesta.data


# Crear categoria
@router.post("/")
def crear_categoria(categoria: Categoria):

    respuesta = supabase.table(
        "categorias"
    ).insert(
        {
            "nombre": categoria.nombre,
            "porcentaje_ganancia": categoria.porcentaje_ganancia
        }
    ).execute()

    return {
        "mensaje": "Categoría creada correctamente",
        "datos": respuesta.data
    }


# Actualizar categoria
@router.put("/{id_categoria}")
def actualizar_categoria(id_categoria: int, categoria: Categoria):

    respuesta = supabase.table(
        "categorias"
    ).update(
        {
            "nombre": categoria.nombre,
            "porcentaje_ganancia": categoria.porcentaje_ganancia
        }
    ).eq(
        "id_categoria",
        id_categoria
    ).execute()

    return {
        "mensaje": "Categoria actualizada correctamente",
        "datos": respuesta.data
    }


# Eliminar categoria
@router.delete("/{id_categoria}")
def eliminar_categoria(id_categoria: int):

    respuesta = supabase.table(
        "categorias"
    ).delete().eq(
        "id_categoria",
        id_categoria
    ).execute()

    return {
        "mensaje": "Categoria eliminada correctamente",
        "datos": respuesta.data
    }