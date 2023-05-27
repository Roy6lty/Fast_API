from src import app, Depends, Body,Header, HTTPException, status
from src import List, Set

#dependency Injection
#Using methods as dependences
async def common_parameters(q:str|None = None, skip:int|None = None, limit:int = 100):
    return{"q":q, "skip":skip,"limit":limit}

@app.get('/dependecies_get', tags = ["dependcies"])
async def read_items(commons: dict =Depends(common_parameters)): 
    return commons



fake_db=[{"item_name":"Foo"},{"item_name":"bar"},{"item_name":"Baz"}]
#Using class as dependencies
class CommonParams:
    def __init__(self, q:str|None = None, skip:int|None= None, limit: int = 3):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get('/dependClass_readitems', tags= ["dependencies"])
async def read_items(params:CommonParams = Depends()):# returns an CommonParamas class object
    response = {}
    if params.q:
        response.update({"q":params.q})
    items = fake_db[params.skip : params.limit] #slicing list
    response.update({"items":items})
    return response

#subqueries and Query depedencies

def query_extarctor(q: str|None=None):
    return q

def query_or_body_extractor(q:str = Depends(query_extarctor), last_query:str | None = Body(...)):
    if not q:
        return last_query
    return q

@app.post('/subdependies', tags = ["dependencies"])
async def subdependencies_extractor(extrator: str = Depends(query_or_body_extractor)):
    return {"q":extrator}


#dependies using path OPerators

async def verify_token(x_token:str = Header(...)):
    if x_token != "token-xxx-xxx":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


async def verify_key(x_key:str = Header(...)):
    if x_key != "key-xxx-xxx":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

#note items key adopted the query parameters for verify_key and verify tokens 
#which permits it to have an empty query parameter


@app.get('/API_Keys', dependencies=[Depends(verify_token),Depends(verify_key)], tags =["dependencies"])
async def items_keys():
    items= [{"token": "Token"},{"keys":"Keys"}]
    return items


