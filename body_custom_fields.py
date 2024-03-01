
from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# Sub Models
class Image(BaseModel):
    name: str
    url: HttpUrl

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    image: Image | None = None

# Instead of do the request 
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }

# You can do the request like this just ussing the Body()
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


