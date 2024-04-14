from fastapi import FastAPI, HTTPException
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


@app.post("/paciente/", status_code=201, response_model=Paciente)
async def create_paciente(paciente: Paciente):
    if type(paciente_busqueda(paciente.doc)) == Paciente:
        raise HTTPException(status_code=409, detail="paciente ya existe")
    list_pacientes.append(paciente)
    return paciente


""" {
  "nombre":"Marcio Farfan", 
  "doc":9876, "contacto":"Esteban"
}
"""


@app.put("/paciente/")
async def update_paciente(paciente: Paciente):
    for index, paci in enumerate(list_pacientes):
        if paci.doc == paciente.doc:
            list_pacientes[index] = paciente
            return list_pacientes
    return {"error": "paciente no encontrado"}


@app.delete("/paciente/{doc}")
async def delete_paciente(doc: int):
    for index, paciente in enumerate(list_pacientes):
        if paciente.doc == doc:
            list_pacientes.pop(index)
            return list_pacientes

    return {"error": "paciente no encontrado"}


def paciente_busqueda(doc: int):
    paciente = list(filter(lambda x: x.doc == doc, list_pacientes))
    try:
        return paciente[0]
    except:
        return {"error": "paciente no encontrado"}
