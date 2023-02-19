"""empty message

Revision ID: 3d75d5abe624
Revises: e5998d115602
Create Date: 2022-12-17 21:36:55.684063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3d75d5abe624"
down_revision = "e5998d115602"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "forum_tags",
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column("updated_date", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "forum_posts",
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column("updated_date", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("author", sa.Integer(), nullable=True),
        sa.Column("content", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author"], ["users.id"], name="fk_forum_posts_users_id_author"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "forum_threads",
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column("updated_date", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=64), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("is_closed", sa.Boolean(), nullable=True),
        sa.Column("author", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author"], ["users.id"], name="fk_forum_threads_users_id_author"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "threads_posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("post", sa.Integer(), nullable=True),
        sa.Column("thread", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["post"],
            ["forum_posts.id"],
            name="fk_threads_posts_forum_posts_post_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["thread"],
            ["forum_threads.id"],
            name="fk_threads_posts_forum_threads_thread_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "threads_tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("tag", sa.Integer(), nullable=True),
        sa.Column("thread", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["tag"],
            ["forum_tags.id"],
            name="fk_threads_tags_forum_tags_tag_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["thread"],
            ["forum_threads.id"],
            name="fk_threads_tags_forum_threads_thread_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("threads_tags")
    op.drop_table("threads_posts")
    op.drop_table("forum_threads")
    op.drop_table("forum_posts")
    op.drop_table("forum_tags")
    # ### end Alembic commands ###
