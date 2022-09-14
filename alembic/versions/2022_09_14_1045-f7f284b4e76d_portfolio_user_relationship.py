"""portfolio-user relationship

Revision ID: f7f284b4e76d
Revises: 5afa7ef8d9fa
Create Date: 2022-09-14 10:45:10.119588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f7f284b4e76d"
down_revision = "5afa7ef8d9fa"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("portfolios")
    op.create_table(
        "portfolios",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_foreign_key(None, "portfolios", "users", ["user_id"], ["id"])


def downgrade() -> None:
    op.drop_column("portfolios", "user_id")
