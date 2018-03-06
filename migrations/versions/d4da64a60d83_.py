"""empty message

Revision ID: d4da64a60d83
Revises:
Create Date: 2018-03-05 16:39:08.273099

"""
from alembic import op
import sqlalchemy as sa
from app import models
import json
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

# revision identifiers, used by Alembic.
revision = 'd4da64a60d83'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('programs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ProgTitle', sa.String(length=1000), nullable=True),
    sa.Column('ProgNumber', sa.String(length=1000), nullable=True),
    sa.Column('GovAgency', sa.String(length=1000), nullable=True),
    sa.Column('PubDate', sa.String(length=1000), nullable=True),
    sa.Column('AgencyShort', sa.String(length=1000), nullable=True),
    sa.Column('WebURL', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_programs_AgencyShort'), 'programs', ['AgencyShort'])
    op.create_index(op.f('ix_programs_GovAgency'), 'programs', ['GovAgency'])
    op.create_index(op.f('ix_programs_ProgNumber'), 'programs', ['ProgNumber'])
    op.create_index(op.f('ix_programs_ProgTitle'), 'programs', ['ProgTitle'])
    op.create_index(op.f('ix_programs_PubDate'), 'programs', ['PubDate'])
    op.create_index(op.f('ix_programs_WebURL'), 'programs', ['WebURL'])

    with open('govProgs.json', 'r') as file:
        seedData = json.load(file)
        # print(seedData)

    programs_table = table('programs',
        column('id', Integer),
        column('ProgTitle', String),
        column('ProgNumber', String),
        column('GovAgency', String),
        column('PubDate', String),
        column('AgencyShort', String),
        column('WebURL', String)
        )

    op.bulk_insert(programs_table,
        seedData
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_programs_id'), table_name='programs')
    op.drop_table('programs')
    # ### end Alembic commands ###