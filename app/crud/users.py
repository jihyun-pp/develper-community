from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.model import User
import app.schema.schemas as schema

def create_user(db: Session, _create_user: schema.CreateUser):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    c_user = User(
        user_id=_create_user.user_id,
        username=_create_user.username,
        email=_create_user.email,
        password=pwd_context.hash(_create_user.password1),
    )
    db.add(c_user)
    db.commit()

def get_existing_user(db: Session, _create_user: schema.CreateUser):
    return db.query(User).filter(User.user_id == _create_user.user_id).first()

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()


def modify_user(db: Session, user_id: str, username: str):
    a = db.query(User).filter(User.user_id == user_id).all()
    a.username = username
    db.commit()
    return a.username