from fastapi import FastAPI  #Clase Body para parámetros en el body, clase path para validar parámetros, Clase para validad parametros Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel  # Clase para realizar el esquema y para validar datos con Field
from utils.jwtmanager import create_token, validate_token # Importar funcion que creamos para generar token
from config.database import engine, Base #Importar funciones para el uso de la base de datos
from middlewares.error_handler import ErrorHandler # Importar el middleware creado  para el manejo de errores
from routers.movie import movie_router
from routers.user import user_router
# Se inicializa FASTAPI en app y se configura el titulo y version 
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler) # se añade el middleware a la app

app.include_router(movie_router) # Se añade la ruta de las peliculas a la app

app.include_router(user_router) # Se añade la ruta de usuarios a la app


Base.metadata.create_all(bind=engine) #Inicializa la base de datos

# Lista de peliculas en formato diccionario
movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }, 
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>') # Uso de clase para retornar HTML

