from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
import uvicorn
from database import SessionLocal, engine
from routes.api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(description="LIA helps you keep track and discover news books you might like")


@app.on_event("startup")
def startup_db_client():
    print("LIA is on!")


app.include_router(api_router)

if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)