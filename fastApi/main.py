from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import products, pacientes
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(pacientes.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/mario")
async def mario():
    return {"hello": "mario"}
