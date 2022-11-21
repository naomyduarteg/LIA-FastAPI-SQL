from pydantic import BaseModel, Field, validator


#input data for the ML model
class Input(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    genre: str = Field(...)
    pages: int = Field(..., gt=0)

    @validator('genre')
    def genre_must_be_in_genres(cls, genre):
        genres = ['Fantasy, Adventure', 'Science Fiction', 'Dystopian', 'Fiction Novel', 'Mystery, Suspense, Horror', 'Graphic Novel', 'Nonfiction']
        if genre not in genres:
            raise ValueError(f'Genre must be in {genres}')
        return genre

#output data from the ML model
class Output(BaseModel):
    label: str 
    prediction: int 

