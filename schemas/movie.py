from pydantic import BaseModel, Field  # Clase para realizar el esquema y para validar datos con Field
from typing import Optional, List

# Clase para el esquema de datos que hereda de BaseModel
class Movie(BaseModel):
    id: Optional[int] = None # Se establece que la entrada id sea opcional
    title: str = Field(min_length=5, max_length=15) #Validación de datos con Field
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)
    # Esquema de ejemplo para establecer valores por defecto en la clase modelo Movie
    model_config= {
            "json_schema_extra": {
                "example": 
                    {
                        "id": 1,
                        "title": "Mi Pelicula",
                        "overview": "Descripcion de la pelicula",
                        "year": 2023,
                        "rating": 9.9,
                        "category": "Acción"
                    }
            }
    }
