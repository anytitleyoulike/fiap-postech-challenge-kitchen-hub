from typing import List

from fastapi import APIRouter

from src.common.dto.order_dto import CreateOrderDTO, OrderResponseDTO, OrderStatusDTO
from src.controller.order import OrderController
from src.external.database.sqlalchemy.repositories.order import OrderRepository


router = APIRouter(prefix="/orders", tags=["orders"])

order_repository = OrderRepository()
order_controller = OrderController(
    order_repository=order_repository
)


@router.post("/", response_model=OrderResponseDTO, response_model_exclude_none=True)
async def create_order(order: CreateOrderDTO):
    return order_controller.create_order(order)


@router.get("/", response_model=List[OrderResponseDTO], response_model_exclude_none=True)
async def list_orders():
    return order_controller.list_orders()


@router.put("/{order_id}")
async def update_order_status(order_id: int, order_status: OrderStatusDTO):
    return order_controller.update_order_status(order_id, order_status.status.title())
