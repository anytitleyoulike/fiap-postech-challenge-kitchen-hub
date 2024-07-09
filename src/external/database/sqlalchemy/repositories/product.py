from typing import List

from src.common.interfaces.product_repository import ProductRepositoryInterface
from src.core.domain.entities.product import ProductEntity
from src.core.domain.exceptions import NotFoundError
from src.external.database.sqlalchemy.models.product import (
    ProductCategoryModel,
    ProductModel,
)
from src.external.database.sqlalchemy.session_mixin import use_database_session


class ProductRepository(ProductRepositoryInterface):
    def create(self, product: ProductEntity):
        with use_database_session() as session:
            product_category = (
                session.query(ProductCategoryModel)
                .filter_by(name=product.category.title())
                .first()
            )
            product_model = ProductModel(
                name=product.name,
                category_id=product_category.id,
                description=product.description,
                price=product.price,
                quantity=product.quantity,
            )
            session.add(product_model)
            session.commit()
        return product

    def update(self, product: ProductEntity) -> ProductEntity:
        with use_database_session() as session:
            product_category = (
                session.query(ProductCategoryModel)
                .filter_by(name=product.category.title())
                .first()
            )

            if not product_category:
                raise NotFoundError("Category not found")

            product_model = (
                session.query(ProductModel).filter_by(id=product.id).first()
            )
            if product_model:
                product_model.name = product.name
                product_model.category_id = product_category.id
                product_model.description = product.description
                product_model.price = product.price
                product_model.quantity = product.quantity
            session.commit()
        return product

    def list_by_category(self, category: str) -> List[ProductEntity]:
        with use_database_session() as session:
            return (
                session.query(ProductModel)
                .join(ProductCategoryModel)
                .filter(ProductCategoryModel.name == category)
                .all()
            )

    def get_by_id(self, product_id: int) -> ProductEntity:
        with use_database_session() as session:
            product = (
                session.query(ProductModel).filter_by(id=product_id).first()
            )
            return product

    def get_by_product_name(self, product_name: str) -> ProductEntity:
        with use_database_session() as session:
            return (
                session.query(ProductModel)
                .filter_by(name=product_name)
                .first()
            )

    def get_many_by_ids(self, product_ids: List[int]) -> List[ProductEntity]:
        with use_database_session() as session:
            products = (
                session.query(ProductModel)
                .filter(ProductModel.id.in_(product_ids))
                .all()
            )
            return products

    def list_all(self) -> List[ProductEntity]:
        with use_database_session() as session:
            products = (
                session.query(ProductModel).join(ProductCategoryModel).all()
            )

            return products

    def delete(self, product_id: int) -> bool:
        with use_database_session() as session:
            product = (
                session.query(ProductModel).filter_by(id=product_id).first()
            )
            if product is None:
                return False
            session.delete(product)
            session.commit()
            return True
