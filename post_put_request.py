from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# POST REQUEST
@app.post("/items/")
async def create_item(item: Item):
    return item

# PUT REQUEST
@app.put("/items_put/{items_id}")
async def see_item(items_id: int, item: Item):
    return {"items_id": items_id, **item.dict()}