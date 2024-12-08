import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ----------------- Alumnos -------------------
def devuelve_alumnos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

def alumnos_por_id(sesion:Session, id_alumno: int):
    print("select * from app.alumnos where id = {id_alumno}")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()

def borrar_alumno_por_id(sesion:Session, id_alumno: int):
    print("delete from app.alumnos where id = {id_alumno}")
    usr = alumnos_por_id(sesion, id_alumno)
    if usr is not None:
        sesion.delete(usr)
        sesion.commit()
    respuesta = {
        "mensaje":"Alumno eliminado"
    }

# ----------------- Fotos -------------------
def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

def fotos_por_id(sesion:Session, id_fotos:int):
    print("select * from app.fotos where id = {id_fotos}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_fotos).first()

def fotos_por_id_alumno(sesion:Session, id_alumnos:int):
    print("select * from app.fotos where id_alumnos = {id_alumnos}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_alumnos).all()

def borrar_foto_por_id(sesion:Session, id_foto:int):
    print("delete from app.fotos where id_alumnos = {id_foto}")
    fotos = fotos_por_id(sesion, id_foto)
    if fotos is not None:
        sesion.delete(fotos)
        sesion.commit()
    respuesta = {
        "mensaje":"Foto eliminada"
    }

def borrar_fotos_por_id_alumno(sesion:Session, id_alumnos:int):
    print("delete from app.fotos where id_alumnos = {id_alumnos}")
    fotos = fotos_por_id_alumno(sesion, id_alumnos)
    if fotos is not None:
        for foto_alumn in fotos:
            sesion.delete(foto_alumn)
        sesion.commit()
    respuesta = {
        "mensaje":"Fotos eliminadas"
    }

# ----------------- Calificaciones -------------------
def devuelve_calificaciones(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

def calificaciones_por_id(sesion:Session, id:int):
    print("select * from app.calificaciones where id_alumnos = {id}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id).first()

def calificaciones_por_id_alumno(sesion:Session, id_alumnos:int):
    print("select * from app.calificaciones where id_alumnos = {id_alumnos}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumnos).all()

def borrar_calificacion_por_id(sesion:Session, id_calificacion:int):
    print("delete from app.calificaciones where id_alumnos = {id_calificacion}")
    calificaciones = calificaciones_por_id(sesion, id_calificacion)
    if calificaciones is not None:
        sesion.delete(calificaciones)
        sesion.commit()
    respuesta = {
        "mensaje":"Calificaciones eliminadas"
    }

def borrar_calificaciones_por_id_alumno(sesion:Session, id_alumnos:int):
    print("delete from app.calificaciones where id_alumnos = {id_alumnos}")
    calificaciones = calificaciones_por_id_alumno(sesion, id_alumnos)
    if calificaciones is not None:
        for calificaciones_alum in calificaciones:
            sesion.delete(calificaciones_alum)
        sesion.commit()
    respuesta = {
        "mensaje":"Calificaciones eliminadas"
    }
