from pydantic import BaseModel

class Categoria(BaseModel):
    nombre: str
    porcentaje_ganancia: float