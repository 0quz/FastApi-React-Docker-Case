from typing import Optional, List

import models
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}

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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, db: Session = Depends(get_db)):

    app = models.App()

    #app.name = q
    #app.id = item_id
    #db.add(app)
    #app.query.filter_by(id=1).delete()
    #app.query.filter_by(id=2).delete()
    #db.commit()

    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")
