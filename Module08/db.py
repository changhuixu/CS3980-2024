from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import os

from models.product import Product


async def init_db():
    conn = os.getenv("DB_CONN")
    client = AsyncIOMotorClient(conn)
    await init_beanie(database=client.get_default_database(), document_models=[Product])
