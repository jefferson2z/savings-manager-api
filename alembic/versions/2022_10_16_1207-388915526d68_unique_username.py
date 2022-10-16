"""unique username

Revision ID: 388915526d68
Revises: a4d6b08e45c8
Create Date: 2022-10-16 12:07:35.144253

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "388915526d68"
down_revision = "a4d6b08e45c8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint(None, "users", ["username"])


def downgrade() -> None:
    op.drop_constraint(None, "users", type_="unique")
