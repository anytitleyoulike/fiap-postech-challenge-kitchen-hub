import abc
from typing import List

from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity


class OrderRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
            self,
            order_detail: OrderDetailEntity,
            order_items: List[OrderItemEntity],
    ) -> OrderDetailEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[OrderDetailEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_order_status(self, order_id: int, order_status: str) -> OrderDetailEntity:
        raise NotImplementedError
