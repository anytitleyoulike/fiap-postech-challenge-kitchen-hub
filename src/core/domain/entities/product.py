from decimal import Decimal
from typing import Union

from pydantic import BaseModel, ConfigDict


class ProductEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    name: str
    description: Union[str, None] = None
    category: str
    price: Union[Decimal, None] = None
    quantity: Union[int, None] = None
