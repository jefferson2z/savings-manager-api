"""create deposits table

Revision ID: a4d6b08e45c8
Revises: 43f74b7de4a3
Create Date: 2022-09-26 11:26:12.666385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a4d6b08e45c8"
down_revision = "43f74b7de4a3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "deposits",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.DECIMAL(precision=19, scale=4), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("asset_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["asset_id"],
            ["assets.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_deposits_amount"), "deposits", ["amount"], unique=False)
    op.create_index(op.f("ix_deposits_date"), "deposits", ["date"], unique=False)
    op.create_index(op.f("ix_deposits_id"), "deposits", ["id"], unique=False)


def downgrade() -> None:
    op.drop_table("deposits")
