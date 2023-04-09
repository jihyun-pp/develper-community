from sqlalchemy.orm import Session
from app.model import Board, User
from sqlalchemy import select, text
import app.schema.schemas as schema
from passlib.context import CryptContext
from datetime import datetime

def get_contents_list(db: Session):
    return db.query(Board).order_by(Board.bid.desc()).all()

def get_user_contents(db: Session, uid: int):
    return db.query(Board).filter(Board.uid==uid).order_by(Board.bid.desc()).all()

def get_content(db: Session, bid: int):
    return db.query(Board).filter(Board.bid==bid).first()

def create_board(db: Session, _board=schema.CreateBoard):
    try:
        board = Board(
            category=_board.category,
            uid=1,
            title=_board.title,
            content=_board.content,
            imgPath=_board.imgPath
        )
        db.add(board)
        db.commit()
        return {"result": "S"}
    except Exception as e:
        return {"result": f"F : {e}"}


def update_board(db: Session, bid: int, _board=schema.UpdateBoard):
    try:
        board = db.query(Board).filter(Board.bid == bid).first()
        board.title = _board.title
        board.content = _board.content
        board.imgPath = _board.imgPath
        board.updatedAt = datetime.now()
        db.commit()

        return {"result": "S"}
    except Exception as e:
        return {"result": f"F : {e}"}


def delete_board(db: Session, bid: int):
    try:
        # db.delete(Board).where(Board.bid == bid)
        content = db.query(Board).filter(Board.bid == bid).first()
        db.delete(content)
        db.commit()
        return {"result": "S"}
    except Exception as e:
        return {"result": f"F : {e}"}
