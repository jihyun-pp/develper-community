from sqlalchemy.orm import Session
from app.model import Board
from sqlalchemy import select, text
import app.schema.schemas as schema
from passlib.context import CryptContext

def board_list(db: Session):
    return db.query(Board).order_by(Board.bid.desc()).all()