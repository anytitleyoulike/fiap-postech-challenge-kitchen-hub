from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.external.database.sqlalchemy.models.base import BaseModel
from src.external.database.sqlalchemy.orm import Base


class OrderDetailModel(Base, BaseModel):
    __tablename__ = "order_details"

    status = Column(String)
    order_items = relationship("OrderItemModel", lazy="joined")


class OrderItemModel(Base, BaseModel):
    __tablename__ = "order_items"

    order_id = Column(Integer, ForeignKey("order_details.id"))
    sku = Column(String)
    quantity = Column(Integer)
    order_detail = relationship(
        "OrderDetailModel", back_populates="order_items"
    )
