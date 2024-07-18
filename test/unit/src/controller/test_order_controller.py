from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from src.common.dto.order_dto import OrderResponseDTO, CreateOrderDTO, ProductDTO
from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.controller.order import OrderController
from src.core.domain.entities.order import OrderItemEntity, OrderDetailEntity
from src.core.domain.exceptions import NotFoundError
from src.core.domain.value_objects.order_status import OrderStatus
from src.core.use_cases.order import OrderUseCase


class TestOrderController(TestCase):

    def setUp(self):
        self.date_now = datetime(2024, 7, 14, 0, 53, 35, 158494)
        self.create_order_dto = CreateOrderDTO(
            products=[ProductDTO(
                sku=12345,
                quantity=1
            )]
        )
        self.mock_order_item_entity = OrderItemEntity(
            sku=12345,
            quantity=1
        )

        self.mock_order_detail_entity = OrderDetailEntity(
            id=1,
            order_items=[self.mock_order_item_entity],
            status=OrderStatus("Recebido"),
            created_at=self.date_now
        )

        self.mock_order_response_dto = OrderResponseDTO(
            id=self.mock_order_detail_entity.id,
            created_at=self.mock_order_detail_entity.created_at,
            status=self.mock_order_detail_entity.status,
            order_items=self.mock_order_detail_entity.order_items
        )

        self.order_repository_mock = Mock(spec=OrderRepositoryInterface)
        self.order_controller = OrderController(order_repository=self.order_repository_mock)
        OrderUseCase.list_all = Mock(return_value=[self.mock_order_detail_entity])
        OrderUseCase.create = Mock(return_value=self.mock_order_response_dto)

    def tearDown(self):
        OrderUseCase.list_all.reset_mock()
        OrderUseCase.create.reset_mock()


    def test_list_orders_with_success(self):
        result = self.order_controller.list_orders()
        OrderUseCase.list_all.assert_called_once_with(order_repository=self.order_repository_mock)
        assert result == [self.mock_order_response_dto]

    def test_update_order_with_wrong_status(self):
        with self.assertRaises(NotFoundError):
            self.order_controller.update_order_status(1, "Wrong Status")

    def test_create_order_with_success(self):

        result = self.order_controller.create_order(order=self.create_order_dto)

        OrderUseCase.create.assert_called_once_with(order=self.create_order_dto,
                                                    order_repository=self.order_repository_mock)
        self.assertEqual(result, self.mock_order_response_dto)

    def test_update_order_status_with_success(self):
        order_status = OrderStatus.DOING.value
        self.mock_order_response_dto.status = order_status
        OrderUseCase.order_status_update = Mock(return_value=self.mock_order_response_dto)
        result = self.order_controller.update_order_status(order_id=self.mock_order_response_dto.id,
                                                           order_status=order_status)
        OrderUseCase.order_status_update.reset_mock()
        self.assertEqual(result.status, order_status)
