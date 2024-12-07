import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

def devuelve_alumnos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

def devuelve_calificaciones(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()
