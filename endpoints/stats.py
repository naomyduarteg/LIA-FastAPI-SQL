from database import SessionLocal
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.books import Book, BookCreate, UpdateBook
from crud import crud_stats
from endpoints.users import get_db

router = APIRouter(prefix="/statistics",
    tags=["Statistics"])

@router.get("/pages/{total_pages}", response_description="Total pages read")
def total_pages(user_id: int, db: Session = Depends(get_db)):
    total_pages = crud_stats.get_total_pages(db, user_id)
    return total_pages

@router.get("/author/{most_read_author}", response_description="Most read author")
def mode_author(user_id: int, db: Session = Depends(get_db)):
    mode_author = crud_stats.get_mode_author(db, user_id)
    return mode_author

@router.get("/genre/{most_least_read_genre}", response_description="Most read genre")
def genre(user_id: int, entry: str, db: Session = Depends(get_db)):
    genre = crud_stats.get_most_least_genre(db, user_id, entry)
    return genre

# @router.get("/genre/{least_read_genre}", response_description="Least read genre")
# def least_read_genre(user_id: int, db: Session = Depends(get_db)):
#     mode_genre = crud_stats.get_least_read_genre(db, user_id)
#     return mode_genre