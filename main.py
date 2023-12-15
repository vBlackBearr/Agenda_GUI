from modelo.item import Item
from fastapi import FastAPI

app = FastAPI()
#app.add_route("/","prb")
#app.add_middleware()



@app.get("/")
def read_root():
    return {'Hola':'Mundo'}

@app.get("/hola")
def read_root2():
    return {'Hola!':'Mundo!'}

@app.put("/item/{item_id}")
def update_item(item_id: int,item: Item):
    return {'item_name':item.name,'item_id':item_id}