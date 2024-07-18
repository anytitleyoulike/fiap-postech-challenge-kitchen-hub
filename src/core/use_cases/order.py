from typing import List

from src.common.dto.order_dto import (
    CreateOrderDTO,
    OrderResponseDTO,
)

from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.exceptions import OperationalException
from src.core.domain.value_objects.order_status import OrderStatus


class OrderUseCase:
    @staticmethod
    def create(
            order: CreateOrderDTO,
            order_repository: OrderRepositoryInterface,
    ) -> OrderResponseDTO:

        order_detail: OrderDetailEntity = OrderDetailEntity(
            status=OrderStatus.RECEIVED
        )

        order_items: List[OrderItemEntity] = [
            OrderItemEntity(sku=item.sku, quantity=item.quantity)
            for item in order.products
        ]

        new_order = order_repository.create(order_detail, order_items)
        if not new_order.id:
            raise OperationalException("Error creating order")

        return OrderResponseDTO(
            id=new_order.id,
            created_at=new_order.created_at,
            status=new_order.status,
            order_items=[
                OrderItemEntity(id=item.id, quantity=item.quantity, sku=item.sku)
                for item in new_order.order_items
            ],
        )

    @staticmethod
    def list_all(
            order_repository: OrderRepositoryInterface,
    ) -> List[OrderDetailEntity]:
        try:
            return order_repository.list_all()
        except Exception as error:
            print(error)

    @staticmethod
    def order_status_update(
            order_repository: OrderRepositoryInterface,
            order_id: int,
            order_status
    ) -> OrderResponseDTO:
        updated_order = order_repository.update_order_status(order_id, order_status)

        return OrderResponseDTO(
            id=updated_order.id,
            status=updated_order.status,
            order_items=updated_order.order_items,
            created_at=updated_order.created_at
        )
