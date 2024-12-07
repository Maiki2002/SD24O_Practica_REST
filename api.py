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

@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generar_sesion)):
    print("Consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generar_sesion)):
    print("Consultando todas las fotos")
    return repo.devuelve_fotos(sesion)

@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generar_sesion)):
    print("Consultando todas las calificaciones")
    return repo.devuelve_calificaciones(sesion)