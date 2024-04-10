from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Paciente(BaseModel):
    nombre: str
    doc: int
    contacto: str


list_pacientes = [
    Paciente(nombre="Mario Figueroa", doc=12345678, contacto="Florinda"),
    Paciente(nombre="Luis Figueroa", doc=87654321, contacto="Leticia"),
    Paciente(nombre="Luisa Figueroa", doc=87654321, contacto="Marcos"),
]


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/mario")
async def mario():
    return {"hello": "mario"}
