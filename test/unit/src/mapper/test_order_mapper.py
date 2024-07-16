import unittest
from datetime import datetime
from unittest.mock import patch, Mock

from src.common.dto.order_dto import OrderResponseDTO
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.value_objects.order_status import OrderStatus
from src.external.database.sqlalchemy.mappers.order_mapper import OrderMapper
from src.external.database.sqlalchemy.models.order import OrderDetailModel, OrderItemModel


class TestOrderMapper(unittest.TestCase):
    def setUp(self):
        self.mock_list_order_item_entity = [OrderItemEntity(
            id=1,
            sku="Mock_321",
            quantity=2
        )]
        self.mock_order_detail_entity = OrderDetailEntity(
            id=100,
            status=OrderStatus.RECEIVED,
            created_at=datetime.now(),
            order_items=self.mock_list_order_item_entity
        )
        self.mock_order_item_model = OrderItemModel(
            order_id=1,
            sku="Mock_123",
            quantity=2,
        )
        self.mock_order_detail_model = OrderDetailModel(
            status='Recebido',
            order_items=[self.mock_order_item_model]
        )

    def test_order_entity_to_response(self):
        order_entity = OrderMapper.entity_to_order_response_dto(self.mock_order_detail_entity)

        self.assertIsInstance(order_entity, OrderResponseDTO)

    def test_order_model_to_entity(self):
        order_detail_entity = OrderMapper.model_to_entity_clean(self.mock_order_detail_model)

        self.assertIsInstance(order_detail_entity, OrderResponseDTO)

    def test_order_entity_to_model(self):
        order_model = OrderMapper.entity_to_model(self.mock_order_detail_entity)
        self.assertIsInstance(order_model, OrderDetailModel)


if __name__ == '__main__':
    unittest.main()
