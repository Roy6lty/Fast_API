from pydantic import BaseModel
from typing import List


class ItemBase(BaseModel):
    title: str
    description: str

class Item(ItemBase):
    id:int
    owner_id:int

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass


# creatinng a user
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    hashed_password : str

class User(UserBase):
    id: int
    is_active = bool
    items: List[Item] = []

    class Config:
        orm_mode = True
    