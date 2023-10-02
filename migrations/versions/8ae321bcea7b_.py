"""empty message

Revision ID: 8ae321bcea7b
Revises: 734c6e2e11f2
Create Date: 2023-10-02 17:47:19.824275

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = '8ae321bcea7b'
down_revision = '734c6e2e11f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_subscription', sa.Column('old_display_role', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_user_subscription_roles_id_old_display_role', 'user_subscription', 'roles', ['old_display_role'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_user_subscription_roles_id_old_display_role', 'user_subscription', type_='foreignkey')
    op.drop_column('user_subscription', 'old_display_role')
    # ### end Alembic commands ###