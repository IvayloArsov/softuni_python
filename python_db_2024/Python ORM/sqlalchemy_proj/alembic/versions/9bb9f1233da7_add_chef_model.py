"""Add chef model

Revision ID: 9bb9f1233da7
Revises: b52a223c7373
Create Date: 2024-07-19 22:07:47.970821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bb9f1233da7'
down_revision: Union[str, None] = 'b52a223c7373'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chefs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('recipes', sa.Column('chef_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipes', 'chefs', ['chef_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'chef_id')
    op.drop_table('chefs')
    # ### end Alembic commands ###
