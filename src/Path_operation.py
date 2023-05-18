from src import app,Body, BaseModel, HttpUrl,status

from datetime import date


from typing import Optional, List, Set


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    shops:Set[str] = set()


@app.post('/path_operations/new_create', response_model = Item, status_code=status.HTTP_201_CREATED , tags = ["Operations"])
async def path_operations_create(item_id:int, item:Item):
    """
    - This method returns a datamodel of:
    - **Name**: str
    - **description** : str
    - **Price**: float
    - **tax** : float
    - **tags**: List
    - **Shops**: Set
    """
    return item

@app.post('/path_operations/', status_code=status.HTTP_201_CREATED , tags = ["Operations"], deprecated= True)
async def path_operations_create(item_id:int, item:Item):

    return {"item_id":item_id, "item":item}




