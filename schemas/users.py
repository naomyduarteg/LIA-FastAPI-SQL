from pydantic import BaseModel, Field, validator
from schemas.books import Book

class UserBase(BaseModel): #creating
    email: str


class UserCreate(UserBase): #creating
    password: str


class User(UserBase): #reading and returning the id
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True
