import unittest
from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

import pytest

from src.common.dto.order_dto import OrderResponseDTO
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.controller.order import OrderController
from src.core.domain.entities.order import OrderItemEntity, OrderDetailEntity
from src.core.domain.entities.product import ProductEntity
from src.core.domain.value_objects.order_status import OrderStatus
from src.core.use_cases.order import OrderUseCase


# def mock_order_detail_entity(mock_order_item_entity) -> OrderDetailEntity:
#     return OrderDetailEntity(
#         id=1,
#         total=10,
#         order_items=[mock_order_item_entity],
#         status=OrderStatus("Em Preparação"),
#         created_at=datetime.now()
#     )
#
#
# @pytest.fixture
# def mock_order_response_dto(mock_order_item_entity):
#     return OrderResponseDTO(id=1,
#                             status=OrderStatus("EM PREPARAÇÃO"),
#                             created_at=datetime.now(),
#                             order_items=[mock_order_item_entity]
#                             )


class TestOrderController(TestCase):

    def setUp(self):
        self.mock_order_item_entity = OrderItemEntity(
            product=ProductEntity(name="test product 1", category="test"),
            quantity=1
        )

        self.mock_order_detail_entity = OrderDetailEntity(
            id=1,
            total=10,
            order_items=[self.mock_order_item_entity],
            status=OrderStatus("Em Preparação"),
            created_at=datetime.now()
        )

        self.mock_order_response_dto = OrderResponseDTO(
            id=self.mock_order_detail_entity.id,
            created_at=self.mock_order_detail_entity.created_at,
            status=self.mock_order_detail_entity.status,
            order_items=self.mock_order_detail_entity.order_items
        )

        self.order_repository_mock = Mock(spec=OrderRepositoryInterface)
        self.product_repository_mock = Mock(spec=ProductRepositoryInterface)
        self.order_controller = OrderController(order_repository=self.order_repository_mock,
                                                product_repository=self.product_repository_mock)

    def test_list_orders_with_success(self):
        OrderUseCase.list_all = Mock(return_value=[self.mock_order_detail_entity])
        result = self.order_controller.list_orders()
        OrderUseCase.list_all.assert_called_once_with(order_repository=self.order_repository_mock)
        assert result == [self.mock_order_response_dto]
