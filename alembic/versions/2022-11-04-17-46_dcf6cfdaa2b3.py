"""tabelle

Revision ID: dcf6cfdaa2b3
Revises: 422892ab6680
Create Date: 2022-11-04 17:46:23.212398

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = 'dcf6cfdaa2b3'
down_revision = '422892ab6680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tecnico', sa.Column('ruoloaa', sa.ARRAY(sa.String()), nullable=True), schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tecnico', 'ruoloaa', schema='edilizia')
    # ### end Alembic commands ###