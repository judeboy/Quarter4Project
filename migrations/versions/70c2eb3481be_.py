"""empty message

Revision ID: 70c2eb3481be
Revises: 
Create Date: 2018-03-08 18:37:06.391287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c2eb3481be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_admin_id'), 'admin', ['id'], unique=False)
    op.create_table('programs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ProgTitle', sa.String(length=1000), nullable=True),
    sa.Column('ProgNumber', sa.String(length=1000), nullable=True),
    sa.Column('GovAgency', sa.String(length=1000), nullable=True),
    sa.Column('PubDate', sa.String(length=1000), nullable=True),
    sa.Column('AgencyShort', sa.String(length=1000), nullable=True),
    sa.Column('WebURL', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ProgNumber'),
    sa.UniqueConstraint('WebURL')
    )
    op.create_index(op.f('ix_programs_id'), 'programs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_programs_id'), table_name='programs')
    op.drop_table('programs')
    op.drop_index(op.f('ix_admin_id'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
