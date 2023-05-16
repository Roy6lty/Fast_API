from fastapi import Body,FastAPI, Path, Query,Cookie, Header
from fastapi.openapi.docs import get_swagger_ui_html 
from pydantic import  Field, BaseModel, validator, HttpUrl, EmailStr
from typing import Optional, List, Set


app =FastAPI()