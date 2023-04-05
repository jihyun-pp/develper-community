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