from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

product = Product(price=100, quantity=4)
print(product.total_price)
print(product.model_dump())