from pydantic import BaseModel, validator, EmailStr
from datetime import datetime

class User(BaseModel):
    uid: int
    user_id: str
    password: str
    username: str
    email: str
    auth: str | None = None  # nullable
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

    @validator('password2')
    def password_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str


class Category(BaseModel):
    cid: int
    category_nm: str

    class Config:
        orm_mode = True


class Board(BaseModel):
    bid: int
    category: str
    uid: int  # user
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime
    hit: int
    imgPath: str

    class Config:
        orm_mode = True


class Reply(BaseModel):
    rid: int
    bid: int
    uid: int
    reply: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True