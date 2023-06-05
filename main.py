from fastapi import FastAPI, Depends
from routers import users, jwt_auth
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
from db import models


from db.database import Base, engine
from db.database import get_db

# def create_table():
#     Base.metadata.create_all(bind=engine)
# create_table()

app = FastAPI()


# #***************************routers****************

app.include_router(jwt_auth.router) #login yes bearer token jwt
app.include_router(users.router)# not bearer token


@app.get('/')
async def home(db:Session = Depends(get_db)):
    print(db)
    return {"connect"}



