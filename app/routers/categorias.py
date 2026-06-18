from fastapi import APIRouter, HTTPException
from app.config.database import supabase
from app.schemas.categoria import Categoria

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)


@router.get("/")
def obtener_categorias():

    respuesta = supabase.table(
        "categorias"
    ).select("*").execute()

    return respuesta.data


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
        "mensaje": "CategorIa creada correctamente",
        "datos": respuesta.data
    }


@router.put("/{id_categoria}")
def actualizar_categoria(id_categoria: int, categoria: Categoria):

    categoria_existente = supabase.table(
        "categorias"
    ).select("*").eq(
        "id_categoria",
        id_categoria
    ).execute()

    if not categoria_existente.data:
        raise HTTPException(
            status_code=404,
            detail="La categoría no existe"
        )

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


@router.delete("/{id_categoria}")
def eliminar_categoria(id_categoria: int):

    categoria_existente = supabase.table(
        "categorias"
    ).select("*").eq(
        "id_categoria",
        id_categoria
    ).execute()

    if not categoria_existente.data:
        raise HTTPException(
            status_code=404,
            detail="La categoría no existe"
        )

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