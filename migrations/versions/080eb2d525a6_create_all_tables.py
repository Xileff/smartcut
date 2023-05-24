"""create all tables

Revision ID: 080eb2d525a6
Revises: 
Create Date: 2023-05-24 11:48:08.778225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '080eb2d525a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hairstyle_categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=21), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=102), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.BigInteger(), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('is_email_verified', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('is_barber', sa.Boolean(), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('barbershops',
    sa.Column('id', sa.String(length=27), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('latitude', sa.Numeric(precision=10, scale=8), nullable=False),
    sa.Column('longitude', sa.Numeric(precision=11, scale=8), nullable=False),
    sa.Column('user_id', sa.String(length=21), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('email_verification_codes',
    sa.Column('code', sa.String(length=8), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('expired_time', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.String(length=21), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('code', name='email_verification_code_pk'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('hairstyles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['hairstyle_categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('id_cards',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.String(length=21), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('picture'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('appointments',
    sa.Column('id', sa.String(length=21), nullable=False),
    sa.Column('schedule', sa.DateTime(), nullable=False),
    sa.Column('is_finished', sa.Boolean(), nullable=False),
    sa.Column('is_canceled', sa.Boolean(), nullable=False),
    sa.Column('will_be_canceled', sa.Boolean(), nullable=False),
    sa.Column('date_canceled', sa.DateTime(), nullable=True),
    sa.Column('barbershop_id', sa.String(length=27), nullable=False),
    sa.Column('user_id', sa.String(length=21), nullable=False),
    sa.ForeignKeyConstraint(['barbershop_id'], ['barbershops.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('predictions',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('picture', sa.String(length=255), nullable=False),
    sa.Column('compatibility', sa.Numeric(precision=4, scale=2), nullable=False),
    sa.Column('hairstyle_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=21), nullable=False),
    sa.ForeignKeyConstraint(['hairstyle_id'], ['hairstyles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.String(length=23), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=100), nullable=True),
    sa.Column('appointment_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['appointment_id'], ['appointments.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('predictions')
    op.drop_table('appointments')
    op.drop_table('id_cards')
    op.drop_table('hairstyles')
    op.drop_table('email_verification_codes')
    op.drop_table('barbershops')
    op.drop_table('users')
    op.drop_table('hairstyle_categories')
    # ### end Alembic commands ###
