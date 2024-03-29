"""empty message

Revision ID: ef3dd2421bd5
Revises: 7652aa212205
Create Date: 2024-02-26 10:11:19.830135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef3dd2421bd5'
down_revision = '7652aa212205'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('musicas_favoritas',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=False),
    sa.Column('artista', sa.String(length=100), nullable=False),
    sa.Column('genero', sa.String(length=50), nullable=True),
    sa.Column('usuario_id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('musicas_favoritas')
    # ### end Alembic commands ###
