from src import app,Body, BaseModel, HttpUrl,status
from fastapi.encoders import jsonable_encoder
from datetime import date, datetime


from typing import Optional, List, Set

fake_db = {

}
    



class Items (BaseModel):
    name: str
    description: Optional[str] = None
    time : date
    price: float
    tax: float
    tags : List[str] = []


fruits = {
    "Apple":{"name":"Apple", "price":20.5},
    "Orange":{"name":"Orange", "price":30.90 , "desription":"Rich in Vitamin C", "tax":20.3, "tags":["old"], "time":"2023-05-19"},
    "Pineapple":{"name":"pineapple", "description":"Very sweet and yellow", "price":30.60, "tax":20.1}
    }


#json encoder transform the object to json_encoded object from items class 
@app.put('/upadte_item', tags = ["json_encoder"])
async def update_items(item_id:str, item: Items):
    json_compatable_object = jsonable_encoder(item)
    fake_db[id] = json_compatable_object
    print(fake_db)
    return "Success"


@app.patch('/upadte_item', tags = ["json_encoder"])
async def update_items(item_id:str, item: Items):
    stored_item_data = fruits.get(item_id)
    if stored_item_data is not None:
        stored_item_data = Items(**stored_item_data)
        print(stored_item_data)
    else:
        stored_item_data = Items()
    update_data = item.dict(exclude_unset= True)
    print(update_data)
    updated_item = stored_item_data.copy(update=update_data)
    fruits[item_id]= jsonable_encoder(updated_item)
    print(fruits[item_id])
    return updated_item
