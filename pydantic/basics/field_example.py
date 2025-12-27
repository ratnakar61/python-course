from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    id: int
    title: str
    image_url: Optional[str] = None

cart_data = {
    "user_id": 1,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"Laptop":1, "Mouse":2}
}

cart = Cart(**cart_data)
print(cart)