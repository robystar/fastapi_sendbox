"""tabelle

Revision ID: 386bdc605229
Revises: d9e0395dd00d
Create Date: 2022-11-04 17:48:39.768132

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '386bdc605229'
down_revision = 'd9e0395dd00d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tecnico', sa.Column('ruolo', sa.ARRAY(sa.String()), nullable=True), schema='edilizia')
    op.drop_column('tecnico', 'ruoloaa', schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tecnico', sa.Column('ruoloaa', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True), schema='edilizia')
    op.drop_column('tecnico', 'ruolo', schema='edilizia')
    # ### end Alembic commands ###