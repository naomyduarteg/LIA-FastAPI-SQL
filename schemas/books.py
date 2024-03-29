from pydantic import BaseModel, Field, validator
from typing import Optional

class BookBase(BaseModel): #creating
    title: str = Field(...)
    author: str = Field(...)
    description: str = Field(..., max_length=1000)
    genre: str = Field(...)
    pages: int = Field(..., gt=0)
    classification: int = Field(..., gt=0)
    

    @validator('classification')
    def classification_must_be(cls, classification):
        classes = [5, 4, 3, 2, 1]
        if classification not in classes:
            raise ValueError(f'Classification must be one of the grades {classes}')
        return classification

    @validator('genre')
    def genre_must_be_in_genres(cls, genre):
        genres = ['Fantasy, Adventure', 'Science Fiction', 'Dystopian', 'Fiction Novel', 'Mystery, Suspense, Horror', 'Graphic Novel', 'Nonfiction']
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

class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    genre: Optional[str]
    pages: Optional[int]
    classification: Optional[int]