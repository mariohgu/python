from fastapi import APIRouter

router = APIRouter(
    prefix="/products", tags=["products"], responses={404: {"description": "Not found"}}
)

product_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def productos():
    return product_list


@router.get("/{id}")
async def producto(id: int):
    return product_list[id]
