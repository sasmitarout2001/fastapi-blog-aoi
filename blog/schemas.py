from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    user_id: int



class ShowBlogForUser(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[ShowBlogForUser] = []
    class Config:
        from_attributes = True



class ShowUserForBlog(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True



class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserForBlog

    class Config:
        from_attributes = True

        

class User(BaseModel):
    name: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str

    