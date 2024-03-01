from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict,List

app = FastAPI()

# You can use a Base model to express how data it will return
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: List[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> List[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
    
@app.post("/items/", response_model=Item)
async def create_itemtwo(item: Item) -> Any:
    return item

@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}