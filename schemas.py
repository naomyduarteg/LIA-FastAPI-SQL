from typing import Union

from pydantic import BaseModel, Field, validator


class BookBase(BaseModel): #creating
    title: str = Field(...)
    author: str = Field(...)
    description: str = Field(..., max_length=1000)
    genre: str = Field(...)
    classification: str
    

    @validator('classification')
    def classification_must_be(cls, classification):
        classes = ['Excelent', 'Good', 'Bad']
        if classification not in classes:
            raise ValueError(f'Class must be in {classes}')
        return classification

    @validator('genre')
    def genre_must_be_in_genres(cls, genre):
        genres = ['Fantasy','Science Fiction', 'Dystopian', 'Action and Adventure', 'Mystery', 'Horror', 'Suspense', 'Graphic Novel', 'Nonfiction']
        if genre not in genres:
            raise ValueError(f'Genre must be in {genres}')
        return genre
    

class BookCreate(BookBase): #creating
    pass


class Book(BookBase): #reading and returning the ids 
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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
