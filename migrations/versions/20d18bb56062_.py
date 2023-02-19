"""empty message

Revision ID: 20d18bb56062
Revises: f1cce498ac1d
Create Date: 2022-12-04 20:04:13.341087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20d18bb56062"
down_revision = "f1cce498ac1d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users_roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("role", sa.Integer(), nullable=True),
        sa.Column("user", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["role"],
            ["roles.id"],
            name="fk_users_roles_roles_role_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user"],
            ["users.id"],
            name="fk_users_roles_users_user_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_roles")
    # ### end Alembic commands ###
