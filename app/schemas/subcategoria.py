from pydantic import BaseModel, Field

class Subcategoria(BaseModel):

    nombre: str = Field(
        min_length=3,
        max_length=100,
        description="Nombre de la subcategoría"
    )

    id_categoria: int = Field(
        gt=0,
        description="Id de la categoría"
    )