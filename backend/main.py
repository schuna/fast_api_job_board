from fastapi import FastAPI

from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine
from webapps.base import api_router as webapp_router
from fastapi.staticfiles import StaticFiles


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(fast_app):
    fast_app.include_router(router=api_router)
    fast_app.include_router(router=webapp_router)


def configure_static(fast_app):
    fast_app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    fast_app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(fast_app)
    configure_static(fast_app)

    return fast_app


app = start_application()
