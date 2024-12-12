import orm.modelos as modelos
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from sqlalchemy import and_
import datetime

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

def guardar_alumno(sesion:Session, alumn_nuevo: esquemas.AlumnoBase):
    alumn_bd = modelos.Alumno()

    alumn_bd.nombre = alumn_nuevo.nombre
    alumn_bd.edad = alumn_nuevo.edad
    alumn_bd.domicilio = alumn_nuevo.domicilio
    alumn_bd.carrera = alumn_nuevo.carrera
    alumn_bd.trimestre = alumn_nuevo.trimestre
    alumn_bd.email = alumn_nuevo.email
    alumn_bd.password =  alumn_nuevo.password

    sesion.add(alumn_bd)
    sesion.commit()
    sesion.refresh(alumn_bd)
    return alumn_bd

def actualiza_alumno(sesion:Session, id_alumn:int, alumn_esquema: esquemas.AlumnoBase):
    alumn_bd = alumnos_por_id(sesion,id_alumn)

    if alumn_bd is not None:
        alumn_bd.nombre = alumn_esquema.nombre
        alumn_bd.edad = alumn_esquema.edad
        alumn_bd.domicilio = alumn_esquema.domicilio
        alumn_bd.carrera = alumn_esquema.carrera
        alumn_bd.trimestre = alumn_esquema.trimestre
        alumn_bd.email = alumn_esquema.email
        alumn_bd.password =  alumn_esquema.password

        sesion.commit()
        sesion.refresh(alumn_bd)
        return alumn_esquema
    else:
        respuesta = {"mensaje" : "No existe el alumno"} 

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

def guardar_foto_por_id_alumno(sesion:Session, id_alumno:int,foto_nuevo:esquemas.FotoBase):
    foto = fotos_por_id_alumno(sesion,id_alumno)

    if foto is not None:
        foto_bd = modelos.Foto()
        foto_bd.id_alumno = id_alumno
        foto_bd.titulo = foto_nuevo.titulo
        foto_bd.descripcion = foto_nuevo.descripcion
        foto_bd.ruta = foto_nuevo.ruta
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd

def actualizar_foto(sesion:Session, id_foto:int, foto_nuevo:esquemas.FotoBase):
    foto = fotos_por_id(sesion, id_foto)

    if foto is not None:
        foto.titulo = foto_nuevo.titulo
        foto.descripcion = foto_nuevo.descripcion
        foto.ruta = foto_nuevo.ruta
        sesion.commit()
        sesion.refresh(foto)
        return foto_nuevo
    else:
        respuesta = {"mensaje" : "No existe la calificación"}

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

def guardar_calificaciones_por_id_alumno(sesion:Session, id_alumno:int,calif_nuevo:esquemas.CalificacionBase):
    calificacion = calificaciones_por_id_alumno(sesion, id_alumno)

    if calificacion is not None:
        calif_bd = modelos.Calificacion()
        calif_bd.id_alumno = id_alumno
        calif_bd.uea = calif_nuevo.uea
        calif_bd.calificacion = calif_nuevo.calificacion
        sesion.add(calif_bd)
        sesion.commit()
        sesion.refresh(calif_bd)
        return calif_bd
    
def actualizar_calificacion(sesion:Session, id_calificacion:int, calif_nuevo:esquemas.CalificacionBase):
    calificacion = calificaciones_por_id(sesion, id_calificacion)

    if calificacion is not None:
        calificacion.uea = calif_nuevo.uea
        calificacion.calificacion = calif_nuevo.calificacion
        sesion.commit()
        sesion.refresh(calificacion)
        return calif_nuevo
    else:
        respuesta = {"mensaje" : "No existe la calificación"}