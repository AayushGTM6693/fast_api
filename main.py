
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def index():
    return {"Hello":"World"}

@app.get("/about")
def about():
    return {'data':{'about page'}} 

@app.get("/blog")
def index1 (limit: int =10,published:bool = True, sort: Optional[str] = None):
    if published:
     return {'data': f'{limit} blogs from db and it is {published}'}
    else:
      return{'data': f"{limit} blogs from db"}



@app.get("/blog/unpublished")
def abcd():
    return {"data":"all blogs"}

@app.get("/blog/{id}")
def abc(id:int):
   return {"data": id}


class Blog(BaseModel):
   title:str
   body:str
   published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog): #blog is request body
   return {'data':f"blog is created {blog.title}"}
