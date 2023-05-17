from fastapi import Body,FastAPI, Path, Query,Cookie, Header, Form,File, UploadFile
from fastapi.openapi.docs import get_swagger_ui_html 
from pydantic import  Field, BaseModel, validator, HttpUrl, EmailStr
from typing import Optional, List, Set,Literal, Union


app =FastAPI()