from fastapi import APIRouter, Depends, HTTPException, status
from .dependecies import get_query_token, get_token

router = APIRouter(
    prefix= "/items_route",
    tags= ["items"],
    dependencies=[Depends(get_query_token)],
    responses={404:{'description':"Not Found"}}
)

fake_db ={"Plumbus"
            :{"name":"Plumbus"},
        "gun"
            :{"name":"portal_gun"}}

@router.get('/')
async def read_items():
    return fake_db

@router.get('/items_id1')
async def read_item(item_id: str):
    if item_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'Item not found')
    return {"name": fake_db[item_id]["name"], "item_id": item_id}

@router.put('/{item_id}', tags = ['custom'], responses = {403:{"descrition":"Operation Forbidden"}})
async def update_item(item_id: str):
    if item_id != 'plumbus':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = 'You can only update the item')
    return {"item_id": item_id, "name":"The Greate Plumbus"}