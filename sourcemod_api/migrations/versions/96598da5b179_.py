"""empty message

Revision ID: 96598da5b179
Revises: cdae3d3781de
Create Date: 2023-11-19 18:56:50.241192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96598da5b179'
down_revision: Union[str, None] = 'cdae3d3781de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'sm_admins', ['identity'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sm_admins', type_='unique')
    # ### end Alembic commands ###
