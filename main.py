from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'Home Page'}
 
@app.get('/about')
def about():
    return {'data':'About Page'}


@app.get('/blog')
def blog():
    return {'data':'All blog lists'}


@app.get('/blog/unpublish')
def unpublish():
    return {'data':'Unpublished blogs'}


@app.get('/blog/{id}')
def blog_by_id(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{1:'comment1',2:'comment2'}}