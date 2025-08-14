from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models
from blog.schemas import Blog

def get_all(db:Session ):
    blogs=db.query(models.Blog).all()
    return blogs


def get_by_id(id: int, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")
    return blog    


def create_blog(request: Blog, db: Session):
    new_blog= models.Blog(title=request.title, body=request.body, user_id= request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(blog_id: int, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id==blog_id)
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {blog_id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog deleted successfully"

def update(id: int, request: Blog, db: Session):
    blog= db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return 'Updated successfully'


