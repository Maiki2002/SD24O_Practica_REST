from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# importar el archivo de modelos 
from orm import modelos
import os

#URL_BASE_DATOS = "postgresql://usuario-ejemplo:1234@localhost:5433/bd_alumnos"

#engine = create_engine(URL_BASE_DATOS, connect_args={
#    "options": "-csearch_path=app"
#})

engine = create_engine(os.getenv("db_uri", "sqlite://alumno_ejemplo.db"))
modelos.BaseClass.metadata.create_all(engine)

SessionClass = sessionmaker(engine)

def generar_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()
