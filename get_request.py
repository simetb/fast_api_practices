from enum import Enum
from fastapi import FastAPI
from  typing import Union

class ModelName(str, Enum):
    test_one = "FOO"
    test_two = "TEST"

app = FastAPI()

# HTTP GET REQUEST EXAMPLE
@app.get("/models/{model_name}")
async def get_mmodel(model_name: ModelName):
    if(model_name == ModelName.test_one):
        return {"model_name": model_name, "message": "Im test_one"}
    else:
        return {"model_name": model_name, "message": "Im test_two"}

# Get a path from a get request
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# There u can see the diferent option variable config that u can use in your functions
@app.get("/query/{item_id}")
async def read_query_params(
    item_id:str,
    needy:str,
    skip: int = 0,
    limit: Union[int,None] = None
):
    item = {"item_id" : item_id, "needy" : needy, "skip" : skip, "limit" : limit}
    return item
