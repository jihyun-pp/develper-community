from pydantic import BaseModel, validator
from datetime import datetime

class User(BaseModel):
    uid: int
    user_id: str
    password: str
    username: str
    email: str
    auth: str
    createdAt: datetime

    class Config:
        orm_mode = True


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