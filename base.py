from datetime import date
from pydantic import BaseModel, Field, validator
from typing import List

class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str= Field(..., max_length=30)
    writer: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int 


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int = Field(..., gt=14, lt=90, description='Author age must be more than 15' )

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15 > 90:
    #         raise ValueError('Author age must be more than 15')
    #     return v



