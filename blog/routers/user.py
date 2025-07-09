from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..repository import user

router = APIRouter(
    tags=['users'],
    prefix="/user"
)

@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)
