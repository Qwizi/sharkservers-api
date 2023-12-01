"""empty message

Revision ID: 6a35b24e57d4
Revises: 9666e912c3fb
Create Date: 2023-12-01 11:11:42.079791

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = "6a35b24e57d4"
down_revision = "9666e912c3fb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("roles", sa.Column("tag", sa.String(length=64), nullable=False))
    op.create_unique_constraint(None, "roles", ["tag"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "roles", type_="unique")
    op.drop_column("roles", "tag")
    # ### end Alembic commands ###