from src import app, Form
from src import BaseModel
from src import Optional

class user_form(BaseModel):
    user :str
    password: str

@app.post('/user_login_form')
async def user_login_form(username: str = Form(...), password:str = Form(...)):
    print(password)
    return {'username': username}

@app.post('/user_login_json')
async def user_login_form(user:user_form ):
   
    return {'user': user_form}