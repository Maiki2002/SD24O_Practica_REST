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