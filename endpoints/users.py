from database import SessionLocal
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import schemas
from crud import crud_users


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/users",
    tags=["Users"])

@router.post("/", response_model=schemas.User, response_description="Create a user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_users.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User], response_description="Get list of users")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_users.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User, response_description="Get user by id")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User with id {user_id} not found")
    return db_user

@router.delete("/{user_id}", response_description="Delete a user")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud_users.delete_user(db, user_id)