from typing import Optional

import io
from base64 import encodebytes

from sqlalchemy.sql.expression import false
import models
from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from PIL import Image

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


class AppID(BaseModel):
    appid: int
    screenshot: Optional[bool] = False


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


@app.post("/webpconverter")
async def webp_converter(img: UploadFile = File(...)):
    image = Image.open(img.file)
    file_name = ""
    for char in img.filename:
        if char == ".":
            file_name += '.webp'
            break
        file_name += char
    image.save(file_name, format='webp')
    image.close()
    return FileResponse(file_name, media_type="image/webp")


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img


@app.get("/get_apps")
async def get_apps(db: Session = Depends(get_db)):
    apps = db.query(models.App).all()
    response = {"sucess": False}
    app_list = []
    for app in apps:
        app_list.append ({
            "id": app.id,
            "name": app.name,
            "icon": get_response_image("icons/" + app.icon)
         })

    response['apps'] = app_list
    response['sucess'] = True

    return response


@app.post("/get_screenshots_by_app_id")
async def get_screenshots_by_app_id(app: AppID, db: Session = Depends(get_db)):
    screenshots = db.query(models.Screenshot).filter(models.Screenshot.app_id == app.appid)
    response = {"sucess": False}
    screenshot_list = []
    for screenshot in screenshots:
        screenshot_list.append ({
            "id": screenshot.id,
            "screenshot": get_response_image("ss/" + screenshot.file_name)
        })

    response['screenshots'] = screenshot_list
    response['sucess'] = True

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