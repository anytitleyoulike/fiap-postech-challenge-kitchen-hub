from src.common.dto.order_dto import OrderResponseDTO
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.entities.product import ProductEntity
from src.core.domain.value_objects.order_status import OrderStatus
from src.external.database.sqlalchemy.models.order import (
    OrderDetailModel,
    OrderItemModel,
)


class OrderMapper:
    @staticmethod
    def model_to_entity(order_detail_model):
        order_items = [
            OrderItemEntity(
                id=item.id,
                order_detail_id=order_detail_model.id,
                product_id=item.product_id,
                product=ProductEntity(
                    id=item.product.id,
                    name=item.product.name,
                    description=item.product.description,
                    category=item.product.category.name,
                    price=item.product.price,
                    quantity=item.product.quantity,
                ),
                quantity=item.quantity,
            )
            for item in order_detail_model.order_items
        ]

        return OrderDetailEntity(
            id=order_detail_model.id,
            order_items=order_items,
            # user_id=order_detail_model.user_id,
            total=round(order_detail_model.total, 2),
            status=OrderStatus(order_detail_model.status),
            created_at=order_detail_model.created_at
        )

    @staticmethod
    def entity_to_model(order_detail_entity):
        order_items_models = [
            OrderItemModel(
                order_id=order_detail_entity.id,
                product_id=item.product_id,
                quantity=item.quantity,
            )
            for item in order_detail_entity.order_items
        ]

        return OrderDetailModel(
            id=order_detail_entity.id,
            status=str(order_detail_entity.status),
            # user_id=order_detail_entity.user_id,
            total=order_detail_entity.total,
            order_items=order_items_models,
        )

    @staticmethod
    def model_to_entity_clean(order_detail_model):
        order_items = [
            OrderItemEntity(
                product=ProductEntity(
                    name=item.product.name,
                    category=item.product.category.name,
                ),
                quantity=item.quantity,
            )
            for item in order_detail_model.order_items
        ]
        return OrderDetailEntity(
            id=order_detail_model.id,
            order_items=order_items,
            total=round(order_detail_model.total, 2),
            status=OrderStatus(order_detail_model.status),
            created_at=order_detail_model.created_at
        )

    @staticmethod
    def entity_to_order_response_dto(entity: OrderDetailEntity) -> OrderResponseDTO:
        return OrderResponseDTO(
            id=entity.id,
            total=entity.total,
            status=entity.status,
            created_at=entity.created_at,
            order_items=entity.order_items
        )
