from fastapi import APIRouter
from app.config.database import supabase
from app.schemas.subcategoria import Subcategoria

router = APIRouter(
    prefix="/subcategorias",
    tags=["Subcategorías"]
)

# Obtener todas las subcategorias
@router.get("/")
def obtener_subcategorias():

    respuesta = supabase.table(
        "subcategorias"
    ).select("*").execute()

    return respuesta.data


# Obtener subcategoria por ID
@router.get("/{id_subcategoria}")
def obtener_subcategoria(id_subcategoria: int):

    respuesta = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    if not respuesta.data:
        return {
            "error": "Subcategoria no encontrada"
        }

    return respuesta.data


# Crear subcategoria
@router.post("/")
def crear_subcategoria(subcategoria: Subcategoria):

    categoria = supabase.table(
        "categorias"
    ).select("*").eq(
        "id_categoria",
        subcategoria.id_categoria
    ).execute()

    if not categoria.data:
        return {
            "error": "La categoria no existe"
        }

    respuesta = supabase.table(
        "subcategorias"
    ).insert(
        {
            "nombre": subcategoria.nombre,
            "id_categoria": subcategoria.id_categoria
        }
    ).execute()

    return {
        "mensaje": "Subcategoria creada correctamente",
        "datos": respuesta.data
    }


# Actualizar subcategoria
@router.put("/{id_subcategoria}")
def actualizar_subcategoria(
    id_subcategoria: int,
    subcategoria: Subcategoria
):

    existe = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    if not existe.data:
        return {
            "error": "Subcategoria no encontrada"
        }

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

    existe = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    if not existe.data:
        return {
            "error": "Subcategoria no encontrada"
        }

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