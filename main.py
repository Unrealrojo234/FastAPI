from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Using pydantic to create a Model
class Item(BaseModel):
    name:str
    price:int
    is_offer:Union[bool, None] = None

#Get Request to root
@app.get("/")
def read_root():
    return {"Hello":"World"}

#Get Request for and item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}
 
#Put Request for an Item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return{"item":item.name,"item_id":item_id }






















