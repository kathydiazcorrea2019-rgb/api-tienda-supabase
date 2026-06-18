from pydantic import BaseModel

class Subcategoria(BaseModel):
    nombre: str
    id_categoria: int