from fastapi import APIRouter

from app.routers.login import router as login
from app.routers.signup import router as signup
from app.routers.score import router as score

router = APIRouter()

router.include_router(login)
router.include_router(score)
router.include_router(signup)
