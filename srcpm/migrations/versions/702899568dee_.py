"""empty message

Revision ID: 702899568dee
Revises: 88b503dfb9d7
Create Date: 2016-07-21 08:13:31.122690

"""

# revision identifiers, used by Alembic.
revision = '702899568dee'
down_revision = '88b503dfb9d7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=64), nullable=True),
    sa.Column('have_perm', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permissions')
    ### end Alembic commands ###