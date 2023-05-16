from src import app,Body, BaseModel, HttpUrl 

from datetime import date


from typing import Optional, List, Set

class Item(BaseModel):
    """
    This is a Datamodel class
    """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    shops:Set[str] = set()


class Discount(BaseModel):
    price_off: float
    expiration_date: date =None
    

class Shops (BaseModel):
    name: str
    url: HttpUrl #vaildate website string
    item: Optional[Item] = None
    discount: Optional[Discount] = None 

    
    
@app.put('/item/item_id')
async def update_item(item_id:int, shop: Shops=Body(None, embed=True)):
    results = {"item_id" : item_id, "shop":shop}
    return results

@app.post('/item/mutiple_post')
async def update_multiple_items(books: dict[int, float]):
    return books


