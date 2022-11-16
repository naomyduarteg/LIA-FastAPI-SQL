from fastapi import APIRouter
from endpoints import books, users

router = APIRouter()
router.include_router(books.router)
router.include_router(users.router)