from beanie import Document
from pydantic import BaseModel, ConfigDict, Field


class Event(Document):
    creator: str = ""
    title: str = ""
    image: str = ""
    description: str = ""
    tags: list[str] = []
    location: str = ""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Project 1 Presentation",
                "image": "https://placehold.co/600x400?text=Project+1+Presentation",
                "description": "Each student will present their FastAPI project to demo basic CRUD operations.",
                "tags": [
                    "python",
                    "fastapi",
                    "project",
                    "presentation",
                    "midterm exam",
                ],
                "location": "168 VAN",
            }
        }
    )

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: str = ""
    image: str = ""
    description: str = ""
    tags: list[str] = []
    location: str = ""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Project 1 Presentation",
                "image": "https://placehold.co/600x400?text=Project+1+Presentation",
                "description": "Each student will present their FastAPI project to demo basic CRUD operations.",
                "tags": [
                    "python",
                    "fastapi",
                    "project",
                    "presentation",
                    "midterm exam",
                ],
                "location": "168 VAN",
            }
        }
    )
