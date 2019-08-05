"""Added users table

Revision ID: f301babfc8ee
Revises: 
Create Date: 2019-08-05 12:53:59.286018+00:00 UTC

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f301babfc8ee"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ext_user_id", sa.Integer(), nullable=True),
        sa.Column("at_date", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ext_user_id"),
    )


def downgrade():
    op.drop_table("users")
