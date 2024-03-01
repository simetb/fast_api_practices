from typing import Annotated

from fastapi import FastAPI, Query, Path

app = FastAPI()


# None its the same ass ... but when u put None the data parameter still required
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
    

 