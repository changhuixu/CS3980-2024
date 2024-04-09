from contextlib import asynccontextmanager
from functools import lru_cache
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from database.connection import Settings
from logging_setup import setup_logging
from routes.events import event_router
from routes.users import user_router

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup event
    logger.info("Application starts up...")
    await get_settings().initialize_database()
    yield
    # on shutdown event
    ...


app = FastAPI(title="Event Planner", version="1.0.0", lifespan=lifespan)


@lru_cache
def get_settings():
    return Settings()


# register origins

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/events")


@app.get("/")
async def home():
    return RedirectResponse(url="/events/")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
