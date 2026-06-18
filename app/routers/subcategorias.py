from fastapi import APIRouter
from app.config.database import supabase
from app.schemas.subcategoria import Subcategoria

router = APIRouter(
    prefix="/subcategorias",
    tags=["Subcategorias"]
)

# Obtener todas las subcategorias
@router.get("/")
def obtener_subcategorias():

    respuesta = supabase.table(
        "subcategorias"
    ).select("*").execute()

    return respuesta.data


# Crear subcategoria
@router.post("/")
def crear_subcategoria(subcategoria: Subcategoria):

    respuesta = supabase.table(
        "subcategorias"
    ).insert(
        {
            "nombre": subcategoria.nombre,
            "id_categoria": subcategoria.id_categoria
        }
    ).execute()

    return {
        "mensaje": "Subcategoría creada correctamente",
        "datos": respuesta.data
    }


# Actualizar subcategoria
@router.put("/{id_subcategoria}")
def actualizar_subcategoria(
    id_subcategoria: int,
    subcategoria: Subcategoria
):

    respuesta = supabase.table(
        "subcategorias"
    ).update(
        {
            "nombre": subcategoria.nombre,
            "id_categoria": subcategoria.id_categoria
        }
    ).eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    return {
        "mensaje": "Subcategoria actualizada correctamente",
        "datos": respuesta.data
    }


# Eliminar subcategoria
@router.delete("/{id_subcategoria}")
def eliminar_subcategoria(id_subcategoria: int):

    respuesta = supabase.table(
        "subcategorias"
    ).delete().eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    return {
        "mensaje": "Subcategoria eliminada correctamente",
        "datos": respuesta.data
    }