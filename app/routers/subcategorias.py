from fastapi import APIRouter, HTTPException
from app.config.database import supabase
from app.schemas.subcategoria import Subcategoria

router = APIRouter(
    prefix="/subcategorias",
    tags=["Subcategorias"]
)


@router.get("/")
def obtener_subcategorias():

    respuesta = supabase.table(
        "subcategorias"
    ).select("*").execute()

    return respuesta.data


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
        "mensaje": "Subcategoria creada correctamente",
        "datos": respuesta.data
    }


@router.put("/{id_subcategoria}")
def actualizar_subcategoria(
    id_subcategoria: int,
    subcategoria: Subcategoria
):

    subcategoria_existente = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    if not subcategoria_existente.data:
        raise HTTPException(
            status_code=404,
            detail="La subcategoria no existe"
        )

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


@router.delete("/{id_subcategoria}")
def eliminar_subcategoria(id_subcategoria: int):

    subcategoria_existente = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        id_subcategoria
    ).execute()

    if not subcategoria_existente.data:
        raise HTTPException(
            status_code=404,
            detail="La subcategoría no existe"
        )

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