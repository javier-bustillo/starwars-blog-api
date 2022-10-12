"""empty message

Revision ID: e6ef1f23c612
Revises: d629e41f3cd3
Create Date: 2022-10-12 09:06:14.058481

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e6ef1f23c612'
down_revision = 'd629e41f3cd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('planet_ibfk_1', 'planet', type_='foreignkey')
    op.drop_column('planet', 'character_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('character_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('planet_ibfk_1', 'planet', 'character', ['character_id'], ['id'])
    op.drop_table('favorite')
    # ### end Alembic commands ###