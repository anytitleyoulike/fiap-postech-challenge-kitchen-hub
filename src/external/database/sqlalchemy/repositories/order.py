from datetime import datetime
from typing import List

from sqlalchemy import case

from src.common.interfaces.order_repository import OrderRepositoryInterface
from src.core.domain.entities.order import OrderDetailEntity, OrderItemEntity
from src.core.domain.exceptions import NotFoundError, OperationalException
from src.core.domain.value_objects.order_status import OrderStatus
from src.external.database.sqlalchemy.mappers.order_mapper import OrderMapper
from src.external.database.sqlalchemy.models.order import (
    OrderDetailModel,
    OrderItemModel,
)
from src.external.database.sqlalchemy.session_mixin import use_database_session


class OrderRepository(OrderRepositoryInterface):

    def create(
            self,
            order_detail: OrderDetailEntity,
            order_items: List[OrderItemEntity],
    ) -> OrderDetailEntity:
        try:

            with use_database_session() as session:
                order_detail_model = OrderDetailModel(
                    total=order_detail.total,
                    updated_at=datetime.now(),
                    status=str(order_detail.status),
                )

                session.add(order_detail_model)

                session.flush()

                order_id: int = order_detail_model.id

                order_items_models = [
                    OrderItemModel(
                        order_id=order_id,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        updated_at=datetime.now(),
                    )
                    for item in order_items
                ]

                session.bulk_save_objects(order_items_models)
                session.commit()
                return OrderMapper.model_to_entity(order_detail_model)
        except Exception as error:
            print(error)

    def list_all(self) -> List[OrderDetailEntity]:
        with use_database_session() as session:

            orders = session.query(OrderDetailModel).filter(OrderDetailModel.status != OrderStatus.DONE.value).order_by(
                ## TO-DO: fazer alguma forma mais clean code usando o valor do enum
                case(
                    (OrderDetailModel.status == 'Pronto', 1),
                    (OrderDetailModel.status == 'Em Preparação', 2),
                    (OrderDetailModel.status == 'Recebido', 3)
                ),
                OrderDetailModel.created_at.asc()).all()
            session.close()
            return [OrderMapper.model_to_entity_clean(order) for order in orders]

    def update_order_status(self, order_id: int, order_status: str) -> OrderDetailEntity:
        with (use_database_session() as session):
            order_detail = session.query(OrderDetailModel).filter_by(
                id=order_id
            ).first()

            if not order_detail:
                raise NotFoundError("Order not found")

            order_detail.status = order_status
            order_detail.updated_at = datetime.now()
            session.commit()

            return OrderMapper.model_to_entity(order_detail)
