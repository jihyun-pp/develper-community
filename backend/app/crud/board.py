from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.model import Board, User
from sqlalchemy import select, text
import app.schema.schemas as schema
from passlib.context import CryptContext
from datetime import datetime


def get_contents_list(db: Session, skip: int = 0, limit: int = 10):
    res = {}
    try:
        data = db.query(Board).order_by(Board.bid.desc())

        count = data.count()
        contents = data.offset(skip).limit(limit).all()

        res['status'] = 'S'
        res['count'] = count
        res['data'] = contents

    except Exception as e:
        res['status'] = e

    return res


def get_user_contents(db: Session, uid: int):
    return db.query(Board).filter(Board.uid==uid).order_by(Board.bid.desc()).all()


def get_content(db: Session, bid: int):
    res = {}
    try:
        data = db.query(Board).filter(Board.bid==bid).first()
        res['status'] = 'S'
        res['data'] = data
    except Exception as e:
        res['status'] = 'F'
    return res


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


async def delete_board(db: AsyncSession, bid: int):
    try:
        # content = db.query(Board).filter(Board.bid == bid).first()
        # db.delete(content)
        # db.commit()

        query = db.delete(Board).where(Board.bid == bid)
        await db.execute(query)

        return {"result": "S"}
    except Exception as e:
        return {"result": f"F : {e}"}
