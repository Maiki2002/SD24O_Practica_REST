from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo
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
