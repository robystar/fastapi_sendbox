"""tabelle

Revision ID: 5acc9346f50b
Revises: e7031677f289
Create Date: 2022-11-07 11:01:21.854884

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5acc9346f50b'
down_revision = 'e7031677f289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('istanza', 'ownersss', schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('istanza', sa.Column('ownersss', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True), schema='edilizia')
    # ### end Alembic commands ###
