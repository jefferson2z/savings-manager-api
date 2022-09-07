"""user password_hash

Revision ID: 5afa7ef8d9fa
Revises: 19fc47043f13
Create Date: 2022-09-06 19:25:01.662286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5afa7ef8d9fa"
down_revision = "19fc47043f13"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("password_hash", sa.String(), nullable=False))
    op.drop_column("users", "password")


def downgrade() -> None:
    op.add_column(
        "users",
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("users", "password_hash")
