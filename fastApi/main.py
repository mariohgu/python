from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/mario")
async def mario():
    return {"hello": "mario"}
