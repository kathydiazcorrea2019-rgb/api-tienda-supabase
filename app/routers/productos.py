from fastapi import APIRouter
from app.config.database import supabase
from app.schemas.producto import Producto

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# Obtener productos
@router.get("/")
def obtener_productos():

    respuesta = supabase.table(
        "productos"
    ).select("*").execute()

    return respuesta.data


# Crear producto
@router.post("/")
def crear_producto(producto: Producto):

    subcategoria = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        producto.id_subcategoria
    ).execute()

    id_categoria = subcategoria.data[0]["id_categoria"]

    categoria = supabase.table(
        "categorias"
    ).select("*").eq(
        "id_categoria",
        id_categoria
    ).execute()

    porcentaje = categoria.data[0]["porcentaje_ganancia"]

    precio_venta = producto.precio_compra + (
        producto.precio_compra * porcentaje / 100
    )

    respuesta = supabase.table(
        "productos"
    ).insert(
        {
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio_compra": producto.precio_compra,
            "porcentaje_aplicado": porcentaje,
            "precio_venta": precio_venta,
            "cantidad_stock": producto.cantidad_stock,
            "id_subcategoria": producto.id_subcategoria
        }
    ).execute()

    return {
        "mensaje": "Producto registrado correctamente",
        "porcentaje_aplicado": porcentaje,
        "precio_venta": precio_venta,
        "datos": respuesta.data
    }


# Actualizar producto
@router.put("/{id_producto}")
def actualizar_producto(
    id_producto: int,
    producto: Producto
):

    subcategoria = supabase.table(
        "subcategorias"
    ).select("*").eq(
        "id_subcategoria",
        producto.id_subcategoria
    ).execute()

    id_categoria = subcategoria.data[0]["id_categoria"]

    categoria = supabase.table(
        "categorias"
    ).select("*").eq(
        "id_categoria",
        id_categoria
    ).execute()

    porcentaje = categoria.data[0]["porcentaje_ganancia"]

    precio_venta = producto.precio_compra + (
        producto.precio_compra * porcentaje / 100
    )

    respuesta = supabase.table(
        "productos"
    ).update(
        {
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio_compra": producto.precio_compra,
            "porcentaje_aplicado": porcentaje,
            "precio_venta": precio_venta,
            "cantidad_stock": producto.cantidad_stock,
            "id_subcategoria": producto.id_subcategoria
        }
    ).eq(
        "id_producto",
        id_producto
    ).execute()

    return {
        "mensaje": "Producto actualizado correctamente",
        "datos": respuesta.data
    }


# Eliminar producto
@router.delete("/{id_producto}")
def eliminar_producto(id_producto: int):

    respuesta = supabase.table(
        "productos"
    ).delete().eq(
        "id_producto",
        id_producto
    ).execute()

    return {
        "mensaje": "Producto eliminado correctamente",
        "datos": respuesta.data
    }
