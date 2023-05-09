import uuid
from pydantic import BaseModel, validator, EmailStr
from datetime import datetime
from typing import Optional


class User(BaseModel):
    uid: int
    email: str
    password: str
    nickname: str
    birth: int
    auth: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True

class NewUser(BaseModel):
    email: EmailStr
    password1: str
    password2: str
    nickname: str
    birth: int

    @validator('email', 'password1', 'nickname')
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
    username: str

class ReqEditInfo(BaseModel):
    token: str
    nickname: str
    birth: int

class ReqEditPw(BaseModel):
    token: str
    password: str
    password_confirm: str