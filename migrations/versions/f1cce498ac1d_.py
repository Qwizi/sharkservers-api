"""empty message

Revision ID: f1cce498ac1d
Revises: 29cee9100685
Create Date: 2022-12-04 15:25:46.182952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f1cce498ac1d"
down_revision = "29cee9100685"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("color", sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "roles_scopes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("scope", sa.Integer(), nullable=True),
        sa.Column("role", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["role"],
            ["roles.id"],
            name="fk_roles_scopes_roles_role_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["scope"],
            ["scopes.id"],
            name="fk_roles_scopes_scopes_scope_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("roles_scopes")
    op.drop_table("roles")
    # ### end Alembic commands ###
