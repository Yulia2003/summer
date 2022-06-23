from typing import Union
from fastapi import FastAPI
from base import Book


app = FastAPI()

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"key": "Hello" }


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/user/items/{item_id}/{us}")
def get_user_item_id(item_id: int, us: str):
    return {"user": us, "item_id": item_id}

@app.post("/item")
def post_items( item: Item):
    return item