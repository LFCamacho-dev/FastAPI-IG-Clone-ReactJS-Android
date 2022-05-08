from fastapi import FastAPI
from sqlalchemy.sql.functions import user
import uvicorn
from db import models
from db.database import engine
from routers import user


app = FastAPI()

app.include_router(user.router)



@app.get("/")
def root():
    return "Hello World!"


models.Base.metadata.create_all(engine)







if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)