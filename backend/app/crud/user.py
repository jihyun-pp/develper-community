# from passlib.context import CryptContext
from sqlalchemy.orm import Session
from backend.app.model import User
from sqlalchemy import select, text

def get_user_list(db: Session):
    result = db.execute(text("select * from tb_user"))
    # result = db.execute(select(User))
    # print(result.all())
    return result.all()