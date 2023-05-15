from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

import app.schema.schemas as schema
from app.schema.users.request import *
from app.schema.users.response import *
from app.crud import users as crud
from app.database import get_db
from app.crud.users import UserCrud

router = APIRouter(
    prefix='/users',
)


@router.post("/login", tags=['LOGIN'], summary='로그인')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = await UserCrud().login(db=db, email=form_data.username, password=form_data.password)
    return token

@router.post('/new', tags=['USER'], summary='회원가입')
async def create_new_user(req: RequestCreateUser, db: Session = Depends(get_db)):
    res = {}
    try:
        result = await UserCrud().create_user(db=db, req=req)
        res['status_code'] = status.HTTP_201_CREATED

    except Exception as e:
        res['status_code'] = e.args[0]
        res['message'] = str(e)

    return res


@router.post('/info', tags=['USER'], summary='내 정보 관리')
async def get_user_info(token: str, db: Session = Depends(get_db)):
    pass

@router.post('/edit/info', tags=['USER'], summary='내 정보 변경')
async def edit_user_info(_edit_user: schema.ReqEditInfo, db: Session = Depends(get_db)):
    pass

@router.post('/edit/password', tags=['USER'], summary='비밀번호 변경')
async def edit_password(_edit_password: schema.ReqEditPw, db: Session = Depends(get_db)):
    pass