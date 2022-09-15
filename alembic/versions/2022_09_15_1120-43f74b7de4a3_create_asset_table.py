"""create asset table

Revision ID: 43f74b7de4a3
Revises: f7f284b4e76d
Create Date: 2022-09-15 11:20:59.950528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "43f74b7de4a3"
down_revision = "f7f284b4e76d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "assets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("portfolio_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["portfolio_id"],
            ["portfolios.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_assets_id"), "assets", ["id"], unique=False)
    op.create_index(op.f("ix_portfolios_id"), "portfolios", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("assets")
