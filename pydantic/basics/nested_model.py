from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(street="123 ABC", city="Hanoi", zip_code="100001")
user = User(id=1, name="MyName", address=address)

print(user)