from datetime import datetime
from typing import List, Union

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities.product import ProductEntity
from src.core.domain.value_objects.order_status import OrderStatus


class OrderItemEntity(BaseModel):
    id: Union[int, None] = None
    order_detail_id: Union[int, None] = None
    product_id: Union[int, None] = None
    product: Union[ProductEntity, None] = None
    quantity: int


class OrderDetailEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    order_items: List[OrderItemEntity] = Field(default_factory=list)
    total: float
    status: OrderStatus
    created_at: Union[datetime, None] = None
