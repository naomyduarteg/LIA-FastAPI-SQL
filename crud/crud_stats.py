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
     #SELECT AUTHOR FROM BOOK WHERE owner_id = user_id GROUP BY AUTHOR ORDER BY COUNT(*) DESC LIMIT 1
    top_rated = db.query(models.Book.author).filter(models.Book.owner_id == user_id, models.Book.classification == 5).group_by(models.Book.author).order_by(func.count(models.Book.classification).desc()).limit(1).scalar()
     #SELECT author FROM books WHERE owner_id = user_id AND classification = 5 GROUP BY author ORDER BY COUNT(classification) DESC LIMIT 1;
    if mode_author and top_rated:
        return f"Your most read and top rated author are, respectively, {mode_author} and {top_rated}."

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")

def get_most_least_genre(db: Session, user_id: int, entry: str):
    if entry == 'most':
        mode_genre = db.query(models.Book.genre).filter(models.Book.owner_id == user_id).group_by(models.Book.genre).order_by(func.count().desc()).limit(1).scalar()
         #SELECT GENRE FROM BOOKS WHERE owner_id = user_id GROUP BY GENRE ORDER BY COUNT(*) DESC LIMIT 1
        return f"Your most read genre is {mode_genre}."
    if entry == 'least':
        least_genre = db.query(models.Book.genre).filter(models.Book.owner_id == user_id).group_by(models.Book.genre).order_by(func.count().asc()).limit(1).scalar()
         #SELECT GENRE FROM BOOKS WHERE owner_id = user_id GROUP BY GENRE ORDER BY COUNT(*) ASC LIMIT 1
        return f"Your least read genre is {least_genre}."
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entry not valid. Choose between 'most' or 'least'.")

def get_class_count(db: Session, user_id: int):
    class_count = db.query(models.Book.classification, func.count(models.Book.classification).label("How many")).filter(models.Book.owner_id == user_id).group_by(models.Book.classification).order_by(func.count(models.Book.classification).desc()).all()
    #SELECT classification, COUNT(classification) as "How many" from Book WHERE owner_id = user_id GROUP BY classification ORDER BY COUNT(classification) DESC
    if class_count:
        return class_count

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")

def get_top_n_books(db: Session, n: int = 5):
    top_books = db.query(models.Book.title).group_by(models.Book.title).order_by(func.sum(models.Book.classification).desc()).limit(n).all()
    #SELECT title FROM Book GROUP BY title ORDER BY SUM(classification) DESC LIMIT n
    if top_books:
        return f"The {n} top rated books from all users are {top_books}"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")

def most_read_books_and_mean_class(db: Session, n: int=5):
    mrbamc = db.query(models.Book.title, func.count(models.Book.title), func.round(func.avg(models.Book.classification),2)).group_by(models.Book.title).order_by(func.count(models.Book.title).desc()).limit(n).all()
    #SELECT title, COUNT(title), ROUND(AVG(classification),2) from Book GROUP BY title ORDER BY COUNT(title) DESC LIMIT n
    if mrbamc:
        return f"The {n} most read books, the number of users who read them and their respective average classification: {mrbamc}"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")

def get_book_title(db: Session, book_id: int):
    title = db.query(models.Book.title).filter(models.Book.id == book_id).one()
    if title:
        return f"You choose the book {title}. Here are the most similar ones to it:"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found!")