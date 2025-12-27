from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def validate_name(cls, value):
        if value.istitle():
            raise ValueError("Name should be capitalize")
        
        return value

class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, value):
        return value.lower().strip()

class Product(BaseModel):
    price: str

    @field_validator("price", mode='before')
    def parse_price(cla, value):
        if isinstance(value, str):
            return float(value.replace("$", ""))
        return value


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_dates(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError("End date must be after start date")
        return values