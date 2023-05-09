from dotenv import load_dotenv
from os import environ
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

import app.schema.schemas as schema
from app.crud import users as crud
from app.database import get_db

router = APIRouter(
    prefix='/users',
)

@router.post('/new', tags=['USER'], summary='회원가입')
async def create_new_user(_create_user: schema.NewUser, db: Session = Depends(get_db)):
    check_duplicate = crud.get_existing_user(db=db, _create_user=_create_user)
    if check_duplicate:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다.")
    else:
        user = crud.create_user(db=db, _create_user=_create_user)

@router.post('/info', tags=['USER'], summary='내 정보 관리')
async def get_user_info(token: str, db: Session = Depends(get_db)):
    pass

@router.post('/edit/info', tags=['USER'], summary='내 정보 변경')
async def edit_user_info(_edit_user: schema.ReqEditInfo, db: Session = Depends(get_db)):
    pass

@router.post('/edit/password', tags=['USER'], summary='비밀번호 변경')
async def edit_password(_edit_password: schema.ReqEditPw, db: Session = Depends(get_db)):
    pass