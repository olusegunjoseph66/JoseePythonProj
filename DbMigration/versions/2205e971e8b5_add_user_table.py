"""add user table

Revision ID: 2205e971e8b5
Revises: 01e5556c699f
Create Date: 2022-07-06 13:13:28.362676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2205e971e8b5'
down_revision = '01e5556c699f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
