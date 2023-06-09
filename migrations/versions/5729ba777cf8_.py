"""empty message

Revision ID: 5729ba777cf8
Revises: b99fe466e496
Create Date: 2023-04-02 17:06:10.650490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5729ba777cf8'
down_revision = 'b99fe466e496'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('alive', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=120), nullable=False),
    sa.Column('dimensions', sa.String(length=80), nullable=False),
    sa.Column('residents', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('locations')
    op.drop_table('characters')
    # ### end Alembic commands ###
