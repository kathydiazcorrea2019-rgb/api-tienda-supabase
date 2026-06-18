from pydantic import BaseModel, Field

class Producto(BaseModel):

    nombre: str = Field(
        min_length=3,
        max_length=100,
        description="Nombre del producto"
    )

    descripcion: str = Field(
        min_length=3,
        max_length=255,
        description="Descripcion del producto"
    )

    precio_compra: float = Field(
        gt=0,
        description="Precio de compra"
    )

    cantidad_stock: int = Field(
        ge=0,
        description="Cantidad disponible"
    )

    id_subcategoria: int = Field(
        gt=0,
        description="Id de la subcategoria"
    )