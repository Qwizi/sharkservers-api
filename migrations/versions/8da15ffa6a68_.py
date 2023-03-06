"""empty message

Revision ID: 8da15ffa6a68
Revises: 9d51f18cadee
Create Date: 2023-02-08 16:47:41.551646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8da15ffa6a68"
down_revision = "9d51f18cadee"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "servers",
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column("updated_date", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("ip", sa.String(length=64), nullable=False),
        sa.Column("port", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ip"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("servers")
    # ### end Alembic commands ###