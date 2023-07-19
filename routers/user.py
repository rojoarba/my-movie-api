from fastapi import APIRouter
from utils.jwtmanager import create_token, validate_token # Importar funcion que creamos para generar token
from pydantic import BaseModel  # Clase para realizar el esquema y para validar datos con Field
from fastapi.responses import JSONResponse
from schemas.user import User # Se importa la clase que sirve como esquema de datos para los usuarios
user_router = APIRouter()

@user_router.post('/login', tags=['auth']) # Ruta para crear un inicio de sesión con el metodo post
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin": # Validación de usuario para crear token
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=token)
