from src import app, Body, Cookie, Header
from src import BaseModel, HttpUrl, Field
from src import Optional, List

'''
Using the pydantic Field variable to set Examples in the Api
'''
class Item (BaseModel):
    name: str = Field(..., example="james") #examples
    description: str = Field(None, example="A very short boy")
    price: float = Field(..., example=20.6)
    tax: Optional[float] = Field(None, example=2.3)
    

    # class Config:
    #     schema_extra ={
    #         "example":{
    #             "name": "James",
    #             "description": "Very short Boy",
    #             "price":16.20,
    #             "tax":1.67
    #         }
    #     }

@app.put('/declare_request/')
async def declare_request(item_id:int,
    item:Item = Body(..., example={
                                        "name":"Femi",
                                        "description":"very Good",
                                        "price":200,
                                        "tax":0.25  }
                                            )):
    results = {'item_id': item_id, "item":item}
    return results

@app.get('/get_cookies')
async def get_cookkies(cook_id:Optional[str] = Cookie(None),
                       accept_encodeing:Optional[str] = Header(None),
                       sec_ch_va : Optional[str] = Header(None),
                       user_agent: Optional[str] = Header(None),
                       x_token_values: List[str] = Header(None)
                       ):
    return {'cookie_id' : cook_id,
            'accept_encodeing': accept_encodeing,
            'sec_ch_va':sec_ch_va,
            'user_agent': user_agent}

