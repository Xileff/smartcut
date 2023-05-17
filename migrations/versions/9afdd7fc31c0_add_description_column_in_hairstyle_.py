"""add description column in hairstyle model

Revision ID: 9afdd7fc31c0
Revises: 2945bb0f0f3d
Create Date: 2023-05-16 21:30:39.560662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9afdd7fc31c0'
down_revision = '2945bb0f0f3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hairstyle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hairstyle', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###