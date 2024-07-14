from src.common.dto.order_dto import OrderResponseDTO
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.value_objects.order_status import OrderStatus
from src.external.database.sqlalchemy.models.order import (
    OrderDetailModel,
    OrderItemModel,
)


class OrderMapper:
    @staticmethod
    def model_to_entity(order_detail_model: OrderDetailModel):
        order_items = [
            OrderItemEntity(
                id=item.id,
                sku=item.sku,
                quantity=item.quantity,
            )
            for item in order_detail_model.order_items
        ]

        return OrderDetailEntity(
            id=order_detail_model.id,
            order_items=order_items,
            status=OrderStatus(order_detail_model.status),
            created_at=order_detail_model.created_at
        )

    @staticmethod
    def entity_to_model(order_detail_entity):
        order_items_models = [
            OrderItemModel(
                order_id=order_detail_entity.id,
                sku=item.sku,
                quantity=item.quantity,
            )
            for item in order_detail_entity.order_items
        ]

        return OrderDetailModel(
            id=order_detail_entity.id,
            status=str(order_detail_entity.status),
            order_items=order_items_models,
        )

    @staticmethod
    def model_to_entity_clean(order_detail_model):
        order_items = [
            OrderItemEntity(
                sku=item.sku,
                quantity=item.quantity,
            )
            for item in order_detail_model.order_items
        ]
        return OrderDetailEntity(
            id=order_detail_model.id,
            order_items=order_items,
            status=OrderStatus(order_detail_model.status),
            created_at=order_detail_model.created_at
        )

    @staticmethod
    def entity_to_order_response_dto(entity: OrderDetailEntity) -> OrderResponseDTO:
        return OrderResponseDTO(
            id=entity.id,
            status=entity.status,
            created_at=entity.created_at,
            order_items=entity.order_items
        )
