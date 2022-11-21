from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.books import Book, BookCreate, UpdateBook
from crud import crud_books
from endpoints.users import get_db


router = APIRouter(prefix="/books",
    tags=["Books"])

@router.post("/{user_id}", response_model=Book, response_description="Create a book")
def create_book_for_user(user_id: int, book: BookCreate, db: Session = Depends(get_db)): 
    return crud_books.create_user_book(db=db, book=book, user_id=user_id)


@router.get("/", response_model=list[Book], response_description="List book")
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud_books.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/classification/{classification}", response_model=list[Book], response_description="List books by classification")
def class_books(user_id: int, classification: str, db: Session = Depends(get_db)):
    books = crud_books.get_books_by_classification(db, user_id, classification)
    return books

@router.get("/author/{author}", response_model=list[Book], response_description="List books by author")
def class_books(user_id: int, author: str, db: Session = Depends(get_db)):
    books = crud_books.get_books_by_author(db, user_id, author)
    return books

@router.get("/genre/{genre}", response_model=list[Book], response_description="List books by genre")
def class_books(user_id: int, genre: str, db: Session = Depends(get_db)):
    books = crud_books.get_books_by_genre(db, user_id, genre)
    return books

@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(user_id: int, book_id: int, book: UpdateBook, db: Session = Depends(get_db)):
    return crud_books.update_book(db, user_id, book_id, book)

@router.delete("/{book_id}", response_description="Delete a book")
def delete_book(user_id: int, book_id: int, db: Session = Depends(get_db)):
    return crud_books.delete_user_book(db, user_id, book_id)