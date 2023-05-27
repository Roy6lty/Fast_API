from fastapi import  Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from src import app

from . import CRUD ,database, models, schema
from .database import Sessionlocal, engine

# creating database
models.Base.metadata.create_all(bind=engine)


#dependecy
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/create_user', response_model = schema.User, tags = ['sql'], status_code=status.HTTP_201_CREATED)
def create_user( user:schema.UserCreate, db:Session = Depends(get_db)):
    db_user = CRUD.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already Registered")
    return CRUD.create_user(db=db, user=user)

@app.get('/users', response_model = list[schema.User], tags = ['sql'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = CRUD.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schema.User, tags = ['sql'])
def read_user(user_id:int, db: Session = Depends(get_db)):
    db_user = CRUD.get_users(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details ="User not found")
    return db_user

@app.post("/users/{users_id}/items", response_model=schema.Item, status_code=201, tags = ['sql'])
def create_item_for_user(
    user_id:int,
    item: schema.ItemCreate, db:Session = Depends(get_db)
    ):

    return CRUD.create_user_item(db, item=item, user_id =user_id)

@app.get('/items',response_model=list[schema.Item], tags = ['sql'])
def read_items(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    items = CRUD.get_items(db, skip=skip, limit=limit)
    return items

    