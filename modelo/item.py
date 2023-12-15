from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int
    is_offer: bool = None