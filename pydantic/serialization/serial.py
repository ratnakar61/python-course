from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []


    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="My Name",
    email="hi@hello.com",
    createdAt=datetime(2025, 12, 27, 12, 23, 54),
    address=Address(street="123 ABC", city="Hanoi", zip_code="100001"),
    is_active=True,
    tags=["Python", "Pydantic"]
)

user_dict = user.model_dump()
print(f"User Dictionary - {user_dict}")
print("="*30)

user_json = user.model_dump_json()
print(f"User JSON - {user_json}")