from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import products, pacientes, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(pacientes.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/mario")
async def mario():
    return {"hello": "mario"}
