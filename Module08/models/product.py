from typing import Annotated, Optional
from beanie import Document, Indexed
from pydantic import BaseModel


class Category(BaseModel):
    name: str
    description: str


class Product(Document):  # this is the model class for MongoDB
    name: str
    description: Optional[str] = None
    price: Annotated[float, Indexed()]
    category: Category

    class Settings:  # pay attention to the spelling. It has an "s" in the end.
        name = "products"
