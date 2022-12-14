"""empty message

Revision ID: c3777297ad9f
Revises: cd9137e588f4
Create Date: 2022-10-15 18:53:42.649438

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c3777297ad9f'
down_revision = 'cd9137e588f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('character', 'birth_year',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.alter_column('favorite', 'character_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorite', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorite', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorite', 'character_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('character', 'birth_year',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    # ### end Alembic commands ###
