import abc
from typing import List

from src.core.domain.entities.product import ProductEntity


class ProductRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, product: ProductEntity) -> ProductEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, product: ProductEntity) -> ProductEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def list_by_category(self, category: str) -> List[ProductEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self) -> List[ProductEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, product_id: int) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_product_name(self, product_name: str) -> ProductEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, product_id: int) -> ProductEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_many_by_ids(self, product_ids: List[int]) -> List[ProductEntity]:
        raise NotImplementedError
