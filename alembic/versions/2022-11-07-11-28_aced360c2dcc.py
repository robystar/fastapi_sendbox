"""tabelle

Revision ID: aced360c2dcc
Revises: e06e6c36bab4
Create Date: 2022-11-07 11:28:52.159034

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aced360c2dcc'
down_revision = 'e06e6c36bab4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('istanza', 'ownersss', schema='edilizia')
    op.add_column('istanza', sa.Column('owners', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True), schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('istanza', sa.Column('ownersss', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True), schema='edilizia')
    # ### end Alembic commands ###
