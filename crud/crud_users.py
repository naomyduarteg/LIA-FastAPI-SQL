from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user_to_delete = db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()

    if user_to_delete == 1:
        return f"Book with id {user_id} deleted sucessfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {user_id} not found!")