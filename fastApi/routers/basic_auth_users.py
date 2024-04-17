from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth = OAuth2PasswordBearer(tokenUrl="login")


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
        "password": "12345",
    },
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@x.com",
        "disabled": True,
        "password": "12345",
    },
    "willrogers": {
        "username": "willrogers",
        "full_name": "Will Rogers",
        "email": "willrogers@x.com",
        "disabled": False,
        "password": "12345",
    },
}


def get_user(username: str):
    if username in user_db:
        return UserDB(**user_db[username])
    else:
        return None


async def current_user(token: str = Depends(oauth)):
    user = get_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user"
        )
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
