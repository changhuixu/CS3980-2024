from beanie import Document

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class User(Document):
    email: EmailStr = ""
    password: str = ""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "python-web-dev@cs.uiowa.edu", "password": "strong!!!"}
        }
    )

    class Settings:
        name = "users"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
