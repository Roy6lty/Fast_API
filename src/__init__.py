from fastapi import ( 
    Body,
    FastAPI, 
    Path, 
    Query,
    Cookie, 
    Header, 
    Form,
    File, 
    Depends,
    status,
    UploadFile, 
    HTTPException, 
    Request, 
    exception_handlers,
    )

from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.openapi.docs import get_swagger_ui_html 
from pydantic import  Field, BaseModel, validator, HttpUrl, EmailStr
from typing import Optional, List, Set,Literal, Union
from fastapi.exceptions import RequestValidationError


app =FastAPI()