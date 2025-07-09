from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List
from .. import models, schemas

def get_all_blogs(db: Session):
    """Get all blogs"""
    return db.query(models.Blog).all()

def create_blog(request: schemas.Blog, db: Session):
    """Create a new blog post"""
    new_blog = models.Blog(
        title=request.title, 
        body=request.body, 
        user_id=1  # TODO: Get user_id from authentication
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog(id: int, db: Session):
    """Get blog by ID"""
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with the id {id} is not available"
        )
    return blog

def update_blog(id: int, request: schemas.Blog, db: Session):
    """Update blog by ID"""
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with the id {id} not found"
        )
    blog.update({
        "title": request.title, 
        "body": request.body
    })
    db.commit()
    return blog.first()

def delete_blog(id: int, db: Session):
    """Delete blog by ID"""
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with the id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog deleted successfully"}
