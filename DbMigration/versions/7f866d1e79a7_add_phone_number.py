"""add phone number

Revision ID: 7f866d1e79a7
Revises: 2205e971e8b5
Create Date: 2022-07-06 13:24:09.077737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f866d1e79a7'
down_revision = '2205e971e8b5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
