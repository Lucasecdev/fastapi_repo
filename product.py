from pydantic import BaseModel


class product(BaseModel):

    name: str
    price: float
