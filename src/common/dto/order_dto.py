from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.core.domain.entities.order import OrderItemEntity
from src.core.domain.value_objects.order_status import OrderStatus


class ProductDTO(BaseModel):
    sku: int
    quantity: int

    model_config = {
        "json_schema_extra": {"examples": [{"sku": 1, "quantity": 1}]}
    }


class CreateOrderDTO(BaseModel):
    products: List[ProductDTO]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "products": [
                        {"sku": 1, "quantity": 1},
                        {"sku": 2, "quantity": 1}
                    ],
                }
            ]
        }
    }


class OrderStatusDTO(BaseModel):
    status: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "EM PREPARAÇÃO",
                },
            ]
        }
    }


class OrderResponseDTO(BaseModel):
    id: int
    created_at: datetime
    status: OrderStatus
    order_items: List[OrderItemEntity]
