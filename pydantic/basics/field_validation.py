from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    id: int
    username: str

    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 4:
            raise ValueError("Username must be at least 4 characters")

        return value


class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def validate_password(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Confirm Password must be match with Password")

        return values


user = User(id=1, username="chaicode")
password = SignUpData(password="123456", confirm_password="12356")
print(user)
print(password)