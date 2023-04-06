from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from datetime import datetime, timedelta

from app.database import get_db
import app.schema.schemas as schema
from app.model import Board
import app.crud.board as crud

router = APIRouter(
    prefix='/api/board',
)

@router.get('/list')
def board_list(db: Session = Depends(get_db)):
    result = crud.board_list(db=db)
    return result