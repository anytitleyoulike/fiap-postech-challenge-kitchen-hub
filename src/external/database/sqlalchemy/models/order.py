from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.external.database.sqlalchemy.models.base import BaseModel
from src.external.database.sqlalchemy.orm import Base


class OrderDetailModel(Base, BaseModel):
    __tablename__ = "order_details"

    # user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Float)
    status = Column(String)
    order_items = relationship("OrderItemModel", lazy="joined")


class OrderItemModel(Base, BaseModel):
    __tablename__ = "order_items"

    order_id = Column(Integer, ForeignKey("order_details.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
    order_detail = relationship(
        "OrderDetailModel", back_populates="order_items"
    )
    product = relationship("ProductModel", lazy="joined")
