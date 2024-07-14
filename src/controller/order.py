from typing import List

from src.common.dto.order_dto import CreateOrderDTO, OrderResponseDTO
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity
from src.core.domain.exceptions import NotFoundError
from src.core.domain.value_objects.order_status import check_order_status
from src.core.use_cases.order import OrderUseCase
from src.external.database.sqlalchemy.mappers.order_mapper import OrderMapper


class OrderController:
    def __init__(
            self,
            order_repository: OrderRepositoryInterface,
    ) -> None:
        self.order_repository = order_repository

    def create_order(self, order: CreateOrderDTO) -> OrderResponseDTO:
        order_repository = self.order_repository
        return OrderUseCase.create(
            order=order,
            order_repository=order_repository,
        )

    def list_orders(self) -> List[OrderResponseDTO]:
        orders = OrderUseCase.list_all(order_repository=self.order_repository)
        return [OrderMapper.entity_to_order_response_dto(order) for order in orders]

    def update_order_status(self, order_id: int, order_status: str) -> OrderDetailEntity:

        if not check_order_status(order_status):
            raise NotFoundError("Order status invalid")

        return OrderUseCase.order_status_update(
            order_repository=self.order_repository,
            order_id=order_id,
            order_status=order_status
        )
