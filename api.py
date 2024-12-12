from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from orm.config import generar_sesion

app = FastAPI()

@app.get("/")
def hola_mundo():
    print("Prueba para ver si funciona")
    respuesta = {
        "mensaje": "Hola"
    }

    return respuesta
# ----------------- Alumnos -------------------
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generar_sesion)):
    print("Consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id:int, sesion:Session=Depends(generar_sesion)):
    print("Consultando los alumnos por id")
    return repo.alumnos_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_alumno(id: int, sesion: Session=Depends(generar_sesion)):
    return repo.calificaciones_por_id_alumno(sesion,id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_alumno(id: int, sesion: Session=Depends(generar_sesion)):
    return repo.fotos_por_id_alumno(sesion,id)

@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_por_alumno(id:int, sesion:Session=Depends(generar_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    return {
        "calificaciones borradas","ok"
    }

@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_por_id_alumno(id:int, sesion:Session=Depends(generar_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion, id)
    return {
        "fotos borradas","ok"
    }

@app.delete("/alumnos/{id}")
def borrar_alumno_por_id(id:int, sesion:Session=Depends(generar_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    repo.borrar_fotos_por_id_alumno(sesion, id)
    repo.borrar_alumno_por_id(sesion, id)
    return {
        "alumno borrado","ok"
    }

@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnoBase, sesion:Session=Depends(generar_sesion)):
    print(alumno)
    repo.guardar_alumno(sesion,alumno)

@app.put("/alumnos/{id}")
def actualizar_alumno(id:int, alumno: esquemas.AlumnoBase, sesion:Session=Depends(generar_sesion)):
 repo.actualiza_alumno(sesion, id, alumno)

# ----------------- Fotos -------------------
@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generar_sesion)):
    print("Consultando la foto por id")
    return repo.fotos_por_id(sesion, id)

@app.delete("/fotos/{id}")
def borrar_foto_por_id(id:int, sesion:Session=Depends(generar_sesion)):
    repo.borrar_foto_por_id(sesion,id)
    return {
        "foto borrada","ok"
    }

@app.post("/alumnos/{id}/fotos")
def guardar_foto_por_id_alumno(id:int, foto: esquemas.FotoBase, sesion:Session=Depends(generar_sesion)):
    repo.guardar_foto_por_id_alumno(sesion, id, foto)

@app.put("/fotos/{id}")
def actualizar_foto(id:int, foto: esquemas.FotoBase, sesion:Session=Depends(generar_sesion)):
    repo.actualizar_foto(sesion, id, foto)
# ----------------- Calificaciones -------------------
@app.get("/calificaciones/{id}")
def lista_calificaciones(id:int, sesion:Session=Depends(generar_sesion)):
    print("Consultando todas las calificaciones")
    return repo.calificaciones_por_id(sesion, id)

@app.delete("/calificaciones/{id}")
def borrar_calificacion_por_id(id:int, sesion:Session=Depends(generar_sesion)):
    repo.borrar_calificacion_por_id(sesion, id)
    return {
        "calificacion borrada","ok"
    }

@app.post("/alumnos/{id}/calificaciones")
def guardar_calificacion(id:int,calificacion:esquemas.CalificacionBase, sesion:Session=Depends(generar_sesion)):
    print(calificacion)
    repo.guardar_calificaciones_por_id_alumno(sesion, id, calificacion)

@app.put("/calificaciones/{id}")
def actualizar_calificacion(id:int, calificacion: esquemas.CalificacionBase, sesion:Session=Depends(generar_sesion)):
    repo.actualizar_calificacion(sesion, id, calificacion)