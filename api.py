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
# ----------------- Fotos -------------------
@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generar_sesion)):
    print("Consultando todas las fotos")
    return repo.devuelve_fotos(sesion)

@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generar_sesion)):
    print("Consultando la foto por id")
    return repo.fotos_por_id(sesion, id)
# ----------------- Calificaciones -------------------
@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generar_sesion)):
    print("Consultando todas las calificaciones")
    return repo.devuelve_calificaciones(sesion)