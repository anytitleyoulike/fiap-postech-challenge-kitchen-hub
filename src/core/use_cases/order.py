from typing import List

from src.common.dto.order_dto import (
    CreateOrderDTO,
    OrderResponseDTO,
)

from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.value_objects.order_status import OrderStatus


class OrderUseCase:
    @staticmethod
    def create(
            order: CreateOrderDTO,
            order_repository: OrderRepositoryInterface,
            product_repository: ProductRepositoryInterface,
    ) -> OrderResponseDTO:
        total: float = 0

        product_ids = [order_product.id for order_product in order.products]
        products = product_repository.get_many_by_ids(product_ids)

        for product, order_product in zip(products, order.products):
            total += product.price * order_product.quantity

        order_detail: OrderDetailEntity = OrderDetailEntity(
           total=total, status=OrderStatus.RECEIVED
        )

        order_items: List[OrderItemEntity] = [
            OrderItemEntity(product_id=item.id, quantity=item.quantity)
            for item in order.products
        ]

        new_order = order_repository.create(order_detail, order_items)
        if not new_order.id:
            raise Exception("Error creating order")

        return OrderResponseDTO(
            id=new_order.id,
            created_at=new_order.created_at,
            status=new_order.status,
            order_items=[
                OrderItemEntity(id=product.id, quantity=product.quantity, product=product.product)
                for product in new_order.order_items
            ],
        )

    @staticmethod
    def list_all(
            order_repository: OrderRepositoryInterface,
    ) -> List[OrderDetailEntity]:
        return order_repository.list_all()

    @staticmethod
    def order_status_update(
            order_repository: OrderRepositoryInterface,
            order_id: int,
            order_status
    ) -> OrderDetailEntity:
        return order_repository.update_order_status(order_id, order_status)
