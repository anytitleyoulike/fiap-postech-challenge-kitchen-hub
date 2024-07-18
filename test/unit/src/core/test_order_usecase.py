import unittest
from datetime import datetime
from unittest.mock import Mock

from src.common.dto.order_dto import CreateOrderDTO, ProductDTO, OrderResponseDTO
from src.core.domain.entities.order import OrderItemEntity, OrderDetailEntity
from src.core.domain.exceptions import OperationalException
from src.core.domain.value_objects.order_status import OrderStatus
from src.core.use_cases.order import OrderUseCase


class TestOrderUseCase(unittest.TestCase):

    def setUp(self):
        self.date_now = datetime(2024, 7, 14, 0, 53, 35, 158494)
        self.mock_order_repository = Mock()
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
            created_at=self.date_now,
            status=self.mock_order_detail_entity.status,
            order_items=self.mock_order_detail_entity.order_items
        )

    def tearDown(self):
        self.mock_order_detail_entity = None
        self.mock_order_repository.create.reset_mock()

    def test_create_order_with_success(self):
        self.mock_order_repository.create = Mock(return_value=self.mock_order_detail_entity)
        result = OrderUseCase.create(order=self.create_order_dto,
                                     order_repository=self.mock_order_repository)

        self.assertEqual(self.mock_order_response_dto, result)

    # def test_create_order_with_fail(self):
    #     order_detail_without_id = self.mock_order_detail_entity
    #     order_detail_without_id.id = None
    #     self.mock_order_repository.create = Mock(return_value=order_detail_without_id)
    #
    #     with self.assertRaises(OperationalException) as context:
    #         OrderUseCase.create(order=self.create_order_dto,
    #                             order_repository=self.mock_order_repository)
    #
    #     self.assertEqual(str(context.exception), "Error creating order")

    def test_list_all(self):
        self.mock_order_repository.list_all = Mock(return_value=[self.mock_order_detail_entity])

        result = OrderUseCase.list_all(self.mock_order_repository)
        self.assertEqual(result, [self.mock_order_detail_entity])

    # def test_update_order_status(self):
    #     mock_order_detail_entity = OrderDetailEntity(
    #         id=1,
    #         created_at=self.date_now,
    #         status=OrderStatus(
    #             "Pronto"
    #         ),
    #         order_items=[
    #             OrderItemEntity(sku="1234abc", quantity=1)
    #         ]
    #     )
    #     self.mock_order_repository.update_order_status = Mock(return_value=mock_order_detail_entity)
    #
    #     result = OrderUseCase.order_status_update(order_repository=self.mock_order_repository,
    #                                               order_status=OrderStatus("Pronto"),
    #                                               order_id=self.mock_order_response_dto.id)
    #     self.assertEqual(result.status, mock_order_detail_entity.status)


if __name__ == '__main__':
    unittest.main()
