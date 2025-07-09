from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
from . import schemas, models
from . database import engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . routers import blog, user , authentication



app = FastAPI()
models.Base.metadata.create_all(engine) #migrating all the tables

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)










