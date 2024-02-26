"""empty message

Revision ID: 7652aa212205
Revises: 
Create Date: 2024-02-25 19:33:11.700261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7652aa212205'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clientes')
    # ### end Alembic commands ###
