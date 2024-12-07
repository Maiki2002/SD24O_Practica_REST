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

def borrar_alumnos_por_id(sesion:Session, id_alumno: int):
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

def fotos_por_id(sesion:Session, id_fotos):
    print("select * from app.fotos where id = {id_fotos}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_fotos).first()

def fotos_por_id_alumno(sesion:Session, id_alumnos):
    print("select * from app.fotos where id_alumnos = {id_alumnos}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumnos == id_alumnos).first()

# ----------------- Calificaciones -------------------
def devuelve_calificaciones(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()
