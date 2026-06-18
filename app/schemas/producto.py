from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio_compra: float
    cantidad_stock: int
    id_subcategoria: int