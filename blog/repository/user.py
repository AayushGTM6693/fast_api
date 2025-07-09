from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext
from .. import models, schemas

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(request: schemas.User, db: Session):
    """Create a new user with hashed password"""
    hashed_password = pwd_ctx.hash(request.password)
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session):
    """Get user by ID"""
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with the id {id} is not available"
        )
    return user

def get_all_users(db: Session):
    """Get all users"""
    return db.query(models.User).all()

def update_user(id: int, request: schemas.User, db: Session):
    """Update user by ID"""
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with the id {id} not found"
        )
    
    hashed_password = pwd_ctx.hash(request.password)
    user.update({
        "name": request.name,
        "email": request.email,
        "password": hashed_password
    })
    db.commit()
    return user.first()

def delete_user(id: int, db: Session):
    """Delete user by ID"""
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with the id {id} not found"
        )
    user.delete(synchronize_session=False)
    db.commit()
    return {"detail": "User deleted successfully"}
