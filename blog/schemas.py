from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    title:str
    body:str

  

# for user 
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog]

    class Config():
        orm_mode = True
   
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class TokenData(BaseModel):
    email: Optional[str] = None