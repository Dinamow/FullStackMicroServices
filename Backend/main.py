# app/main.py
from fastapi import FastAPI
from routers import auth
from core.config import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


app = FastAPI()

# Include auth routes
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI JWT Auth system"}

@app.get("/try_db")
def db_try(db: Session = Depends(get_db)):
    if db:
        return {"message": "DB connection is successful"}
    else:
        return {"message": "DB connection is not successful"}