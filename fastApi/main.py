from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Paciente(BaseModel):
    nombre: str
    doc: int
    contacto: str


list_pacientes = [
    Paciente(nombre="Mario Figueroa", doc=1234, contacto="Florinda"),
    Paciente(nombre="Luis Figueroa", doc=8765, contacto="Leticia"),
    Paciente(nombre="Luisa Figueroa", doc=8965, contacto="Marcos"),
]


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/mario")
async def mario():
    return {"hello": "mario"}


@app.get("/paciente/{doc}")
async def get_pacientes(doc: int):
    return paciente_busqueda(doc)


@app.get("/paciente/")
async def get_pacientes(doc: int):
    return paciente_busqueda(doc)


@app.get("/pacientes/")
async def get_pacientes():
    return list_pacientes


@app.post("/paciente/")
async def create_pacientes(paciente: Paciente):
    if paciente_busqueda(paciente.doc):
        return {"error": "paciente ya existe"}
    list_pacientes.append(paciente)
    return list_pacientes


def paciente_busqueda(doc: int):
    paciente = list(filter(lambda x: x.doc == doc, list_pacientes))
    try:
        return paciente[0]
    except:
        return {"error": "paciente no encontrado"}
