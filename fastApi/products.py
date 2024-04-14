from fastApi import FastAPI

app = FastAPI()


@app.get("/products/")
async def productos():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]
