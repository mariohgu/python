from enum import Enum
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'cosumables'
    
class Item(BaseModel):
    name:str
    price:float
    count:int
    id:int
    category:Category
    
items = {
    0: Item (name="Hammer",price=9.99,count=20,id=0,category=Category.TOOLS),
    1: Item (name="Pliers",price=8.45,count=14,id=1,category=Category.TOOLS),
    2: Item (name="Nails", price=8.55,count=19,id=2,category=Category.CONSUMABLES)
}



@app.get('/')
def index() -> dict[str, dict[int, Item]]:
    return{'items':items}

@app.get('/items/{item_id}')
def item_search_id(item_id:int)->Item:
    if item_id not in items:
        raise HTTPException(status_code=404,detail=f'item with {item_id} does not exist')
    return items[item_id]

Selection = dict[str, str | float | int | Category | None]

@app.get("/items/")
def select_by_data(
    name:str | None = None, 
    price:float | None = None, 
    count:int | None = None, 
    category:Category | None = None ) -> dict[str, Selection]:
    def check_item(item: Item)-> bool:
        return all((
            name is None or item.name == name,
            price is None or item.price == price,
            count is None or item.count == count,
            category is None or item.category is category,
            
        ))
    selection = [item for item in items.values() if check_item(item)]
    return {'query':{'name':name,'price':price,'count':count,'category':category,'selection':selection,}}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)