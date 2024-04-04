from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

SECRET_KEY = "a2ddad598b891e78cbbc00c4d53c8346a58c29f6a1dd4b4ce05c13b999a0c3e1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token:
    access_token: str
    token_type: str


class TokenPayload:
    def __init__(self, username: str | None, exp: int | None) -> None:
        self.username = username
        self.exp = exp
        self.exp_datetime = datetime.fromtimestamp(exp)

    def __str__(self) -> str:
        return f"username=[]"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt_token(token: str) -> TokenPayload | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        exp: int = payload.get("exp")
        return TokenPayload(username, exp)
    except JWTError:
        print("invalid JWT token")


my_token = create_access_token(
    data={"sub": "my_username"},
    expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
)

print(my_token)

payload = decode_jwt_token(my_token)
print(payload.username)
print(payload.exp_datetime)
