from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    active: bool

input_data = {'id': 101, 'name': "Chaicode", 'active': True}

user = User(**input_data)

print(user)