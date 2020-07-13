from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}