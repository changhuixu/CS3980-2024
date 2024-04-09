import json
from typing import Any

from beanie import init_beanie, PydanticObjectId
from pydantic_settings import BaseSettings, SettingsConfigDict
from models.events import Event
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field


class Settings(BaseSettings):
    DATABASE_URL: str = Field(default="")
    SECRET_KEY: str = Field(default="")

    model_config = SettingsConfigDict(env_file=".env")

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(), document_models=[Event, User]
        )


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> PydanticObjectId:
        m = await document.create()
        return m.id

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> list[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.model_dump_json(exclude_defaults=True)
        des_body = json.loads(des_body)
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.set(des_body)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
