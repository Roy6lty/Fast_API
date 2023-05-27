from fastapi import Depends, FastAPI
from .routers.dependecies import get_token, get_query_token
from .routers import users, items


from src import app

app.include_router(users.router)
app.include_router(items.router)


@app.get('/')
async def root():
    return{'message':"Hello Bigger Application"}