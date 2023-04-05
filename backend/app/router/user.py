from fastapi import APIRouter, Depends, HTTPException
from backend.app.crud import user as crud
from backend.app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter('/api/user')

@router.get("/list")
def get_user_list(db: Session = Depends(get_db)):
    result = crud.get_user_list(db=db)
    return result