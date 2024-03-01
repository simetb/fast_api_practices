from fastapi import FastAPI

app = FastAPI()

# HTTP GET
@app.get("/")
async def root():
    return {"message":"Hello World!"}

# HTTP GET with the same url but diferent fixed value
@app.get("/items/item_id")
async def read_item():
    return {"item_id" : "FOO"}

# HTTP GET with data
# Data:
#   {itemId : int}
@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id" : item_id}