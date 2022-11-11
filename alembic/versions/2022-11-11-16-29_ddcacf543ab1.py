"""tabelle

Revision ID: ddcacf543ab1
Revises: 8b00e4de3827
Create Date: 2022-11-11 16:29:10.390034

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = 'ddcacf543ab1'
down_revision = '8b00e4de3827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('civico', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('mappale_nceu', 'foglio',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('mappale_nceu', 'mappale',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('mappale_nct', 'foglio',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('mappale_nct', 'mappale',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('uiu', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('uiu', 'foglio',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    op.alter_column('uiu', 'mappale',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='edilizia')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uiu', 'mappale',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('uiu', 'foglio',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('uiu', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('mappale_nct', 'mappale',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('mappale_nct', 'foglio',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('mappale_nceu', 'mappale',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('mappale_nceu', 'foglio',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    op.alter_column('civico', 'civico',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='edilizia')
    # ### end Alembic commands ###
