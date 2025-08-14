from fastapi import Depends, HTTPException, status
from blog.database import get_db
from sqlalchemy.orm import Session
from blog import models
from blog.schemas import User
from blog.hashing import Hashing


def get_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def get_by_id(id: int, db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")
    return user

def create(request:User, db: Session = Depends(get_db)):
    new_user=models.User(name=request.name, email=request.email, password= Hashing.bcrypt_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user