from fastapi import FastAPI, status

app = FastAPI()

# U can use this
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# Or this
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_items(name: str):
    return {"name": name}