from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from datetime import datetime, timedelta

from app.database import get_db
import app.schema.schemas as schema
from app.model import Board, User
import app.crud.reply as crud
from app.router.user import get_current_user

router = APIRouter(
    prefix='/api/reply',
)

@router.get('/{bid}')
def get_replys(bid: int, db: AsyncSession = Depends(get_db)):
    try:
        res = crud.get_replys(db=db, bid=bid)
    except Exception as e:
        return {"status": "F"}

    return {"status": "S", "data": res}


@router.post('/insert/{bid}')
def insert_reply(bid: int, uid: int, reply: schema.InsertReply, db: AsyncSession = Depends(get_db)):
    try:
        res = crud.insert_reply(bid=bid, uid=uid, _reply=reply, db=db)
    except Exception as e:
        return {"status": "F"}
    return {"status": res}