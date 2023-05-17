from src import app, Body, Cookie, Header
from src import BaseModel, HttpUrl, Field, EmailStr
from src import Optional, List, Literal, Union

class user(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    

class user_password(user):
    password: str

class user_summit(user):
    pass

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

class Baseitem(BaseModel):
    name: Optional[str] =None
    description: str
    type: str

class caritem(Baseitem):
    type :str ="car"

class planeitem(Baseitem):
    type:str = "plane"
    size: int


items = {
    "Apple":{"name":"Apple", "price":20.5},
    "Orange":{"name":"Orange", "price":30.90 , "desription":"Rich in Vitamin C", "tax":20.3},
    "Pineapple":{"name":"pineapple", "description":"Very sweet and yellow", "price":30.60, "tax":20.1}
    }

base_item = {
    "item1":{"description":"All my friends drive lowriders", "type":"car"},
    "item2":{"description":"Music is my Aeroplane", "type":"plane","size":5}
}

list_items = [
    {"name":"item1","description":"All my friends drive lowriders", "type":"car"},
    {"name":"item1","description":"Music is my Aeroplane", "type":"plane","size":5}
]

# response model returs a model for the response to the api call
@app.post('/user/usermodel',response_model= user_summit)
async def user_model(create_user:user_password):
    return user


#'response_model_model_exclude_unset' -> Excludes default value from the response
@app.post('/user/fruits', response_model = Item, response_model_exclude_unset=True)
async def get_fruits(fruits: Literal["Apple","Orange","Pineapple"]):
    return items[fruits]


#'response_model_model_exclude_unset' -> Excludes specified values[tax, price] from the response
@app.post('/user/fruits_exclude', response_model = Item, response_model_exclude ={"tax", "price"})
async def get_fruits(fruits: Literal["Apple","Orange","Pineapple"]):
    return items[fruits]


#'response_model_model_exclude_unset' -> includes only specified values  for  response
@app.post('/user/fruits_include', response_model = Item, response_model_include ={"name", "price","tax"})
async def get_fruits(fruits: Literal["Apple","Orange","Pineapple"]):
    return items[fruits]

@app.get('/response_union', response_model=Union[caritem, planeitem])
def response_union(item_id: Literal["item1", "item2"]):
    return base_item[item_id]

app.get('/list_items', response_model=list[list_items])
def response_union():
    return list_items
