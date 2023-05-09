from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status
from passlib.context import CryptContext
from jose import jwt, JWTError
from dotenv import load_dotenv
from os import environ
from datetime import datetime, timedelta

from app.database import get_db
from app.crud import users as crud

router = APIRouter(
    prefix='/auth',
)

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/login", tags=['LOGIN'], summary='로그인')
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
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
    access_token = jwt.encode(data, 'SECRET_KEY', algorithm="HS256")

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.user_id
    }

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
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