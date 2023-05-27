from fastapi import APIRouter, Depends
from .dependecies import get_query_token

router =APIRouter(
    prefix= "/users_route",
    tags= ["users"],
    dependencies=[Depends(get_query_token)],
    responses={404:{'description':"Not Found"}}
)


@router.get("users/", tags = ["users"])
async def read_users():
    return [{"username":"Rick"}, {"username": "Morty"}]

@router.get("/user.me", tags = ['users'])
async def read_user_me():
    return {'username':"current_user"}


@router.get("/users/{username}", tags = ['users'])
async def read_user_me():
    return {'username':"username"}


