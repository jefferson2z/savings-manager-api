"""users table

Revision ID: 19fc47043f13
Revises: 3f39ccf845d0
Create Date: 2022-09-06 11:14:30.413300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "19fc47043f13"
down_revision = "3f39ccf845d0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("users")
