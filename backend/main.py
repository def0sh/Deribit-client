from fastapi import FastAPI, APIRouter
from starlette import status

from backend.app.database import Base, engine
from backend.app.routers import currencies
from backend.config import get_settings

search_router = APIRouter(prefix='', tags=['derbit_currencies'])


def start_application():
    app = FastAPI(title=get_settings().APP_TITLE)
    app.include_router(search_router)
    return app


Base.metadata.create_all(bind=engine)

app = start_application()

app.include_router(currencies.router)


@app.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    return {"message": "test", "docs": "/docs"}
