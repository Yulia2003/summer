from ctypes import Union
from datetime import date
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    name: str
    price: float
    date: date
    is_offer: Union[bool, None] = None
