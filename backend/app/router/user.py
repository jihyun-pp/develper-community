from dotenv import load_dotenv
from os import environ
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional

import app.schema.schemas as schema
from app.crud import user as crud
from app.database import get_db

router = APIRouter(
    prefix='/api/user',
)

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

@router.get("/list", response_model=list[schema.User])
def get_user_list(db: AsyncSession = Depends(get_db)):
    result = crud.user_list(db=db)
    return result

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def create_user(_create_user: schema.CreateUser, db: AsyncSession = Depends(get_db)):
    check_duplicate = crud.get_existing_user(db=db, _create_user=_create_user)
    if check_duplicate:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다.")
    else:
        user = crud.create_user(db=db, _create_user=_create_user)


@router.get('/{user_id}', response_model=schema.User)
def get_userid(user_id: str, db: AsyncSession = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    return user


@router.post("/contests")
def user_contents(uid: int, db: Session = Depends(get_db)):
    result = crud.get_user_contents(db=db, uid=uid)
    return result


@router.post("/login", response_model=schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # check user and password
    user = crud.get_user(db, user_id=form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {
        "sub": user.user_id,
        "exp": datetime.utcnow() + timedelta(minutes=60*60*24)
    }
    access_token = jwt.encode(data, environ['SECRET_KEY'], algorithm="HS256")

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.user_id
    }


def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, environ['SECRET_KEY'], algorithms="HS256")
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