from src import app, Form, File, UploadFile, HTTPException, Request, status
from src import JSONResponse
from src import BaseModel, List
from src import Optional

from fastapi.exceptions import RequestValidationError

from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as starletteHTTPException
 
items ={
    "Apple":{"description": "Delicious Fruit"}

}

@app.get('/Basic_errors')
async def asic_errors(item_id : str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item_id not found")

    return items[item_id]


class UnicornException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT, content={"message":f"exeception with {exc.name} did something"})

@app.get('/error_handling/unicorn/{name}')
async def unicorn_handled(name:str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name":name}

# Overiding the default error and returning a customized message
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,  exc ):
    return PlainTextResponse(str(exc, status = status.HTTP_400_BAD_REQUEST))


@app.exception_handler(starletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code = exc.status_code)


@app.get('/validationitems')
async def Request_vaildation(item_id:int):
    if item_id == 3:
        raise HTTPException(status_code=400, detail="i dont like 3")
    return {"items_id": item_id}