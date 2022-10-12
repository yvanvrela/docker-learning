from fastapi import FastAPI, Depends
# import uvicorn
from . import crud
from . import models
from sqlalchemy.orm import Session
from .database import engine, get_db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def hello():
    return {'Hello': 'World'}


@app.get('/add_user',)
def add_user(db: Session = Depends(get_db)):
    fake_user = {
        'name': 'Prueba',
    }

    return crud.create_user(fake_user, db)


@app.get('/users',)
def users(db: Session = Depends(get_db)):
    return crud.users(db)