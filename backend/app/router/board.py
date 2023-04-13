from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from datetime import datetime, timedelta

from app.database import get_db
import app.schema.schemas as schema
from app.model import Board, User
import app.crud.board as crud
from app.router.user import get_current_user

router = APIRouter(
    prefix='/api/board',
)

@router.get('/list')
def all_contents(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    res = crud.get_contents_list(db=db, skip=skip, limit=limit)
    return res

@router.get("/user/{uid}")
def user_contents(uid: int, db: Session = Depends(get_db)):
    result = crud.get_user_contents(db=db, uid=uid)
    return result

@router.get("/{bid}")
def get_content(bid: int, db: Session = Depends(get_db)):
    result = crud.get_content(db=db, bid=bid)
    return result

# @router.post('/create', response_model=schema.Board)
# def create_board(board: schema.CreateBoard,
#                  db: Session = Depends(get_db),
#                  user: User = Depends(get_current_user)):
#     try:
#         crud.create_board(db=db, _board=board, user=user.uid)
#     except Exception as e:
#         print(e)

@router.post('/create-nonuser', response_model=schema.Board)
def create_board(board: schema.CreateBoard, db: Session = Depends(get_db)):
    try:
        result = crud.create_board(db=db, _board=board)
    except Exception as e:
        return {"error": e}

    return result


@router.put("/modify")
def update_board(bid: int, board: schema.UpdateBoard, db: Session = Depends(get_db)):
    try:
        result = crud.update_board(db=db, bid=bid, _board=board)
    except Exception as e:
        result = {"error": e}
    return result


@router.delete("/delete")
async def delete_board(bid: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await crud.delete_board(db=db, bid=bid)
    except Exception as e:
        result = {"result": e}
    return result


