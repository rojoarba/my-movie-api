from models.movie import Movie as MovieModel#Importar la clase para el manejo de tablas de la base de datos
from schemas.movie import Movie # Esquema creado para los datos de las pelis
from typing import List
# CLASE QUE SIRVE COMO SERVICIO
class MovieService():
    def __init__(self, db) -> None: # Metodo constructor para que cada que se llame al servicio se le envie una sesión a la bd
        self.db = db

    def get_movies(self): # Metodo para la obtención de todas las peliculas
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id): # Metodo para la obtención de una pelicula por su id
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category): # Metodo para la obtención de peliculas por su id
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie): # Metodo para crear o registrar pelis en la bd
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 
    
    def update_movie(self, id: int, data: Movie): # Metodo para actualizar datos de una peli filtrando por su id
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, id : int): # Metodo para eliminar una pelicula por su id
        self.db.query(MovieModel).filter(MovieModel == id).delete()
        self.db.commit()
        return 