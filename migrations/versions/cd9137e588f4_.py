"""empty message

Revision ID: cd9137e588f4
Revises: b70ef3595877
Create Date: 2022-10-12 10:49:36.460757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd9137e588f4'
down_revision = 'b70ef3595877'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'favorite', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorite', type_='foreignkey')
    op.drop_column('favorite', 'user_id')
    # ### end Alembic commands ###