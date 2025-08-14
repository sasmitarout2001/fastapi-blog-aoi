from fastapi import FastAPI
import blog.models as models
from blog.database import engine
from routers import blog, user, authentication


app= FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




