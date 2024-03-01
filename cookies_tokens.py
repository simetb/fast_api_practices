from fastapi import FastAPI, Cookie

app = FastAPI()

# To get the cookie_token
@app.get("/items/")
async def read_items(cookie_token: str = Cookie(None)):
    return {"cookie_token": cookie_token}
