from database import SessionLocal
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import schemas
from crud import crud_books

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/books",
    tags=["Books"])

@router.post("/{user_id}", response_model=schemas.Book, response_description="Create a book")
def create_book_for_user(
    user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud_books.create_user_book(db=db, book=book, user_id=user_id)


@router.get("/", response_model=list[schemas.Book], response_description="List book")
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud_books.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/classification/{classification}", response_model=list[schemas.Book], response_description="List books by classification")
def class_books(classification: str, db: Session = Depends(get_db)):
    books = crud_books.get_books_by_classification(db, classification)
    return books

@router.get("/author/{author}", response_model=list[schemas.Book], response_description="List books by author")
def class_books(author: str, db: Session = Depends(get_db)):
    books = crud_books.get_books_by_author(db, author)
    return books

@router.get("/genre/{genre}", response_model=list[schemas.Book], response_description="List books by genre")
def class_books(genre: str, db: Session = Depends(get_db)):
    books = crud_books.get_books_by_genre(db, genre)
    return books

@router.delete("/{book_id}", response_description="Delete a book")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud_books.delete_user_book(db, book_id)