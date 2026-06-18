from pydantic import BaseModel, Field

class Categoria(BaseModel):

    nombre: str = Field(
        min_length=3,
        max_length=100,
        description="Nombre de la categoría"
    )

    porcentaje_ganancia: float = Field(
        ge=0,
        le=100,
        description="Porcentaje de ganancia"
    )