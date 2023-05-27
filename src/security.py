from src import app, Depends, BaseModel, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class User(BaseModel):
    username: str
    email: str
    full_name: str
    disbled :bool

class Userin(User):
    hashed_password:str



fake_db = {
    "Johndoe":dict(
    username ="johndoe",
    full_name = "John Doe",
    email = "johndoe@example.com",
    haseded_password = "fakepassword",
    disabled= False
    
    ),
    "maryjane": dict(
    username ="maryjane",
    full_name = "mary jane",
    email = "maryjane@example.com",
    haseded_password = "fakepassword2",
    disabled= True
    )
}


oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_hash_password(password: str):
    f"fakehased{password}"

def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return Userin(**user_dict) #instatiating a user object

def fake_decode_token(token):
    return get_user(fake_db, token)

async def get_current_user(token:str = Depends(oauth_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code =status.HTTP_401_UNAUTHORIZED,
            detail= "username and password don't match",
            headers = {"www.Authenticate":"Bearer"}
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, details ="Inactive user")
    return current_user


@app.post('token',  tags = ["security"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect username or password")
    user = Userin(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail ="Incorrect username aor password")
    
    return {"acess_token":user.username,"token_type":"bearer"}


@app.get("/users.me",  tags = ["security"])
async def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get('/items', tags = ["security"])
async def read_items(token: str = Depends(oauth_scheme)):
    return {"token": token}





@app.get('/security_items', tags = ["security"])
async def read_items(token: str = Depends(oauth_scheme)):
    return {token: token}