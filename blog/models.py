from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(100))
    body = Column(VARCHAR(500))
    user_id = Column(Integer, ForeignKey('users.id'))

    creator= relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100), unique=True, index=True)
    password = Column(VARCHAR(100))

    blogs = relationship("Blog", back_populates="creator")

