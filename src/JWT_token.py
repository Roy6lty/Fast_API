from src import app, Depends, BaseModel, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import timedelta, datetime
from src import logger

SECRET_KEY = '89a9e0123ee2b43fa3a25d7f'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_db = dict(
    Johndoe =dict(
    username ="johndoe",
    full_name = "John Doe",
    email = "johndoe@example.com",
    hashed_password = "$2b$12$OxqoDDD5Oxc3b6eAPOx.h.1M.CBIbanaJDFxU5POZCaWLp8vmhqiu",
    disabled= False
    
    ),
    maryjane =dict(
    username ="maryjane",
    full_name = "mary jane",
    email = "maryjane@example.com",
    hashed_password = "fakepassword2",
    disabled= True
    )
)

class Token(BaseModel):
    access_token: str
    tokentype: str

class TokenData(Token):
    username : str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    fullname : str | None = None
    disabled : bool = False

class UserInDB(User):
    hashed_password : str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    '''
    Compares and verify Plainpassword with hashed password
    '''
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    '''
    get's the password and hashes it
    '''
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username:str, password:str):
    user = get_user(fake_db,username)
    if not user: #verify username -> True
        return False
    if not verify_password(password, user.hashed_password): #verify password -> True
        return False
    return user
    
def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + expires_delta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post('/login_token', response_model= Token, tags = ['jwt_security']) 
async def  login_for_access_token(form_data:OAuth2PasswordRequestForm =  Depends()): #OAOAuth2PasswordRequestForm retrives its method from te default settings using default
    user = authenticate_user(fake_db, form_data.username,form_data.password )
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail='incorrect username or password',
                            headers = {"www.Authenicate"}
                            )
    access_token_expires = timedelta(minutes =ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub":user.username}, expires_delta =access_token_expires
    )

    return {"access_token":access_token, "tokentype":"bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    crednetals_Exception =  HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='could not be validated',
    headers = {"WWW. Authenticate_Bear"})
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
        username: str = payload.get('sub')
        if username is None:
            raise crednetals_Exception
        token_data = TokenData(username = username)
    except JWTError:
        raise crednetals_Exception
    user = get_user(fake_db, username=token_data.username)
    if user is None:
        raise crednetals_Exception
    return user
    

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="inactive_user")
    return current_user

@app.get('/src/me', response_model=User, tags=['securtiy'])
async def get_me(current_user:User = Depends(get_current_active_user)):
    return current_user