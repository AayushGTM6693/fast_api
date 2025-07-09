from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, models,oauth2
from typing import List
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)

@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_post(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db ), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_blog(id, db)