"""empty message

Revision ID: cb3366d9d1cd
Revises: 6af1e1ea2cb8
Create Date: 2024-08-17 13:54:20.754924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb3366d9d1cd'
down_revision: Union[str, None] = '6af1e1ea2cb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collections', sa.Column('slug', sa.String(), nullable=False))
    op.create_index(op.f('ix_collections_slug'), 'collections', ['slug'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_collections_slug'), table_name='collections')
    op.drop_column('collections', 'slug')
    # ### end Alembic commands ###
