"""Populate product table

Revision ID: cf34a91c26e5
Revises: d2e4edc14fab
Create Date: 2024-07-09 18:58:35.248350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf34a91c26e5'
down_revision: Union[str, None] = 'd2e4edc14fab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO product (name, description,price,category_id,quantity, created_at, updated_at)
        VALUES
          ('Delícia de Frango', 'Frango suculento com temperos irresistíveis', 24.99,2, 10, now(), now()),
          ('Supremo Vegano', 'Uma explosão de sabores vegetais em cada mordida', 29.99,2,10, now(),now()),
          ('Turbilhão de Bacon', 'O equilíbrio perfeito entre crocância e sabor defumado', 26.99, 2, 10, now(), now()),
          ('Sabor do Mar', 'Frutos do mar frescos em um sanduíche inesquecível', 32, 2, 10, now(), now()),
          ('Trio de Queijos', 'Três queijos distintos, derretidos e deliciosos', 19.99, 2, 10, now(), now()),
          ('Divino Parmesão', 'Frango empanado com parmesão, uma combinação celestial', 26.99, 2, 10, now(), now()),
          ('Veggie Bliss', 'Pura felicidade vegetal em cada camada', 25.99, 2, 10, now(), now()),
          ('Frango Grelhado Deluxe', 'Grelhado, suculento e repleto de sabores premium', 30, 2, 10, now(), now()),
          ('Zesty BBQ Chicken', 'Frango com molho barbecue picante e irresistível', 30.99, 2, 10, now(), now()),
          ('Cheddar Sensation', 'Camadas generosas de cheddar para uma sensação incrível', 28.99, 2, 10, now(), now()),
          ('Coca-cola', 'Delicioso refrigerante sabor cola', 7.99, 3, 10, now(), now()),
          ('Suco de laranja', 'Suco refrescante de laranja', 7.99, 3, 10, now(), now()),
          ('Pudim de Leite', 'Delicioso pudim de leite', 10, 1, 10, now(), now());
    """
    )


def downgrade() -> None:
    pass
