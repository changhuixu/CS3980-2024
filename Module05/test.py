from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str | None = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


data = {
    "id": 123,
    "signup_ts": "2024-02-12 13:05",
    "tastes": {"wine": 9, "cabbage": "1"},
}

user = User(**data)

print(repr(user.tastes))

external_data = {"id": "not an int", "tastes": {}}

try:
    User(**external_data)
except ValidationError as e:
    print(e.errors())
