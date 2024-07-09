from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.external.database.sqlalchemy.models.base import BaseModel
from src.external.database.sqlalchemy.orm import Base


class ProductModel(Base, BaseModel):
    __tablename__ = "product"

    name = Column(String(100), unique=True, index=True)
    description = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey("product_category.id"))
    price = Column(Float)
    quantity = Column(Integer)
    category = relationship("ProductCategoryModel", lazy="joined")


class ProductCategoryModel(Base, BaseModel):
    __tablename__ = "product_category"

    name = Column(String(30), unique=True, index=True)
