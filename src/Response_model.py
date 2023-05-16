from src import app, Body, Cookie, Header
from src import BaseModel, HttpUrl, Field, EmailStr
from src import Optional, List

class user(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str



@app.post('/user/usermodel')
def user_model(create_user:user):
    return user
