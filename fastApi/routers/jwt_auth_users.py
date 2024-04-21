from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 30

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


user_db = {
    "mariof": {
        "username": "mariof",
        "full_name": "Mario Figueroa",
        "email": "johndoe@x.com",
        "disabled": False,
        "password": "$2a$12$WBHwUvi2mc78lslTMm5vBOBlJkumim0XWRIYm4KR945lhYBPmF37u",
    },
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@x.com",
        "disabled": True,
        "password": "$2a$12$m6EPus86hceA.PEoLv/uMOGqhQBi6R40WDeOm2MTmGME0DNa3nSiq",
    },
    "willrogers": {
        "username": "willrogers",
        "full_name": "Will Rogers",
        "email": "willrogers@x.com",
        "disabled": False,
        "password": "123457",
    },
}


def search_user_db(username: str):
    if username in user_db:
        return UserDB(**user_db[username])
    else:
        return None


def search_user(username: str):
    if username in user_db:
        return User(**user_db[username])
    else:
        return None


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales invalidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo"
        )
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user_db(form.username)

    if not user_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.utcnow() + access_token_expiration
    access_token = {
        "sub": user_db.username,
        "exp": expire,
    }
    return {
        "access_token": jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM),
        "token_type": "bearer",
    }


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
