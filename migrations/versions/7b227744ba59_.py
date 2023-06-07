"""empty message

Revision ID: 7b227744ba59
Revises: 34517fc94e07
Create Date: 2023-06-07 18:35:50.820743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b227744ba59'
down_revision = '34517fc94e07'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forum_reputation',
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=7), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], name='fk_forum_reputation_users_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts_likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('like', sa.Integer(), nullable=True),
    sa.Column('post', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['like'], ['forum_reputation.id'], name='fk_posts_likes_forum_reputation_like_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post'], ['forum_posts.id'], name='fk_posts_likes_forum_posts_post_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_likes')
    op.drop_table('forum_reputation')
    # ### end Alembic commands ###
