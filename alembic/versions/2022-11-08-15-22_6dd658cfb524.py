"""tabelle

Revision ID: 6dd658cfb524
Revises: 7a9c7d7e17f1
Create Date: 2022-11-08 15:22:48.884450

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = '6dd658cfb524'
down_revision = '7a9c7d7e17f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posizione', 'istanza_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='edilizia')
    op.drop_column('posizione', 'id', schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posizione', sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('edilizia.posizione_id_seq'::regclass)"), autoincrement=True, nullable=False), schema='edilizia')
    op.alter_column('posizione', 'istanza_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='edilizia')
    # ### end Alembic commands ###
