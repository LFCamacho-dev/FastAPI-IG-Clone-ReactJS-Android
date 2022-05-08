from fastapi import FastAPI
from sqlalchemy.sql.functions import user
import uvicorn
from db import models
from db.database import engine
from routers import user, post, comment
from auth import authentication
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)




@app.get("/")
def root():
    return "Hello World!"


origins = [
    'http//localhost:3000' # for Java/Android app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')





if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)