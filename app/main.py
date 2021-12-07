from typing import Optional, List

import base64
import secrets
import models
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal, engine
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class User(BaseModel):
    username: str
    password: str


fake_users_db = {
    "appz": {
        "username": "appz",
        "password": "`123456&*"
    }
}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/login")
async def login(user: User, db: Session = Depends(get_db)):
    user_object = fake_users_db.get(user.username)
    response = {
        "success": False, 
        "message": "Incorrect username or password."
    }
    if user_object and user_object["password"] == user.password:
        response["message"] = "Successfully logged in."
        response["success"] = True
    
    return response


"""
#This endpoint will add the sample data to the database if there is not the same data in the database.
@app.get("/csvtodatabase/")
def csv_to_database(db: Session = Depends(get_db)):
    response = {
        "message": "error"
    }
    import csv
    from datetime import datetime
    with open("sample_apps.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            app = models.App()
            app.id = int(row[0])
            app.name = str(row[1])
            app.icon = str(row[2])
            app.created_at = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            app.updated_at = row[4] if row[4] else None
            db.add(app)
            db.commit()
    
    with open("sample_screeshots.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            screenshot = models.Screenshot()
            screenshot.id = int(row[0])
            screenshot.app_id = int(row[1])
            screenshot.file_name = str(row[2])
            screenshot.created_at = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            screenshot.updated_at = row[4] if row[4] else None
            db.add(screenshot)
            db.commit()

    response["message"] = "success"
    return response
"""

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")