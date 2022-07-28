from datetime import datetime, timedelta
from typing import Optional

import bcrypt


from fastapi import Depends, FastAPI, Security, HTTPException
from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPAuthorizationCredentials,
    OAuth2PasswordRequestForm,
)

from pydantic import BaseModel
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError

app = FastAPI()
Security = HTTPBearer()
Security_B = HTTPBasic()

# http base
@app.get("/users/me")
def get_current_user(credentials:HTTPBasicCredentials = Depends(Security_B)):
    return {"username": credentials.username, "password": credentials.password}


ALGORITHM = "HS256"
SECRET_KEY = "3c593c123e9d13794f20264e22e80da48fc35b96d12aaafcfa78251f30388f17"
fake_user_db = {
    "fastcampus": {
        "id": 1,
        "username": "fastcampus",
        "email": "fastcampus@fastcampus.com",
        "password": "$2b$12$kEsp4W6Vrm57c24ez4H1R.rdzYrXipAuSUZR.hxbqtYpjPLWbYtwS",
    }
}

class User(BaseModel):
    id: int
    username: str
    email: str


class UserPayload(User):
    exp: datetime


async def create_access_token(data: dict, exp: Optional[timedelta] = None):
    expire = datetime.utcnow() + (exp or timedelta(minutes=30))
    user_info = UserPayload(**data, exp=expire)

    return jwt.encode(user_info.dict(), SECRET_KEY, algorithm=ALGORITHM)


async def get_user(cred: HTTPAuthorizationCredentials = Depends(Security)):
    token = cred.credentials
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(401, "Expired")
    except JWTClaimsError:
        raise HTTPException(400, "잘못된 claims")
    user_info = User(**decoded_data)

    return fake_user_db[user_info.username]

@app.post("/login")
async def issue_token(data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db[data.username]

    if bcrypt.checkpw(data.password.encode(), user["password"].encode()):
        return await create_access_token(user, exp=timedelta(minutes=30))
    raise HTTPException(401)


@app.get("/login/me", response_model=User)
async def get_current_user(user: dict = Depends(get_user)):
    return user