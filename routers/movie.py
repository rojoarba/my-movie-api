from fastapi import APIRouter
from fastapi import Depends, Path, Query #Clase Body para parámetros en el body, clase path para validar parámetros, Clase para validad parametros Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session #Importar funciones para el uso de la base de datos
from models.movie import Movie as MovieModel#Importar la clase para el manejo de tablas de la base de datos
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer  # Importar el middleware para autenticar las rutas con token
from services.movie import MovieService # Importa el servicio de peliculas
from schemas.movie import Movie # Se importa la clase que sirve como esquema de datos para las peliculas

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) # se define funcion get / se declara Dependencias para pedir a la función que aplique la clase JWTBearer
def get_movies() -> List[Movie]:
    db = Session() # Se realiza la sesion con la base de datos
    #result = db.query(MovieModel).all() # Se consulta a la bd con la funcion query y se obtiene todos los resultados con la función all
    result = MovieService(db).get_movies() # Se aplica el servicio creado
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) # Se envia como contenido en formato Json

@movie_router.get('/movies/{id}',tags=['movies'], response_model=Movie) # Ruta para enviar parámetros en la url, filtra pelicula por su id
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie: #En la función se define los parámetros a ingresar
    db = Session()
    #result = db.query(MovieModel).filter(MovieModel.id == id).first() # Se establece el filtrado de la base de datos en base al parámetro en la URL con la función filter y la función first obtiene el primer resultado
    result = MovieService(db).get_movie(id) # Se aplica el servicio para el filtrado de la pelicula por su id como parametro
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) # Se envia como contenido en formato Json
    

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie]) #Para establecer parametros query ingresar / al final de la ruta
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    #result = db.query(MovieModel).filter(MovieModel.category == category).all() # Se establece el filtrado de la base de datos en base al parámetro en la URL con la función filter y la función first obtiene el primer resultado
    result = MovieService(db).get_movies_by_category(category) # Se aplica el servicio para la busqueda de pelis por categoria
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Categoria no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) # Se envia como contenido en formato Json

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201) #Metodo post para agregar peliculas
def create_movie(movie: List[Movie]) -> dict: #Con la clase Body se hace que los parámetros sean ingresados en el body de la url
    db = Session() # Se realiza la sesion con la base de datos
    # new_movie = MovieModel(**movie.dict()) # Se crea el objeto de la tabla con la clase MovieModel
    # db.add(new_movie) # Se añade la tabla a la base de datos
    # db.commit() # Se guarda los cambios en la bd
    for info in movie:
        MovieService(db).create_movie(info)
    if len(movie) == 1:
        return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})
    return JSONResponse(status_code=201, content={"message": "Se han registrado las peliculas"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200) #  Metodo put para actualizar datos en base a un id especifico requerido
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    #result = db.query(MovieModel).filter(MovieModel.id == id).first() # Primero se filtra el item a editar por su id
    result = MovieService(db).get_movie(id) # Utilización de la función de filtrado por id del servicio creado
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Pelicula no encontrada'})
    # Como es un objeto, se modifica a travez del resultado seguido de un punto y cada columna
    MovieService(db).update_movie(id, movie) # Utilización de la función de actualización de datos del servicio creado
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200) # Metodo delete para eliminar un elemento de la lista movies en base a un parámetro id
def delete_movie(id: int) -> dict:
    db = Session()
    #result = db.query(MovieModel).filter(MovieModel.id == id).first() # Primero se filtra el item a editar por su id
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Pelicula no encontrada'})
    MovieService(db).delete_movie(id) # Utilización de la función para eliminar una peli por su id
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la pelicula"})