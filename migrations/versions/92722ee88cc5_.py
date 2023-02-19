"""empty message

Revision ID: 92722ee88cc5
Revises: 878577a701c5
Create Date: 2023-02-08 23:11:11.143670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "92722ee88cc5"
down_revision = "878577a701c5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "steamrep_profiles", sa.Column("scammer", sa.Boolean(), nullable=True)
    )
    op.drop_column("steamrep_profiles", "banned")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "steamrep_profiles",
        sa.Column("banned", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.drop_column("steamrep_profiles", "scammer")
    # ### end Alembic commands ###
