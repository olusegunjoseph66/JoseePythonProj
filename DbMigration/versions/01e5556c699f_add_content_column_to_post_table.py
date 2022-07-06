"""add content column to post table

Revision ID: 01e5556c699f
Revises: 4bf519495584
Create Date: 2022-07-06 11:21:11.630563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01e5556c699f'
down_revision = '4bf519495584'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
