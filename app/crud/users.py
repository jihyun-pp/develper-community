from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status
from passlib.context import CryptContext
from datetime import datetime

from app.model import User
import app.schema.schemas as schema
from app.core.exceptions import NotFoundException, DuplicateEmailException, BadRequestException
from app.core.token import Token
from app.schema.users.request import *
from app.schema.users.response import *


def modify_user(db: Session, email: str, nickname: str):
    a = db.query(User).filter(User.email == email).all()
    a.nickname = nickname
    db.commit()
    return a.nickname

class UserCrud:
    async def login(self, db: Session, email: str, password: str):
        try:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            user = db.query(User).filter(User.email == email).first()
            if not user:
                raise NotFoundException
            elif not pwd_context.verify(password, user.password):
                raise NotFoundException

            return LoginResponseSchema(
                token=Token.encode(payload={'user_id': user.email}),
                refresh_token=Token.encode(payload={"sub": "refresh"})
            )

        except Exception as e:
            return str(e)

    async def create_user(self, db: Session, req: RequestCreateUser):
        result = {}
        try:
            is_exist = db.query(User).filter(User.email == req.email).first()
            if is_exist:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다.")

            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            user = User(
                email=req.email,
                password=pwd_context.hash(req.password1),
                nickname=req.nickname,
                # birth=req.birth,
                auth='p011',
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )
            db.add(user)
            db.commit()
            result['message'] = 'OK'

        except Exception as e:
            result['message'] = str(e)

        return result