from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
from sqlalchemy.sql import func


def get_total_pages(db: Session, user_id: int):
    total_pages = db.query(func.sum(models.Book.pages)).filter(models.Book.owner_id == user_id).scalar()
     #SELECT SUM(PAGES) FROM BOOKS
    if total_pages:
        return f"You have read {total_pages} pages so far! Keep on reading!"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")

def get_mode_author(db: Session, user_id: int):
    mode_author = db.query(models.Book.author).filter(models.Book.owner_id == user_id).group_by(models.Book.author).order_by(func.count().desc()).limit(1).scalar()
     #SELECT AUTHOR FROM BOOK GROUP BY AUTHOR ORDER BY COUNT(*) DESC LIMIT 1
    top_rated = db.query(models.Book.author).filter(models.Book.owner_id == user_id, models.Book.classification == 'Excellent').group_by(models.Book.author).order_by(func.count(models.Book.classification).desc()).limit(1).scalar()
     #SELECT author FROM books WHERE classification = 'Excellent' GROUP BY author ORDER BY COUNT(classification) DESC LIMIT 1;
    if mode_author and top_rated:
        return f"Your most read and top rated author is, respectively, {mode_author} and {top_rated}."

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")

def get_most_least_genre(db: Session, user_id: int, entry: str):
    if entry == 'most':
        mode_genre = db.query(models.Book.genre).filter(models.Book.owner_id == user_id).group_by(models.Book.genre).order_by(func.count().desc()).limit(1).scalar()
         #SELECT GENRE FROM BOOKS GROUP BY GENRE ORDER BY COUNT(*) DESC LIMIT 1
        return f"Your most read genre is {mode_genre}."
    if entry == 'least':
        least_genre = db.query(models.Book.genre).filter(models.Book.owner_id == user_id).group_by(models.Book.genre).order_by(func.count().asc()).limit(1).scalar()
         #SELECT GENRE FROM BOOKS GROUP BY GENRE ORDER BY COUNT(*) ASC LIMIT 1
        return f"Your least read genre is {least_genre}."
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entry not valid. Choose between 'most' or 'least'.")

def get_class_count(db: Session, user_id: int):
    class_count = db.query(models.Book.classification, func.count(models.Book.classification).label("How many")).filter(models.Book.owner_id == user_id).group_by(models.Book.classification).order_by(func.count(models.Book.classification).desc()).all()
    if class_count:
        return class_count

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")