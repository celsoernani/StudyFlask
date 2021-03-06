"""empty message

Revision ID: 1419339816cf
Revises: 
Create Date: 2018-08-23 11:06:46.803742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1419339816cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('passaword', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
