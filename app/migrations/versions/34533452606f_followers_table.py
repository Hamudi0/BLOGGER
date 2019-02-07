"""followers table

Revision ID: 34533452606f
Revises: 7b9d2d440581
Create Date: 2019-01-06 13:20:07.239276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34533452606f'
down_revision = '7b9d2d440581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
