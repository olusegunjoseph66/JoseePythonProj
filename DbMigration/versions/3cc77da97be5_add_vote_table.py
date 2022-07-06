"""add vote table

Revision ID: 3cc77da97be5
Revises: df8de3dd6a15
Create Date: 2022-07-06 13:46:44.959672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc77da97be5'
down_revision = 'df8de3dd6a15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
