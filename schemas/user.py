from pydantic import BaseModel

# Clase para definir el esquema que va a tener para crear el usuario
class User(BaseModel):
    email: str
    password: str
