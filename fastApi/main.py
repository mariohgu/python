from enum import Enum
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
#etre2
app = FastAPI()

class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'cosumables'
    
class Item(BaseModel):
    name:str
    price:float
    count:int
    id:int
    Category:Category
    
items = {
    0: Item (name="Hammer",price=9.99,count=20,id=0,Category=Category.TOOLS),
    1: Item (name="Pliers",price=8.45,count=14,id=1,Category=Category.TOOLS),
    2: Item (name="Nails", price=8.55,count=19,id=2,Category=Category.CONSUMABLES)
}

@app.get('/')
def index() -> dict[str, dict[int, Item]]:
    return{'items':items}

@app.get('/items/{item_id}')
def item_search_id(item_id:int)->Item:
    if item_id not in items:
        raise HTTPException(status_code=404,detail=f'item with {item_id} does not exist')
    return items[item_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)