from httpx import ASGITransport, AsyncClient
import pytest
from auth.hash_password import HashPassword
from database.connection import Settings
from main import app
from models.users import User

hash_password = HashPassword()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/test_db"
    test_settings.SECRET_KEY = "test_secret"

    await test_settings.initialize_database()


@pytest.mark.anyio
async def test_sign_new_user() -> None:
    await init_db()
    # clean up database
    await User.find_all().delete()

    payload = {"email": "python-web-dev@cs.uiowa.edu", "password": "test-password"}

    headers = {"accept": "application/json", "Content-Type": "application/json"}

    test_response = {"message": "User created successfully"}
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://app"
    ) as client:
        response = await client.post("/user/signup", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.anyio
async def test_sign_user_in() -> None:
    await init_db()
    # clean up database
    await User.find_all().delete()
    await User.insert_one(
        User(
            email="test-user@cs.uiowa.edu",
            password=hash_password.create_hash("test-password"),
        )
    )

    payload = {"username": "test-user@cs.uiowa.edu", "password": "test-password"}

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://app"
    ) as client:
        response = await client.post("/user/sign-in", data=payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"
