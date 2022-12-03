from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from crud import crud_stats
from endpoints.users import get_db

router = APIRouter(prefix="/statistics",
    tags=["Statistics"])

@router.get("/pages/{total_pages}", response_description="Total pages read")
def total_pages(user_id: int, db: Session = Depends(get_db)):
    total_pages = crud_stats.get_total_pages(db, user_id)
    return total_pages

@router.get("/author/{most_read_top_rated_author}", response_description="Most read and top rated author")
def most_read_top_rated_author(user_id: int, db: Session = Depends(get_db)):
    mode_author = crud_stats.get_mode_author(db, user_id)
    return mode_author

@router.get("/genre/{most_least_read_genre}", response_description="Most and least read genre")
def genre(user_id: int, entry: str, db: Session = Depends(get_db)):
    genre = crud_stats.get_most_least_genre(db, user_id, entry)
    return genre

@router.get("/classification/", response_description="Ordered classifications")
def class_order(user_id: int, db: Session = Depends(get_db)):
    class_count = crud_stats.get_class_count(db, user_id)
    return class_count

@router.get("/classification/{top_books}", response_description="Choose n to see the n top books from all users")
def top_books(n: int = 5, db: Session = Depends(get_db)):
    top_books = crud_stats.get_top_n_books(db, n)
    return top_books