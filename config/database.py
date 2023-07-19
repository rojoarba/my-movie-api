import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite" # Nombre de la base de datos

base_dir = os.path.dirname(os.path.realpath(__file__)) # Se obtiene la dirección local de donde se ubica la base de datos

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" # URL donde se unifica la ubicacion local con el nombre de la base de datos

engine = create_engine(database_url, echo=True) # Se crea el motor de la base de datos

Session = sessionmaker(bind=engine) # Se establece una sesión con la base de datos

Base = declarative_base() # Base para clear las tablas de la base de datos