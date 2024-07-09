"""Populate product category table

Revision ID: d2e4edc14fab
Revises: 6d8093099a67
Create Date: 2024-07-09 18:57:13.424680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2e4edc14fab'
down_revision: Union[str, None] = '6d8093099a67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO product_category
            VALUES
            ('Sobremesa',1,now(),now()),
            ('Lanche',2,now(),now()),
            ('Bebida',3,now(),now()),
            ('Acompanhamento',4,now(),now())
    """
    )


def downgrade() -> None:
    # op.drop_column(table_name="product", column_name="quantity")
    op.execute(
        """
        DELETE FROM product_category
    """
    )
