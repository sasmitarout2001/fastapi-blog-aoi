from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data':'Home Page'}
 
@app.get('/about')
def about():
    return {'data':'About Page'}


@app.get('/blog')
def blog(limit :int =10, published :bool =True, sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} blogs are published'}
    else:
        return {'data': f'{limit} blogs are unpublished'}


@app.get('/blog/unpublish')
def unpublish():
    return {'data':'Unpublished blogs'}


@app.get('/blog/{id}')
def blog_by_id(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{1:'comment1',2:'comment2'}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.put('/blog')
def create_blog(blog:Blog):
    return {'data':f'Blog is create with the title {blog.title}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)