from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()

# How to get a Header parameter
@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}