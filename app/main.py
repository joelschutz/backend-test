from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymodm.connection import connect

from app.settings import settings
from app.routers import router

api = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    debug=settings.DEBUG
)

api.mount("/static", StaticFiles(directory="app/static"), name="static")

api.include_router(router)

connect(settings.MONGODB_URI, settings.TITLE)
