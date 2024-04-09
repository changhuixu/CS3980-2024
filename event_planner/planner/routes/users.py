import logging
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.connection import Database
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.users import User, TokenResponse

logger = logging.getLogger(__name__)

user_router = APIRouter(
    tags=["User"],
)

user_database = Database(User)
hash_password = HashPassword()


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    logger.info(f"User [{user.email}] is signing up.")
    user_exist = await User.find_one(User.email == user.email)

    if user_exist:
        logger.warning(f"\t User [{user.email}] has already signed up.")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already.",
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    logger.info(f"\t User [{user.email}] is created.")
    return {"message": "User created successfully"}


@user_router.post("/sign-in", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    logger.info(f"User [{user.username}] is signing in the system.")
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        logger.warning(f"\t User [{user.username}] not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist.",
        )
    if hash_password.verify_hash(user.password, user_exist.password):
        logger.warning(f"\t User [{user.username}] signed in")
        access_token = create_access_token(user_exist.email)
        return {"access_token": access_token, "token_type": "Bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid details passed."
    )
