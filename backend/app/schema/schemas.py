import uuid

from pydantic import BaseModel, validator, EmailStr
from datetime import datetime
from typing import Optional
import uuid

class User(BaseModel):
    uid: int
    user_id: str
    password: str
    username: str
    email: str
    auth: str | None = None
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    user_id: str
    password1: str
    password2: str
    username: str
    email: EmailStr

    @validator('user_id', 'password1', 'username', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('user_id')
    def userid_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    @validator('password2')
    def password_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str


class Category(BaseModel):
    cid: int
    category_nm: str

    class Config:
        orm_mode = True


class Board(BaseModel):
    bid: int
    category: int
    uid: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime
    hit: int
    imgPath: str | None = None

    class Config:
        orm_mode = True

class CreateBoard(BaseModel):
    category: int
    uid: int
    title: str
    content: str
    imgPath: str | None = None

    @validator('title', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class UpdateBoard(BaseModel):
    title: str
    content: str
    imgPath: str | None = None
    updatedAt: Optional[datetime] = datetime.now()

    @validator('title', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Reply(BaseModel):
    rid: int
    bid: int
    uid: int
    reply: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True

class InsertReply(BaseModel):
    # bid: int
    # uid: int
    reply: int
    createdAt: Optional[datetime] = datetime.now()
    updatedAt: Optional[datetime] = datetime.now()

    @validator('reply')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v