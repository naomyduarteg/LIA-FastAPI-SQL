from fastapi import APIRouter
from endpoints import books, users, stats

router = APIRouter()
router.include_router(books.router)
router.include_router(users.router)
router.include_router(stats.router)
# router.include_router(ml.router)