"""rename address

Revision ID: 39d614b913b8
Revises: cd0359d9d3f0
Create Date: 2024-04-03 16:37:55.866575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39d614b913b8'
down_revision = 'cd0359d9d3f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('location', sa.String(), nullable=True))
    op.alter_column('departments', 'address',  new_column_name='location')    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.alter_column('departments', 'location',  new_column_name='address')    
    # ### end Alembic commands ###
