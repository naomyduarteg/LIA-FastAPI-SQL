from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_user_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_book = models.Book(**book.dict(), owner_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books_by_classification(db: Session, classification: str):
    return db.query(models.Book).filter(models.Book.classification == classification).all()

def get_books_by_author(db: Session, author: str):
    return db.query(models.Book).filter(models.Book.author == author).all()

def get_books_by_genre(db: Session, genre: str):
    return db.query(models.Book).filter(models.Book.genre == genre).all()

def delete_user_book(db: Session, book_id: int):
    book_to_delete = db.query(models.Book).filter(models.Book.id == book_id).delete()
    db.commit()

    if book_to_delete == 1:
        return f"Book with id {book_id} deleted sucessfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found!")