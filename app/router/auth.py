from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

from app.database import get_db
from app.crud import users as crud
from app.core.env import environ
from app.core.token import Token
from app.schema.users import request, response
from app.core.exceptions import NotFoundException
from app.crud.users import UserCrud

router = APIRouter(
    prefix='/auth',
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, key=environ('JWT_SECRET_KEY'), algorithms=environ('JWT_ALGORITHM'))
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = crud.get_user(db, user_id=username)
        if user is None:
            raise credentials_exception
        return user



